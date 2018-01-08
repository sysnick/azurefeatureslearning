from azure.keyvault import KeyVaultClient,KeyVaultAuthentication
from azure.common.credentials import ServicePrincipalCredentials

#from azure.keyvault import K
credentials = None

def auth_callack(server,resource,scope):

    credentials =  ServicePrincipalCredentials(
        client_id='73d64247-3c9e-493c-9ae3-3abae61ee024',
        secret = '44QXoAKboDS5AIkXKmjUEsiu2AEneiHXFA6dfUB0i1U=',
        tenant = 'microsoft.onmicrosoft.com',
        resource = resource
    )

    token = credentials.token
    return token['token_type'],token['access_token']



client = KeyVaultClient(KeyVaultAuthentication(auth_callack))


vault_url = 'https://contosodemokeyvault.vault.azure.net/'

key_name = 'contosodemokey1'

key_version = '73cc4eca25b9409a83f57fdf8c55c82a'

key_bundle = client.get_key(vault_url,key_name,key_version)

json_key = key_bundle.key

print(json_key)

