import typer
from pathlib import Path
from typing import List
from logger import pretty_log_info, log_info
from google_image import Google
from parameters_callback import (
    image_directory_callback,
    chromedriver_directory_callback,
)


def main(
    image_directory: Path = typer.Option(
        ...,
        "--image-directory",
        "-id",
        help="Set the image directory where you want to save the scrapped images",
        callback=lambda path: image_directory_callback(path),
    ),
    chromedriver_directory: Path = typer.Option(
        ...,
        "--chromedriver-directory",
        "-cd",
        help="Set the chrome driver directory. In the root of that directory the"
        " `chromedriver` file must be",
        callback=chromedriver_directory_callback,
    ),
    image_names: List[str] = typer.Option(
        ...,
        "--image-names",
        "-in",
        help="List of image names that you want to download from google image."
        " Their must be separated by space e.g: apple book desk",
    ),
):
    log_info("The parameters are:")
    pretty_log_info(
        {
            "image_directory": str(image_directory.absolute()),
            "chromedriver_directory": str(chromedriver_directory.absolute()),
            "image_names": image_names,
        }
    )

    # search just one
    for image_name in image_names:
        google = Google(chromedriver_directory / "chromedriver")
        images_link = google.search(image_name)
    # finish scrapping src of img tag in google image search!
    # TODO: Save base64 images source, download image url and save it!
