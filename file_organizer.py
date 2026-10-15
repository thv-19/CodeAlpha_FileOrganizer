import os
import shutil
# contains the test image
source_folder = "TestFiles"
# where we will put the image
destination_folder = "Images"
# create the destionation folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
print("Image folder is ready!")
# Find and move JPG images
for filename in os.listdir(source_folder):
    if filename.lower().endswith((".jpg","jpeg",".png",".gif")):
        source_path = os.path.join(source_folder, filename)
        destination_path= os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        print("Move image:", filename)
print("File organiztion completed!")
print()
