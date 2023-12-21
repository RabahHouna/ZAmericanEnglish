from random import choice
from subprocess import call

list_py = ['01 Knowledge and understanding.py','02 Memory and mind.py', '03 Communicating.py', '04 Priorities and decisions.py', '05 Relationships.py', '06 Help and encouragement.py', '07 Involvement and interest.py']


a = 0
b = 1
while a!=b:
    a = choice(list_py)
    b = choice(list_py)
call(['python',f'{a}'])