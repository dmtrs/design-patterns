run-pytest:
	poetry run pytest tests/ --cov=patterns --cov-report=term-missing:skip-covered # --cov-report=xml

run-pytest_mypy:
	poetry run pytest --mypy tests/ --cov=patterns --cov-report=term-missing:skip-covered # --cov-report=xml

watch-pytest:
	poetry run ptw -- tests/ --cov=patterns --cov-report=term-missing:skip-covered # --cov-report=xml

watch-pytest_mypy:
	poetry run ptw -- --mypy tests/ --cov=patterns --cov-report=term-missing:skip-covered # --cov-report=xml
