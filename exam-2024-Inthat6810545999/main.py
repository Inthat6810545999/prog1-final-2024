# 01219114/5 Laboratory Examination
#
# Department of Computer Engineering
# Faculty of Engineering, Kasetsart University
# **THIS IS AN EXAMINATION**: all regulations regarding examinations apply
# FRI 06 DEC 2024 09:00-12:00 (*time shared with other parts*)

# Hint: Look for the words TODO and pass.
# Hint: Once you make something and it works, no matter how small, COMMIT!
# Note: The situation presented in this examination is a work of fiction
#       and is not intended to reflect any real-world situation.

# Run this file to see which modules you still have to fix.
# Do not modify this file.

if __name__ == '__main__':
    import doctest
    import importlib
    modules = ['item', 'resource', 'tool', 'recipe', 'crafter']
    for module_name in modules:
        module = importlib.import_module(module_name)
        result = doctest.testmod(module)
        if result.failed == 0:
            print(f'PASS: {module_name}')
        else:
            print(f'FAIL: {module_name}')