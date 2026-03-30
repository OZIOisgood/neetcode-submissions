class Solution:
    DIGITS_PER_CHAR: int = 7
    SEP: str = '-'

    def encodeWord(self, word: str) -> str:
        resList: List[str] = []
        for letter in word:
            order_number = ord(letter)
            resList.append(f'{order_number:0{self.DIGITS_PER_CHAR}d}')
        return ''.join(resList)

    def decodeWord(self, s: str) -> str:
        if len(s) == 0:
            return ''
        if len(s) % self.DIGITS_PER_CHAR != 0:
            raise ValueError(
                f'Encoded word length must be a multiple of {self.DIGITS_PER_CHAR}, '
                f'but got value: {s}, with the length {len(s)}'
            )
        chars: List[str] = []
        for i in range(0, len(s), self.DIGITS_PER_CHAR):
            chunk = s[i:i + self.DIGITS_PER_CHAR]
            code_point = int(chunk)
            chars.append(chr(code_point))
        return ''.join(chars)

    def encode(self, strs: List[str]) -> str:
        resList: List[str] = []
        for word in strs:
            resList.append(self.encodeWord(word) + self.SEP)
        res = ''.join(resList)
        print(f'Encoded: "{res}"')
        return res

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        encodedWords: List[str] = s.split(self.SEP)
        if encodedWords and encodedWords[-1] == '':
            encodedWords.pop()
        print(f'encodedWords: {encodedWords}')
        words: List[str] = []
        for word in encodedWords:
            print(f'To decode word: "{word}"')
            words.append(self.decodeWord(word))
        print(f'Decoded: {words}')
        return words
