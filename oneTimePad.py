import logging
import math
from random import randint

# Configure logging to write debug messages to a file
logging.basicConfig(level=logging.INFO)

MESSAGE = '✖️➗🏂'
CHARACTERS = max(ord(char) for char in MESSAGE)
BINARY_LENGTH = math.ceil(math.log2(CHARACTERS))

################# One Time Pad Generation #################
def generate_one_time_pad(message: str):
    message_length = len(message)
    pad_length = message_length * (BINARY_LENGTH+1)
    
    one_time_pad = ''
    for _ in range(pad_length):
        binary_num = randint(0, 1)
        one_time_pad += str(binary_num)
    
    # Log the generated one-time pad
    logging.debug(f'Generated One-Time Pad: {one_time_pad}')
    logging.info(f"One Time Pad: {one_time_pad}")
    
    return one_time_pad

################# Character <--> Binary #################
def charIntoBinary(character: str) -> str:
    ordinal_character = ord(character)
    
    binary_character = bin(ordinal_character)[2:].zfill(BINARY_LENGTH)
    binary_character = '0' + binary_character
    
    # Log character to binary conversion
    logging.debug(f'Character: {character}, Binary: {binary_character}')
    
    return binary_character

def turnIntoBinary(message: str) -> str:
    binary_message = ''
    for character in message:
        binary_char = charIntoBinary(character)
        binary_message += binary_char
    
    # Log the entire binary message
    logging.debug(f'Binary Message: {binary_message}')
    
    return binary_message

def binaryIntoChar(binary_char: str) -> str:
    binary_char = binary_char[1:] # Removing first 0.
    number = int(binary_char, 2)
    logging.debug(f"Number: {number}")
    character = chr(number) # Number turned into character.
    return character

def turnIntoString(binary_message: str) -> str:
    characters = []
    for i in range(0, len(binary_message), (BINARY_LENGTH+1)):
        binary_char = binary_message[i:i+(BINARY_LENGTH+1)]
        character = binaryIntoChar(binary_char)
        characters.append(character)
    return ''.join(characters)

################# Encryption #################
def bitMath(message_bit: str, pad_bit: str) -> str:
    encoded_bit = (int(message_bit) + int(pad_bit)) % 2
    return str(encoded_bit)

def Encrypt(binary_message: str, one_time_pad: str) -> int:
    output_byte = ''
    for message_bit, pad_bit in zip(binary_message, one_time_pad):
        output_bit = bitMath(message_bit, pad_bit)
        output_byte += output_bit
    
    return output_byte

################# Encode Decode #################
def encode(message: str, one_time_pad: str) -> str:
    binary_message = turnIntoBinary(message)
    logging.info(f"Original Binary Message: {binary_message}")

    encoded_message = Encrypt(binary_message, one_time_pad)
    return encoded_message

def decode(encoded_message: str, one_time_pad: str) -> str:
    decoded_binary_message = Encrypt(binary_message=encoded_message, one_time_pad=one_time_pad)
    decoded_message = turnIntoString(decoded_binary_message)
    return decoded_message

################# Main #################
if __name__ == '__main__':
    logging.info(f"Message Before: {MESSAGE}")
    one_time_pad = generate_one_time_pad(MESSAGE)

    encoded_message = encode(MESSAGE, one_time_pad)
    logging.info(f"Encoded Message: {encoded_message}")
    decoded_message = decode(encoded_message, one_time_pad)

    logging.info(f'Message After: {decoded_message}')
