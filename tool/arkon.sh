#!/usr/bin/env bash

set -e -u

readonly this_dir=$( dirname "$0" )
readonly base_dir=$( cd $this_dir/.. && pwd )
readonly pyenv_dir=$base_dir/.pyenv

cd $base_dir
[ -d $pyenv_dir ] && source $pyenv_dir/bin/activate

echo "### base_dir=$base_dir"
echo "### pyenv_dir=$pyenv_dir"
