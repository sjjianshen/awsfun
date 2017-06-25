def parseRef(sg):
  if sg.startswith('!Ref'):
    return {"Ref": sg.split(' ')[1]}
  return sg
