import sys

NON_TOKENS = {',', ';', ':'}

def is_token(entry):
    if entry in NON_TOKENS:
        return False

    return True

    
def get_tokens(line):
    if not line:
        return []
        
    return [x for x in line.split() if is_token(x)]

    
def test_given_line_without_tokens_returns_empty_list():
    assert [] == get_tokens(None)

    
def test_given_line_with_one_non_token_returns_empty_list():
    assert [] == get_tokens(" ")

    
def test_given_line_with_one_token_returns_list_with_one_token():
    assert ['t'] == get_tokens("t")

    
def test_given_line_with_two_tokens_returns_list_with_tokens():
    assert ['t', 'o'] == get_tokens("t o")

    
def test_given_line_with_token_non_token_token_returns_list_with_tokens():
    assert ['t', 'o'] == get_tokens("t , o")

    
def test_complex():
    print get_tokens("Log <12,33,44z>: alpha: 5, beta: 6, gamma: 9")
    assert False
        