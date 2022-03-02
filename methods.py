import os

colors = {
     "red": "\033[91m",
     "green": "\033[32m",
     "cyan": "\033[36m",
     "white": "\033[0m"
}


def getFullPath(ext='.txt'):
     filePath = os.path.join(os.curdir, 'data')
     filesFullPath = [os.path.join(filePath, _) for _ in os.listdir(filePath) if _.endswith(ext)]
     return filesFullPath


def findWords(str2find):

     redC = colors['red']
     greenC = colors['green']
     whiteC = colors['white']
     cyanC = colors['cyan']

     allFiles = getFullPath()

     for file in allFiles:

          if ("/" in file):
               filename  = file.split('/')[-1]
          else: 
               filename = file.split('\\')[-1]

          with open(file,'r') as f:
               lines = f.readlines()
               counter = 0
               for line in lines: 
                    if str2find in line:

                         counter += 1
                         filename = filename.replace(filename, f'{greenC}{filename}{whiteC}')
                         prettified = line.replace(
                              str2find, '%s%s%s' % (redC,str2find,whiteC)
                         )

                         _2print = '- {} : {}'.format(filename, prettified)
                   
                         print(_2print)
               print('{}-------------- TOTAL : {} --------------{}'.format(redC,counter,whiteC))
          print('{}-------------- FILE  : {} --------------\n\n{}'.format(cyanC,file,whiteC))
