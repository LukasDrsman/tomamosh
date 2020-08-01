# tomamosh

A tkinter frontend for [itsKaspar's tomato](https://github.com/itsKaspar/tomato)

## Install and run

### On unix-like systems (gnu/linux, OSX, bsd, etc.):
Using cli:
```sh
git clone https://github.com/LukasDrsman/tomamosh.git
cd tomamosh
./tomamosh
```
Using gui:
1. Download zip on https://github.com/LukasDrsman/tomamosh/archive/master.zip
2. Unzip the file
3. Run `tomamosh` with bash

### On windows
1. Download zip on https://github.com/LukasDrsman/tomamosh/archive/master.zip
2. Unzip the file
3. Navigate to `src` directory and run `tomamosh.py` with python

## Usage
1. A window with a button **Select AVI file** will appear, click the button
2. You will be prompted to select avi file
3. A window with options will appear
4. Change options to desired state and press **Render !** <br><br>
![preview image](https://github.com/LukasDrsman/tomamosh/blob/master/assets/preview.png)

### Mode:
- `void` - does nothing
- `random` - randomizes frame order
- `reverse` - reverse frame order
- `invert` - switches each consecutive frame witch each other
- `bloom` - duplicates **Positional frame** number n times
- `pulse` - duplicates groups of **Positional frames** n times
- `overlapped` - copy group of **Positional frames** taken from every nth position<br><br>
\*n refers to the number in **Quantity** option
