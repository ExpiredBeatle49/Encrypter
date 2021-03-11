import os

try:
    import wget
except ImportError:
    print('Fatal Error: Please install wget lib')
    print("Use the command 'pip install wget")

CURR_DIR = os.path.dirname(os.path.realpath(__file__))

Decoder = "https://github.com/ExpiredBeatle49/Encrypter/releases/download/2.0/Decode.py"
Encoder = "https://github.com/ExpiredBeatle49/Encrypter/releases/download/2.0/Encode.py"

try:
    wget.download(Encoder, CURR_DIR + "/Encoder.py")
except:
    os.remove(CURR_DIR + "/Encoder")
    wget.download(Encoder, CURR_DIR + "/Encoder.py")

try:
    wget.download(Decoder, CURR_DIR + "/Decoder.py")
except:
    os.remove(CURR_DIR + "/Decoder")
    wget.download(Encoder, CURR_DIR + "/Decoder.py")