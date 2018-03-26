# -*- coding: utf-8 -*-

#! python3

# USAGE
# python3 pdf_encrypter_032618_1.py FOLDERPATHSTRING PWDSTRING
# python3 pdf_encrypter_032618_1.py "../tests/testpdfs1" "yuhelia"

import os, re, shutil, PyPDF2, sys

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

#####################################
# COMMAND LINE ARGUMENTS AND DATA
#####################################

# get command line arguments and data

user_folderpath = sys.argv[1]
logging.debug('The target folder is:  %s' % (user_folderpath)  )

user_pwd = sys.argv[2]
logging.debug('The password to encrypt with is:  %s' % (user_pwd) )

#####################################
# END COMMAND LINE ARGUMENTS AND DATA
#####################################


#####################################
# REGEX
#####################################

# create a regex statement to match `user_file_ext_input`
# https://regexr.com/3kvi4
# re.compile should turn a raw string into current regex language so you can skip creating the formula sort of...

user_file_ext_input = '.pdf' # we're targeting only pdf file endings
# alternatively could use .endswith("pdf") to find it with logic

file_type_regex1 = re.compile(user_file_ext_input + "$")
# print(file_type_regex1) # for testing
# print(file_type_regex1.search("testTextA1.txt")) # for testing

#####################################
# END REGEX
#####################################


#####################################
# ANALYZE
#####################################

# analyze folders and subfolders in search of pdf files


#####################################
# END ANALYZE
#####################################


#####################################
# ENCRYPT
#####################################

# encrypt the pdfs

#####################################
# END ENCRYPT
#####################################


#####################################
# DECRYPT
#####################################

# double check encryption

#####################################
# END DECRYPT
#####################################


