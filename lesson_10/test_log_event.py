import os
import pytest
import logging
from homework_10 import log_event

LOG_FILE = "login_system.log"

@pytest.mark.parametrize(
    "status,expected_level",
    [
        ("success", "INFO"),
        ("expired", "WARNING"),
        ("failed", "ERROR"),
    ]
)
def test_log_event_appends_to_log_file(status, expected_level):
    username = "Vasyl"
    expected_message = f"Login event - Username: {username}, Status: {status}"

# Read the log file before calling the function
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            before = file.read()
    else:
        before = ""
# Let's reset the logging configuration so that basicConfig works again
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

# Call the function
    log_event(username, status)

# Read the log file after the call
    with open(LOG_FILE, "r") as file:
        after = file.read()

# Extract new strings
    new_entries = after.replace(before, "", 1).strip().splitlines()

# Check that at least one new entry has appeared
    assert new_entries, "No new log entries found."

# We check that the last entry contains the expected message and logging level
    last_entry = new_entries[-1]
    assert expected_message in last_entry, f"Expected message not found in log: {last_entry}"
    assert expected_level in last_entry, f"Expected logging level '{expected_level}' not found in the log: {last_entry}"
