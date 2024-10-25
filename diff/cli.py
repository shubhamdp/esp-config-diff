#!/usr/bin/env python3

import click

# ANSI color codes for styling
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

# array to json
def to_json(config):
    json_data = {}
    for line in config:
        parts = line.strip().split('=')
        if len(parts) == 2:
            json_data[parts[0]] = parts[1]
    return json_data

# file to json
def make_config(sdkconfig):
    with open(sdkconfig, 'r') as f:
        conf_lines = f.readlines()
    config = [line.strip() for line in conf_lines if not line.startswith('#')]
    return config

@click.command()
@click.option('--conf', required=True, help='Current config file')
@click.option('--old-conf', required=True, help='Older config file')
@click.option('--no-color', is_flag=True, help='Disable colored output')
def main(conf, old_conf, no_color):
    # Determine if colors should be used
    use_color = not no_color

    # Read the config into lists
    new_conf = make_config(conf)
    old_conf = make_config(old_conf)

    # Remove common config
    for item in new_conf[:]:  # Copy to modify in-place
        if item in old_conf:
            new_conf.remove(item)
            old_conf.remove(item)

    new_conf_json = to_json(new_conf)
    old_conf_json = to_json(old_conf)

    # Generate diff list
    diff_list = []

    # Process new configuration items
    for key, val in new_conf_json.items():
        j = {key: {'old': 'ABSENT', 'new': val}}
        if key in old_conf_json:
            j[key]['old'] = old_conf_json[key]
            old_conf_json.pop(key)
        diff_list.append(j)

    # Process remaining old configuration items
    for key, val in old_conf_json.items():
        j = {key: {'old': val, 'new': 'ABSENT'}}
        diff_list.append(j)

    # Display formatted output
    header = f"{BOLD}{'CONFIG':<60}{'Old Value':<60}{'New Value'}{RESET}" if use_color else f"{'CONFIG':<60}{'Old Value':<60}{'New Value'}"
    print(header)
    print(f"{'='*140}")

    for item in diff_list:
        key = list(item.keys())[0]
        old_val = item[key]['old']
        new_val = item[key]['new']

        # Set color based on value status
        if use_color:
            if old_val == 'ABSENT':
                color = GREEN  # New addition
            elif new_val == 'ABSENT':
                color = RED  # Removed
            else:
                color = YELLOW  # Modified
            reset_color = RESET
        else:
            color = ""
            reset_color = ""

        print(f"{color}{key:<60}{old_val:<60}{new_val}{reset_color}")

if __name__ == '__main__':
    main()
