from app import *
import time

def call():
    print('\n Enter e or exit to quit.')
    count=1
    atmp=welcome()
    start= time.time()
    while True:
        user=int(input('    Enter your guess: '))
        if user  == 'e' or user == 'exit':  #terminate program
            print('Bye!')
            break
        if procced_next(user, count):
            print(f'  It took {int(time.time() - start)} second.')
            break
        if count == atmp:
            fail()
            break
        count+=1


if __name__ == "__main__":
    call()