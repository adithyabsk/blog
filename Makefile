.PHONY: help
help:
	@cat Makefile

.PHONY: generate_redirects
generate_redirects:
	./scripts/generate_redirects.py

.PHONY: serve
serve: generate_redirects
	zola serve

.PHONY: build
build: generate_redirects
	zola build

.PHONY: clean
clean:
	rm -rf public

.PHONY: format
format:
	pre-commit run -a
