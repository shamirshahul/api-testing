import requests
from requests.structures import CaseInsensitiveDict
import json

user_id = None

#url
url="https://gorest.co.in"

#Authetication token
headers= CaseInsensitiveDict()
headers["Authorization"] = "Bearer 1560b8efcd7228fc4f6a50abb2681610dc2dcedfd3f7d29951003188eeb9d3ad"

#json data
file = open("data.json",'r')
json_input = file.read()
request_json = json.loads(json_input)

#edit json data
editfile = open("edit.json",'r')
edit_json_input = editfile.read()
edit_request_json = json.loads(edit_json_input)


def getUser():
    getapi = url + "/public-api/users"
    response = requests.get(getapi,headers= headers)
    if response.status_code == 200:
        print("get users api Success")
    else:
        print("get users api fails")

def negativeCreateUser():
    global user_id
    #Not authentication token
    createapi = url + "/public-api/users"
    response = requests.post(createapi,  json=request_json)
    res = response.json()
    if response.json()['code'] == 401:
        print("no authentication create user api success,error returned")
    else:
        print("no authentication create user api fails")

def createUser():
    global user_id
    createapi = url + "/public-api/users"
    response = requests.post(createapi, headers= headers, json=request_json)
    res = response.json()['data']
    user_id =str(res['id'])
    if response.json()['code'] == 201:
        print("positive create user api success")
    else:
        print("positive create user api fails")


def getspecificUser():
    getspecapi = url + "/public-api/users/" + user_id
    response = requests.get(getspecapi,  headers= headers)
    if response.json()['code'] == 200:
        print("get a user api success")
    else:
        print("get a user api fails")

def editUser():
    editapi= url + "/public-api/users/" + user_id
    response = requests.put(editapi, headers=headers, json=edit_request_json)
    if response.json()['code'] == 200:
        print("edit user api success")
    else:
        print("edit user api fails")


def negativeDeleteUser():
    #wrong user id
    delapi = url + "/public-api/users/7666"
    response = requests.delete(delapi, headers=headers)
    if response.json()['code'] == 404:
        print("Negative delete user api success")
    else:
        print("Negative delete user api fails")


def deleteUser():
    delapi = url + "/public-api/users/" + user_id
    response = requests.delete(delapi, headers=headers)
    if response.json()['code'] == 204:
        print("Positive delete user api success")
    else:
        print("Positive delete user api fails")


getUser()
negativeCreateUser()
createUser()
getspecificUser()
editUser()
negativeDeleteUser()
deleteUser()





