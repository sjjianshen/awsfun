import yaml
import subprocess

def deploy(stack_name, template):
  with open('template.yaml', 'w') as f:
    yaml.dump(template, f, default_flow_style=False)
  action = 'create'
  if is_stack_created(stack_name):
    action = 'update'
  ret = subprocess.run(['aws', 'cloudformation', '{}-stack'.format(action), '--stack-name', stack_name, '--template-body', yaml.dump(template)])

def is_stack_created(stack_name):
  ret = subprocess.run(['aws', 'cloudformation', 'describe-stacks', '--stack-name', stack_name])
  return ret.returncode == 0
