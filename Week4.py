# File Read & Write Challenge:a program that reads a file and writes a modified version to a new file.

def modify_and_write_file(input_filename, output_filename):
    """
    Reads content from input_filename, modifies it (e.g., converts to uppercase),
    and writes the modified content to output_filename.
    """
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()

        modified_content = content.upper()  # Example modification: convert to uppercase

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File '{input_filename}' read, modified, and saved to '{output_filename}' successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# Create a dummy input file for testing
with open("input.txt", "w") as f:
    f.write("This is a test file.\n")
    f.write("It contains multiple lines.\n")

modify_and_write_file("input.txt", "output.txt")

#  Error handling; Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.


def read_file_with_error_handling():
    """
    Prompts the user for a filename and attempts to read its content.
    Handles FileNotFoundError if the file doesn't exist and IOError for other
    input/output-related errors during reading.
    """
    filename = input("Please enter the name of the file: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError as e:
        print(f"Error: Could not read the file '{filename}'. Reason: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function to execute the file reading process
read_file_with_error_handling()