"""This script should be run on your local machine."""

import requests

API_HOST = 'http://34.223.213.54:5000'

TEST_API = '/test_endpoint'
PREDICT_API = '/predict'
TRAIN_API = '/train'

TEST_PASSENGER_DATA = [{"Age": 85, "Sex": "male", "Embarked": "S"},
                       {"Age": 24, "Sex": "female", "Embarked": "C"}]


def test_endpoint():
    print("Trying test endpoint...")
    url = API_HOST + TEST_API
    print("URL is", url)

    # Try to access the URL. The response will be stored in 'r'.
    r = requests.get(url)

    # The response status code tells us whether or not we were
    # successful in accessing the URL. Generally, HTTP status codes
    # starting with 2 are good and ones starting with 4 or 5 are bad.
    # HTTP status codes:
    # https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
    if r.status_code == 200:
        print("Success!")
        print(r.text)
    else:
        print("Status code indicates a problem:", r.status_code)


def train():
    print("Trying train endpoint...")
    r = requests.get(API_HOST + TRAIN_API)

    if r.status_code == 200:
        print("Success!")
        print(r.text)
    else:
        print("Status code indicates a problem:", r.status_code)


def predict(passenger_data):
    print("Trying predict endpoint...")
    # Note that this is a POST request as we need to send the
    # passenger data to the server.
    # The requests library converts the passenger data into
    # JSON before sending it over. This is because the server
    # expects to receive the passenger data in the form of a JSON.
    r = requests.post(API_HOST + PREDICT_API,
                      json=passenger_data)

    # Also note that we're now using r.json(), not r.text.
    # This is because the server sends its response back as a
    # JSON object, which needs to be decoded by the requests
    # library.
    if r.status_code == 200:
        print("Success!")
        print(r.json())
    else:
        print("Status code indicates a problem:", r.status_code)


def main():
    test_endpoint()
    train()
    predict(TEST_PASSENGER_DATA)

# Entry point for application (i.e. program starts here)
if __name__ == '__main__':
    main()
