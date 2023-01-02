class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        #if all Upper
        if word.upper() == word:
            return True
        #if all lower
        elif word.lower() == word:
            return True
        #if first letter is upper and the rest is lower
        elif word[0].upper() == word[0] and word[1:].lower() == word[1:]:
            return True
        else:
            return False
