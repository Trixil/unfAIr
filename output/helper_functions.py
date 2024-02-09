
def test_get_phonemes(text, expected_phonemes):
    result = get_phonemes(text)
    if result == expected_phonemes:
        return True
    else:
        return False
