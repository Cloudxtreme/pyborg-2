# pyborg
A python based bot with (some) AI

## Development Environment Setup
1. Install [PyCharm community edition](https://www.jetbrains.com/pycharm/download/)
2. Fork or Pull the source for from GitHub (*TO-DO: push to GitHub*)

## Setup Text To Speech Engine and Wrapper Python Library
Install `pyttsx` along with its dependencies.
### Mac
Install `pyaudio` dependency and for that you'd need `portaudio`
```commandline
# brew install portaudio
# sudo python -m pip install pyaudio
# sudo python -m pip install pyttsx
```
### Windows
On windows `pyaudio` installation should fetch and install prepackaged binaries which include `portaudio`.
```commandline
# sudo python -m pip install pyaudio
# sudo python -m pip install pyttsx
```

## Setup Speech Recognition
```commandline
sudo python -m pip install SpeechRecognition
```
If you want to use an offline recognizer you may want to install `CMU-Sphinx`
```commandline
# brew tap watsonbox/cmu-sphinx
# brew install --HEAD watsonbox/cmu-sphinx/cmu-sphinxbase
# brew install --HEAD watsonbox/cmu-sphinx/cmu-pocketsphinx
```
