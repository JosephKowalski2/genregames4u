import os
import zipfile

os.system('kaggle datasets download -d xcherry/games-of-all-time-from-metacritic')

zip_filepath = 'games-of-all-time-from-metacritic.zip'
filepath = 'genregames4u'
with zipfile.ZipFile(zip_filepath, 'r') as zip_file:
    zip_file.extractall(filepath)
