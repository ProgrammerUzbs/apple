file = open('test.txt','r')
result = file.read()
print(len(result))

with open('result.txt','w') as f:
    f.write(f"test.txt: {len(result)}")