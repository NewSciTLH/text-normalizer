from text_normalizer import TextNormalizer

contractions_dict  =  {"aren’t": "are not", 
                       "can’t": "cannot", 
                       "could’ve": "could have",
                       "couldn’t": "could not", 
                       "didn’t": "did not", 
                       "doesn’t": "does not",
                       "don’t": "do not", 
                       "hadn’t": "had not", 
                       "hasn’t": "has not",
                       "haven’t": "have not", 
                       "he’d": "he had", 
                       "he’ll": "he will",
                       "he’s": "he is", 
                       "how’d": "how did", 
                       "how’s": "how is", 
                       "i’d": "i would",
                       "i’ll": "i will", 
                       "i’m": "i am", 
                       "i’ve": "i have", 
                       "isn’t": "is not",
                       "it’d": "it would", 
                       "it’ll": "it will", 
                       "it’s": "it is", 
                       "let’s": "let us",
                       "ma’am": "madam", 
                       "might’ve": "might have", 
                       "must’ve": "must have",
                       "mustn’t": "must not", 
                       "needn’t": "need not", 
                       "she’d": "she had", 
                       "she’ll": "she will", 
                       "she’s": "she is", 
                       "should’ve": "should have",
                       "shouldn’t": "should not", 
                       "that’d": "that would", 
                       "that’s": "that is",
                       "there’s": "there is", 
                       "they’d": "they would", 
                       "they’ll": "they will",
                       "they’re": "they are", 
                       "they’ve": "they have", 
                       "wasn’t:": "was not",
                       "we’d": "we would", 
                       "we’ll": "we will", 
                       "we’re": "we are", 
                       "we’ve": "we have", 
                       "weren’t": "were not", 
                       "what’ll": "what will",
                       "what’s": "what is",
                       "what’ve": "what have",
                       "when’s": "when is",
                       "when’ve": "when have",
                       "where’d": "where did",
                       "where’s": "where is",
                       "where’ve": "where have",
                       "who’ll": "who will",
                       "who’s": "who is",
                       "who’ve": "who have",
                       "why’s": "why is",
                       "why’ve": "why have",
                       "will’ve": "will have",
                       "won’t": "will not",
                       "would’ve": "would have",
                       "wouldn’t": "would not",
                       "y’all": "you all",
                       "ya’ll": "you all",
                       "you’d": "you would",
                       "you’ll": "you will",
                       "you’re": "you are",
                       "you’ve": "you have"
                      }

tn = TextNormalizer()


def test_email_input():
    """Test the cleaning and formatting of emails"""

    inpt = "mathnathan@gmail.com"
    result = tn(inpt)

    assert result == "mathnathan at gmail dot com"

    inpt = "SuzieCoyle1987@yahoo.eu.com"
    result = tn(inpt)

    assert result == "suziecoyle one nine eight seven at yahoo eu dot com"


def test_contractions():
    """Test contraction expansions"""

    inpt, output = zip(*contractions_dict.items())
    result = tn(inpt)

    assert all([r in output for r in result])


def test_phonenumbers():
    """Test conversion of phone numbers to single words"""

    inpt = "344 891 0807"
    result = tn(inpt)

    assert result == "three four four eight nine one zero eight zero seven"


def test_large_numbers():
    """Test conversion of large number strings to single words"""

    inpt = "twenty five thirty five and seventy one"
    result = tn(inpt)

    assert result == "two five three five and seven one"


def test_final():
    """Test requiring multiple regular expressions to ensure order is applied
    correctly"""

    inpt = ("(≥ 1 + E-1 or D-1, 2, 3) If there is a defibrillator (AED) "
    "available get/grab it. Also, if they're at twenty one 38 King Dr. "
    "I'll need to know. Meet me at 1:12 pm. Call me at +1 800 forty "
    "three fifty one or email me at myname123_pizza@twentyone-5.net.")

    output = ("if there is a defibrillator available get or grab it also if "
    "they are at two one three eight king dr i will need to know meet me at one "
    "one two pm call me at one eight zero zero four three five one or email me "
    "at myname one two three pizza at twentyone five dot net")

    result = tn(inpt)

    assert result == output
