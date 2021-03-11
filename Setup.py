import os
import sys

try:
    import wget
except ImportError:
    print('Fatal Error: Please install wget lib')
    print("Use the command 'pip install wget")

CURR_DIR = os.path.dirname(os.path.realpath(__file__))

Decoder = "https://pastebin.com/raw/A9skHdKf"
Encoder = "https://pastebin.com/raw/CLqRJNGe"

De = os.path.isfile(CURR_DIR + "/Decoder.py")
En = os.path.isfile(CURR_DIR + "/Encoder.py")

if En == "True":
    os.remove(CURR_DIR + "/Encoder.py")
    wget.download(Encoder, CURR_DIR + "/Encoder.py")

if En == "False":
    wget.download(Encoder, CURR_DIR + "/Encoder.py")

if De == "True":
    os.remove(CURR_DIR + "/Decoder")
    wget.download(Encoder, CURR_DIR + "/Decoder.py")

if De == "False":
    wget.download(Decoder, CURR_DIR + "/Decoder.py")