import datetime

def add_log_entry(message):
    """Appends a new entry with a timestamp to data.log."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("data.log", "a") as log_file:
        log_file.write(f"[{timestamp}] - {message}\n")
    print("Log entry added.")

if __name__ == "__main__":
    add_log_entry("Script started successfully.")
    add_log_entry("Processing complete.")
