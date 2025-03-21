from botocore.exceptions import ClientError


def entry(secret_client, Name=None, password=None, user_id=None):
    try:
        Name = input("Secret identifier: ")
        user_id = input("UserId: ")
        password = input("Password: ")
        secret = secret_client.create_secret(
            Name=Name, SecretString=f'"Key": {user_id}, "Value": {password}'
        )
        print("Secret saved.")
    except ClientError as e:
        print("Secret already exists.")
