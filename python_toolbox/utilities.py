
def isnamed(item):
  try:
    item.__name__
    return True
  except:
    return False
