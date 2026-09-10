# Contributing to CodeMentor-AI

Thank you for considering contributing to CodeMentor-AI! We're excited to have you as part of our community. This guide will help you get started.

## Code of Conduct

Please be respectful and constructive in all interactions. We're committed to providing a welcoming environment for everyone.

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating a bug report, please check existing issues. When reporting, include:

- Clear title and description
- Steps to reproduce the issue
- Expected vs. actual behavior
- Screenshots or error logs if applicable
- Your environment (OS, Python version, etc.)

### 💡 Suggesting Features

Feature suggestions are welcome! Describe:

- Use case and motivation
- Proposed implementation (if you have ideas)
- Potential drawbacks

### 📝 Writing Documentation

Documentation improvements are valuable:

- Fix typos and unclear explanations
- Add examples and clarifications
- Improve tutorials and guides

### 💻 Writing Code

1. **Fork the repository**
   ```bash
   git clone https://github.com/your-username/CodeMentor-AI.git
   cd CodeMentor-AI
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the coding style
   - Write clear, concise commits
   - Add tests for new functionality

4. **Run tests**
   ```bash
   pytest tests/
   ```

5. **Push to your fork and submit a pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

## Coding Standards

- **Python**: Follow [PEP 8](https://pep8.org/)
- **JavaScript/React**: Use ESLint configuration in the repo
- **Comments**: Write clear, meaningful comments
- **Commits**: Use conventional commit messages

Example: `feat: add AI-powered code review feature`

## Pull Request Process

1. Update README.md if needed
2. Add/update tests for new features
3. Ensure all tests pass
4. Link related issues in PR description
5. Request review from maintainers
6. Be open to feedback and iterate

## Development Setup

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Setup pre-commit hooks
pre-commit install

# Run tests
pytest tests/ -v

# Check code coverage
pytest tests/ --cov=backend
```

## Questions?

Feel free to open a Discussion or reach out to the team at support@codementor-ai.dev

Happy coding! 🚀