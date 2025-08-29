# Error Handling Lab 🧪

def modify_content(text):
    """Modify the content by making it uppercase (you can change this rule)."""
    return text.upper()

def main():
    # Ask user for filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try opening the file for reading
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ File modified and saved as '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
