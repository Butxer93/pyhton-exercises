role = 'guest'

auth = 'can access' if role == 'admin' else 'cannot access'
# Zen of Python: Simple is better than complex.

if role == 'admin':
  auth = 'can access'
else:
  auth = 'cannot access'

print(auth)