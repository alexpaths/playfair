# Playfair Matrix Creator

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)

This script creates a random 6x6 matrix consisting of capital letters 
and numbers (0-9) for use with the [Wheatstone–Playfair cipher][1] - a systemmatic digram substitution cipher. This easy to use pocket cipher is a great intro ciphers and encryption.

## How it works

### Authentication

1. Users predistribute matrix pair
2. Alice (person 1) picks any two characters and asks Bob (person 2) to 'authenticate <Char 1> <Char 2>'
3. Bob (person 2) would respond with the characters  as if they were encrypting the digram as instructed below.

### Encrypting

Message: "HELLO WORLD!"

1. The Message is broken into digrams: HE LL OW OR LD !
	-	digrams consisting of repeat letters must be eliminated. Common practice is to replace with a lesser used letter such as 'X'. For this matrix, since numbers are included, we shall use '2' to indicate a double letter
	- Punctuation and spaces are normally not included in the message. For this case, we will use '0' to indicate stop or period if the last digram consists of a singular character. For this message, the '!' is ignored. Some have used numbers in lieu of spaces. When in doubt, the shorter the message, the better.
2.	The final pre-encryption message is now: HE L2 OW OR LD
3. Encryption is done in pairs. Take the sample matrix below

| A | B | C | D | E | 0 |
| --- | --- | --- | --- | --- | --- |
| F | G | H | I | J | 1 |
| K | L | M | N | O | 2 |
| P | Q | R | S | T | 3 |
| U | V | W | X | Y | 4 |
| Z | 5 | 6 | 7 | 8 | 9 |

'HE' the first pair, forms the corners of a box. Therefore the encrypted text are the opposing corners or 'JC'

'L2' are in the same row. We then chose the character immediately to the right of each character or 'MK' (since '2' was on the end of the row, we wrap around to the beginning).

Similarly, if the characters had been in the same column, we would choose the character immediately below the original characters, wrapping to the top of the column if required. 

'OW' again forms a box, so 'MY'

'OR' again forms a box, so 'MT'

Lastly 'LD' forms a box, so 'NB'

The transferred, encrypted message would read: 'JC MK MY MT NB'

Decryption would work in the opposite way. Both parties would require the exact matrix in order to communicate.

By collecting multiple messages encrypted using this method, common pairs may be found that reveals the original matrix. Hence this cipher is no longer used for more than demonstration.  

## Disclaimer

This code and the cipher used here are very rudimentary and should not be used in life-threatening situations. This code is provided as an academic exercise only. 

Contributors are not responsible for any bodily harm or legal claim incurred. Contributors make no claim as to effectiveness of this cipher for privacy or security.

[1]: https://en.wikipedia.org/wiki/Playfair_cipher
