def group_anagrams(strs):
    '''
    Группирует слова, являющиеся анаграммами

    Args:
        strs: список строк

    Returns:
        Список групп анаграмм
    '''
    groups = {}

    for word in strs:
        key = ''.join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())

