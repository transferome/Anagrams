import get_dictionary as getd
from timeit import default_timer as timer


word_list = getd.return_dictionary()


def method1(name):
    word_sorted = sorted(name)
    anagram_list = list()
    for word in word_list:
        word = word.lower()
        if word != name:
            if sorted(word) == word_sorted:
                anagram_list.append(word)
    print(anagram_list)
    return anagram_list


def permutations(word):
    if len(word) == 1:
        return [word]

    perms = permutations(word[1:])
    char = word[0]
    result = []
    # anagram_list = list()
    for perm in perms:
        for i in range(len(perm)+1):
            print(type(perm[:i]+ char + perm[i:]))
            result.append(perm[:i]+ char + perm[i:])
    return result
    # for r in result:
    #     if r in word_list:
    #         anagram_list.append(r)
    # return anagram_list


def check_dictionary(result_list, dictionary_in):
    anagram_list = list()
    for result in result_list:
        if result in dictionary_in:
            anagram_list.append(result)
    return anagram_list


start = timer()
output = permutations('dogs')
verify = check_dictionary(output, word_list)
end = timer()
print(end - start)


def permutations(word):
    if len(word) == 1:
        return [word]

    perms = permutations(word[1:])
    char = word[0]
    result = []

    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i]+ char + perm[i:])
    return result

print(permutations('dogs'))
