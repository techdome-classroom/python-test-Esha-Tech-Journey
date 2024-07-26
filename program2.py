def decode_message( s: str, p: str) -> bool:

# write your code here
##        def match_decoder_key(message, pattern):
    if len(message) == 0 and len(pattern) == 0:
        return True
    if len(message) == 0 or len(pattern) == 0:
        return False

    if pattern[0] == '*':
        # Try matching the star symbol with no letters, one letter, or multiple letters
        return match_decoder_key(message, pattern[1:]) or \
               match_decoder_key(message[1:], pattern) or \
               match_decoder_key(message[1:], pattern[1:])
    elif pattern[0] == '?':
        # Try matching the question mark with any single letter
        return match_decoder_key(message[1:], pattern[1:])
    else:
        # Check if the current letters match
        return message[0] == pattern[0] and match_decoder_key(message[1:], pattern[1:])
*/
  
        return False