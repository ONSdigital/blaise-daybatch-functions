.PHONY: lint lint-fix typecheck deptry vulture test test-behave

lint:
	poetry run ruff check
	poetry run ruff format --check

lint-fix:
	poetry run ruff check --fix || true
	poetry run ruff format
	poetry run ruff check

typecheck:
	poetry run pyright

deptry:
	poetry run deptry .

vulture:
	poetry run vulture .

test:
	poetry run python -m pytest

test-behave:
	poetry run python -m behave tests/features