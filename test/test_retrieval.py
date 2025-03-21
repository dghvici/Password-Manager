
from moto import mock_aws
import boto3
import os
import pytest
from unittest.mock import patch
from utils.retrieval import retrieval
import json
import regex as re 
from botocore.exceptions import ClientError


@pytest.fixture(scope="function", autouse=True)
def aws_credentials():
    """Mocked AWS Credentials for moto."""

    os.environ["AWS_ACCESS_KEY_ID"] = "test"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
    os.environ["AWS_SECURITY_TOKEN"] = "test"
    os.environ["AWS_SESSION_TOKEN"] = "test"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"

@pytest.mark.skip
class TestRetrieval:

    @pytest.mark.skip
    def test_retrieval_returns_message_upon_successful_retrieval(aws_credentials):
            with mock_aws():
                secret_client = boto3.client('secretsmanager')
                secret = secret_client.create_secret(
                Name="gg", SecretString=f'"Username": "gg", "Password": "gg"')
                response = retrieval(secret_client)
                assert response == f"Secrets stored in local file secretsgg.txt"

    @pytest.mark.skip
    def test_retrieval_writes_name_username_password_of_secret_to_file(aws_credentials):
            result = None
            with mock_aws():
                secret_client = boto3.client('secretsmanager')
                secret = secret_client.create_secret(
                Name="gg",  SecretString=json.dumps({"Username": "gg", 
                                                     "Password": "gg"}))
                retrieval(secret_client)
            
                #file path
                with open("secrets.txt", "r") as output:
                    result = output.read()
                pattern = r"'Name': '([^']*)'|'Credentials': '{\"Username\": \"([^\"]*)\", \"Password\": \"([^\"]*)\"}'"
                match = re.findall(pattern, result)
                extracted_values = {
                    'Name': match[0][0],
                    'Username': match[1][1],
                    'Password': match[1][2]
                }
                
                assert extracted_values == {"Name": "gg", "Username": "gg", "Password": "gg"}

    @pytest.mark.skip
    def test_retrieval_writes_name_username_password_of_secret_to_file(aws_credentials):
                with mock_aws():
                    secret_client = boto3.client('secretsmanager')
                    secret= retrieval(secret_client)
                    print(secret)
                    assert secret == 'Cannot find a secret with specified ID.' 