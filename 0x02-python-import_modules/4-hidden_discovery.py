#!/usr/bin/python3

import types
import importlib.util

# Load the compiled module
spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Get the names defined by the module
names = [name for name in dir(module) if not name.startswith("__")]

# Sort and print the names
for name in sorted(names):
    print(name)
