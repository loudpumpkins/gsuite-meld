import os
os.environ['GSUITE_CREDENTIALS'] = 'C:/Path/to/credentials.json'


from gsuite_meld import Drive, Sheet, Document

# initialize our Google Drive object
drive = Drive()

# suppose we want to operate in a specific Google Drive folder
# you'll need to extract this id from your Google Drive URL
# url = https://drive.google.com/drive/folders/longstringofcharacters
folder_id = 'longstringofcharacters'

# list all files in this folder
files = drive.list_files_in_folder(folder_id)
for file in files:
    print(file)

# > {'id': 'uniquefileorfoldereid1', 'name': 'file1.txt', 'kind': 'drive#file', 'driveId': '- id -', 'mimeType': '- type -', 'teamDriveId': '- team drive id -'}
# > {'id': 'uniquefileorfoldereid2', 'name': 'folder1', 'mimeType': 'application/vnd.google-apps.folder', 'kind': 'drive#file', 'driveId': '- id -', 'id': '- file/folder id -', 'name': '- file/folder name -', 'teamDriveId': '- team drive id -'}


# say we're interested in a specific document in this folder, let's find it
doc_id = drive.get_id('important_document', folder_id)

# load document into memory
document = Document().download(doc_id)

# iterate through the document, printing out each line
for line in document:
    print(line)

# add some text to the document
new_content = "This is some new content that I want to add to the document."
document.upload(new_content)



# We can also look for specific sheets within the drive folder
sheet_id = drive.get_id('important_sheet', folder_id)

# Initialize our Sheet object and download it
sheet = Sheet().download(sheet_id, 'Tab Name')

# Let's print all rows from the sheet
for row in sheet:
    print(row)

# append some data to the sheet
new_data = [['New', 'Row', 'Data']]
sheet.append(new_data)
