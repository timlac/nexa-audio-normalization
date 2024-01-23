from box_sdk_gen.client import BoxClient
from box_sdk_gen.jwt_auth import BoxJWTAuth, JWTConfig

jwt_config = JWTConfig.from_config_file(
    config_file_path='/home/tim/.config/box-file-downloader-2.0/252066_212a53z3_config.json')

auth = BoxJWTAuth(config=jwt_config)
client = BoxClient(auth=auth)

service_account = client.users.get_user_me()
print(f'Service Account user ID is {service_account.id}')
