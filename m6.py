attempts=0
while attempts<3:
    password=input('Enter the Password:')
    if password=='correctpassword':
          print('you are in!')
    else:
        attempts+=1
        print('incorrect!')
        if attempts==3:
            print('too many attempts')
