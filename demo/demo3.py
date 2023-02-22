def ask_ok(prompt, retries=4, reminder="Please try again!"):
  while True:
    ok = input(prompt)
    if ok in ('y', 'ye', 'yes'):
      return True
    if ok in ('n', 'no', 'nop', 'nope'):
      return False
    retries = retries - 1
    if retries < 0:
      raise ValueError('invalid user response')
    print(reminder)



i = 5

def f(arg=i):
  print(arg)

i = 6


def f2(a, L=[]):
  L.append(a)
  return L

def f3(a, L=None):
  if L is None:
    L = []
  L.append(a)
  return L


print(f3(1))
print(f3(2))
print(f3(3))

