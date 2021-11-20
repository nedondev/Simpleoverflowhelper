#!/bin/python3
import argparse, os, sys, toml


# Inspired by Tib3rius's autorecon

# TODO

## read argument value
## read toml config file

## check the argument for specific generate script
## if the argument not fit the script check the config file 

## add suggest for next command

# code

## read arguments

VERSION = "0.0.1"

def main():
    config = None
    if os.path.isfile(os.path.join(os.getcwd(), 'config.toml')): 
        config = toml.load("config.toml")
    
    parser = argparse.ArgumentParser(add_help=False, description='Basic Bufferoverflow value repaster and suggesster.Instead of have to repaste command output, ip, port, etc this tool do it for you and also suggest next step to do.')
    parser.add_argument('generate-step', action='store', type=int, help='The bufferoverflow step (e.g. 1)', nargs='*')
    parser.add_argument('-h', '--host', action='store', help='IP addresses of target host (e.g. 10.0.0.1)')
    parser.add_argument('-p', '--port', action='store', type=int, help='The vulnerable to bufferoverflow service port (e.g. 9999)')
    parser.add_argument('-r', '--prefix', action='store', type=str, help='The bufferoverflow prefix before send value to actual vulnerable input field (e.g. "TRUN ")')
    parser.add_argument('-g', '--pattern', action='store', type=str, help='The generated pattern from msf pattern_create.rb (e.g. Aa0Aa1Aa2Aa3Aa4Aa5Aa)')
    parser.add_argument('-b', '--badchar', action='store', type=int, help='The bufferoverflow step (e.g. \\x00,\0x0a')
    parser.add_argument('--offset', action='store', type=str, help='The bufferoverflow step payload offset before replace the EIP regeister value. (e.g. 2003)')
    parser.add_argument('-j', '--jmpaddress', action='store', type=str, help='The bufferoverflow jump to esp address (e.g. 65459201)')
    parser.add_argument('-s', '--shell-file', action='store', type=str, help='A filename contain the reverse shell code generated from msfvenom. (e.g. reverseshell.txt)')
    parser.add_argument('-o', '--output', action='store', type=str, help='Specify output file name. If not specified will be the template file name without template word. (e.g. 1-fuzzer.py)')
    parser.add_argument('--version', action='store_true', help='Prints the Simple Overflow Helper version and exits.')
    args, unknown = parser.parse_known_args()

    if args.version:
        print('Simple Overflow Helper v' + VERSION)
        sys.exit(0)
    
    def unknown_help():
        if '--help' in unknown:
            parser.print_help()
            print()

    unknown_help()

if __name__ == '__main__':
	main()
