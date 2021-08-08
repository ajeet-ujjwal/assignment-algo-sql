from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    table = dict()
    # Fill the actual value of last occurrence
    for i in range(256):
        table[i] = -1
    for i in range(len(pattern)):
        table[ord(pattern[i])] = i;
    return table


class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)

    def decide_slide_width(self, c: str) -> int:
        return self.table[ord(c)]

    def search(self) -> int:
        s = 0
        n = len(self.text)
        m = len(self.pattern)
        while(s<=n-m):
            j = m-1
            while j>=0 and self.pattern[j] == self.text[s+j]:
                j -= 1
            if j<0:
                return s
            else:
                s += max(1, j-self.decide_slide_width(self.text[s+j]))      
        return -1
