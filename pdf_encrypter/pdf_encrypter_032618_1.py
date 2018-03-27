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
# GLOBAL VARIABLES
#####################################

encrypt_output_folder = "./encrypted_f/" # this should lead to a folder within cwd of this program

#####################################
# END GLOBAL VARIABLES
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

def analyzeAllFiles (user_folderpath,file_type_regex1):
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

def pdf_encryptor(file_item,pwd):
	# this is a function to encrypt a single file that is passed to it
	# it uses the password passed to it in the 2nd arg
	
	pdfFile = open(file_item,'rb') # open in binary mode
	pdfReader = PyPDF2.PdfFileReader(pdfFile)
	pdfWriter = PyPDF2.PdfFileWriter() # temporary new file to hold gathered data

	for pageNum in range(pdfReader.numPages):
		pdfWriter.addPage( pdfReader.getPage(pageNum) )

	pdfWriter.encrypt(pwd) # encrypted with supplied password

	# save the file to new destination folder
	new_filepath = encrypt_output_folder
	# create new filename 
	# where `file_item` is already a path
	# using os.path.basename(file_item) we get only the file's name
	new_filename = os.path.basename(file_item) +'_encrypted.pdf'
	final_filename_path = new_filepath + new_filename

	# check if the directory you want to save to already exists
	if not os.path.exists("encrypted_f"):
		os.makedirs("encrypted_f")

	resultPdf = open(final_filename_path,'wb')
	pdfWriter.write(resultPdf) # the resulting save will be in current working directory
	logging.debug('Encrypted file %s has been written and saved.' % (new_filename) )
	resultPdf.close()

def encrypt_pdfs(file_path_list,pwd):
	# this function runs a single file encryption function over files in a list
	# loop through the file_path_list and encrypt each file with the password
	
	for file_item in file_path_list:
		pdf_encryptor(file_item,pwd)

	

#####################################
# END ENCRYPT
#####################################


#####################################
# DECRYPT
#####################################

# double check encryption

def pdf_decryptor_tester(file_item,pwd):
	# function decrypts a single file that is passed to it and tells us if True/False
	# we want isEncrypted = False
	
	pdf_file = open(file_item,'rb') # open in read binary mode

	pdfReader = PyPDF2.PdfFileReader( pdf_file )
	logging.debug('PDF file to be decrypted is:  %s' % os.path.basename(file_item) )

	# logging.debug('Is PDF file encrypted?')
	# logging.debug(pdfReader.isEncrypted) # True/False - this should read as True before decryption

	# check if the password will decrypt the file
	if ( pdfReader.decrypt(pwd) ) == 1 or ( pdfReader.decrypt(pwd) == 2 ): # pdfReader.decrypt(pwd) returns an integer
		logging.debug("The password matches and works.")

def decrypt_test_pdfs(file_path_list,pwd):
	# this function runs a single file decryption tester function over files in a list to test that the file is encrypted correctly
	# loop through the file_path_list and encrypt each file with the password
	
	for file_item in file_path_list:
		pdf_decryptor_tester(file_item,pwd)

#####################################
# END DECRYPT
#####################################


#####################################
# DELETE ORIGINAL FILE
#####################################

def delete_file(file_name):
	os.remove(file_name)
	logging.debug("Deleted file:  %s" % os.path.basename(file_name) )

def delete_files_mass(file_path_list):
	for file_name in file_path_list:
		delete_file(file_name)
	logging.debug("All files deleted.")

#####################################
# END DELETE ORIGINAL FILE
#####################################


#####################################
# EXECUTION
#####################################

# find all unencrypted pdfs
analyzeAllFiles(user_folderpath,file_type_regex1)

# encrypt files
encrypt_pdfs(file_path_list,user_pwd)

# save pre-encrypted files to another list
# this list will be used for deleting the original files
pre_encrypt_file_list = file_path_list

# reset both folder_path_list and file_path_list to an empty list at this point
# if you don't you'll mix with pre-encrypted file paths
# you'll throw an error because you try to decrypt unencrypted files
# this has to happen before you run analyzeAllFiles() again
folder_path_list = []
file_path_list = []

# find all encrypted files
analyzeAllFiles(encrypt_output_folder,file_type_regex1)

# double check the files are all encrypted correctly
decrypt_test_pdfs(file_path_list,user_pwd)

# delete original, unencrypted files
delete_files_mass(pre_encrypt_file_list)

#####################################
# END EXECUTION
#####################################


