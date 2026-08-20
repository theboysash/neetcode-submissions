class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dictionary = {}
        for char in text:
            if char in dictionary:
                dictionary[char]+=1
            else:
                dictionary[char]=1
        b = dictionary.get('b', 0)
        a = dictionary.get('a',0)
        l = dictionary.get('l',0)//2
        o = dictionary.get('o',0)//2
        n = dictionary.get('n',0)

        return min(b,a,l,o,n)

        