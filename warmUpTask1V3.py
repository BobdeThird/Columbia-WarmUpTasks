# imports
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import json

# define query
query = gql('''query($owner:String!, $name:String!){
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
''')

# define headers
headers = {'Authorization': 'bearer AUTH_TOKEN',
          'Accept' : 'application/vnd.github.hawkgirl-preview+json',
          'Content-Type' : 'appliction/json'
        }

# variables for query
owner = 'psf'
name = 'requests'
variables = {'owner': owner, 'name': name}

# query endpoint
url = 'https://api.github.com/graphql'

# build request framework
transport = RequestsHTTPTransport(url=url, headers = headers, use_json = True)

# Create the client
client = Client(transport = transport, fetch_schema_from_transport= True)


r = client.execute(query, variable_values=variables) # dictionary format


# print query
print('-'*100)
print(r)
print('-'*100)
print(type(r))
print('-'*100)


# format the output (String)
jsonR = json.dumps(r, indent = 4, separators=(',', ': '), sort_keys=True)

# print the new formatted version
print(jsonR)
