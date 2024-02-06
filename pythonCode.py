#!/usr/bin/env python3
import yaml

def writeYaml(data):
    with open("output.yaml", "w") as write_file:
       yaml.dump(data, write_file)
