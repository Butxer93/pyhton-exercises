tags = ['python', 'development', 'tutorials', 'code']

# Nope
tags[-1] = 'Programming' # ['python', 'development', 'tutorials', 'Programming']

# In Place
tags.extend('Programming') # ['python', 'development', 'tutorials', 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
tags.extend(['Programming']) #  ['python', 'development', 'tutorials', 'Programming']

# New List
new_tags = tags + ['Programming'] # ['python', 'development', 'tutorials', 'Programming']

print(new_tags)

print(tags)