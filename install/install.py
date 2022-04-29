import os

print('Intalling all required things...')
try:
    os.system("pip install -r requirements.txt")
    print('DONE!')
except exception as e:
    print("Error!",e)
    
os.system("PAUSE")