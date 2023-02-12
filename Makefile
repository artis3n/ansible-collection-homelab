#!/usr/bin/env make
.DELETE_ON_ERROR:

.PHONY: test
test:
	cd tests && poetry run molecule test -s role_canonical_ads
