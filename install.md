#  Installation instructions:

## Brief version

If you are already familiar with Javelin-Script:

1. Create a new layer
2. Go to layer -> Custom scripts -> New
3. Copy and paste from [javelin-taipo](/javelin-taipo/3_javelin_inputs/javelin-taipo.javelin-script) into new script
4. Set up keys

    Go to each key and set the press and release scripts for each key

    0 for left, 1 for right

   ### Examples on how to make the press and release scripts

    press script for left inner button:
    ```cpp
    pressTaipoInner(0);
    ```

    release script for right R button:
    ```cpp
    releaseTaipoR(1);
    ```

## Detailed version

### Keeb
You will need a keyboard that Javelin firmware can build for.  At the time of writing this was:
- Asterisk
- Corne
- Jarne
- Jarne Blade
- Kyria
- Polyglot
- Starboard
- The Uni

### Javelin
Go to the [Javelin firmware builder](https://lim.au/#/software/javelin-steno) and select your board.

![alt text](<docs/images/Screenshot 2025-01-10 201754.png>)

### Select 'expert options'.

![alt text](<docs/images/Screenshot 2025-01-10 202702.png>)

### Defaults
Accept the defaults generally.

![alt text](<docs/images/Screenshot 2025-01-10 202904.png>)

![alt text](<docs/images/Screenshot 2025-01-10 202932.png>)

![alt text](<docs/images/Screenshot 2025-01-10 203012.png>)

### Dictionaries
Add your dictionaries, or accept Plover/Lapwing defaults

![alt text](<docs/images/Screenshot 2025-01-10 203217.png>)

### Start a layout
Select 'edit layout', then add layer.

![alt text](<docs/images/Screenshot 2025-01-10 203419.png>)

![alt text](<docs/images/Screenshot 2025-01-10 203534.png>)

### Name the layer 'Taipo' (or your choice).

![alt text](<docs/images/Screenshot 2025-01-10 203634.png>)

###  Main script
Select 'Custom Scripts' and click the plus to add a script.  Name it, and paste the code from the `javelin-taipo` link above into the 'User Script' area.

![alt text](docs/images/Screenshot%202025-02-22%20173043.png)

![alt text](docs/images/Screenshot%202025-02-22%20173455.png)

### Key scripts / prefabs
Select each key in turn and select a 'Prefab' from the 'Taipo' layer.  This should pre-populate the key name, press and release scripts.  The 'Prefab' is a code element that identifies the key, associates the key press script, and also attempts to highlight the next key for you, to reduce this setup time.

![alt text](docs/images/Screenshot%202025-02-22%20173455.png)

![alt text](docs/images/Screenshot%202025-02-22%20174012.png)
![alt text](docs/images/Screenshot%202025-02-22%20174056.png)

### Layer control

Add layer change keys, so that you can change between default (steno) and taipo.

![alt text](<docs/images/Screenshot 2025-01-11 153136.png>)

![alt text](<docs/images/Screenshot 2025-01-11 153251.png>)

### Save. Save. Save.

Don't forget to download both your layout and script files when you're done, and save them somewhere (just in case!).  3-dots at top-right of screen.

![alt text](<docs/images/Screenshot 2025-01-10 204716.png>)
   
### Alt: Direct load layout

Alternatively, for the starboard, you can direct load [this layout](<3_javelin_inputs/Starboard.javelin-layout>) with the 'load layout' button.

![alt text](<docs/images/Screenshot 2025-01-10 204817.png>)

###  Follow the instructions for Orthography.

![alt text](<docs/images/Screenshot 2025-01-10 204926.png>)

### Click 'Create Firmware'.
The firmware is created locally in your browser (yes, incredible, right?) and your browser will download the `.uf2` file to your desktop.  Follow the instructions to load the firmware onto your keyboard and test.  Note that the firmware upload buttons may differ for different hardware (eg Starboard), please refer your hardware-specific instructions if required.

![alt text](<docs/images/Screenshot 2025-01-10 205058.png>)

###  Good luck on your steno and taipo journey.