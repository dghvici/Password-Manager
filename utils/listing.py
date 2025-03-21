def listing(secret_client):
    secrets = secret_client.list_secrets()
    secrets_manager = secrets["SecretList"]
    list_of_secrets = []
    if len(secrets_manager) == 0:
        print("You have no secrets.")
    else:
        for secret in secrets_manager:
            list_of_secrets.append("{0}".format(secret["Name"]))
            print(list_of_secrets)
