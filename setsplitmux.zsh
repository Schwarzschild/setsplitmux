cd $HOME/dev/splitmux
SPLITMUXDIR=$HOME/Dropbox/LIVESTREAMING/TechnicalFiles/"SPLITMUX - CUSTOM LAYOUTS"



if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi

pyenv shell splitmux
python setsplitmux.py $SPLITMUXDIR/$@
