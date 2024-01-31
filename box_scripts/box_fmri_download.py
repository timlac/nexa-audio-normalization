from box_sdk_gen.developer_token_auth import BoxDeveloperTokenAuth
from box_sdk_gen.client import BoxClient
import shutil
from box_sdk_gen.utils import ByteStream

from dotenv import load_dotenv
import os
from nexa_coding_interpreter.constants import video_id_pattern
from nexa_coding_interpreter.metadata import Metadata

from fmri_filter import belongs_to_fmri_dataset


def file_exists_in_folder(local_folder_path, filename):
    # List all files in the given directory
    files_in_folder = os.listdir(local_folder_path)

    # Check if the specific file is in the list
    return filename in files_in_folder


def download_file(client, file_id, local_path):
    file_content_stream: ByteStream = client.downloads.download_file(file_id=file_id)
    with open(local_path, 'wb') as f:
        shutil.copyfileobj(file_content_stream, f)
    print(f'File was successfully downloaded to {local_path}')


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


def iterate_files(client):
    for top_level_item in client.folders.get_folder_items('0').entries:
        if top_level_item.name == "Edited":
            for video_id_folder in get_all_items_in_folder(client, top_level_item.id):
                if video_id_pattern.match(video_id_folder.name):
                    for video_id_content in get_all_items_in_folder(client, video_id_folder.id):
                        if video_id_content.name == "audio_video" or video_id_content.name == "audio-video clips":
                            for video_file in get_all_items_in_folder(client, video_id_content.id):
                                yield video_file


def iterate_a65(client):
    for top_level_item in client.folders.get_folder_items('0').entries:
        if top_level_item.name == "Edited":
            for video_id_folder in get_all_items_in_folder(client, top_level_item.id):
                if video_id_folder.name == "A65":
                    for video_id_content in get_all_items_in_folder(client, video_id_folder.id):
                        if video_id_content.name == "normalized audio-video clips":
                            for video_file in get_all_items_in_folder(client, video_id_content.id):
                                yield video_file


def iterate_video_ids(client):
    """
    Only for overview of the videos, not used in dl script
    # TODO: Could probably place within iterate files func
    """
    for top_level_item in client.folders.get_folder_items('0').entries:
        if top_level_item.name == "Edited":
            for video_id_folder in get_all_items_in_folder(client, top_level_item.id):
                if video_id_pattern.match(video_id_folder.name):
                    yield video_id_folder


def list_video_ids():
    auth = BoxDeveloperTokenAuth(token=DEV_TOKEN)
    client = BoxClient(auth=auth)

    i = 0
    for video_id in iterate_video_ids(client):
        print(video_id.name)
        i += 1
    print(i)


def download_fmri():
    download_folder = "../data/box_downloads/"

    auth = BoxDeveloperTokenAuth(token=DEV_TOKEN)
    client = BoxClient(auth=auth)

    for filename in iterate_a65(client):
        if belongs_to_fmri_dataset(filename.name):
            if not file_exists_in_folder(download_folder, filename.name):
                print(f'{filename.name} belongs to fmri dataset, downloading...')
                download_file(client, filename.id, os.path.join(download_folder, filename.name))
            else:
                print(f'{filename.name} already exists, skipping...')


if __name__ == '__main__':
    load_dotenv()
    DEV_TOKEN = os.getenv("BOX_DEV_TOKEN")

    download_fmri()
    # list_video_ids()
