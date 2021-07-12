#!/bin/bash

echo "machine urs.earthdata.nasa.gov login $EARTHDATA_LOGIN password $EARTHDATA_PASSWORD" > .netrc
chmod 0600 .netrc
jb build book
