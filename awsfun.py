#!/usr/bin/env python3

import sys
import os.path
import yaml
from lib import AwsDumper
from lib import AwsCreator

print('Number of arguments: {} arguments'.format(len(sys.argv)))
print('Argument List: {}'.format(str(sys.argv)))

def usage():
  print('awsfun create [ -c /path/to/config/file ]')

def load_config(config_path):
  with open(config_path, 'r') as f:
    config = yaml.safe_load(f)
  return config['stack_name'], config['resources']

def main(args):
  arg_size = len(args)
  if arg_size != 1 and arg_size != 3:
    print('invalid arguments number')
    usage()
    sys.exit(1)

  if arg_size == 1:
    config_path = 'resource.yml'
  else:
    if args[1] != '-c':
      print('invalid option {}'.format(args[1]))
      usage()
      sys.exit(1)
    config_path = args[2]
  if not os.path.exists(config_path):
    print('config file not found at {}'.format(config_path))
    usage()
    sys.exit(1)

  stack_name, config = load_config(config_path)

  if not stack_name:
    print('stack_name is required in config file')
    sys.exit(1)

  if args[0] == 'create':
    template = AwsDumper.dump(config)
    AwsCreator.deploy(stack_name, template)
  elif args[0] == 'dump':
    template = AwsDumper.dump(config)
    print(yaml.dump(template, default_flow_style=False))
  else:
    print('invalid subcommand {}'.format(args[0]))
    usage()
    sys.exit(1)
  template_path = './config/default.yaml'
if __name__ == "__main__":
     main(sys.argv[1:])
