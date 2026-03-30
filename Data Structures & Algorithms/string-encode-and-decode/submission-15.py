class Solution:
    DIGITS_PER_CHAR: int = 7          # 0-1114111 → 7-digit decimal

    # ---------- helpers ----------
    def encodeWord(self, word: str) -> str:
        resList: List[str] = []
        for letter in word:
            order_number = ord(letter)
            # фикс-ширина, но не меньше 7-ми
            resList.append(f'{order_number:0{self.DIGITS_PER_CHAR}d}')
        return ''.join(resList)

    def decodeWord(self, s: str) -> str:
        if len(s) == 0:                # пустая строка
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

    # ---------- public API ----------
    def encode(self, strs: List[str]) -> str:
        """
        Каждое слово → код + дополнительный '-' в конце.
        Пример:
            ["a", "", "bc"] -> "0000097--0000098 0000099-"
        """
        resList: List[str] = []
        for word in strs:
            resList.append(self.encodeWord(word) + '-')  # «минус» после КАЖДОГО слова

        res = ''.join(resList)
        print(f'Encoded: "{res}"')
        return res

    def decode(self, s: str) -> List[str]:
        """
        Пустая строка => []
        Каждый '-' обозначает границу слова.
        Два подряд '-' → закодированная пустая строка.
        Заканчиваем всегда на '-', поэтому последний сплит-фрагмент пустой и отбрасывается.
        """
        if len(s) == 0:
            return []

        encodedWords: List[str] = s.split('-')
        if encodedWords and encodedWords[-1] == '':
            encodedWords.pop()         # убираем «хвостовой» пустой элемент

        print(f'encodedWords: {encodedWords}')

        words: List[str] = []
        for word in encodedWords:
            print(f'To decode word: "{word}"')
            words.append(self.decodeWord(word))

        print(f'Decoded: {words}')
        return words