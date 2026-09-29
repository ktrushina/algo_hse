from anagrams import group_anagrams

def test_group_anagrams():
    result = group_anagrams(
        ["eat", "tea", "tan", "ate", "nat", "bat"]
    )
    assert sorted(map(sorted, result)) == sorted(
        map(sorted, [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    )


def test_empty_list():
    assert group_anagrams([]) == []


def test_one_word():
    assert group_anagrams(["hello"]) == [["hello"]]


def test_all_anagrams():
    result = group_anagrams(["abc", "bca", "cab"])
    assert sorted(map(sorted, result)) == [["abc", "bca", "cab"]]


def test_no_anagrams():
    result = group_anagrams(["cat", "dog", "fish"])
    assert sorted(map(sorted, result)) == [
        ["cat"],
        ["dog"],
        ["fish"],
    ]


def test_duplicate_words():
    result = group_anagrams(["eat", "eat", "tea"])
    assert sorted(map(sorted, result)) == [["eat", "eat", "tea"]]


def test_case_sensitivity():
    result = group_anagrams(["eat", "Eat"])
    assert sorted(map(sorted, result)) == [["Eat"], ["eat"]]


def test_empty_string():
    result = group_anagrams([""])
    assert result == [[""]]


def test_multiple_empty_strings():
    result = group_anagrams(["", ""])
    assert result == [["", ""]]


def test_repeated_letters():
    result = group_anagrams(["aab", "aba", "baa", "ab"])
    assert sorted(map(sorted, result)) == sorted(
        map(sorted, [["aab", "aba", "baa"], ["ab"]])
    )


def test_order_preserved_within_group():
    result = group_anagrams(["tea", "eat", "ate"])
    for group in result:
        assert group == ["tea", "eat", "ate"]


def test_single_char_words():
    result = group_anagrams(["a", "b", "a"])
    assert sorted(map(sorted, result)) == sorted(map(sorted, [["a", "a"], ["b"]]))


def test_words_with_numbers_or_symbols():
    result = group_anagrams(["a1", "1a", "a2"])
    assert sorted(map(sorted, result)) == sorted(
        map(sorted, [["a1", "1a"], ["a2"]])
    )


def test_different_lengths_never_grouped():
    result = group_anagrams(["aab", "ab", "aabb"])
    assert sorted(map(sorted, result)) == sorted(
        map(sorted, [["aab"], ["ab"], ["aabb"]])
    )
