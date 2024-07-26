def decode_message( s: str, p: str) -> bool:

# write your code here
    if len(s) == 0 and len(p) == 0:
        return True
    if len(s) == 0 or len(p) == 0:
        return False

    if p[0] == '*':
        # Try matching the star symbol with no letters, one letter, or multiple letters
        return d(s, p[1:]) or \
               d(s[1:], p) or \
               d(s[1:], p[1:])
    elif p[0] == '?':
        # Try matching the question mark with any single letter
        return d(s[1:], p[1:])
    else:
        # Check if the current letters match
        return s[0] == p[0] and d(s[1:], p[1:])#
  
        return False