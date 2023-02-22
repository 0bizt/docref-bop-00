def say(message, times=1):
  print(message * times)

say('Hello')
say('World', 5)

# CAUTION:
# Only those parameters which are at the end of the 
# parameter list can be given default argument values
# for example:
# def func(a, b=5) is valid
# def func(a=5, b) is not valid