#!/usr/bin/env python3

import sys
import json
import click

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

    config = []
    for line in conf_lines:
        if not line.startswith('#'):
            config.append(line.strip())

    return config

@click.command()
@click.option('--conf', help='current config file')
@click.option('--old-conf', help='older config file')
def main(conf, old_conf):
    # read the config into list
    new_conf = make_config(conf)
    old_conf = make_config(old_conf)

    # remove common config
    for item in new_conf[:]:  # new_conf[:] -> to create a copy, so that we can modify the original list
        if item in old_conf:
            new_conf.remove(item)
            old_conf.remove(item)

    new_conf_json = to_json(new_conf)
    old_conf_json = to_json(old_conf)

    # key = {old_val: old_val, new_val: new_val}
    diff_list = []

    # Find items present in new-conf and remove them from old-conf
    for key, val in new_conf_json.items():
        j = {} 
        j[key] = {'old': 'ABSENT', 'new': val}
        if key in old_conf_json:
            j[key]['old'] = old_conf_json[key]
            old_conf_json.pop(key)

        diff_list.append(j)

    # new-conf will be exhaused at this point so lets get away with remaining items in old-conf
    for key, val in old_conf_json.items():
        j = {}
        j[key] = {'old': val, 'new': 'ABSENT'}
        diff_list.append(j)


    print('{:<60}{:<60}{}'.format('CONFIG', 'Old Value', 'New Value'))
    for item in diff_list:
        key = list(item.keys())[0]
        old_val = item[key]['old']
        new_val = item[key]['new']
        print('{:<60}{:<60}{}'.format(key, old_val, new_val));

if __name__ == '__main__':
    main()
