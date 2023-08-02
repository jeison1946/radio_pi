#! /bin/bash

# Show errors
function catch_errors() {
   echo "Error";
}

trap catch_errors ERR;

# Make sure only root can run the script
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# Global variables
HOME_PI="/home/pi"

echo "Installing git..."
apt-get install git

echo "Cloning repositories from https://github.com/sdtorresl/exeamonitor_player..."
cd $HOME_PI
git clone https://github.com/sdtorresl/exeamonitor_player

# Verify that git works fine
rc=$?
if [[ $rc != 0 ]] ; then
    exit $rc
fi

echo "Updating system..."
apt-get -y update

echo "Installing some tools..."
apt-get install -y python3-vlc python3-dev python3-setuptools python3-pip

echo "Installing dependencies"
cd $HOME_PI/exeamonitor_player/src
pip3 install -r requirements.txt

rc=$?
if [[ $rc != 0 ]] ; then
    exit $rc
fi


echo "Copying files for automatic initialization of software..."
cp $HOME_PI/exeamonitor_player/scripts/player /etc/init.d/

echo "Copying files for check sound..."
cp $HOME_PI/exeamonitor_player/scripts/checkSound.sh /usr/bin/

# Verify command
rc=$?
if [[ $rc != 0 ]] ; then
    exit $rc
fi

# Permisions of the file
chmod +x /etc/init.d/player
update-rc.d player defaults
chmod +x /usr/bin/checkSound.sh
(crontab -l 2>/dev/null; echo "@reboot sudo /usr/bin/checkSound.sh") | crontab -


echo "Creating Music directory..."
mkdir $HOME_PI/Music

chown -Rf pi $HOME_PI/*

echo "Finishing setup"