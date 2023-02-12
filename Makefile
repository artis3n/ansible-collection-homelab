#!/usr/bin/env make
.DELETE_ON_ERROR:

.PHONY: install
install:
	poetry install
	poetry run ansible-galaxy collection install community.general

.PHONY: update
update:
	poetry update
	poetry run ansible-galaxy collection install --upgrade community.general

.PHONY: test
test:
	cd tests && poetry run molecule test -s role_canonical_ads

.PHONY: lint
lint:
	poetry run ansible-lint --profile=production
