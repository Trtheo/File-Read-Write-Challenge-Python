def read_and_modify_file():
    try:
        # Ask user for input file
        input_file = input("Enter the name of the file to read: ")

        # Try to open the file
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        # Modify the contents: Add line numbers
        modified_lines = [f"{i+1}: {line}" for i, line in enumerate(lines)]

        # Define output file
        output_file = "modified_" + input_file

        # Write to the new file
        with open(output_file, 'w') as outfile:
            outfile.writelines(modified_lines)

        print(f" Modified file saved as '{output_file}'.")

    except FileNotFoundError:
        print(" Error: The file does not exist.")
    except IOError:
        print(" Error: Could not read or write the file.")
    except Exception as e:
        print(f" Unexpected error: {e}")

# Run the function
read_and_modify_file()
