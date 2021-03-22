#!/bin/bash

continue_init () {
    # echo -n "Clearing files... "
    # find . ! -name 'init.bash' -type rf -exec rm -r {} +
    # echo -e "$(tput -T xterm setaf 2)OK$(tput -T xterm sgr0)"

    echo -n "Sourcing ROS2... "
    source /opt/ros/foxy/setup.bash
    echo -e "$(tput -T xterm setaf 2)OK$(tput -T xterm sgr0)"

    
}

clone_repo() {
    echo $1
    git clone $1
}

if ! (($(ls -1 | wc -l) == 2))
then
    echo -e "[$0] $(tput -T xterm setaf 1)Error: $(tput -T xterm sgr0) Files/folders other than this script exist in the current directory. Please remove them."
    exit -1
fi

echo -e "$(tput -T xterm setaf 6)Sourcing ROS$(tput -T xterm sgr0)"
source /opt/ros/foxy/setup.bash
echo -e "$(tput -T xterm setaf 6)Cloning repos from luna_repos.txt$(tput -T xterm sgr0)"
mkdir src && cd src
while read line; do clone_repo $line; done < ../luna_repos.txt
echo -e "$(tput -T xterm setaf 6)Installing ROS dependencies$(tput -T xterm sgr0)"
cd ..
rosdep install -i --from-path src --rosdistro ${ROS_DISTRO} -y
echo -e "$(tput -T xterm setaf 2)Done.$(tput -T xterm sgr0) Luna WS is ready to be built and sourced 🎉"
# read yn
# case $yn in
#     [Yy]* ) continue_init;;
#     * ) echo "Cancelled.";;
# esac