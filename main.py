import json
import requests

def get_api():
    '''
    Returns the result of the API call that generates random number, string formatted..

            Returns:
                   json_result (str): Binary string containing JSON API call result.
    '''
    api = requests.get('https://random-data-api.com/api/code/random_code').text
    json_result = json.loads(api)
    return json_result

def is_even(npi):
    '''
    Returns the parity of a number.

            Parameters:
                    npi (int): A string containing an integer.

            Returns:
                    Ternary (boolean): Return True if the number is even, False otherwise.
    '''
    return int(npi) % 2 == 0


def main():
    '''
    Retrieves two random numbers from the API and checks that they are both even.

            Returns:
                    Boolean : Return True if both are even, False otherwise.
    '''
    first_call = get_api()
    second_call = get_api()
    return is_even(first_call['npi']) and is_even(second_call['npi'])

if __name__ == "__main__":
    print(main())
