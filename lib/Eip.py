import yaml

"""this is a class parsing config into aws template"""

def generate_template(config):
  with open('./templates/eip.yaml', 'r') as f:
    eip_template = yaml.safe_load(f)
    eip_template['Properties'].update(config)
  return eip_template
