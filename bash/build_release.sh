#!/bin/bash
echo "🏗️Script for developer. Copy files from source to build"
firstline=$(head -n 1 source/changelog.md)
read -a splitfirstline <<< $firstline
version=${splitfirstline[1]}
echo "Building version:" $version
echo "Do you want to continue? Enter 1 for continue or 0 to exit:"
read versioncontinue
if [ $versioncontinue -eq 1 ]
then 
		echo "OK"
    for filename in source/*
    do
    	if [ $filename == "source/secretinfo.md" ]
      then
      		secretline=$(head -n 1 source/secretinfo.md)
          echo "${secretline/42/XX}" > build/secretinfo.md
          echo "The file is being modified and copied:" $filename
      else
      		echo "The file is being copied:" $filename
          cp $filename build/.
      fi
    done
    cd build/
    echo "Build version $version contains:"
    ls
    echo "Creating zip-file: build-$version.zip"
    zip -r "build-$version.zip" .
    cd ..
    
else 
		echo "Please come back when you are ready"
fi