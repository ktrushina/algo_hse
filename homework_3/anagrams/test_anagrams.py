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
