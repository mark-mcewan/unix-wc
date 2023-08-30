import os
import sys

# Check if the required number of arguments is provided
if len(sys.argv) > 3:
    print("Usage: python ccwc.py  [-clmw] [file ...]")
    sys.exit(1)
elif len(sys.argv) < 3 and sys.stdin.isatty():
    print("Usage: python ccwc.py  [-clmw] [file ...]")
    sys.exit(1)
elif (
    sys.argv[1] != "-c"
    and sys.argv[1] != "-l"
    and sys.argv[1] != "-w"
    and sys.argv[1] != "-m"
):
    print("First argument must be [-clmw]")
    sys.exit(1)

# Access the command-line arguments
operation_flag = sys.argv[1]

if len(sys.argv) == 2:
    useInput = True
    file_path = "piped input"
else:
    useInput = False
    file_path = sys.argv[2]

if operation_flag == "-c":
    if useInput:
        file_size = len(sys.stdin.buffer.read())
    else:
        file_size = os.path.getsize(file_path)
    print(str(file_size) + " " + file_path)

if operation_flag == "-l":
    line_count = 0

    if useInput:
        lines = sys.stdin.readlines()
        line_count = len(lines)
    else:
        with open(file_path, "r") as file:
            for line in file:
                line_count += 1
    print(str(line_count) + " " + file_path)

if operation_flag == "-w":
    if useInput:
        contents = sys.stdin.read()
    else:
        with open(file_path, "r") as file:
            contents = file.read()
            word_count = len(contents.split())

    word_count = len(contents.split())
    print(str(word_count) + " " + file_path)

if operation_flag == "-m":
    if useInput:
        character_count = len(sys.stdin.read())
    else:
        with open(file_path, "r") as file:
            contents = file.read()
            character_count = len(contents)
    print(str(character_count) + " " + file_path)

sys.exit(0)
