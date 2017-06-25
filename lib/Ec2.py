import yaml
from lib import RefParser

"""this is a class parsing config into aws template"""

def generate_template(config):
  sgs = config.get('SecurityGroupIds')
  if sgs is not None:
    config['SecurityGroupIds'] = [RefParser.parseRef(sg) for sg in sgs]
  with open('./templates/ec2.yaml', 'r') as f:
    ec2Template = yaml.safe_load(f)
    ec2Template['Properties'].update(config)

  return ec2Template
