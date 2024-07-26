def decode_s( s: str, p: str) -> bool:

# write your code here
 def match_decoder_key(s, p):
    if len(s) == 0 and len(p) == 0:
        return True
    if len(s) == 0 or len(p) == 0:
        return False

    if p[0] == '*':
        # Try matching the star symbol with no letters, one letter, or multiple letters
        return match_decoder_key(s, pattern[1:]) or \
               match_decoder_key(s[1:], pattern) or \
               match_decoder_key(s[1:], pattern[1:])
    elif pattern[0] == '?':
        # Try matching the question mark with any single letter
        return match_decoder_key(s[1:], pattern[1:])
    else:
        # Check if the current letters match
        return s[0] == pattern[0] and match_decoder_key(s[1:], pattern[1:])#
  
        return False