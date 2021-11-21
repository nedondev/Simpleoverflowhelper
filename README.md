# Simpleoverflowhelper

Basic Bufferoverflow value repaster and suggesster.Instead of have to repaste an command output, ip, port, etc. This tool do it for you and also suggest next step to do.

# Origin

Simpleoverflowhelper was inspired by AutoRecon which the author used during practice for the OSCP exam. Simpleoverflowhelper carried over an idea that the tool suggest the next step command to execute. The tool built to minimize human error like mistyping , mispasting and etc and minimize action that have to be done to create a script by repaste payload from argument to script instead.

# Usage

Simpleoverflowhelper uses Python3 to generate Python2 script.

```
usage: simpleoverflowhelper.py [-h HOST] [-p PORT] [-r PREFIX] [-g PATTERN] [-b BADCHAR] [--offset OFFSET] [-j JMPADDRESS] [-s SHELLFILE] [-o OUTPUT] [--version] [generatestep]

Basic Bufferoverflow value repaster and suggesster.Instead of have to repaste an command output, ip, port, etc. This tool do it for you and also suggest next step to do.

positional arguments:
  generatestep          The bufferoverflow step (e.g. 1)

optional arguments:
  -h HOST, --host HOST  IP addresses of target host (e.g. 10.0.0.1)
  -p PORT, --port PORT  The vulnerable to bufferoverflow service port (e.g. 9999)
  -r PREFIX, --prefix PREFIX
                        The bufferoverflow prefix before send value to actual vulnerable input field (e.g. "TRUN ")
  -g PATTERN, --pattern PATTERN
                        The generated pattern from msf pattern_create.rb (e.g. Aa0Aa1Aa2Aa3Aa4Aa5Aa)
  -b BADCHAR, --badchar BADCHAR
                        The bufferoverflow step (e.g. 0,a)
  --offset OFFSET       The bufferoverflow step payload offset before replace the EIP regeister value. (e.g. 2003)
  -j JMPADDRESS, --jmpaddress JMPADDRESS
                        The bufferoverflow jump to esp address (e.g. 65459201)
  -s SHELLFILE, --shellfile SHELLFILE
                        A filename contain the reverse shell code generated from msfvenom. (e.g. reverseshell.txt)
  -o OUTPUT, --output OUTPUT
                        Specify output file name. If not specified will be the template file name without template word. (e.g. 1-fuzzer.py)
  --version             Prints the Simple Overflow Helper version and exits.
```

# Requirement for each step to repaste config to a script.

## Step 1 generate fuzzing script

**Required**
- ip
- port
- prefix

**Example**
`./draft.py 1 -h 192.168.227.130 -p 9999 -r "TRUN "`

## Step 2 generate offset finding script

**Required**
- Step 1 or ip, port, prefix
- pattern

## Step 3 generate verify overwritten pattern script

**Required**
- Step 1 or ip, port, prefix
- offset

## Step 4 generate finding bad chars script

**Required**
- Step 1 or ip, port, prefix
- Step 3 or offset
- badchar

## Step 5 generate verify jmp address script

**Required**
- Step 1 or ip, port, prefix
- Step 3 or offset
- jmp address

## Step 6 generate reverse shell script

**Required**
- Step 1 or ip, port, prefix
- Step 3 or offset
- Step 5 or jmp address
- shellcode file

