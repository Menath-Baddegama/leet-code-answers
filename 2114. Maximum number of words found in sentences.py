class Solution:
    def mostWordsFound(sentences):
        numOfWords = [len(s.split()) for s in sentences]
        return max(numOfWords)

if __name__ == "__main__":
    pass