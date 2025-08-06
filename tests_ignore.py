from stdlib_list import stdlib_list
import sys

# Get the list of standard library modules for the current Python version
# The version is formatted as 'major.minor', e.g., '3.9'
python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
all_stdlib_modules = stdlib_list(python_version)

module_name = 'json' # Replace with the module you want to check

if module_name in all_stdlib_modules:
    print(f"'{module_name}' is in the standard library for Python {python_version}.")
else:
    print(f"'{module_name}' is NOT in the standard library for Python {python_version}.")