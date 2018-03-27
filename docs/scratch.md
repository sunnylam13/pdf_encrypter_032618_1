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

