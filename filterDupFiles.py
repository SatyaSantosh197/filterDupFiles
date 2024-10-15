import os
import shutil
import hashlib

def getFileHash(filePath):
    hashAlgo = hashlib.md5()
    with open(filePath, 'rb') as f:
        while chunk := f.read(8192):
            hashAlgo.update(chunk)
    return hashAlgo.hexdigest()

def organizeFiles(inputFolder):
    currentDir = os.getcwd()
    originalsFolder = os.path.join(currentDir, 'originals')
    duplicatesFolder = os.path.join(currentDir, 'duplicates')
    nonDuplicatesFolder = os.path.join(currentDir, 'non-duplicates')

    if not os.path.exists(originalsFolder):
        os.makedirs(originalsFolder)
    if not os.path.exists(duplicatesFolder):
        os.makedirs(duplicatesFolder)
    if not os.path.exists(nonDuplicatesFolder):
        os.makedirs(nonDuplicatesFolder)

    fileHashes = {}

    for root, dirs, files in os.walk(inputFolder):
        for file in files:
            filePath = os.path.join(root, file)

            fileSize = os.path.getsize(filePath)
            if fileSize == 0:
                continue

            fileHash = getFileHash(filePath)

            if fileHash not in fileHashes:
                fileHashes[fileHash] = {'originalPath': filePath, 'count': 1}
                shutil.copy(filePath, os.path.join(originalsFolder, file))
                print(f"Original file saved: {file} in originals")
            else:
                fileHashes[fileHash]['count'] += 1
                if fileHashes[fileHash]['count'] == 2:
                    originalFileName = os.path.basename(fileHashes[fileHash]['originalPath'])
                    shutil.copy(fileHashes[fileHash]['originalPath'], os.path.join(nonDuplicatesFolder, originalFileName))
                    shutil.copy(filePath, os.path.join(duplicatesFolder, file))
                    print(f"Duplicate file found: {file}, storing in duplicates and original in non-duplicates.")

    print("File organization complete.")

# Get input folder from user
inputFolder = input("Enter the path of the folder containing files: ")
organizeFiles(inputFolder)
