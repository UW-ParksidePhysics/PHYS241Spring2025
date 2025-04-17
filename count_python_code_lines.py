import os
import sys
import re


def analyze_files(file_paths):
    total_files = 0
    total_code_lines = 0
    total_comment_lines = 0
    total_blank_lines = 0
    total_function_defs = 0

    func_def_pattern = re.compile(r'^\s*def\s+\w+\s*\(')

    for file_path in file_paths:
        if os.path.isdir(file_path):
            for root, _, files in os.walk(file_path):
                for file in files:
                    if file.endswith(".py"):
                        full_path = os.path.join(root, file)
                        total_files += 1
                        with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                            for line in f:
                                stripped = line.strip()
                                if not stripped:
                                    total_blank_lines += 1
                                elif stripped.startswith("#"):
                                    total_comment_lines += 1
                                else:
                                    total_code_lines += 1
                                    if func_def_pattern.match(line):
                                        total_function_defs += 1
        elif file_path.endswith(".py") and os.path.isfile(file_path):
            total_files += 1
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    stripped = line.strip()
                    if not stripped:
                        total_blank_lines += 1
                    elif stripped.startswith("#"):
                        total_comment_lines += 1
                    else:
                        total_code_lines += 1
                        if func_def_pattern.match(line):
                            total_function_defs += 1

    print("\nAnalysis Summary")
    print("----------------------------")
    print(f"Files scanned:        {total_files}")
    print(f"Code lines:           {total_code_lines}")
    print(f"Comment lines:        {total_comment_lines}")
    print(f"Blank lines:          {total_blank_lines}")
    print(f"Function definitions: {total_function_defs}")
    print(f"Total lines:          {total_code_lines + total_comment_lines + total_blank_lines}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        analyze_files(args)
    else:
        analyze_files(["."])
