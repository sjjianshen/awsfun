from lib import Eip
from lib import Sg
from lib import Ec2
import yaml

def dump(config):
  eips = config['eip']
  eip_templates = { key:Eip.generate_template(value) for key, value in eips.items() }
  sgs = config['sg']
  sg_templates = { key:Sg.generate_template(value) for key, value in sgs.items() }
  ec2s = config['ec2']
  ec2_templates = { key:Ec2.generate_template(value) for key, value in ec2s.items() }
  with open('templates/cloudformation.yaml', 'r') as f:
    cloud_template = yaml.safe_load(f)
  cloud_template['Resources'].update(eip_templates)
  cloud_template['Resources'].update(sg_templates)
  cloud_template['Resources'].update(ec2_templates)
  return cloud_template
