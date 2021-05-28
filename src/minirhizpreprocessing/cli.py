"""
Command line interface for the minirhizepreprocessing module.
"""
import argparse
import logging
import sys

import minirhizpreprocessing
from . import cliutils

from pathlib import Path
import cv2
import numpy as np
from tqdm import tqdm

_LOGGER = logging.getLogger(__name__)


def create_parser():
	"""
	Create the parser for the minirhizepreprocessing command.

	:return: Configured parser.
	:rtype: argparse.ArgumentParser
	"""
	parser = argparse.ArgumentParser(
		description='''

'''
		)
	parser.add_argument(
		'-v', '--version',
		action='version',
		version='%(prog)s v{}'.format(minirhizpreprocessing.__version__)
		)

	# Positional arguments, declaration order is important
	parser.add_argument(
		'input_folder',
		type=cliutils.sanitize_path,
		help='Directory where the input images are stocked'
		)

	# Positional arguments, declaration order is important
	parser.add_argument(
		'output_folder',
		type=cliutils.sanitize_path,
		help='Directory where the results will be generated.'
		)

	# Positional arguments, declaration order is important
	parser.add_argument(
		'process',
		type=cliutils.sanitize_path,
		help='process to apply : ex rotation'
		)


	# Optional arguments
	cliutils.add_boolean_flag(parser, 'debug', 'Enable debug outputs. Imply --verbose.')
	cliutils.add_boolean_flag(parser, 'verbose', 'Enable debug logging.')

	return parser

def main(args=None):
	"""
	Run the main procedure.

	:param list args: List of arguments for the command line interface. If not set, arguments are
		taken from ``sys.argv``.
	"""
	parser = create_parser()
	args = parser.parse_args(args)
	args.verbose = args.verbose or args.debug

	# Ensure the directory exists to create the log file
	args.output_folder.mkdir(parents=True, exist_ok=True)
	log_filename = args.output_folder.joinpath('minirhizpreprocessing.log')

	cliutils.setup_logging(debug=args.verbose, filename=log_filename)
	_LOGGER.debug('command: %s', ' '.join(sys.argv))
	_LOGGER.debug('version: %s', minirhizpreprocessing.__version__)

	# check the method that have been called
	method = args.process

	# Call the main function of the module
	extensions = ("jpg","tif","png","JPG","jpeg","JPEG")
	images= []
	for ext in extensions:
		images += list(Path(args.input_folder).glob(f"*{ext}"))

	for imgp in tqdm(images,desc="Rotate images"):
		img = cv2.imread(str(imgp))

		if 'rotation' in str(method):
			img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

		out = Path(args.output_folder) / imgp.name
		cv2.imwrite(str(out),img)

if __name__ == '__main__':
	main()
