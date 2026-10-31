# Automated API Testing and Reporting Framework

## Project Overview
This project is a Python-based Automated API Testing and Reporting Framework developed using Requests and Pytest.

It automatically tests REST APIs, validates responses, measures response time, and generates a CSV test report.

## Technologies Used
- Python 3.13
- Pytest
- Requests
- Git and GitHub
- GitHub Actions
- JSONPlaceholder REST API

## APIs Tested
1. User API: https://jsonplaceholder.typicode.com/users/1
2. Posts API: https://jsonplaceholder.typicode.com/posts

## Project Features
- HTTP status code validation
- JSON response validation
- Required field validation
- User address and company validation
- Negative testing for missing users
- Posts response validation
- Unique post ID validation
- API response time measurement
- Automated CSV report generation
- Continuous Integration using GitHub Actions

## Project Structure

automated-api-testing-framework/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── reports/
│   └── api_test_report.csv
│
├── api_client.py
├── test_api.py
├── run_tests.py
├── requirements.txt
└── .gitignore

## Installation

Install the required dependencies:

pip install -r requirements.txt

## Run Automated Tests

Execute:

python -m pytest -v

## Generate Test Report

Execute:

python run_tests.py

The generated report is saved in:

reports/api_test_report.csv

## Test Results

Total Test Cases: 10
Passed: 10
Failed: 0

## Continuous Integration

GitHub Actions automatically executes the test cases whenever code is pushed to the repository or a pull request is created.

## Conclusion

This project demonstrates automated REST API testing, test validation, report generation, and continuous integration using Python, Pytest, and GitHub Actions.
