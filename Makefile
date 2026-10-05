.PHONY: install test run clean

PYTHON = .\venv\Scripts\python.exe
PIP = .\venv\Scripts\pip.exe
PYTEST = .\venv\Scripts\pytest.exe

install:
	$(PIP) install -r requirements.txt

test:
	$(PYTEST) code/backend/tests -v

run:
	$(PYTHON) code/backend/app.py

clean:
	rmdir /s /q code\backend\__pycache__ 2>nul || true
	rmdir /s /q code\backend\tests\__pycache__ 2>nul || true
	rmdir /s /q .pytest_cache 2>nul || true
