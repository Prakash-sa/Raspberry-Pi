import os,sys

#k=os.system("wget http://www.pdf995.com/samples/pdf.pdf")
#print("     \n\n"+str(k)+"   \n\n")
#k=os.system('evince pdf.pdf')
#print(k)

import glob
na1='pdf'
na=na1+'.pdf'
#for name in glob.glob('pdf.*'):
#    if na!=name:
##        os.system("wget http://www.pdf995.com/samples/pdf.pdf")
##        os.system('evince '+str(na))
#        print('1')
#    else :
##        os.system('evince '+str(na))
#        print('0')
from pathlib import Path
p = Path('.')
na='pdf1'
name=na+'.pdf'
for name in p.glob(name):
    print('hi')
        
