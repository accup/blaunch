from argparse import ArgumentParser


def launch(parser : ArgumentParser):
	'''Parse the command-line arguments and run the main function'''
	args = parser.parse_args()
	if hasattr(args, '_main'):
		args._main(args)
	else:
		parser.print_help()
