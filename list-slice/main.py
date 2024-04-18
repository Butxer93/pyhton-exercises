tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

print(tags[1:4:2]) # ['development', 'code']

slice_obj = slice(1, 4, 2)

print(slice_obj.start) # 1
print(slice_obj.stop) # 4
print(slice_obj.step) # 2

print(tags[slice_obj]) # ['development', 'code']