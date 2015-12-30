import os
from sys import argv,exit 

#Take bundle as argument
workdir = argv[1]




#Generating Rest Controller
f = os.popen("find ./src -type d -name \"Entity\" | xargs ls -A | cut -d . -f1")
result = f.read()
entities = result.split('\n')
entities.pop()
for entity in entities:
    myReturn = os.system("php app/console voryx:generate:rest --entity=\""+workdir+":"+entity+"\"")
print(myReturn)


exit
