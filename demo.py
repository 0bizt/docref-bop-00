users = {'Hans': 'active', 'Jerry': 'active', 'Leo': 'inactive'}

# Strategy: Iterate over a copy
# for user, status in users.copy().items():
#   if status == 'inactive':
#     del users[user]

# Strategy: Create a new collection of inactive users
inactive_users = {}
for user, status in users.items():
  if status == 'inactive':
    inactive_users[user] = user

# Strategy: Create a new collection of active users
active_users = {}
for user, status in users.items():
  if status == 'active':
    active_users[user] = status

print(inactive_users)
print(active_users)