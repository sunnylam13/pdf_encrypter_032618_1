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

# a list of all folders and subfolders to be analyzed
folder_path_list = [] # a list to hold all finalized folder paths (not folder names)

# a list of all files to be analyzed
file_path_list = [] # a list to hold all finalized folder paths (not folder names)


def scanFolder(foldername_path):
	# this function scans the parent folder and subfolders
	# it then adds them to a list so that its files can be scanned individually

	# `foldername_path` should actually be a string path to folder	

	# as we get deeper and deeper into subfolders it should add onto the folder's path string that we pass to it so accuracy should be maintained

	dirs = os.listdir(foldername_path) # list all files of any kind (i.e. all file and folder names)
	# absPath = dirPath
	# absPath = os.path.dirname(foldername_path) # returns the directory path except basename to the foldername_path

	# folder_path_list = [] # a list to hold all finalized folder paths (not folder names)

	for file in dirs:
		# new_path = os.path.join(absPath,file) # creates a path to the file/folder
		new_path = os.path.join(foldername_path,file) # creates a path to the file/folder

		if os.path.isdir(new_path): #if the file is a folder
			folder_path_list.append(new_path) # add it to the list of folders with its full path name
		else:
			continue # otherwise skip and keep going


def scanFile(foldername_path,regex):
	# the file scanner that gets all of the files and pushes them into a list after we get the full string path to it
	
	dirs = os.listdir(foldername_path) # list all files of any kind (i.e. all file and folder names)

	for file in dirs:
		# new_path = os.path.join(absPath,file) # creates a path to the file/folder
		new_path = os.path.join(foldername_path,file) # creates a path to the file/folder

		if os.path.isfile(new_path) and regex.search(file): #if the file is a folder AND has regex match
			file_path_list.append(new_path) # add it to the list of folders with its full path name
		else:
			continue # otherwise skip and keep going

def analyzeAllFiles ():
	# run an initial scan of the upper level main folder tree
	# find subfolders
	# find matching files
	scanFolder(user_folderpath)
	scanFile(user_folderpath,file_type_regex1)

	# then scan all the sub folders by cycling through folder_path_list until no more subfolders are added
	# this should keep going until no more subfolders are analyzed
	# then scan all the files by cycling through folder_path_list until no more subfolders are added/left
	for subfolder in folder_path_list:
		scanFolder(subfolder)
		scanFile(subfolder,file_type_regex1)

	logging.debug("The folder_path_list is:  ")
	logging.debug(folder_path_list)
	logging.debug("The file_path_list is:  ")
	logging.debug(file_path_list)

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


#####################################
# EXECUTION
#####################################

analyzeAllFiles()

#####################################
# END EXECUTION
#####################################


