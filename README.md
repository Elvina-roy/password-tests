# Password Manager App

Simple desktop Password Manager built with **Python** and **Tkinter**.

## Features
- Save website, email, and password
- Generate random password
- Copy password to clipboard
- Store credentials in `password.txt`

Example:
```text
google.com | test@gmail.com | Secret123!
```
## Technologies
- Python
- Tkinter
- Pyperclip
- Pytest
--------------------------------------------------------------
## Testing

The project includes **18 automated test cases** written with `pytest`.

### Test Types
- Functional Testing
- Validation Testing
- Boundary Testing
- Security Testing
- Negative Testing
 
### Covered Scenarios
- empty fields validation
- password generation and length
- password content validation
- saving data to file
- duplicate records
- long input values
- plain text password storage
- password field behavior

Some tests intentionally return **FAILED** to demonstrate bug detection and security findings.
### Run Tests
```
pytest test_password_manager.py
```
### Test Report
After execution, a readable report is generated:
```
test_report.txt
```
The report includes:
- Test Case ID
- Priority
- Input Data
- Expected Result
- Actual Result
- Status (PASSED / FAILED)
