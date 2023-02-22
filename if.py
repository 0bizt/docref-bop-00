number = 23
guess = int(input('Enter an integer: '))

if guess == number:
  # New block starts here
  print("Congratulations, you guess it.")
  print('(but you do not win any prizes!)')
  # New block ends here
elif guess < number:
  # Another block
  print('No, it is a little higher than that')
  # You can do whatever you want in a block...
else:
  print('No, it is a little lower than that')
  # you mus have guessed > number to reach here

print('Done')
# This is statement is always executed,
# after the if statement is executed.