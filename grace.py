#asking for user's name and printing it
username = input('💀 what is your name?\n🐨 ')
usernamecapital = username.title()
print(f'💀 Oh hello, {usernamecapital}')

#inroducing itself
userinput = input('💀 I am Grace a personal assistant of Aryan Nagar. So, what can I do for you.\n🐨 ')
userinputnospaces = userinput.replace(" ", "")
x = userinputnospaces.title()

#contact
if x == 'Contact' or x == 'Name':
     print('💀 \nName: Aryan Nagar\nEmail:aryannagarco@gmail.com\nInstagram: aryansnagar\n')

#age
elif x == 'what is his age?' or x == 'what is his age' or x == 'Age':
     print( '💀 18')

#email
elif x == 'what is his email?' or x == 'what is his email' or x == 'Email' or x == 'E-mail':
     print('💀 The E-mail address of Aryan is aryannagarco@gmail.com.')

#instagram
elif x == 'what is his instagram?' or x == 'what is his instagram'  or x == 'Instagram':
     print('💀 The Instagram ID of Aryan is @aryansnagar. ')

#age
elif x == 'what is his education?' or x == 'what is his education' or x == 'Education':
     print( '💀 Highschool: R.N international public school, Meerut - 2020\n   Diploma in mechanical engineering: D.N polytechnic, Meerut - 2023\n   Bachelor in  computer science: Meerut Institute of technology, Meerut - current.')

#end conversation
else:
     print('💀 Sorry, I can not help you with this. please check the spelling of words you provided or maybe you used the spaces inappropriately.')

end = input('💀 Anything else..\n🐨 ')
