import os
import time

time.sleep(0.5)

print('Hello!')

time.sleep(1)

osinput = input('''Select your operating system from the list below:
 1) RedHat Linux (Fedora, CentOs);
 2) Debian-like Linux (ubuntu, Pop_os!, Mint);
 3) Arch/Mangaro 
 Your aswer: ''')


def install_vim():
    start = input('Have you already installed VIM? (y/n) ')

    if start == 'y':
        settings()
    else:
        install = input('Want to install VIM now? (y\n) ')
        if install == 'y':
            if osinput == 1:
                os.system('sudo yum install vim -y')
            if osinput == 2:
                os.system('sudo apt install vim -y')
            if osinput == 3:
                os.system('sudo pacman -S vim -y')
            else:
                print('You entered an invalid number')
                install_vim()


def settings():
    os.system('cd ~/Downloads && ls')
    time.sleep(0.3)
    print('All is OK')


install_vim()
