if [[ $(uname -s) == "Linux" ]]
then
    [ ! -d "/usr/lib/tomamosh" ] && mkdir /usr/lib/tomamosh
    cp -r ./src/* /usr/lib/tomamosh/
    cp ./assets/icon.png /usr/lib/tomamosh/
    cp ./setup/linux/tomamosh /usr/bin/
    cp ./setup/linux/tomamosh.desktop /usr/share/applications/
elif [[ $(uname -s) == "Darwin" ]]
then
    [ ! -d "/usr/local/lib/tomamosh"] && mkdir /usr/local/lib/tomamosh
    cp -r ./src/* /usr/local/lib/tomamosh/
    cp ./setup/darwin/tomamosh /usr/local/bin/
else
    echo "Cannot install on your system"
    echo "Current supported systems: Linux, Darwin (macOS)"
fi
