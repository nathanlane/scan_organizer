
import os,re

with open(os.path.join('..','remote','Output','microfilms-catalog.csv'),'r') as catalog:
    group=0
    for i, line in enumerate(catalog):
        if i==0:
            continue
        path,type = re.search("^([^,]+),([^,]+)\n$",line).groups()
        path = os.path.abspath(re.search("..{0}(.*)".format(os.sep),path).group(1))
        file_name = os.path.split(path)[1]
        ignore=False

        if type=="2":
            group+=1
            os.mkdir(os.path.join('..','remote','Output','folders-by-year','group{0}'.format(group)))
            os.symlink(path,os.path.join('..','remote','Output','folders-by-year','group{0}'.format(group),file_name))
            ignore=False

        elif type=="3":
            ignore=True
            os.symlink(path,os.path.join('..','remote','Output','folders-by-year','group{0}'.format(group),file_name))

        elif not ignore:
            os.symlink(path,os.path.join('..','remote','Output','folders-by-year','group{0}'.format(group),file_name))

        else:
            print('This case should not be reached')
