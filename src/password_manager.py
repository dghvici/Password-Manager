import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import boto3
from utils.listing import listing
from utils.entry import entry
from utils.retrieval import retrieval
from utils.deletion import deletion


"""Check for connection to AWS Account"""
sts = boto3.client('sts')
try:
    sts.get_caller_identity()
    print("Credentials are valid.")
except boto3.exceptions.ClientError:
    print("Credentials are NOT valid.")

"""Connection to AWS SecretsManager"""
secret_client = boto3.client('secretsmanager')


"""Password Managment Application"""
def password_manager_real(secret_client):
    response = None
    while response != 'x':
        response = input('Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it: ')
        if response not in ['e', 'r', 'd', 'l', 'x']:
            print('Invalid input.')
        elif response == 'l':
            listing(secret_client)
        elif response == 'e':
            entry(secret_client)
        elif response =='r':
            retrieval(secret_client)
        elif response =='d':
            deletion(secret_client)
        elif response =='x':
            print('Thank you. Goodbye.')
    return secret_client

if __name__ == '__main__':
   password_manager_real(secret_client)