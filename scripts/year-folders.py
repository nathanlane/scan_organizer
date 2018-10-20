#! python
'''
This script reads the csv file created using the categorize-images.py script and creates a directory into the local
folder of the repository that contain hard links to the original images, reordering them by year.
'''
import os,re

#os.chdir('/home/felipe/projects/scan_project_nathans/scripts')

with open(os.path.join(os.pardir,'remote','Output','microfilms-catalog.csv'),'r') as catalog:
    group=-1

    # These are the years we will classify the folders into.
    years=['1891','1899','1900','1901','1902','1903','1904','1905','1906','1907','1908','1909','1910','1911','1912-1913','1913-1914','1920-1921','1923-1924','1924-1925','1925-1926','1926-1927','1927-1928','1928-1929','1929-1930','1930-1931','1931-1932','1932-1933']

    for i, line in enumerate(catalog):
        # The first line contains the header, we skip it
        if i==0:
            continue

        # For other lines, we reed what is the relative path to the file from the script folder an its classification
        path,type = re.search("^([^,]+),([^,]+)\n$",line).groups()

        # Set helper variable ignore to false. This will be useful to skip empty images between years.
        ignore=False

        # Type two is the first image of a year.
        if type=="2":
            # We advance to the following year folder
            group+=1
            # Create a directory where the links will be stored.
            try:
                new_dir = os.path.abspath(os.path.join(os.pardir,'local','folders-by-year','{0}'.format(years[group])))
            except:
                new_dir = os.path.abspath(os.path.join(os.pardir,'local','folders-by-year','{0}'.format(group)))
            os.makedirs(new_dir, exist_ok=True)

            # Create link from the new directory to the original file
            parent, file_name = os.path.split(path)
            file_name_path = os.path.join(os.path.relpath(new_dir,os.getcwd()),file_name)

            # Hard Link
            target_path = os.path.relpath(os.path.abspath(path),os.path.split(os.path.abspath(os.getcwd()))[0])

            # Symbolic Link
            #target_path = os.path.relpath(os.path.abspath(path),os.path.split(os.path.abspath(new_dir))[0])
            #os.symlink(target_path,file_name_path)

            os.link(target_path,file_name_path)

            # Set ignore to False, so following images are incorporated into this folder
            ignore=False

        # Case 3 is the last image of a year. We save the image but set ignore to true.
        elif type=="3":
            ignore=True
            parent, file_name = os.path.split(path)
            file_name_path = os.path.join(os.path.relpath(new_dir,os.getcwd()),file_name)

            #Hard Link
            target_path = os.path.relpath(os.path.abspath(path),os.path.split(os.path.abspath(os.getcwd()))[0])

            #Symbolic Link
            #target_path = os.path.relpath(os.path.abspath(path),os.path.split(os.path.abspath(new_dir))[0])
            #os.symlink(target_path,file_name_path)
            os.link(target_path,file_name_path)

        elif not ignore:
            # For all images in between the first and last image, we make a link.
            parent, file_name = os.path.split(path)
            file_name_path = os.path.join(os.path.relpath(new_dir,os.getcwd()),file_name)

            #Hard Link
            target_path = os.path.relpath(os.path.abspath(path),os.path.split(os.path.abspath(os.getcwd()))[0])

            #Symbolic Link
            #target_path = os.path.relpath(os.path.abspath(path),os.path.split(os.path.abspath(new_dir))[0])
            #os.symlink(target_path,file_name_path)
            os.link(target_path,file_name_path)

        else:
            print('This case should not be reached')
