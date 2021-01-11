"""
Command line interface for the minirhizpreprocessing module.
"""
import argparse
import logging
import sys

import minirhizpreprocessing
from . import cliutils


_LOGGER = logging.getLogger(__name__)


def create_parser():
	"""
	Create the parser for the minirhizpreprocessing command.

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
		'output_folder',
		type=cliutils.sanitize_path,
		help='Directory where the results will be generated.'
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

	# Call the main function of the module


if __name__ == '__main__':
	main()
