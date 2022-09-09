This is a Python story game loaded into a virtual machine/environment.

If you are on an ARM/M1 computer, go into Vagrantfile to comment out the Vagrant.configure lines underneath "#INTEL/AMD VIRTUAL BOX"
Comment in the lines underneath "#ARM/M1 Vmware

Comment in or out items by highlighting text and pressing "ctrl and /"

To create the virtual machine and install python on it, navigate to "python-minigame" folder and run command "vagrant up"

To play the game, run command "vagrant ssh", "cd app" then "python3 game.py"