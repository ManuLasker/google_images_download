from pathlib import Path
from files_callback import create_dir, check_chromedriver_file
from logger import raise_error, log_info


def image_directory_callback(image_directory: Path, verbose: bool = True) -> Path:
    # validate image directory exist
    # if exist -> validate if image directory is in fact a directory
    # if does not exist -> create image directory with parents = True "mkdir -p"
    return create_dir(image_directory, verbose)


def chromedriver_directory_callback(chromedriver_directory: Path) -> Path:
    # validate chromedriver_directory exist
    # if not exist raise an error
    # if exist check if `chromedriver` file is located inside
    # there is not `chromedriver` raise an error
    # if there is chromedriver file check using subporcess webdriver
    if chromedriver_directory.exists():
        for driver_file in chromedriver_directory.rglob("chromedriver"):
            try:
                log_info("Testing driver binary file ...")
                check_chromedriver_file(driver_file)
                return chromedriver_directory
            except Exception as error:
                raise_error(
                    f"bad {chromedriver_directory} binary file, error in execution: {error}"
                )
        raise_error(f"{chromedriver_directory} must contain chromedriver binary file!")
    raise_error(
        f"{chromedriver_directory} must exist and contain chromedriver binary file!"
    )
