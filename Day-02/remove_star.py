string=input()
stack=[]
for i in string:
   if stack and i=='*':
      stack.pop()
   else:
      stack.append(i)
print("".join(stack))         
