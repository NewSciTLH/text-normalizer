from text_normalizer import TextNormalizer
import pandas as pd

tn = TextNormalizer()


def test_empty_input():
    """Test processing an empty string"""
    
    inpt = ""
    result = tn(inpt)
    assert result == ""


def test_string_input():
    """Test the processing of a single input string"""

    inpt = "hello this sentence should come out exactly how it went in"
    result = tn(inpt)
    assert result == inpt


def test_docstring_input():
    """Test the processing of a single input docstring"""

    inpt = """hello this sentence should come out exactly how it went in"""
    result = tn(inpt)
    assert result == inpt


def test_list_input():
    """Test the processing of lists of strings"""

    inpt = ["clean string one", "we are cleaning things"]
    result = tn(inpt)

    assert result == ["clean string one", "we are cleaning things"]


def test_set_input():
    """Test the processing of sets of strings as input"""

    trgt_sentences = [ "sentence one", 
                       "sentence two", 
                       "three sentences total"]
    inpt = set(trgt_sentences)
    result = tn(inpt)

    assert all([r in trgt_sentences for r in result])


def test_pandas_input():
    """Test processing pandas Series as input"""

    words = ("howdy", "seven four", "erase keep")
    inpt = pd.Series(words)
    result = tn(inpt)

    assert all([r in words for r in result])
