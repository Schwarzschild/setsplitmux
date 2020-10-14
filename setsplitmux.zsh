#!/bin/zsh

cd $HOME/dev/setsplitmux
SPLITMUXDIR=$HOME/Dropbox/LIVESTREAMING/TechnicalFiles/"SPLITMUX - CUSTOM LAYOUTS"


eval "$(pyenv init -)"
if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi

pyenv shell splitmux
python setsplitmux.py $SPLITMUXDIR/$@
