secret = 'password123!'

password = 'thisisnotapassword' #nohorus

command = 'print "this command is not secure!!"'

exec(command)

print(secret)

assert 2 + 2 == 5, "Wrong!"


import pickle
serialized_data = input("Enter serialized data: ")
deserialized_data = pickle.loads(serialized_data.encode('latin1'))  # Unsafe deserialization


