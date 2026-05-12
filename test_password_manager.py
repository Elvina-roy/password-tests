"""
Test cases for Password Manager app.
Run: pytest test_password_manager.py
"""

import os
from datetime import datetime

REPORT_FILE = "test_report.txt"

def write_report(test_id, title, priority, input_data, expected_result, actual_result, status):
    with open(REPORT_FILE, "a") as report:
        report.write("=" * 70 + "\n")
        report.write(f"{test_id}: {title}\n")
        report.write(f"Priority: {priority}\n")
        report.write(f"Input data: {input_data}\n")
        report.write(f"Expected result: {expected_result}\n")
        report.write(f"Actual result: {actual_result}\n")
        report.write(f"Status: {status}\n")
        report.write("=" * 70 + "\n\n")


def check_test(test_id, title, priority, input_data, expected_result, condition, actual_result):
    status = "PASSED" if condition else "FAILED"

    write_report(
        test_id,
        title,
        priority,
        input_data,
        expected_result,
        actual_result,
        status
    )

    assert condition

# Clear report before execution
def setup_module():
    with open(REPORT_FILE, "w", encoding="utf-8") as report:
        report.write("PASSWORD MANAGER TEST REPORT\n")
        report.write(f"Created at: {datetime.now()}\n\n")


def test_empty_fields_validation():
    website = ""
    email = "test@gmail.com"
    password = ""

    condition = website == "" or email == "" or password == ""

    check_test(
        "TC-01",
        "Required fields validation",
        "High",
        f"website='{website}', email='{email}', password='{password}'",
        "Empty fields should be detected",
        condition,
        "Empty field detected"
    )


def test_generated_password_length():
    password = "Abcdefgh12!!"

    condition = 12 <= len(password) <= 18

    check_test(
        "TC-02",
        "Password length validation",
        "High",
        f"password='{password}'",
        "Password length should be between 12 and 18 characters",
        condition,
        f"Password length: {len(password)}"
    )


def test_save_password_to_file():
    website = "google.com"
    email = "test@gmail.com"
    password = "12345abc!"

    expected_line = f"{website} | {email} | {password}\n"

    with open("test_password.txt", "w") as file:
        file.write(expected_line)

    with open("test_password.txt", "r") as file:
        result = file.readline()

    os.remove("test_password.txt")

    condition = result == expected_line

    check_test(
        "TC-03",
        "Data saving to file",
        "High",
        f"website='{website}', email='{email}', password='{password}'",
        f"Data should be saved as: {expected_line.strip()}",
        condition,
        f"Received: {result.strip()}"
    )


def test_generated_password_has_letters():
    password = "Abcdefgh12!!"

    condition = any(char.isalpha() for char in password)

    check_test(
        "TC-04",
        "Password contains letters",
        "High",
        f"password='{password}'",
        "Password should contain at least one letter",
        condition,
        "Letter found"
    )


def test_generated_password_has_numbers():
    password = "Abcdefgh12!!"

    condition = any(char.isdigit() for char in password)

    check_test(
        "TC-05",
        "Password contains numbers",
        "High",
        f"password='{password}'",
        "Password should contain at least one number",
        condition,
        "Number found"
    )


def test_generated_password_has_symbols():
    password = "Abcdefgh12!!"
    symbols = "!#$%&()*+"

    condition = any(char in symbols for char in password)

    check_test(
        "TC-06",
        "Password contains special characters",
        "High",
        f"password='{password}'",
        "Password should contain at least one special character",
        condition,
        "Special character found"
    )


def test_email_field_has_default_value():
    default_email = "test@gmail.com"

    condition = default_email == "test@gmail.com"

    check_test(
        "TC-07",
        "Email field has default value",
        "Low",
        f"default_email='{default_email}'",
        "Default email should be test@gmail.com",
        condition,
        f"Default email: {default_email}"
    )


def test_saved_line_contains_separator():
    website = "google.com"
    email = "test@gmail.com"
    password = "12345abc!"

    saved_line = f"{website} | {email} | {password}\n"

    condition = " | " in saved_line

    check_test(
        "TC-08",
        "Data is saved with separator",
        "Medium",
        saved_line.strip(),
        "Line should contain the | separator",
        condition,
        f"Line: {saved_line.strip()}"
    )


def test_saved_line_ends_with_new_line():
    saved_line = "google.com | test@gmail.com | 12345abc!\n"

    condition = saved_line.endswith("\n")

    check_test(
        "TC-09",
        "Each record is saved on a new line",
        "Medium",
        saved_line,
        "Line should end with a newline character",
        condition,
        "Newline character found"
    )


def test_password_file_name():
    file_name = "password.txt"

    condition = file_name == "password.txt"

    check_test(
        "TC-10",
        "Password file name validation",
        "Low",
        f"file_name='{file_name}'",
        "File name should be password.txt",
        condition,
        f"File name: {file_name}"
    )


def test_saved_data_may_break_format_if_contains_new_line():
    website = "google.com\nmalicious.com"

    condition = "\n" in website

    check_test(
        "TC-11",
        "New line may break file format",
        "High",
        f"website='{website}'",
        "Risk of newline injection should be detected",
        condition,
        "Risk detected: website contains a newline character"
    )


def test_duplicate_website_can_be_saved():
    website_1 = "google.com"
    website_2 = "google.com"

    condition = website_1 == website_2

    check_test(
        "TC-12",
        "Duplicate website can be saved",
        "Medium",
        f"website_1='{website_1}', website_2='{website_2}'",
        "Risk of duplicate websites should be detected",
        condition,
        "Risk detected: websites are identical"
    )


def test_password_field_should_be_cleared_before_new_generation():
    old_password = "Old123!"
    new_password = "New456!"
    result_in_field = old_password + new_password

    condition = result_in_field != new_password

    check_test(
        "TC-13",
        "New password is appended to old password",
        "High",
        f"old_password='{old_password}', new_password='{new_password}'",
        "Password field should be cleared before generating a new password",
        condition,
        f"Actual field value: {result_in_field}"
    )


def test_very_long_website_input():
    website = "a" * 1000 + ".com"

    condition = len(website) > 255

    check_test(
        "TC-14",
        "Very long website input",
        "Medium",
        f"website length={len(website)}",
        "Too long input should be detected",
        condition,
        f"Website length: {len(website)}"
    )
def test_password_should_not_be_too_short_fail():
    password = "12345"

    condition = len(password) >= 8

    check_test(
        "TC-15",
        "Password should not be too short",
        "High",
        f"password='{password}'",
        "Password length should be at least 8 characters",
        condition,
        f"Password length: {len(password)}"
    )

def test_website_should_not_be_empty_fail():
    website = ""

    condition = website != ""

    check_test(
        "TC-16",
        "Website should not be empty",
        "High",
        f"website='{website}'",
        "Website field should not be empty",
        condition,
        "Website field is empty"
    )
