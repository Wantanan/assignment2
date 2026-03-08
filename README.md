#ALC Risk-Assessment Tool

## Project Overview
This Python-based tool is developed for Antrim Logistics Company (ALC) to screen client email addresses against known data breaches. It servers as proactive risk-management tool to protect client credentials and inform mitigation strategies.

## Project Structure
The project follows a modular architecture for scalability and maintainability:
- 'src/' : Core logic including API clients and data processors.
- 'tests/' : Unit tests to ensure reliability.
- 'config.yaml' : Centralized configuration management.
- 'logs/' : Structured logging for observability.

## Setup & Installation
1. Install required
    - pip install requests PyYAML, python-dotenv, and pytest

2. Configure your API key in the env. file:
    Intelx_API_KEY = ""

## Usage
- Terminal
    python main.py


## Testing and Quality Assurance
- Terminal
    python3 -m pytest

## Limitation & Ethics
- GDPR Awarenes: This tool processes Personally identifiable information(PII), data must be handled according to GDPR principle.
- Rate Limitating: The free tier of intelligence X has usage limits. The tool includes basic delays but requires proper API management for high-volume scans.
- Accuracy: Breach data is historical, a "no-hit" result does not guarantee a user is 100% secure.ß