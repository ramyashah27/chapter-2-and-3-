name=input('Enter your name\n')
date=input('enter date\n')
letter='''dear friend <|NAME>|
you are selected for tournament
date:<|DATE>|
'''
letter=letter.replace("<|NAME>|", name)
letter=letter.replace("<|DATE>|", date)
print(letter)