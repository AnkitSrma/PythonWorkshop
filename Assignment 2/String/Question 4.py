def add_string(st):
  l = len(st)

  if l > 2:
    if st[-3:] == 'ing':
      st += 'ly'
    else:
      st += 'ing'

  return st
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))
