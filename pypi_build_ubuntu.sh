#rm -r dist ;
python3 setup.py sdist bdist_wheel ;
if twine check dist/* ; then
    if [ "$1" = "--upload" ] ; then
        if [ "$2" = "--prod" ] ; then
            twine upload dist/* ;
        else
            twine upload --repository-url https://test.pypi.org/legacy/ dist/*
        fi
    fi
fi