# test-jpmc

requirements: 
 1. pip install -r test_jpmc.egg-info/requires.txt --user
 2. python 3.11


In order to run the test someone first needs to start the RestServer simply by running python RestServer/main.py.

You can modify the .env file to change some parameters for the server such as the SERVER_HOST, SERVER_PORT and SERVER_VALIDATION_TEXT.

In order to run the client you can just run the RestClient.py file with the appropriate parameters in the .env file.

If you need to run the test which calculates the percentages of success and failures and asserts the result you can simply run inside RestClient folder: python  -m unittest TestClient.MyTestCase.test_something
You can modify the number of requests send from the TEST_QUANTITY environmental variable in .env file of the client.
Important: TARGET_TEXT  and SERVER_VALIDATION_TEXT should match otherwise the server will respond with 400 and a customized message. 
Logs are commented out and can be commented in for more insights.
The assertion criteria have a range of +-2 points for each percentage.