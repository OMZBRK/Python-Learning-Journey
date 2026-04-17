# Analysis Function - Create a function named analyze_combat_log(file_path) that: Opens the file using the with open() context manager. Initializes an empty set for active_ninjas and a counter for error_count. Iterates through each line: If the line starts with "INFO", splits the string to extract the ninja's name and adds it to the set. If the line starts with "ERROR", increments the error counter. Returns the error_count and the active_ninjas set.

def analyze_combat_log(log_file):
    active_ninjas = set()
    error_count = 0
    line_count = 0
    with open(log_file, 'r') as file:
        for line in file:
            line_count += 1
            parts = line.strip().split(':')
            if len(parts) < 2:
                raise IndexError(f"Malformed entry at line {line_count}")
            if line.startswith("INFO"):
                active_ninjas.add(parts[1])
            elif line.startswith("ERROR"):
                error_count += 1
    return error_count, active_ninjas, line_count

# Display Program Start - At the start of the program, prompt the user to enter the name of the log file to be analyzed and display a message confirming the start of the analysis process.

log_file = input("Enter the name of the log file to analyze: ")
print(f"Starting analysis of log file: {log_file}...")

# User Interaction - Use an else block to display the following results if the analysis is successful: Total number of lines processed. Total number of system errors detected. The list of unique ninjas who participated in the combat. Use a finally block to display: Log analysis attempt finished.
try:
    errors, ninjas, total_lines = analyze_combat_log(log_file)
except FileNotFoundError:
    print(f"Error: The file '{log_file}' was not found.")
except IndexError as e:
    print(f"Error: {e}")
except Exception as e :
    print(f"An unexpected error occurred: {e}")

else: 
    print("\n=== Analysis Report ===")
    print(f"Total lines processed: {total_lines}")
    print(f"Total system errors detected: {errors}")
    print(f"Unique ninjas participated: {', '.join(ninjas)}")
finally: 
    print("Log analysis attempt finished.")


