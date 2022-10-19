import code

print("test case 1 : [1,4,5]")
if code.min([1,4,5]) == 1:
	print("Passed!")
else: 
	print("Failed!")

print("test case 2 : [96,28,50,3,7]")
if code.min([96,28,50,3,7]) == 3:
	print("Passed!")
else: 
	print("Failed!")

print("test case 3 : [-1,1]")
if code.min([-1,1]) == -1:
	print("Passed!")
else: 
	print("Failed!")

print("test case 4 : [], no error")
try:
	code.min([])
except:
	print("Failed!")
else:
	print("Passed!")