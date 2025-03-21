from botocore.exceptions import ClientError


def deletion(secret_client):
    SecretID = input("What secret would you like to delete? (Input any letter key if you change your mind): ")
    try:
        secret_client.delete_secret(SecretId=SecretID, ForceDeleteWithoutRecovery=False)
        print("The secret has been deleted.")
    except ClientError as e:
        print("Secrets Manager can't find the specified secret - or you have changed your mind")
