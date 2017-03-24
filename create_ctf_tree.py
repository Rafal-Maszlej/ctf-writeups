import os, sys


def usage():
    print('Usage: ' + sys.argv[0] + ' <writeups path>')
    print('Writeups dir names format: "<category>|<points>|<name>"')
    sys.exit(1)

def update_main_README():
    with open('README.md') as f:
        lines = f.readlines()
        lines = lines[:2] + \
                ['#### [{ctf} (2017)]({ctf}_(2017))\n'.format(ctf=CTF_NAME)] + \
                lines[2:]
        
    with open('README.md', 'w') as f:
        for line in lines:
            f.write(line)

def create_ctf_dir():
    os.mkdir(CTF)
    os.chdir(CTF)

def create_challenges_dir_tree():
    readme = open('README.md', 'w') # Create ctf README
    readme.write('# {} 2017\n\n'.format(CTF_NAME))
    
    for chall in challenge_list:
        category, points, name = chall
        dir_name = '{}-{}{}'.format(name, category.lower(), points)
        
        readme.write(fmt.format(name=name, category=category, points=points, dir_name=dir_name)) # Update ctf README
        os.mkdir(dir_name) # Create challenge dir
        
        with open(dir_name + '/README.md', 'w') as f: # Create README for challenge
            f.write(template.format(name=name, category=category, points=points))
    
    readme.close()

def main():
    update_main_README()
    create_ctf_dir()
    create_challenges_dir_tree()
    
    print('DONE')
    sys.exit(0)



if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        usage()
    
    PATH = sys.argv[1]
    CTF_NAME = PATH.rpartition('/')[-1].strip('/')
    CTF = '{}_(2017)'.format(CTF_NAME)
    
    fmt = '* [{name} ({category} {points})]({dir_name})\n'
    with open('README_ctf_template.md', 'r') as t:
        template = t.read()
    
    try:
        challenge_list = sorted([chall.split('|') for chall in os.listdir(PATH)], key=lambda chall: int(chall[1]))
    except FileNotFoundError:
        usage()

    
    main()
