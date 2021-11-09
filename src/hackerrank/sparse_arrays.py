# https://www.hackerrank.com/challenges/sparse-arrays/problem



def matching_strings(strings, queries):
    # string_occurrence = {query: 0 for query in queries}
    # for query in queries:
    #     for string in strings:
    #         if query == string:
    #             string_occurrence[query] = string_occurrence[query] + 1
    # # return string_occurrence.values()
    return [strings.count(q) for q in queries]


occurrence = matching_strings(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc'])
for count in occurrence:
    print(count)
