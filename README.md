# TODO

Added generate python script script

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

