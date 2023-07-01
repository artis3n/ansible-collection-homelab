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
test: test-canonical-ads test-code-server

.PHONY: test-code-server
test-code-server:
	cd tests && poetry run molecule test -s role_code_server
	cd tests && poetry run molecule test -s role_code_server_with_pass

.PHONY: test-canonical-ads
test-canonical-ads:
	cd tests && poetry run molecule test -s role_canonical_ads

.PHONY: lint
lint:
	poetry run ansible-lint --profile=production
