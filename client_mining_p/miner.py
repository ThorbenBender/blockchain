import hashlib
import requests
import json

import sys


# TODO: Implement functionality to search for a proof

def valid_proof(last_proof, proof):
    """
    Validates the Proof:  Does hash(last_proof, proof) contain 4
    leading zeroes?
    """
    # encode a guess
    guess = f"{last_proof}{proof}".encode()
    # hashing the guess
    guess_hash = hashlib.sha256(guess).hexdigest()

    # return True if the last 4 digits of the hash ar zreos
    return guess_hash[-4:] == "0000"


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # Run forever until interrupted
    while True:
        # TODO: Get the last proof from the server and look for a new one
        request = requests.get('http://localhost:5000/last_proof')
        last_proof = request.json()['last_proof']
        print(last_proof)
        proof = 0
        while valid_proof(last_proof, proof) is False:
            proof += 1
        # TODO: When found, POST it to the server {"proof": new_proof}
        # TODO: If the server responds with 'New Block Forged'
        response = requests.post(
            'http://localhost:5000/mine', data=json.dumps({'proof': proof}))
        print(response.json())
        # if response.json()['error'] is None:
        #     coins_mined += 1
        #     print('hello')
        # # add 1 to the number of coins mined and print it.  Otherwise,
        # # print the message from the server.
        # else:
        #     print(response.json()['error'])
