import importlib.util
import sys
import os

# Path to your module
module_name = "lazy_paginate"
file_path = os.path.join(os.path.dirname(__file__), "2-lazy_paginate.py")

# Load the module dynamically
spec = importlib.util.spec_from_file_location(module_name, file_path)
lazy_module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = lazy_module
spec.loader.exec_module(lazy_module)

# Now use the function from the module
def test():
    page_size = 10
    for page in lazy_module.lazy_paginate(page_size):
        for user in page:
            print(user)

if __name__ == "__main__":
    test()
