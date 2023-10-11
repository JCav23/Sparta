# LeetCode75 : 1768 - Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

def merge_alternately(word1, word2):
    merged = ""
    len1 = len(word1)
    len2 = len(word2)
    min_len = min(len1, len2)
    for i in range(min_len):
        merged += word1[i] + word2[i]
    if len1 == len2:
        return merged
    elif len1 > len2:
        merged += word1[min_len:]
        return merged
    else:
        merged += word2[min_len:]
        return merged


print(merge_alternately('abc', 'qpr'))
