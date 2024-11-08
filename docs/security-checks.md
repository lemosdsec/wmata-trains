# Pre-commit Hooks and CI Pipeline

This repository uses pre-commit hooks for local development quality checks and GitHub Actions for CI/CD pipeline.

## Local Development Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- git

### Setting Up Pre-commit Hooks

1. Install pre-commit:

   ```bash
   pip install pre-commit
   ```

2. Install the git hooks:

   ```bash
   pre-commit install
   ```

3. (Optional) Run pre-commit against all files:

   ```bash
   pre-commit run --all-files
   ```

### Pre-commit Hooks Included

- **TruffleHog**: Scans for potential secrets and sensitive information
- **Flake8**: Checks Python code style and quality
- **Pre-commit-hooks**:
  - trailing-whitespace: Removes trailing whitespace
  - end-of-file-fixer: Ensures files end with a newline
  - check-yaml: Validates YAML files
  - check-added-large-files: Prevents large files from being committed

### Working with Pre-commit

- Hooks run automatically on `git commit`
- To temporarily bypass hooks (NOT recommended):
  ```bash
  git commit -m "message" --no-verify
  ```
- To update hooks to latest versions:
  ```bash
  pre-commit autoupdate
  ```

## CI Pipeline

The CI pipeline runs on GitHub Actions and is triggered on:
- Push to main branch
- Pull requests to main branch

### CI Pipeline Steps

1. **Security Checks**:
   - Runs all pre-commit hooks
   - Executes TruffleHog scan
   - Checks for secrets and sensitive information

2. **Tests**:
   - Sets up Python environment
   - Installs dependencies
   - Runs test suite (when available)

### Viewing CI Results

1. Go to the "Actions" tab in the GitHub repository
2. Click on the latest workflow run
3. Review the results of each job

## Troubleshooting

### Common Pre-commit Issues

1. **Hook Failed**:
   - Review the error message
   - Fix the indicated issues
   - Stage your changes
   - Try committing again

2. **TruffleHog False Positives**:
   - Verify if the detected "secret" is actually sensitive
   - If needed, update TruffleHog configuration in `.pre-commit-config.yaml`

3. **Hook Installation Failed**:
   ```bash
   # Try cleaning and reinstalling
   pre-commit clean
   pre-commit uninstall
   pre-commit install
   ```

### CI Pipeline Issues

1. **Workflow Failed**:
   - Check the specific step that failed in GitHub Actions
   - Review logs for error messages
   - Make necessary corrections and push again

## Best Practices

1. Always review changes before committing
2. Never commit real secrets or sensitive information
3. Use environment variables for sensitive data
4. Keep dependencies up to date
5. Run `pre-commit run --all-files` before pushing to remote

## Contributing

1. Fork the repository
2. Install pre-commit hooks
3. Make your changes
4. Ensure all checks pass locally
5. Create a pull request

## Additional Resources

- [Pre-commit Documentation](https://pre-commit.com/)
- [TruffleHog Documentation](https://github.com/trufflesecurity/trufflehog)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
