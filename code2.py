import subprocess
import os
import argparse


def run_code2prompt_codebase():
    """
    Generates documentation for the main codebase excluding API package.
    """
    include_patterns = [
        'trunk/3rdparty/srs-docs/doc/**/*.md',
        'trunk/3rdparty/srs-docs/pages/**/*.md',
    ]


    command = (
        'code2prompt . --no-clipboard '
        '-O ".github/instructions/codebase.instructions.md" '
        f'--include "{",".join(include_patterns)}"'
    )

    print(f"Executing codebase command:\n{command}\n")

    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("Codebase documentation generated successfully!")
        print("STDOUT:\n", result.stdout)
        if result.stderr:
            print("STDERR:\n", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error executing codebase command: {e}")
        print("STDOUT:\n", e.stdout)
        print("STDERR:\n", e.stderr)
    except FileNotFoundError:
        print("Error: 'code2prompt' command not found. Make sure it's installed and in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    run_code2prompt_codebase()
