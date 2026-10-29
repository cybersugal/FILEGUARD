
import os
user_input = input(
    "Enter file names separated by commas: "
)

files = [
    name.strip()
    for name in user_input.split(",")
    if name.strip()
]
signatures = {
    "PDF": bytes.fromhex("25 50 44 46 2D"),
    "PNG": bytes.fromhex("89 50 4E 47 0D 0A 1A 0A"),
    "JPEG": bytes.fromhex("FF D8 FF"),
    "ZIP": bytes.fromhex("50 4B 03 04"),
}
expected_types = {
    ".pdf": "PDF",
    ".png": "PNG",
    ".jpg": "JPEG",
    ".jpeg": "JPEG",
    ".zip": "ZIP",
}
if not files:
    print("No filenames entered.")

for file_path in files:
    print("\n--- Checking:", file_path, "---")

    try:
        with open(file_path, "rb") as file:
            first_bytes = file.read(8)

    except FileNotFoundError:
        print("Error: File not found.")
        continue

    # Detect the file type.
    if len(first_bytes) == 0:
        file_type = "Empty file"
    elif first_bytes.startswith(signatures["PDF"]):
        file_type = "PDF"
    elif first_bytes.startswith(signatures["PNG"]):
        file_type = "PNG"
    elif first_bytes.startswith(signatures["JPEG"]):
        file_type = "JPEG"
    elif first_bytes.startswith(signatures["ZIP"]):
        file_type = "ZIP"
    else:
        file_type = "Unknown"

    # Check the extension.
    extension = os.path.splitext(file_path)[1].lower()
    expected_type = expected_types.get(extension)

    if file_type == "Empty file":
        extension_status = "Cannot verify: file is empty"
    elif file_type == "Unknown":
        extension_status = "Unknown file signature"
    elif expected_type is None:
        extension_status = "Unrecognised extension"
    elif file_type == expected_type:
        extension_status = "Extension matches detected type"
    else:
        extension_status = "WARNING: extension mismatch"

    # Display the report.
    print("Detected type:", file_type)
    print("First bytes:", first_bytes.hex(" "))
    print("Extension type:", expected_type)
    print("Extension check:", extension_status)
    

print("\nFileGuard scan complete.")
