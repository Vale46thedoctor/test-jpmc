import os
import http.client
import json

from dotenv import load_dotenv


load_dotenv()


headers = {'Content-type': 'application/json'}

data = {
    'data': os.getenv("TARGET_TEXT")
}

def RestClientGetRequest():
    connection =  http.client.HTTPConnection(os.getenv("TARGET_HOST"), os.getenv("TARGET_PORT"), timeout=10)
    connection.request("POST", "/", json.dumps(data), headers)
    response = connection.getresponse()
    responseData = response.read().decode()
    #print("Response to Connection: " + responseData)

    connection.close()
    return responseData

if __name__ == '__main__':
    RestClientGetRequest()
