import requests as rq
from pathlib import Path
import files_callback, validators

from typing import List


class ImageSrcUrlDownload:
    def __init__(self, directory_path: Path, image_name: str):
        # Make sure the directory exists
        self.directory = files_callback.create_dir(directory_path / image_name)
        self.image_name = image_name

    def __call__(self, image_urls: List[validators.ImageSrcUrl]) -> None:
        for image_url in image_urls:
            content: bytes = rq.get(image_url.url).content
            files_callback.save_bytes_image(content, self.directory, self.image_name)


class ImageSrcBase64Download:
    def __init__(self, directory_path: Path, image_name: str):
        self.directory = files_callback.create_dir(directory_path / image_name)
        self.image_name = image_name

    def __call__(self, images_base64: List[validators.ImageSrcBase64]) -> None:
        for image_base64 in images_base64:
            files_callback.save_base64_image(
                image_base64.base64_src, self.directory, self.image_name
            )
