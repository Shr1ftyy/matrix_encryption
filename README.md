# Hill Cipher-like encryption Implementation in Python 3
### Author: Syeam Bin Abdullah
## Info:
 - mod.py - Hill Cipher, but with a twist (adds a stop char if length of
	 sentence is odd)
 - mod_complex.py - Uses an receives nx1 vector (sentence), and encodes it
	 using a nxn encoding matrix. To decipher cipher text, the program finds the
	 dot product between the inverse of the encoding matrix and the cipher text
 - modinv.py - script to find the reciprocal modulo (modular inverse) _k_, using
	 inputs _k_ and _m_, such that _ak = 1 mod m_
