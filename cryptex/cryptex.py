from Crypto import Random
from Crypto.Cypher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join

class Cryptex:
    def __init__(self,key):
        self.key = key

    def pad(self,s):
        return s+b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt():
        message =

