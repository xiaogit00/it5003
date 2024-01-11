message = input()

if ':)' in message and ':(' not in message:
    print('alive')
elif ':(' in message and ':)' not in message:
    print('undead')
elif ':)' in message and ':(' in message:
    print('double agent')
else: 
    print('machine')