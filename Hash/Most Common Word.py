from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        new_paragraph = ''
        for para in paragraph:
            if para.isalpha() or para==' ':
                new_paragraph+=para.lower()
            else:
                new_paragraph+=' '
        answer=[0,'none']
        words = new_paragraph.split()
        word_list = defaultdict(int)
        banned_list = {word: 1 for word in banned}
        for word in words:
            if word in banned_list: continue
            word_list[word]+=1
            if answer[0] < word_list[word]:
                answer = [word_list[word], word]
        return answer[1]
