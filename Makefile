#!/usr/bin/make -f

export PYTHONPATH=$(shell pwd)
PYTEST:=env PYTHONPATH=$(shell pwd) py.test-3

test: test.cfg
	@rm -f test.log
	python3 setup.py test
t: test.cfg
	@rm -f test.log
	$(PYTEST) -s -x -v
# --cov-report term-missing --cov-config .coveragerc --cov=qbroker.unit --cov=qbroker.proto --assert=plain

test.cfg:
	@cp test.cfg.sample $@
	@echo "Warning: copied test.cfg.sample to $@" >&2

update:
	@sh utils/update_boilerplate

pypi:
	python3 setup.py sdist upload
	git tag v$(shell python3 setup.py -V)

upload:	pypi
	git push-all --tags
