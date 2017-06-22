from lib import Eip
from lib import Sg
import yaml

def dump(config):
  eips = config['eip']
  eip_templates = { key:Eip.generate_template(value) for key, value in eips.items() }
  sgs = config['sg']
  sg_templates = { key:Sg.generate_template(value) for key, value in sgs.items() }
  with open('templates/cloudformation.yaml', 'r') as f:
    cloud_template = yaml.safe_load(f)
  cloud_template['Resources'].update(eip_templates)
  cloud_template['Resources'].update(sg_templates)
  return cloud_template
