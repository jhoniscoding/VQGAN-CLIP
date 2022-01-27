#!/bin/bash

echo "Installing tools..."
apt-get install -y tmux vim zsh imagemagick ffmpeg
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
./commands/install_ohmyzsh.sh
echo "Installing tools... Done"

echo "Exporting poetry venv..."
ZSH_CONFIG_PATH="$HOME/.zshrc"
POETRY_BIN="$HOME/.poetry/bin"
POETRY_VENV=$(cat <<EOF
export PATH="$POETRY_BIN:$PATH"
export POETRY_VENV=$( $POETRY_BIN/poetry env list --full-path | grep Activated | cut -d' ' -f1 )
EOF
)
echo "$POETRY_VENV" >> "$ZSH_CONFIG_PATH"
echo "Exporting poetry venv... Done"

echo "Installing Lab libs..."
$POETRY_BIN/poetry install
echo "Installing Lab libs... Done"
