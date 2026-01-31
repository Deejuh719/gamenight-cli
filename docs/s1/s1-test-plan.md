# Sprint 1 Test Plan

## Purpose

This test plan documents initial testing and validation of the Flask environment, testing infrastructure, and the functional requirements of User Stories US-GN-000, US-GN-001, US-GN-003, US-GN-004, US-GN-005, US-GN-006, and US-GN-007.

This plan will outline automated and manual testing strategies used during the sprint with focuses on:

- Establishing test-driven development (TDD) with `pytest`
- Validating continuous integration with GitHub Actions
- Ensuring code coverage with `pytest-cov`
- Implementing manual testing to verify the functionality of the web application with tools like `curl` and Postman
- Verifying core functionality through CLI still remains functional

## Sprint Information

- **Sprint:** 1
- **Start Date:** 01/31/2026
- **End Date:** MM/DD/YYYY
- **Prepared by:** [K Surratt](https://github.com/deejuh719)
- **Last Updated:** 01/01/2026

## Test Scope by User Story

#### US001: Health Check

- `GET /api/health` returns `{'status': 'ok'}`

#### US003: Game Selection via Web UI

- `GET /api/games/` renders the game selection page
- `GET /api/games/{invalid_game}` renders error message if game doesn't exist

#### US004 - Start New Game Session

- `POST /api/games/{game}/` creates a new game session

#### US005 - View Game State

- `GET /api/games/play/{session_id}` displays the game state
- `GET /api/games/play/{invalid_session_id}` renders error message if session doesn't exist

#### US006 - Make Moves in Game

- `POST /api/games/play/{session_id}` updates the game state

#### US007 - End Game Session

- `POST /api/games/end/{session_id}` ends the game session
- `GET /api/games` displays list of games available to play via redirect

## Test Types

Type | Description
-----|------------
Unit Tests | Test individual components of the codebase and validation with `pytest`
API Tests | Ensure expected responses from API endpoints using Flask test client
Error Handling Tests | Simulate invalid inputs and ensure appropriate error responses
CI Tests | Run tests on every push/PR and generate coverage report automatically with GitHub Actions
Manual Tests | Test functionality of the web application with tools like `curl` and Postman

## Testing Tools

Tool | Purpose
-----|------------
`pytest` | Main testing framework
`pytest-cov` | Code coverage analysis tool for pytest
Flask test client | Simulate API requests and responses
GitHub Actions | Automatic test execution on push/PR to `main`
CLI UI | Manual entry and validation of inputs
Postman | Manual API testing

## Test Environment

- **OS:** Ubuntu 22.04 runner (CI) & local developer machines
- **Python:** 3.11+
- **Dependencies:** Flask 2.x, pytest 8.x, pytest-cov 4.x (installed via `requirements.txt`)
- **Virtualenv:** .venv per developer (ensure isolation)
- **Testing:** located in `tests/` directory
- Run tests with:
    ```bash
    pytest -v
    ```
  With Coverage:
    ```bash
    pytest --cov=app --cov-report=term-missing
    ```

## Test Coverage Goals

- 100% coverage:
    - `GET /api/health`
    - `GET /api/games/{game}`
    - `POST /api/games/{game}`
- Confirm 4xx errors returned for invalid inputs (e.g. game doesn't exist)
- Identify and fix any untested edge cases
- Overall coverage &ge; 80%
- Domain coverage &ge; 90%
- Service coverage &ge; 90%
- Routes coverage &ge; 70%

## CI Integration (GitHub Actions)

- Run tests on every push/PR to `main`
- Generate coverage report automatically
- If tests fail, CI blocks merge to main
- CI uses `.github/workflows/python-app.yml`