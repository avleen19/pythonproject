#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyspellchecker


# In[2]:


from spellchecker import SpellChecker


# In[3]:



def spell_check(text):
    spell = SpellChecker()
    words = text.split()
    corrected_text = []
    corrected_flag = False
    for word in words:
        corrected_word = spell.correction(word)
        if corrected_word != word:
            corrected_text.append(corrected_word)
            corrected_flag = True
        else:
            corrected_text.append(word)
    corrected_text = ' '.join(corrected_text)
    print("Original text:")
    print(text)
    print("\nCorrected text:")
    print(corrected_text)

    if not corrected_flag:
        print("\nNo misspelled words found.")


# In[4]:


text = "This is a testt to chck the spellinng of worrds."


# In[5]:


spell_check(text)


# In[ ]:




