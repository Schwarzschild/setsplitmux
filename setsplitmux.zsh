#!/bin/zsh

export SPLITMUX_IP=192.168.10.12
export SPLITMUX_DIR=$HOME/Dropbox/LIVESTREAMING/TechnicalFiles/"SPLITMUX - CUSTOM LAYOUTS"
export SPLITMUX_USER=marc
export SPLITMUX_PW=marc


cd $HOME/dev/setsplitmux
eval "$(pyenv init -)"
if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi

pyenv shell splitmux
# python setsplitmux.py $@
# python setsplitmux.py "2-shot C&D.xml"
python setsplitmux.py "BBoy_3+1(usk).xml"