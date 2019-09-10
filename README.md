# A GUI Interface for Generating Multi-channel Audio

This repository contains the code and other necessary files for generating mulit-channel audio. 


### Prerequisites

You need to have GNU C++ coompiler for Windows/G++ compiler for linux installed to run the RIR generation based on Habets RIR source – receiver model. Other installed requirements are:

* octave
* python3
* PyQt5 for python3

For installing PyQt5 for python3 for Linux(Ubuntu):
```
sudo apt-get install python3-pyqt5 
```
For installing PyQt5 for python3 for Windows:
```
pip install pyqt5
```

### Instructions to Setup

Clone the repository to any directory with:
```
$ git clone ...
```
and change to the repository folder with
```
$ cd ....
```
You need to compile rir_generator.cpp to mex file supported by octave with :
```
$ mkoctfile --mex rir_generator.cpp
```
## Using the GUI interface

To use GUI to generate RIR run:
```
python gui.py 1
```
![GUI for RIR/Audio generation](https://github.com/iitbdaplab/multi-channel_audio_simulator/blob/master/images/gui1.png)
### Description of the GUI

This interface can do **two** tasks : 
1) Generate multi-channel Room Impulse Response(RIR)
2) Generate multi-channel audio from the stored RIR.

#### Generate Room Impulse Response(RIR)
Two radio buttons are provided for one to generate the RIR and other to generate multi-channel audio.
To generate the RIR, the parameters needed are : Type of Room, Type of Array, Number of Channels, Number of Speakers, Array and Speaker locations, Reverberation time ms(T60). Other parameters required to generate RIR like sampling frequency is 16kHz, reflection coefficient is -1.

Here are the allowable choices for the parameters to be specified inside GUI, some default choices about the array locations and speaker locations will be shown:
```
**Description**      : **Values**
Room Type              3 rooms are choosen for analysis 
Array Type             {Linear,Circular}
Number of channels     {2..6} linear, Circular {4 mics on rim, 5 with 4 on rim             
                       and 1 at center,8 mics on rim}
Array center           x,y co-ordinates tuple in meters
Array Radius/Spacing   [2-5] in cm
Speaker Locations      {(x1,y1),(x2,y2),...} each tuple is speaker location
T60                    Value in range 0-1 in seconds
 
```
The *Generate-RIR* button will generate the RIR, which by default will be stored at *rir/* folder.

#### Generate multi-channel audio from the stored RIR 
To generate multi-channel audio from the generated RIR, browse the stored RIR file(stored in .mat format). Choose the required number of source files from any desired folder. After all the source files are choosen, *Generate-multi channel audio* button will be enabled. This will generate the multi-channel audio and will be stored at *multi_audio* folder bu default.

###
Alternatively, to Generate the RIR from command line without running the GUI, using:
```
python gui.py 0 --a_type <Array type> --num_c <Number of channels> --num_s <Number of speakers> --center=<Array center> --radius <Radius/Spacing> --spk_loc <Speaker locations> --room <Room Dimensions> --t60=<Reverration time constant>

``` 
For Example, you can run:
```
python gui.py 0 --a_type l --num_c 4 --num_s 2 --center 2 1.5 1 –radius 5 --spk_loc 2 3.15 1 2.65 1 1 --room 6 4 --t60 0.3  

```
Here, the choices of the arguments are as follows:
```
**Description**     : **Arguments** : **Values**
Array type            a_type          ‘l’,’c’ 
No. of channels       num_c           2-8
No. of Speakers       num_s           2-5
Arr. Radius(cm)       radius          2-5
Arr. Center(x,y,z)    center          x1 y1 z1
Speaker locations     spk_loc         x1 y1 z1, ... ... ...,
Room Dimensions(M)    room            l  w h
Reverberation Time    t60             [0,1]
```
Note that speaker and array locations needs to be within the room dimension when you sepcify them, else it will give an error.




### Authors

* **Sachin Nayak **--Feel free to contact me at sachin.ee@iitb.ac.in for any issues 


