# WMATA Train Positions Project - Security Demo

This project serves two purposes:
1. A functional WMATA train tracking application
2. A demonstration project for secret scanning and secure development practices

## 🎯 Security Learning Objectives

This repository demonstrates:
- Pre-commit hook implementation for secret detection
- CI/CD pipeline with security checks
- Common patterns of leaked secrets
- Best practices for secret management

## 🚂 Application Features

- Tracks WMATA train positions
- Filters for yellow line trains to Huntington Station
- Provides both CLI and web interface

## 🛠️ Setup

### Prerequisites

- Python 3.x
- pip (Python package manager)
- git

### Development Environment Setup

1. Clone the repository:
```bash
git clone https://github.com/lemosdsec/wmata-trains
cd wmata-trains
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install pre-commit hooks:
```bash
pip install pre-commit
pre-commit install
```

## 🔒 Security Features

### Pre-commit Hooks

This project includes pre-commit hooks that:
- Scan for potential secrets using TruffleHog
- Check code style with Flake8
- Enforce file formatting standards

To manually run security checks:
```bash
pre-commit run --all-files
```

### CI Pipeline

The GitHub Actions pipeline includes:
- Automated secret scanning
- Dependency security checks
- Code quality verification

## 🎮 Application Usage

### CLI Version
```bash
python simple.py
```

### Web Application
```bash
python trains.py
```
Access the web interface at: http://localhost:5000

## 🔍 Security Demo Instructions

### Testing Secret Detection

1. Try committing a file with a fake AWS key:
```python
# test_secrets.py
AWS_KEY = 'AKIA1234567890ABCDEF'
```

2. Observe how pre-commit hooks prevent the commit

### Common Secret Patterns Detected

- AWS Access Keys
- API Keys
- Private Keys
- Authentication Tokens
- Database Credentials

## 🎓 Learning Resources

- [Secret Scanning Best Practices](link-to-resource)
- [Pre-commit Documentation](https://pre-commit.com/)
- [TruffleHog Documentation](https://github.com/trufflesecurity/trufflehog)

## ⚠️ Important Notes

This is a demonstration project for educational purposes:
- Some secrets may be intentionally placed for demonstration
- Do NOT use any credentials found in this repository
- In real projects, always use secure secret management solutions

## 🤝 Contributing

1. Fork the repository
2. Install pre-commit hooks
3. Make your changes
4. Ensure all security checks pass
5. Submit a pull request

## 📝 License

[Your License Here]

## 🔗 Additional Documentation

- [Pre-commit and CI Setup](docs/security-checks.md)
- [WMATA API Documentation](docs/api-docs.md)