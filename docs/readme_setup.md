# test sphinx

sudo pip3 install sphinx sphinx-rtd-theme

mkdir docs

cd docs

sphinx-quickstart

sphinx-apidoc -o ./source ../pyciosa

make clean && make html
