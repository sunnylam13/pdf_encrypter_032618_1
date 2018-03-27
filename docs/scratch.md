# Scratch Notes

## Monday, March 26, 2018 6:15 PM

Program actions

* save each file with `_encrypted.pdf` suffix added to original name

* before deleting original, program should error check - try to read and decrypt the file to ensure that it's encrypted right

on the flip side...

we also write a pdf decryption program

write a program that finds all encrypted pdfs in a folder and subfolders...

which creates a decrypted copy of pdf using a provided password

if password is wrong, program should print message to user and move onto the next pdf

## Monday, March 26, 2018 7:16 PM

[How can I create a directory if it does not exist?](https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist)

## Monday, March 26, 2018 9:32 PM

PyPDF `decrypt()` only returns 0 if the password doesn't work or 1 if it does...

> 0 if the password failed, 1 if the password matched the user password, and 2 if the password matched the owner password.

[The PdfFileReader Class](https://pythonhosted.org/PyPDF2/PdfFileReader.html)

> isEncrypted
> Read-only boolean property showing whether this PDF file is encrypted. Note that this property, if true, will remain true even after the decrypt() method is called.

[how to delete a file or folder](https://stackoverflow.com/questions/6996603/how-to-delete-a-file-or-folder)

## Tuesday, March 27, 2018 11:00 AM

for the decryption program

the folder is:

	pdf_encrypter/encrypted_f

since it's in the same folder as the execution program, the path is:

	./encrypted_f

## Tuesday, March 27, 2018 11:25 AM

For the decryption program the problem is that PyPDF2 `decrypt()` method does not actually decrypt - it only tells you if the password works.  

	MacBook-Air:pdf_encrypter sunnyair$ python3 pdf_decrypter_032618_1.py "pdf_encrypter/encrypted_f" "yuhelia"
	 2018-03-27 11:24:03,806 - DEBUG - The target folder is:  pdf_encrypter/encrypted_f
	 2018-03-27 11:24:03,806 - DEBUG - The password to encrypt with is:  yuhelia
	 2018-03-27 11:24:03,807 - DEBUG - The folder_path_list is:
	 2018-03-27 11:24:03,808 - DEBUG - []
	 2018-03-27 11:24:03,808 - DEBUG - The file_path_list is:
	 2018-03-27 11:24:03,808 - DEBUG - ['./encrypted_f/poetry1.pdf_encrypted.pdf', './encrypted_f/poetry2.pdf_encrypted.pdf', './encrypted_f/poetry3.pdf_encrypted.pdf', './encrypted_f/meetingminutes2.pdf_encrypted.pdf', './encrypted_f/combinedminutes.pdf_encrypted.pdf', './encrypted_f/meetingminutes.pdf_encrypted.pdf']
	 2018-03-27 11:24:03,809 - DEBUG - PDF file to be decrypted is:  poetry1.pdf_encrypted.pdf
	 2018-03-27 11:24:03,809 - DEBUG - Decrypted PDF file name and path:  ./decrypted_f/poetry1.pdf
	Traceback (most recent call last):
	  File "pdf_decrypter_032618_1.py", line 210, in <module>
	    decrypt_test_pdfs(file_path_list,user_pwd)
	  File "pdf_decrypter_032618_1.py", line 195, in decrypt_test_pdfs
	    pdf_decryptor(file_item,pwd)
	  File "pdf_decrypter_032618_1.py", line 182, in pdf_decryptor
	    add_pages_2_pdf(decrypted_file,pdfWriter) # read decrypted file, copy contents to new file
	  File "pdf_decrypter_032618_1.py", line 178, in add_pages_2_pdf
	    for pageNum in range(pdfReaderObj.numPages):
	AttributeError: 'int' object has no attribute 'numPages'

It only returns an integer and not a decrypted file object meaning that we need another module to run the decryption with the password...

## Tuesday, March 27, 2018 3:47 PM

[PyPDF 2 Decrypt Not Working](https://stackoverflow.com/questions/26242952/pypdf-2-decrypt-not-working)

[Query - is there a way to bypass security restrictions on a pdf? #53](https://github.com/mstamy2/PyPDF2/issues/53)

> I used qpdf and the following hack-y code to decrypt the documents if PyPDF2 fails at decryption.

	import os
	import PyPDF2
	from PyPDF2 import PdfFileWriter, PdfFileReader
	filename=raw_input('\nFilename:')

	fp = open(filename)
	pdfFile = PdfFileReader(fp)
	if pdfFile.isEncrypted:
	    try:
	        pdfFile.decrypt('')
	        print 'File Decrypted (PyPDF2)'
	    except:
	        command="cp "+filename+" temp.pdf; qpdf --password='' --decrypt temp.pdf "+filename
	        os.system(command)
	        print 'File Decrypted (qpdf)'
	        #re-open the decrypted file
	        fp = open(filename)
	        pdfFile = PdfFileReader(fp)
	else:
	    print 'File Not Encrypted'
	#dostuff with pdfFile here

> Be careful not to accept any user input for the filename for your application using this code, if you do, be sure to sanitize it before os.system executes it.

search terms:

* pypdf2 decrypt file


