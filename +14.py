#password check


#password check
print('#make sure your password contains alphabits and numbers# ')

pas = input("write a password: ")

if(pas.isalnum):
  print('password valid')

else:
  print('password invalid')
