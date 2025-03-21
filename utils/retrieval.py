from botocore.exceptions import ClientError

def retrieval(secret_client):
    try:
        SecretIDInput = input("Secret identifier: ")
        response = secret_client.get_secret_value(SecretId=SecretIDInput)
        desired_response = {
            "Name": response["Name"],
            "Credentials": response["SecretString"],
        }
        with open(f"secrets{SecretIDInput}.txt", "w") as f:
            f.write(str(desired_response))
        outcome = f"Secrets stored in local file secrets{SecretIDInput}.txt"
        print(outcome)
        return outcome
    except ClientError as e:
        outcome = "Cannot find a secret with specified ID."
        print(outcome)
        return outcome
