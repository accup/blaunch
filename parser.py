from argparse import ArgumentParser

from importlib import import_module
from inspect import stack, getmodule

from .defaults import PARSER_ARGUMENTS


def create_parser(**parser_arguments):
	# Prepare new sub-command parser arguments
	current_parser_arguments = dict()
	current_parser_arguments.update(PARSER_ARGUMENTS)
	current_parser_arguments.update(parser_arguments)
	# Create new parser
	return ArgumentParser(**current_parser_arguments)


def make_subcommand(
		subparsers,
		subcommand_name : str,
		subcommand_module = None,
		**parser_arguments):
	'''Make a sub-command
	
	subparsers :
		a sub-parsers which is created by `ArgumentParser.add_subparsers` method.
	
	subcommand_name : str
		the name of the new sub-command. 
	'''
	# Prepare new sub-command parser arguments
	current_parser_arguments = dict()
	current_parser_arguments.update(PARSER_ARGUMENTS)
	current_parser_arguments.update(parser_arguments)
	# Create sub-command parser
	parser = subparsers.add_parser(subcommand_name, **current_parser_arguments)
	
	if subcommand_module is None:
		# Load module which is <caller_package>.<subcommand_name>
		# if the subcommand_module is not specified.
		caller_package = getmodule(stack()[1][0]).__package__
		subcommand_module = import_module(
			'.' + subcommand_name, caller_package)
	
	if (hasattr(subcommand_module, 'main')
			and callable(subcommand_module.main)):
		# Set the `main` function of sub-module as the default `_main` argument if exists.
		parser.set_defaults(_main=subcommand_module.main)
	
	# Define the sub-command parser by calling the `subparser` function of sub-module.
	subcommand_module.subparser(parser)

