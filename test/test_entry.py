from moto import mock_aws
import boto3
import os
import pytest
from utils.entry import entry
from unittest.mock import patch
from utils.listing import listing


@pytest.fixture(scope="function", autouse=True)
def aws_credentials():
    """Mocked AWS Credentials for moto."""

    os.environ["AWS_ACCESS_KEY_ID"] = "test"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
    os.environ["AWS_SECURITY_TOKEN"] = "test"
    os.environ["AWS_SESSION_TOKEN"] = "test"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


def get_user_input():
    return input("Enter a number: ")


inputs = patch("builtins.input", return_value=["secret_name", "user_id", "password"])


class TestEntry:

    def test_entry_records_secret(aws_credentials):
        with mock_aws():
            secret_client = boto3.client("secretsmanager")
            response = entry(secret_client)
            assert response == "Secret saved."

    def test_entry_records_secret_to_secret_manager(aws_credentials):
        with mock_aws():
            secret_client = boto3.client("secretsmanager")
            new_secret = entry(secret_client)
            secrets = secret_client.list_secrets()
            assert secrets["SecretList"][0]["Name"] == "gg"

    def test_entry_raises_error_id_secret_exists(aws_credentials):
        with mock_aws():
            secret_client = boto3.client("secretsmanager")
            entry(secret_client)
            response = entry(secret_client)
            assert response == "Secret already exists."
