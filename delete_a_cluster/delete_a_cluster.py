#Delete a cluster
import requests
import json
import sys
import time


def get_request(url,username,password):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers,auth=(username, password))
    if(response.status_code == 200):
        data = json.loads(response.text)
    else:
        print ("Error reaching the server.")
        exit(1)
    return data


def poll_on_id(url,username,password):
    status = get_request(url,username,password)['status']
    c = 0
    while(status == 'IN_PROGRESS'):
        c = c+1
        n = c%6
        print ("\rOperation in progress" + "."*n + " "*(5-n),end = "")
        status = get_request(url,username,password)['status']
        time.sleep(5)
    print ("")
    return status

def get_help():
    help_description = '''\n\t\t----Delete Cluster----
    Usage:
    python delete_.clusterpy <hostname> <username> <password> <domain_id>\n'''
    print (help_description)

def delete_cluster():
    arguments = sys.argv
    if(len(arguments) < 3):
        get_help()
        return
    hostname = 'https://'+arguments[1]
    username = arguments[2]
    password = arguments[3]
    cluster_id = arguments[4]
    headers = {'Content-Type': 'application/json'}
    data = '{"markForDeletion" : true}'
    url = hostname+'/v1/clusters/'+cluster_id
    response = requests.patch(url, headers=headers,data=data,auth=(username, password))
    if(response.status_code == 200):
        response = requests.delete(url, headers=headers,data=data,auth=(username, password))
        if(response.status_code == 202):
            response = json.loads(response.text)
            task_id = response['id']
            url = hostname+'/v1/tasks/'+task_id
            result = poll_on_id(url,username,password)
            print ("Cluster deletion Status:" + result)
        else:
            print ("Error while deleting.")
        print (json.dumps(response,indent=4, sort_keys=True))
    else:
        print ("Error reaching the server.")
        exit(1)
delete_cluster()
