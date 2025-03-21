from utils.listing import listing
from moto import mock_aws
import boto3
import os
import pytest


@pytest.fixture(scope="function", autouse=True)
def aws_credentials():
    """Mocked AWS Credentials for moto."""

    os.environ["AWS_ACCESS_KEY_ID"] = "test"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
    os.environ["AWS_SECURITY_TOKEN"] = "test"
    os.environ["AWS_SESSION_TOKEN"] = "test"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


# @pytest.mark.skip
class TestListing:

    def test_listing_return_message_when_no_secrets(self, aws_credentials):
        with mock_aws():
            secret_client = boto3.client("secretsmanager")
            response = listing(secret_client)
            assert response == "You have no secrets."

    def test_listing_return_a_list_of_secrets(self, aws_credentials):
        with mock_aws():
            secret_client = boto3.client("secretsmanager")
            secret = secret_client.create_secret(Name="test_secret")
            response = listing(secret_client)
            assert response == ["test_secret"]
