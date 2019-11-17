from argparse import ArgumentParser
from typing import Sequence, Optional


def launch(
		parser : ArgumentParser,
		command_line_args : Optional[Sequence[str]] = None):
	'''Parse the command-line arguments and run the main function
	
	Parameters
	----------
	parser : argparse.ArgumentParser
		a parser which is created by `blaunch.create_parser` function
		or `argparse.ArgumentParser` constructor.
	
	command_line_args : sequence of str, optional
		custom command-line arguments.
		If it is not specified, the normal command-line arguments are used.
	'''
	# Parse the command-line arguments
	if command_line_args is None:
		args = parser.parse_args()
	else:
		args = parser.parse_args(command_line_args)
	
	if hasattr(args, '_main'):
		# Run the main function
		args._main(args)
	else:
		# Show the help
		parser.print_help()
