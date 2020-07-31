# tomamosh

A tkinter frontend for [itsKaspar's tomato](https://github.com/itsKaspar/tomato)

## Install and run

### On unix-like systems:
```sh
git clone https://github.com/LukasDrsman/tomamosh.git
cd tomamosh
./tomamosh        # you can also run `tomamosh` script trough file explorer
```

### On windows
1. Download zip on https://github.com/LukasDrsman/tomamosh/archive/master.zip
2. Unzip the file
3. Navigate to `src` directory and run `tomamosh.py` with python

## Usage
1. A window with a button "Select AVI file" will appear, click the button
2. You will be prompted to select avi file
3. A window with options will appear: <br><br>
![preview image](https://github.com/LukasDrsman/tomamosh/blob/master/assets/preview.png)

### Mode:
- `void` - does nothing
- `random` - randomizes frame order
- `reverse` - reverse frame order
- `invert` - switches each consecutive frame witch each other
- `bloom` - duplicates positional frame number n times
- `pulse` - duplicates groups of positional frames n times 
- `overlapped` - copy group of `c` frames taken from every `n`th position
- `jiggle` - take frame from around current position. `n` parameter is spread size [broken]
 
