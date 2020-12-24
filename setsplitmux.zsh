#!/bin/zsh

export PATH=/usr/local/bin:$PATH

export SPLITMUX_DIR=$HOME/dev/setsplitmux
export SPLITMUX_IP=192.168.88.205
export SPLITMUX_LAYOUTDIR=$HOME/Dropbox/LIVESTREAMING/TechnicalFiles/SplitmuxCustomLayouts
export SPLITMUX_USER=marc
export SPLITMUX_PW=marc

if [[ $HOST == "mm" ]]
then
  export SPLITMUX_DIR=$HOME/Documents/dev/setsplitmux
  export SPLITMUX_LAYOUTDIR=$SPLITMUX_DIR/ConfigFiles
  export PCMD=$HOME/.pyenv/versions/3.8.2/envs/splitmux/bin/python
else
  export PCMD=$HOME/.pyenv/shims/python
fi

cd $SPLITMUX_DIR

export PYENV_ROOT="$HOME/.pyenv"
eval "$(pyenv init -)"
export VIRTUAL_ENV=""
if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi
pyenv shell splitmux

echo "About to run setsplitmux.py"
python $SPLITMUX_DIR/setsplitmux.py $@

echo "Finished."
