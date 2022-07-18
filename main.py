from text_normalizer import TextNormalizer

# Create TextNormalizer object
tn = TextNormalizer()

text = """(≥ 1 + E-1 or D-1, 2, 3) If there is a defibrillator (AED) available get/grab it. 
        Also, if they're at twenty one 38 King Dr. I'll need to know. Meet me at 1:12 pm. 
        Call me at +1 800 forty three fifty one or email me at myname123_pizza@twentyone-5.net."""
print("\nRaw Text\n\n" + text)

# Clean input text with builtin __call__ routine
text = tn(text)
print("\nClean Text\n\n" + text + '\n')
