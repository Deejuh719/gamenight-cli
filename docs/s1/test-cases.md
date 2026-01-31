# Sprint 1 Test Cases

These test cases ensure that the newly implemented features from US-GN-000, US-GN-001, US-GN-003, US-GN-004, US-GN-005, US-GN-006, and US-GN-007 are working as intended and do not break existing functionality.

Each test case includes:

- Test Case ID
- Description
- Preconditions
- Test Steps
- Expected Results
- Test Type (Automated, Manual, or Both)

## API Tests

### TC-GN-API-001: Basic Pytest Function Executes

- **Description:** Verify that a basic, standalone Python test can be discovered and executed with `pytest` (i.e. `assert 1+1==2`).
- **Test Type:** Automated
- **Preconditions:**
    1. Python venv is active
    2. `pytest` is installed
    3. Test file `tests/test_basics.py` exists with at least one test function
- **Test Steps:**
    1. Open terminal in project root directory
    2. Run the command `pytest`
    3. Observe output for discovery of the test file and execution of the test function
- **Expected Results:**
    1. Pytest reports the test in `tests/test_basics.py` is located
    2. Pytest executes the test function in `tests/test_basics.py` and passes

### TC-GN-API-002: Health Check Returns 200

- **Description:** Verify that the `/api/health` endpoint returns a 200 status code.
- **Test Type:** Automated
- **Preconditions:**
    1. Flask app is running
- **Test Steps:**
    1. Send a GET request to `/api/health`
    2. Observe the response status code
- **Expected Results:**
    1. The response status code is 200
    2. The JSON response body is `{'status': 'ok'}`

### TC-GN-API-004: Flask Returns 404 without Routes Defined

- **Description:** Verify that the Flask app returns a 404 status code when no routes are defined.
- **Test Type:** Manual
- **Preconditions:**
    1. Flask and dependencies are installed
- **Test Steps:**
    1. Send a GET request to `/`
    2. Observe the response status code
- **Expected Results:**
    1. The response status code is 404

### TC-GN-API-005: Flask Creates Local Server

- **Description:** Verify that the Flask app creates a local server.
- **Test Type:** Manual
- **Preconditions:**
    1. Flask and dependencies are installed
- **Test Steps:**
    1. Activate the venv
    2. Run the command `flask run`
    3. Observe the output and navigate to `http://127.0.0.1:5000/`
- **Expected Results:**
    1. A local server is created at `http://127.0.0.1:5000/` without a 404 error or crashing

### TC-GN-API-001: List Games Endpoint

- **Description:** Verify that the `/api/games` endpoint returns a list of games.
- **Test Type:** Manual
- **Preconditions:**
    1. Flask app is running
- **Test Steps:**
    1. Send a GET request to `/api/games`
    2. Observe the response status code
    3. Observe the JSON response body
- **Expected Results:**
    1. The response status code is 200
    2. The JSON response body is a list of games

## Domain Layer Testing

### TC-GN-DL-001: Game Model Creation

- **Description:** Verify that the Game model initializes correctly.
- **Test Type:** Automated
- **Preconditions:**
    1. Game model is defined in `game.py`
- **Test Steps:**
    1. Create a new Game instance with valid parameters (for this sprint, `name="Magic 8 Ball" type="one_player"`)
    2. Call the `is_valid` method
- **Expected Results:**
    1. The `name` attribute is set to "Magic 8 Ball"
    2. The `type` attribute is set to "one_player"
    3. `is_valid` returns `True`

### TC-GN-DL-002: Game Model Validation

- **Description:** Verify that the Game requires a name and type.
- **Test Type:** Automated
- **Preconditions:**
    1. Game model is defined in `game.py`
- **Test Steps:**
    1. Create a new Game instance with no name or type
    2. Call the `is_valid` method
- **Expected Results:**
    1. The `is_valid` method returns `False`

### TC-GN-DL-003: GameSession Initialization

- **Description:** Verify GameSession is initialized correctly.
- **Test Type:** Automated
- **Preconditions:**
    1. GameSession is defined in `game_service.py`
- **Test Steps:**
    1. Create a new GameSession instance with a valid game
    2. Call the `is_valid` method
- **Expected Results:**
    1. The `is_valid` method returns `True`

## Service Layer

### TC-GN-SRV-001: List All Games

- **Description:** Verify GameService returns a list of all games.
- **Test Type:** Manual
- **Preconditions:**
    1. Venv is activated
- **Test Steps:**
    1. Run command `game_service.list_games()`
    2. Observe the output
- **Expected Results:**
    1. The output is a list of all games
    2. Should not be empty and total should equate to the number of games currently in the database

### TC-GN-SRV-002: Create GameSession

- **Description:** Verify that the `/api/games` endpoint returns a list of games.
- **Test Type:** Manual
- **Preconditions:**
    1. Flask app is running
- **Test Steps:**
    1. Send a GET request to `/api/games`
    2. Observe the response status code
    3. Observe the JSON response body
- **Expected Results:**
    1. The response status code is 200
    2. The JSON response body is a list of games

## UI Tests

### TC-GN-UI-001: Home Page

- **Description:** Verify that the home page (welcome screen with a `List Games` button) is displayed.
- **Test Type:** Manual
- **Preconditions:**
    1. Flask app is running
- **Test Steps:**
    1. Go to `http://localhost:5000/`
    2. Observe the home page
    3. In Postman, send a GET request to `/`
- **Expected Results:**
    1. The home page is displayed
    2. The "List Games" button is present
    3. The response status code is 200

### TC-GN-UI-002: Start Game Redirects

- **Description:** Verify that clicking the "Start Game" button redirects to the game page.
- **Test Type:** Manual
- **Preconditions:**
    1. Flask app is running
- **Test Steps:**
    1. In Postman, send a GET request to `/games/start`
    2. Observe the response status code
    3. Observe the response body
- **Expected Results:**
    1. The response status code is 200