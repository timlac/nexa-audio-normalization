from box_sdk_gen.developer_token_auth import BoxDeveloperTokenAuth
from box_sdk_gen.client import BoxClient
from dotenv import load_dotenv
import os
from nexa_coding_interpreter.constants import video_id_pattern


def get_all_items_in_folder(client, folder_id):
    all_items = []
    offset = 0
    limit = 100

    while True:
        response = client.folders.get_folder_items(folder_id=folder_id, offset=offset, limit=limit)
        all_items.extend(response.entries)

        if len(response.entries) < limit:
            break

        offset += limit

    return all_items


def main(token: str):
    auth = BoxDeveloperTokenAuth(token=token)
    client = BoxClient(auth=auth)
    video_id_dict = {}

    for top_level_item in client.folders.get_folder_items('0').entries:
        if top_level_item.name == "Edited":
            for video_id_folder in get_all_items_in_folder(client, top_level_item.id):
                if video_id_folder.name == "A101":
                    video_id_dict[video_id_folder.name] = []
                    print()
                    print(video_id_folder.name)
                    for video_id_content in get_all_items_in_folder(client, video_id_folder.id):
                        if video_id_content.name == "audio_video" or video_id_content.name == "audio-video clips":
                            print(video_id_content.name)
                            for video_file in get_all_items_in_folder(client, video_id_content.id):
                                print(video_file.name)
                                video_id_dict[video_id_folder.name].append(video_file.name)

    return video_id_dict


load_dotenv()

DEV_TOKEN = os.getenv("BOX_DEV_TOKEN")

if __name__ == '__main__':
    video_id_dict = main(DEV_TOKEN)

    for key, val in video_id_dict.items():
        print(key)
        print(len(val))
        print()
