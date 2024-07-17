#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[85]:


sent = "Kim chased Lee"


# In[86]:


tokens = sent.split()


# In[87]:


kim = {'CAT': 'NP', 'ORTH':'Kim', 'REF':'k'}


# In[88]:


chase = {'CAT': 'V', 'ORTH':'chased', 'REL':'chase'}


# In[89]:


lee = {'CAT': 'NP', 'ORTH':'Lee', 'REF':'l'}


# In[90]:


def lex2fs(word):
    for fs in [kim, lee, chase]:
        if fs['ORTH'] == word:
            return fs


# In[96]:


subj, verb, obj = lex2fs(tokens[0]), lex2fs(tokens[1]), lex2fs(tokens[2])


# In[97]:


chase['AGT'] = 'sbj'


# In[98]:


chase['PAT'] = 'obj'


# In[99]:


verb['AGT'] = subj['REF']


# In[100]:


verb['PAT'] = obj['REF']


# In[101]:


for k in ['ORTH', 'REL', 'AGT', 'PAT']:
    print("%-5s => %s" % (k, verb[k]))


# In[102]:


nltk.data.show_cfg('grammars/book_grammars/feat0.fcfg')


# In[103]:


#second


# In[108]:


tokens = 'Kim likes children'.split()


# In[109]:


from nltk import load_parser


# In[110]:


cp = load_parser('grammars/book_grammars/feat0.fcfg', trace=2)


# In[111]:


trees = cp.parse(tokens)


# In[112]:


for tree in trees:
    print(tree)


# In[114]:


#Processing feature Structure


# In[115]:


fs1 = nltk.FeatStruct(TENSE='past', NUM='sg')


# In[116]:


print(fs1)


# In[117]:


fs1 = nltk.FeatStruct(PER=3, NUM='pl', GND='fem')


# In[118]:


print(fs1['GND'])


# In[120]:


fs2 = nltk.FeatStruct(POS='N', AGR=fs1)


# In[121]:


print(fs2)


# In[124]:


print(nltk.FeatStruct("""[NAME='Lee', AGE=33, ADDRESS=(1)[NUMBER=74, STREET='rue Pascal'], 
SPOUSE=[NAME='Kim', ADDRESS->(1)]]"""))


# In[129]:


fs1 = nltk.FeatStruct(NUMBER=74, STREET='rue Pascal')


# In[130]:


fs2 = nltk.FeatStruct(CITY='Paris')


# In[131]:


print(fs1.unify(fs2))


# In[133]:


fs0 = nltk.FeatStruct("""[NAME=Lee,
ADDRESS=[NUMBER=74,
STREET='rue Pascal'], SPOUSE= [NAME=Kim,
ADDRESS=[NUMBER=74, 
STREET='rue Pascal']]]""")
print(fs0)


# In[134]:


fs1 = nltk. FeatStruct("[SPOUSE = [ADDRESS = [CITY = Paris]]]")
print (fs1.unify(fs0))


# In[136]:


fs1 = nltk.FeatStruct("[ADDRESS1=[NUMBER=74, STREET='rue Pascal']]")
fs2 = nltk.FeatStruct("[ADDRESS1=?x, ADDRESS2=?x]")
print(fs2)


# In[137]:


print (fs2.unify(fs1))


# In[ ]:




