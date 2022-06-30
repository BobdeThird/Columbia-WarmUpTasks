import json
import pandas as pd
import requests
from pandas.io.json import json_normalize
from pandas import DataFrame

# query to call for dependencies
query = """ query($owner:String!, $name:String!){
  repository(owner: $owner, name: $name) {
    dependencyGraphManifests {
      totalCount
      nodes {
        filename
      }
      edges {
        node {
          blobPath
          dependencies {
            totalCount
            nodes {
              packageName
              requirements
              hasDependencies
              packageManager
            }
          }
        }
      }
    }
  }
}
"""

# owner & name of repo
owner = 'psf'
name = 'requests'

# variables for query
variables = {'owner': owner, 'name': name}

# query endpoint
url = 'https://api.github.com/graphql'

# headers 
headers = {'Authorization': 'bearer AUTH_TOKEN',
          'Accept' : 'application/vnd.github.hawkgirl-preview+json',
          'Content-Type' : 'appliction/json'
        }

# requests for output of query
r = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)

# print the status code (200) and raw text
print(r.status_code)
print(r.text)

print('-'*100)

# print a formatted version of the raw output
strversion = str(r.text)
newstr = ""
numIndents = 0
for i in strversion:
  if i == "{":
    newstr += i
    numIndents += 1
    newstr += '\n'
    for j in range(numIndents):
      newstr += '\t'
  elif i == ",":
    newstr += i
    newstr +='\n'
    for j in range(numIndents):
      newstr += '\t'
  elif i == "}":
    numIndents -= 1
    newstr += '\n'
    for j in range(numIndents):
      newstr += '\t'
    newstr += i
  else:
    newstr += i

print(newstr)