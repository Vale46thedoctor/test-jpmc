# test-jpmc

In order to run the test someone first needs to start the RestServer simply by running RestServer.py.

You can modify the .env file to change some parameters for the server such as the host and port.

In order to run the client you can just run the RestClient.py file with the appropriate parameters in the .env file.
If you need to run the test which calculates the percentages of success and failures and asserts the result you can simply run: python -m unittest TestClient.MyTestCase.test_something
