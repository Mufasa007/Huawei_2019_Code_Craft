import os
os.chdir(os.getcwd())
print(os.getcwd())
print(os.path.dirname(os.path.realpath(__file__)))
print(os.path.realpath(__file__))