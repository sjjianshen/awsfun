import yaml

"""this is a class parsing config into aws template"""
portMapping = {'http': 80, 'ssh': 22, 'https': 443}

def generate_template(config):
  with open('./templates/security_group.yaml', 'r') as f:
    sgTemplate = yaml.safe_load(f)
    tags = []
    if config.get('Tags'):
      tags = config.get('Tags')
    sgTemplate['Properties']['Tags'].extend(tags)
    sgTemplate['Properties']['VpcId'] = config.get('VpcId')
    sgTemplate['Properties']['GroupDescription'] = config.get('GroupDescription')
    rules = []
    allowEntries = config.get('allow')
    if allowEntries is None:
      return sgTemplate
    for key, value in allowEntries.items():
      if key == 'tcp':
        rules.extend(buildTcpRules(value))
      elif key == 'icmp':
        rules.append(buildIcmpRules(value))
    sgTemplate['Properties']['SecurityGroupIngress'] = rules
  return sgTemplate

def buildTcpRules(config):
  return [ buildRule('tcp', portMap(key), value) for key, value in config.items() ]

def buildIcmpRules(config):
  return {'IpProtocol': 1, 'FromPort': -1, 'ToPort': -1, **config.get('from')}
def portMap(key):
  if type(key) == str:
    return portMapping.get(key)
  return key

def buildRule(protocol, port, value):
  return {'IpProtocol': protocol, 'FromPort': port, 'ToPort': port, **value.get('from')}

