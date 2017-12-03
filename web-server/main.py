#!/usr/bin/python
import requests
import os
from flask import Flask
from flask import request
from subprocess import call
app = Flask(__name__)

def kill_pod(pod_name):
  headers = {"Authorization": "Bearer "+token}
  print "kill_pod"
  url=apiserver+"/api/v1/namespaces/"+namespace+"/pods/"+pod_name
  print "about to call "+url
  try:
     ret=requests.delete(url, headers=headers, verify=False)
     print "after call to "+url
     print ret.status_code
     print ret.json()
     print str(ret)
     return str(ret)
  except requests.exceptions.RequestException as e:
        print "failed connecting "+apiserver
        print str(e)

@app.route("/")
def hello():
    pod_name=request.args.get('pod_name')
    print pod_name
    ret=kill_pod(pod_name)
    return ret

if __name__ == '__main__':
   apiserver = os.environ['apiserver']
   print apiserver
   token = os.environ['token']
   namespace = os.environ['namespace']
   print namespace
   port = os.environ['port']
   app.run(host='0.0.0.0',port=port)
