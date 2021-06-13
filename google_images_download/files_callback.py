from pathlib import Path
from logger import raise_error, log_info
from google_image import Google
import uuid
from base64 import b64decode


def create_dir(directory_path: Path, verbose: bool = False) -> Path:
    if not directory_path.exists():
        if verbose:
            log_info(f"{directory_path} directory does not exist, creating ...")
        directory_path.mkdir(parents=True)
    else:
        if not directory_path.is_dir():
            raise_error(f"{directory_path} is not a directory!")
    return directory_path


def check_chromedriver_file(chromedriver_file: Path) -> None:
    # Check if chrome driver execution binary file is good
    # using a mock webdriver execution headless mode :=)
    google = Google(driver_path=chromedriver_file)
    try:
        google.check()
    except Exception as error:
        raise error


def save_bytes_image(bytes_image: bytes, directory_path: Path, image_name: str):
    with open(
        directory_path / "{}_{}.jpg".format(image_name, uuid.uuid4().hex), "wb"
    ) as file_image:
        file_image.write(bytes_image)


def save_base64_image(base64_image: str, directory_path: Path, image_name: str):
    save_bytes_image(b64decode(base64_image), directory_path, image_name)
