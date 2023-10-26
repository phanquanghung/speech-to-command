# Speech-to-Command
Server for a VR world that enables users to use their voice to control 3D objects, like hiding, pulling, or pushing them.

## Overview

The project uses the WhisperX speech-to-text module to convert the user's speech to text, then uses a large language model (LLM) to detect the intended command, and finally sends that command to the VR world.

The project is divided into two parts: the Python server and the VR Environment (C#) client. The server handles all of the speech-to-text/text-to-command processing and communication with the VR world. The Unity3D VR environment implements voice commands to modify the selected object's position or appearance.

## Installation
To reproduce exact results, I recommend installing an environment identical to mine. You also need to have a VR headset, such as Oculus Rift or HTC Vive, connected to your computer.

1. Create a new conda environment with

```
conda create --name myenv python=3.9
conda activate myenv
```

2. Install [WhisperX](https://github.com/m-bain/whisperX#3-install-this-repo)

This speech-to-text module requires CUDA 11 or lower versions to run. Please make sure you have the compatible CUDA version installed before running this module.

3. Install the remaining dependencies:

```
pip install -r requirements.txt
```

## Usage
### Running the server

```
python server.py
```

This will start the server on port 3000 and listen for incoming messages from the VR client. The server will also load the Large Language Model and initialize the speech-to-text engine.

### Running Unity3D

To start the VR world, you will need to open the [Unity3D project](https://drive.google.com/file/d/19hGW-0N1CVpwQZsCQTHoWVReVM1cIccg/view?usp=drive_link) and press the Play button.

Once both the server and the VR world are running, you can use your voice to control 3D objects in the VR world. 

To start voice command, point your controller at an object and press the trigger. This will start recording and send the audio to the server for speech-to-command processing.

The following are some examples of voice commands:
- Get over here! -> towards
- Show yourself! -> show
- Put on camouflage! -> hide

## Limitations
This project is still under development and has the following limitations:

- Voice recording is currently done on the server side because I am not proficient in C#, the programming language of Unity3D. This may affect voice recognition and command execution performance.

- The socket connection between the server and the VR client can be disconnected unexpectedly. This can happen due to network issues, server errors, or VR client crashes. 

- The VR environment is currently plain and simple due to time constraints and the limitations of my hardware.

I am working to address these limitations and improve the project over time.

## Acknowledgements

I hope that this project will be useful to the community and that it will help to make VR experiences more immersive and accessible.

I hope you enjoy trying my speech-to-command VR experience as much as I enjoyed creating it. 😊
