
import os,re

base_dir = os.path.abspath(os.path.join(os.pardir,'remote'))
os.chdir(base_dir)

with open(os.path.join('Output','microfilms-catalog.csv'),'r') as catalog:
    group=-1
    years=['1891','1899','1900','1901','1902','1903','1904','1905','1906','1907','1908','1909','1910','1911','1912-1913','1913-1914','1920-1921','1923-1924','1924-1925','1925-1926','1926-1927','1927-1928','1928-1929','1929-1930','1930-1931','1931-1932','1932-1933']

    for i, line in enumerate(catalog):
        if i==0:
            continue
        path,type = re.search("^([^,]+),([^,]+)\n$",line).groups()
        ignore=False

        if type=="2":
            group+=1
            os.chdir(base_dir)
            try:
                new_dir = os.path.abspath(os.path.join('Output','folders-by-year','{0}'.format(years[group])))
            except:
                new_dir = os.path.abspath(os.path.join('Output','folders-by-year','{0}'.format(group)))
            os.mkdir(new_dir)
            os.chdir(new_dir)
            parent, file_name = os.path.split(path)
            reel = os.path.split(parent)[1]
            path = os.path.abspath(os.path.join(os.pardir,os.pardir,os.pardir,'Input','microfilms-scans',reel,file_name))
            os.symlink(os.path.relpath(path),file_name)
            ignore=False

        elif type=="3":
            ignore=True
            parent, file_name = os.path.split(path)
            reel = os.path.split(parent)[1]
            path = os.path.abspath(os.path.join(os.pardir,os.pardir,os.pardir,'Input','microfilms-scans',reel,file_name))
            os.symlink(os.path.relpath(path),file_name)

        elif not ignore:
            parent, file_name = os.path.split(path)
            reel = os.path.split(parent)[1]
            path = os.path.abspath(os.path.join(os.pardir,os.pardir,os.pardir,'Input','microfilms-scans',reel,file_name))
            os.symlink(os.path.relpath(path),file_name)

        else:
            print('This case should not be reached')
