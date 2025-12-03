# Name: Inthat # Student ID: 68010545999
from pathlib import Path


def configs(content, config=None):
    if config is None:
        config = {}

    for line in content.splitlines():
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        if "=" in line:
            key, value = line.split("=", 1)
            key, value = key.strip(), value.strip()

            if value.startswith("{") and value.endswith("}"):
                nested_dict = {}
                inner_content = value[1:-1].strip()

                if inner_content:
                    for pair in inner_content.split(";"):
                        pair = pair.strip()
                        if "=" in pair:
                            nested_key, nested_value = pair.split("=", 1)
                            nested_key, nested_value = nested_key.strip(), nested_value.strip()

                            if nested_value.isdigit():
                                nested_value = int(nested_value)
                            nested_dict[nested_key] = nested_value

                if key in config and isinstance(config[key], dict):
                    config[key].update(nested_dict)
                else:
                    config[key] = nested_dict

            else:
                if value.isdigit():
                    value = int(value)
                elif value.startswith("[") and value.endswith("]"):
                    list_content = value[1:-1].strip()
                    value = [item.strip() for item in list_content.split(
                        ",")] if list_content else []
                elif "," in value:
                    value = [item.strip()
                             for item in value.split(",") if item.strip()]
                elif value == "":
                    value = ""

                config[key] = value

    return config

def validate(config):
    """Validate configuration and return error message if invalid, None if valid"""
    if "port" not in config or not isinstance(config["port"], int) or not (1 <= config["port"] <= 65535):
        return "Validation Error: Port must be an integer between 1 and 65535."

    if "allowed_users" not in config or not config["allowed_users"] or any(user.strip() == "" for user in config["allowed_users"]):
        return "Validation Error: Allowed users list must not be empty."

    if ("database" not in config or
        "user" not in config["database"] or
        "password" not in config["database"] or
        not config["database"]["user"] or
            not config["database"]["password"]):
        return "Validation Error: Database dictionary must contain both 'user' and 'password' keys."

    if ("timeout" not in config["database"] or
        not isinstance(config["database"]["timeout"], int) or
            config["database"]["timeout"] < 0):
        return "Validation Error: Database timeout must be a positive integer."

    return None


def display_config(content, config):
    config = configs(content, config)

    error = validate(config)
    if error:
        print(error)
        return

    print("Configuration file is valid.")
    print("Parsed Data:")
    for key, value in config.items():
        if isinstance(value, dict):
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value}")
        elif isinstance(value, list):
            print(f"{key}: {",".join(value)}")
        else:
            print(f"{key}: {value}")


# Main program execution
config = {
    "port": "",
    "allowed_users": [],
    "database": {
        "user": "",
        "password": "",
        "timeout": ""
    }
}

load_method = input("Load from 'file' or 'manual' input? ")

if load_method == "file":
    filename = input("Enter filename: ")
    file_path = Path(filename)

    if file_path.exists():
        with open(filename, "r") as f:
            content = f.read()
        display_config(content, config)
    else:
        print(f"Error: File '{filename}' not found.")

elif load_method == "manual":
    print("Enter configuration (type 'DONE' to finish):")
    lines = []
    while True:
        line = input()
        if line == "DONE":
            break
        lines.append(line)

    content = "\n".join(lines)
    display_config(content, config)