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
test: test-canonical-ads

.PHONY: test-canonical-ads
test-canonical-ads:
	cd tests && poetry run molecule test -s role_canonical_ads

.PHONY: lint
lint:
	poetry run ansible-lint --profile=production

.PHONY: release
release: changelog-lint
	poetry run antsibull-changelog release --update-existing

.PHONY: changelog
changelog: changelog-lint
	poetry run antsibull-changelog generate

.PHONY: changelog-lint
changelog-lint:
	poetry run antsibull-changelog lint
