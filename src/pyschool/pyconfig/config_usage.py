"""This module demonstrates the usage of the two configs."""

import global_config as gconf
from class_config import config as cconf

if __name__ == "__main__":
    print("Global Config:")
    print(f"string_key: {gconf.string_key}")
    print(f"int_key: {gconf.int_key}")
    print(f"bool_key: {gconf.bool_key}")
    print(f"person: {gconf.person}")

    # Newline
    print()

    print("Class Config:")
    print(f"string_key: {cconf.string_key}")
    print(f"int_key: {cconf.int_key}")
    print(f"bool_key: {cconf.bool_key}")
    print(f"person: {cconf.person}")
