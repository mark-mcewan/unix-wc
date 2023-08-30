# unix-wc
A Unix command line "wc" tool alternative written in python. Gets word, line, character, or byte count of a given input.

## Syntax
```ccwc [-clmw] [file ...]```

## Options
    -c    The number of bytes in each input file is written to the standard output.
    
    -l    The number of lines in each input file is written to the standard output.
    
    -m    The number of characters in each input file is written to the
         standard output.  If the current locale does not support multi-
         byte characters, this is equivalent to the -c option.
    
    -w    The number of words in each input file is written to the standard output.

## Usage
Call script directly from terminal:\
```$ python ccwc.py [-clmw] [path_to_file ...]```\
\
Read from standard input if no filename is specified:\
```$ cat [path_to_file ...] | python ccwc.py [-clmw]```

## Examples
Count the number of lines in file1.txt\
```$ python ccwc.py -l file1.txt```

Count the number of words in file2.txt\
```$ python ccwc.py -w file2.txt```
