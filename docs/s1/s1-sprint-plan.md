# Sprint Planning

## Overall Goal

This project is focusing on a major refactor of my existing "Gamenight" app that is currently terminal/CLI based. The refactor will turn the terminal-based app into a web app utilizing Flask. I will also include various tests utilizing `pytest`, `Selenium/Playwright`, and `pytest-bdd`. The goal is to make the app more user-friendly, more visually appealing, as well as implementing a few new features while integrating SQA practices learned in class to improve the quality and maintainability of the codebase.

# Sprint 1 Plan

## Sprint Goal

Establish the foundation for the Game Night web app by creating a service layer, Flask API, and web UI from exsiting game logic. As well as implementing automated testing with CI/CD.

## Sprint Duration
- Approximately 3-4 weeks
- Start Date: 01/31/2026
- End Date: __ /__ /__

## Team
This is a solo project created, refactored, and implemented by [K Surratt](https://github.com/deejuh719).

## Deliverables

- [ ] Service Layer
- [ ] Web API
- [ ] Web UI
- [ ] Automated Testing

## Sprint 1 User Stories

- US-GN-000 - Initial Setup and Valdiation
- US-GN-001 - Health Check Endpoint
- US-GN-003 - Game Selection via Web UI
- US-GN-004 - Start New Game Session
- US-GN-005 - View Game State
- US-GN-006 - Make Moves in Game
- US-GN-007 - End Game Session

## Technical Goals
1. **Architecture** - Service layer, dependency injection, separation of concerns
2. **Testing** - Unit testing & integration testing, TDD approach, ~80% coverage
3. **CI/CD** - GitHub Actions workflow, automated test execution

## Definition of Done

- [x] Code written following PEP-8 standards
- [x] All tests passing (unit + integration)
- [x] Code coverage &ge; 80%
- [x] Docs updated
- [x] Merges to main branch
- [x] CI pipeline passing

## Risks and Mitigation
Risk | Impact | Probability | Mitigation |
----- | ----- | ----------- | ---------- |
Complex CLI hard to extract | High | Medium | Start with simplest game first (Magic 8 Ball)
Low test coverage for refactored code | Medium | Low | Follow TDD approach with tests first
Breaking existing CLI | Low | Low | Preserve CLI, build Flask separate (Separation of concerns)