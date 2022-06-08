test-run:
	poetry run pytest --mypy tests/ --cov=patterns --cov-report=term-missing:skip-covered # --cov-report=xml

test-watch:
	poetry run ptw -- --mypy tests/ --cov=patterns --cov-report=term-missing:skip-covered # --cov-report=xml
