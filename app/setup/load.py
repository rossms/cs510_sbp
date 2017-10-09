fname = raw_input('Please provide a file and absolute path..')
print (fname)

with open(fname) as f:
    content = f.read()

print (content)
