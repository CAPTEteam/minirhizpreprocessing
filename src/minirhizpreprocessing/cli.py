"""
Command line interface for the minirhizepreprocessing module.
"""
from pathlib import Path
import cv2
from tqdm import tqdm
import click

from internallibraries.system import log as logging

MODULE_NAME = "minirhizepreprocessing"

@click.command()
@click.version_option()
@click.argument("input_folder", type=click.Path(exists=True, file_okay=False))
@click.argument("output_folder", type=click.Path(exists=True, file_okay=False))
@click.option("--rotate", is_flag=True, help="Rotate images")
@click.option("--verbose", "-v", is_flag=True, help="Verbose output.")
def main(input_folder, output_folder, rotate, verbose):
    """
    transformtoadmiralfdrgbi module : Transform mask for admiral

    input_folder is the directory where the input images are stocked

    output_folder is the directory where the results will be generated.
    """

    # load logging settings from internallibraries
    logging.setup_logging(verbose=verbose)

    logger = logging.get_logger()
    logger.info("%s processing data for %s to %s", MODULE_NAME, input_folder, output_folder)
    
    # Call the main function of the module
    extensions = ("jpg","tif","png","JPG","jpeg","JPEG")
    images= []
    for ext in extensions:
        images += list(Path(input_folder).glob(f"*{ext}"))

    for imgp in tqdm(images,desc="Rotate images"):
        img = cv2.imread(str(imgp))

        if rotate:
            img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

        out = Path(output_folder) / imgp.name
        cv2.imwrite(str(out),img)

if __name__ == "__main__":
    main()
