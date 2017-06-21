from lib import Eip
import yaml

def dump(config):
  eips = config['eip']
  eip_templates = { key:Eip.generate_template(value) for key, value in eips.items() }
  with open('templates/cloudformation.yaml', 'r') as f:
    cloud_template = yaml.safe_load(f)
  cloud_template['Resources'].update(eip_templates)
  return cloud_template
