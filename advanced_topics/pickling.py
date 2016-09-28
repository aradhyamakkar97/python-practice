import pickle

dick1 = {'a':100,
'b':200,
'c':300}

list1 = [400,500,600]

print(dick1)
print(list1)

output = open("save1.pkl","wb")

pickle.dump(dick1,output,pickle.HIGHEST_PROTOCOL)
pickle.dump(list1,output,pickle.HIGHEST_PROTOCOL)
output.close()
print('..........')

inputFile = open('save1.pkl','rb')

dick2 = pickle.load(inputFile)
list2 = pickle.load(inputFile)

print(dick2)
print(list2)
