# import os
#
# def clear_screen():
#     if os.name == 'int':
#         os.system('cls')
#     else:
#         os.system('clear')
#
# print("Test 1")
# clear_screen()
# print("Test 2")

# from IPython.display import clear_output
#
# print("Это сообщение будет на экране")
# clear_output()
# print("Экран очищен")

# import os
#
# print('Hello')
# input()
# os.system('cls||clear')
# print("Привет")
# input()

# import os
#
# print('Hello')
# os.system("printf '\033c'")
# print("Привет")

# from replit import clear
#
# print('Hello')
# clear()
# print("Привет")

import os
import time

def clear():
    os.system("clear")

print("Hello,")
time.sleep(1)
clear()
print("World!")
