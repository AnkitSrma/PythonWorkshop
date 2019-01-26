def change_char(st):
  char = st[0]
  st = st.replace(char, '$')
  st = char + st[1:]
  return st
print(change_char('restart'))
