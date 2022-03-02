import methods as m
import sys

if __name__ == '__main__':
     try:
          print('\n')
          str2find = sys.argv[1]
          m.findWords(str2find)
     except IndexError:
          print("\n\tPlease provide an argumemt\n\tExample: python main.py foo\n")


#     print('Hrishabh Goel')