import string
import re

class TextNormalizer():
    
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
    
    # We will use this mostly for digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. We leave the other possible mappings there for future use 
    numerals2digits_dict = {'0': 'zero', 
                            '1': 'one', 
                            '2': 'two', 
                            '3': 'three', 
                            '4': 'four',
                            '5': 'five', 
                            '6': 'six',
                            '7': 'seven', 
                            '8': 'eight', 
                            '9': 'nine', 
                            '10': 'ten', # Probably won't use any of these mappings from here and below, but keep them here in case we do later
                            '11': 'eleven', 
                            '12': 'twelve', 
                            '13': 'thirteen', 
                            '14': 'fourteen', 
                            '15': 'fifteen', 
                            '16': 'sixteen', 
                            '17': 'seventeen', 
                            '18': 'eighteen', 
                            '19': 'nineteen', 
                            '20': 'twenty', 
                            '30': 'thirty', 
                            '40': 'forty', 
                            '50': 'fifty', 
                            '60': 'sixty', 
                            '70':'seventy', 
                            '80': 'eighty', 
                            '90': 'ninety'
                           }
    
    # Here we assume that when people want to communicate the number 21 they say "twenty one" and we map the "twenty" -> 2 and leave the "one" so we turn
    # "twenty one" into "two one". Or if they want to communicate the number 79 they say "seventy nine" and we map the "seventy" -> "seven" and leave the
    # "nine" so we turn "seventy nine" into "seven nine". That means this process will work 9/10 times. For example, if someone wants to communicate the 
    # number 50 they say "fifty" and we map the "fifty" -> "five" and do not append the "zero". That is the one scenario where this process fails. 
    # This is a more general problem that cannot be solved because the mapping from word numbers to numerals is not a bijection. We cannot know if by 
    # "twenty one" they meant 20 1, or 21. So we assume they meant the latter because it will likely be correct the majority of the time.
    words2digits_dict = {'ten': 'one zero', 
                         'eleven': 'one one', 
                         'twelve': 'one two', 
                         'thirteen': 'one three', 
                         'fourteen': 'one four',
                         'fifteen': 'one five', 
                         'sixteen': 'one six', 
                         'seventeen': 'one seven', 
                         'eighteen': 'one eight',
                         'nineteen': 'one nine', 
                         'twenty': 'two', 
                         'thirty': 'three', 
                         'forty': 'four',
                         'fifty': 'five', 
                         'sixty': 'six', 
                         'seventy': 'seven', 
                         'eighty': 'eight', 
                         'ninety': 'nine'
                        }
    
    
    def __init__(self):
        """Here we compile all of the regular expressions ahead of time so they
        can be used more quickly in the __call__ routine"""

        # Used to find all occurences of the ' apostrophe and replace with the ’ apostrophe
        self.apostrophe_re = re.compile(r'\'')
        self.she_re = re.compile(r's/he')
        # Find everything in parenthesis
        self.parenthesis_re = re.compile(r'\(.*?\)')
        # Match email templates
        self.emails_re = re.compile(r'\b([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+)\.([A-Z|a-z]{2,})\b')
        # Find the word1/word2 patterns
        self.slash_re = re.compile(r'\b(\w+)/(\w+)\b')
        # Find the word1.word2 patterns
        self.dot_re = re.compile(r'\b(\w+)\.(\w+)\b') 
        # Find any special characters
        self.puncts_re = re.compile(r'[' + string.punctuation + 'øØ§£€¥©®°±¶¼½¾×–—•™¢₧ƒ¬≤≥±δΩΘΦσ' + ']')
        self.contractions_re = re.compile(r'(%s)' % '|'.join(TextNormalizer.contractions_dict.keys()))
        # After contractions have been expanded we now wish to remove all possessives
        self.possessives_re = re.compile(r'’s')
        self.numerals2digits_re = re.compile(r'(\d)')
        self.words2digits_re = re.compile(r'(%s)' % str(r'\b' + r'\b|\b'.join(TextNormalizer.words2digits_dict.keys())+r'\b'))
        self.whitespaces_re = re.compile('\s+')
        
        
    def __expand_contractions(self, text):
        
        """This internal routine manages the contraction expansion process. This is important because the 
        Universal Sentence Encoder ignores many punctuations. When that happens, the beginning and ending 
        of contractions concatenate into a single non-word or out-of-context word. 
        
        For example, he's -> hes, I'd -> id, I'll -> ill, aren't -> arent.
        """
        
        def replace(match):
            return self.contractions_dict[match.group(0)]
        
        return self.contractions_re.sub(replace, text)


    def __num2words(self, text):
        
        """
        An internal routine that normalizes all number/numeric content into single digit text words.
        """
        
        def replace_numerals(match):
            return ' %s ' % self.numerals2digits_dict[match.group(0)]
        text = self.numerals2digits_re.sub(replace_numerals, text)
        
        def replace_numwords(match):
            return self.words2digits_dict[match.group(0)]
        
        return self.words2digits_re.sub(replace_numwords, text)
    
    
    def __process(self, text):
        
        # Standardize apostrophe's
        text = self.apostrophe_re.sub(r'’', text.strip().lower())
        # Emails challenge the USE. Here we break them down to "username at domainname dot top-leveldomain"
        text = self.emails_re.sub(r'\1 at \2 dot \3', text)
        # Replace all of the s/he's with she
        text = self.she_re.sub(r'she', text)
        # Remove everything in parenthesis
        text = self.parenthesis_re.sub(r'', text)
        # Replace the "word1/word2" patterns with "word1 or word2". 
        text = self.slash_re.sub(r'\1 or \2', text)
        # Replace the "word1.word2" patterns with "word1 word2". 
        text = self.dot_re.sub(r'\1 \2', text)
        # Expand all contractions according to the contractions dict
        text = self.__expand_contractions(text)
        # Now we remove all possessive clauses to have a uniform representation for subjects/nouns
        text = self.possessives_re.sub(r'', text)
        # Replace all arabic numerals and complex number words to single digit words
        text = self.__num2words(text)
        # Replace any left over punctuations with nothing
        text = self.puncts_re.sub(r'', text)
        # Finally replace all dupliacte whitespace characters (space, tab, newline, carriage return) with a single space
        text = self.whitespaces_re.sub(' ', text)
        
        return text.strip()
        

    def __call__(self, text_input):
        
        module = text_input.__class__.__module__
        name = text_input.__class__.__name__

        if isinstance(text_input, str):
            cleaned_text = self.__process(text_input)
        elif isinstance(text_input, list):
            cleaned_text = [self.__process(s) for s in text_input]
        elif isinstance(text_input, set) or isinstance(text_input, tuple):
            cleaned_text = self.__call__(list(text_input))
        elif (module, name) == ('pandas.core.series', 'Series'):
            cleaned_text = text_input.apply(self.__call__)
        elif (nodule, name) == ('numpy', 'ndarray'):
            cleaned_text = self.__call__(text_input.tolist())
        else:
            raise TypeError(f"Input type {type(text_input)} is not currently supported")
        
        return cleaned_text

    
# Example use case
if __name__ == "__main__":
    
    from preprocess import TextNormalizer
    
    # Create TextNormalizer object
    clean = TextNormalizer()
    
    text = """(≥ 1 + E-1 or D-1, 2, 3) If there is a defibrillator (AED) available get/grab it. 
            Also, if they're at twenty one 38 King Dr. I'll need to know. Meet me at 1:12 pm. 
            Call me at +1 800 forty three fifty one or email me at myname123_pizza@twentyone-5.net."""
    print("\nRaw Text\n\n" + text)
    
    # Clean input text with builtin __call__ routine
    text = clean(text)
    print("\nClean Text\n\n" + text + '\n')
