
def test_get_phonemes():
    test_cases = [
        {"text": "hello", "expected_phonemes": ["h", "e", "l", "o"]},
        {"text": "world", "expected_phonemes": ["w", "o", "r", "l", "d"]},
        {"text": "python", "expected_phonemes": ["p", "y", "t", "h", "o", "n"]}
    ]
    
    for test_case in test_cases:
        assert test_get_phonemes(test_case["text"], test_case["expected_phonemes"]) == True, f'Error at {test_case["text"]}'
        
test_get_phonemes()
