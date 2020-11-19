# AUTOGENERATED! DO NOT EDIT! File to edit: utils.ipynb (unless otherwise specified).

__all__ = ['load_config', 'config', 'load_yaml', 'default_yaml']

# Cell

import pkg_resources
import configparser
import yaml

# Cell

def load_config(*configs):
    config = configparser.ConfigParser()
    config.read(configs)
    return config

def config(new_config=None):
    default_config=pkg_resources.resource_filename('pybiotools4p','default.ini')
    if None is new_config:
        print('loading default_config['+default_config+']')
        return load_config(default_config)
    else:
        print('loading default_config and '+ new_config)
        return load_config(pkg_resources.resource_filename('pybiotools4p','default.ini'),new_config)


def load_yaml(*yamls):
    my_dict={}
    for y in yamls:
        with open(y,'r') as yf:
            my_dict.update(yaml.load(yf))
    return my_dict

def default_yaml(new_yaml=None):
    default_config=pkg_resources.resource_filename('pybiotools4p','default.yaml')
    if None is new_yaml:
        print('loading default_config['+default_config+']')
        return load_yaml(default_config)
    else:
        print('loading default_config and '+ new_yaml)
        return load_yaml(pkg_resources.resource_filename('pybiotools4p','default.yaml'),new_yaml)

