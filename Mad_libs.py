def get_input(word_type: str):
    user_input: str = input(f"Enter a word {word_type}: ")
    return user_input

adjective_1 = get_input("adjective")
adverb_2 = get_input("adverb")
noun_3 = get_input("noun")
plural_noun_4 = get_input("plural noun")
noun_5 = get_input("noun")
noun_plural_6 = get_input("plural noun")
noun_7 = get_input("noun")
name_8 = get_input("noun")
noun_9 = get_input("noun")
adverb_10 = get_input("adverb")
noun_11 = get_input("noun")
plural_noun_12 = get_input("plural noun")
noun_13 = get_input("noun")
plural_noun_14 = get_input("plural noun")
noun_15 = get_input("noun")
noun_16 = get_input("noun")

text = f"""A/An {adjective_1} dictionary is the essential reference for home,
 school, or {noun_7}. A dictionary not only defines {plural_noun_12}, 
 but tells you how to spell words and how to pronounce them {adverb_2}. 
 Dictionaries are available in local {name_8} stores or, if necessary, 
 you can order one with a/an {noun_13} card over the Internet. 
 For the average {noun_3}, a medium-sized dictionary is best. 
 For researchers, an unabridged {noun_9}, which has more than 200,000 {plural_noun_14}, 
 will be needed. For those who can’t remember the meaning of any {plural_noun_4}, 
 a pocket-sized dictionary works {adverb_10}. These dictionaries are small enough to fit in a woman’s {noun_15}, 
 the pocket of a man’s {noun_5}, or a kid’s back {noun_11}. As Henry Wadsworth Longefellow, the famous , wrote, 
 “I’d rather go without food in my {noun_16} than go without a dictionary on my {noun_plural_6} shelf.”
"""

print(text)