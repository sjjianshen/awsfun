import yaml
from lib import RefParser

"""this is a class parsing config into aws template"""

def generate_template(config):
  if config.get('InstanceId') is not None:
    config['InstanceId'] = RefParser.parseRef(config['InstanceId'])
  with open('./templates/eip.yaml', 'r') as f:
    eip_template = yaml.safe_load(f)
    eip_template['Properties'].update(config)
  return eip_template
