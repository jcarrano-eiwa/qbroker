#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division, unicode_literals
##
## This file is part of QBroker, an easy to use RPC and broadcast
## client+server using AMQP.
##
## QBroker is Copyright © 2016 by Matthias Urlichs <matthias@urlichs.de>,
## it is licensed under the GPLv3. See the file `README.rst` for details,
## including optimistic statements by the author.
##
## This paragraph is auto-generated and may self-destruct at any time,
## courtesy of "make update". The original is in ‘utils/_boilerplate.py’.
## Thus, please do not remove the next line, or insert any blank lines.
##BP

import asyncio
from qbroker.unit import Unit
from qbroker.util.tests import load_cfg
import logging
import sys
from pprint import pprint
logging.basicConfig(stream=sys.stderr, level=logging.INFO)
import json

import os
cfg = os.environ.get("QBROKER","test.cfg")
u=Unit("test.ping", **load_cfg(cfg)['config'])

@asyncio.coroutine
def cb(r):
	pprint(r.data)
	if False:
		yield from None

@asyncio.coroutine
def example():
	yield from u.start()
	yield from asyncio.sleep(0.2) # allow monitor to attach
	try:
		yield from asyncio.wait_for(u.alert(sys.argv[1],_data=json.loads(' '.join(sys.argv[2:])),callback=cb), timeout=3)
	except asyncio.TimeoutError:
		pass
	finally:
		yield from u.stop()

def main():
	loop = asyncio.get_event_loop()
	loop.run_until_complete(example())
try:
	if len(sys.argv) < 3:
		print("Usage: %s route.key {some.json.expression}" % (sys.argv[0],),file=sys.stderr)
		sys.exit(1)
	main()
except KeyboardInterrupt:
	pass

