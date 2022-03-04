import json
import os
# import requests
# from simple_crud import Delete
# def insert():
#     if(os.path.exists("crude.json")): 
#         with open('crude.json','r') as f:
#             b=json.load(f)
#             c={}
#             c["Name"]=input("Enter the name:- ")
#             c["Email"]=input("Enter the Email:- ")
#             c["Password"]=input("Enter the password:- ")
#             b.append(c)
#             with open('crude.json','w') as y:
#                 json.dump(b,y,indent=4)
#     else:
#         with open('crude.json','w') as l:
#             l.write('[]')
# insert()

# def Update():
#     if(os.path.exists("crude.json")):
#         n=input("enter the password:- ")
#         with open('crude.json','r') as l:
#             p=json.load(l)
#             for j in p:
#                 for r in j.values():
#                     if n==r:
#                         j["Name"]=input("Enter the name:- ")
#                         j["Password"]=input("Enter the password:- ")
#                 with open ('crude.json','w') as ll:
#                     json.dump(p,ll,indent=4)
#     else:
#         with open('crude.json','w') as l:
#             l.write('[]')
# # Update()

# def Delete():
#     if(os.path.exists("crude.json")):
#         user=input("Enter the password:- ")
#         with open('crude.json','r') as kk:
#             m=+0
#             bb=json.load(kk)
#             for w in bb:
#                 m=+1
#                 for v in w.values():
#                     if v==user:
#                         bb.pop(m-1)
#                 with open('crude.json','w') as q:
#                     json.dump(bb,q,indent=4)
#     else:
#         with open('crude.json','w') as g:
#             g.write('[]')
# # Delete()
# a=int(input("1. add user:- \n2. update usere:- \n3. delete user:- \n"))
# if a==1:
#     insert()
# elif a==2:
#     Update()
# elif a==3:
#     Delete()
    







