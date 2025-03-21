from utils.deletion import deletion
import os
import pytest
import boto3
from moto import mock_aws

@pytest.fixture(scope="function", autouse=True)
def aws_credentials():
    """Mocked AWS Credentials for moto."""

    os.environ["AWS_ACCESS_KEY_ID"] = "test"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
    os.environ["AWS_SECURITY_TOKEN"] = "test"
    os.environ["AWS_SESSION_TOKEN"] = "test"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"

@pytest.mark.skip
class TestDeletion:
    
    def test_removes_secret_from_secret_manager(aws_credentials):
         with mock_aws():
                secret_client = boto3.client('secretsmanager')
                secret = secret_client.create_secret(
                Name="Test", SecretString=f'"Username": "Test_User", "Password": "Test_Pass"')
                response = deletion(secret_client)
                assert response == 'The secret has been deleted.'

    def test_raises_error_with_non_existent_secret_id(aws_credentials):
         with mock_aws():
                secret_client = boto3.client('secretsmanager')
                response = deletion(secret_client)
                assert response == "Secrets Manager can't find the specified secret - or you have changed your mind"
