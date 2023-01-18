# voting 

name = input('what is your name:')
change = int(input('what do you wanna change this year:'))
if(change>=18):
  print('good')
else:
  print('you cant participate in the voting yada yda because you are'+str(change)+'years old you can after'+str(18-change)+'done')
