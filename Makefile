#!/usr/bin/env make

molecule_scenarios := $(patsubst %,%,$(notdir $(wildcard tests/molecule/*)))

.PHONY: test
test:
	cd tests && poetry run molecule test -s ${molecule_scenarios}
