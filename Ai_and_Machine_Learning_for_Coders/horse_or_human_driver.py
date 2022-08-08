import os.path
import urllib.request
import zipfile

# Importing the Training Dataset.
url = 'https://storage.googleapis.com/laurencemoroney-blog.appspot.com/horse-or-human.zip'

file_name = "horse-or-human.zip"
training_dir = "horse-or-human/training/"

if os.path.exists(training_dir):
    pass
else:
    urllib.request.urlretrieve(url, file_name)

    zip_ref = zipfile.ZipFile(file_name, "r")
    zip_ref.extractall(training_dir)
    zip_ref.close()

# Importing the validation dataset.

validation_url = "https://storage.googleapis.com/laurencemoroney-blog.appspot.com/validation-horse-or-human.zip"

validation_file_name = 'validation-horse-or-human.zip'
validation_dir = 'horse-or-human/validation/'

if os.path.exists(validation_dir):
    pass
else:
    urllib.request.urlretrieve(validation_url, validation_file_name)
    zip_ref = zipfile.ZipFile(validation_file_name, 'r')
    zip_ref.extractall(validation_dir)
    zip_ref.close()
    print(f'new files added under:{validation_dir + validation_file_name}')
