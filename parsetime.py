#import timex
from mytime import Time
import nltk
import re


from nltk import pos_tag, word_tokenize

from word2number import w2n


types_of_sentence = {0:'[unknown]', 1:'[tStamp]', 2:'[tPeriod]', 3:'[tTrigger]'}

def parse_sentence(input):
    #tx = timex.tag(input)
    pos_tagged = nltk.pos_tag(word_tokenize(input))
    #print(pos_tagged)
    

    sentence_type = 1
    important_words = []


    for pos in pos_tagged:
        val = pos[0].lower()
        key = pos[1]

        timevalue = 0

        time = Time()

        

        if(key == 'CD'):
            if(val.isdigit()):
                timevalue = val
            else:
                timevalue = w2n.word_to_num(val)

        if(key == 'NN' or key == 'NNS'):
            if(val[:4] == 'year' or val[:5] == 'month' or val[:4] == 'week'):
                important_words += [val]
                sentence_type = 2
            if(val == 'minutes'):
                important_words += [val]

        if(key == 'JJ'):
            if(val == 'next' or val == 'last'):
                important_words += [val]
                sentence_type = 2

        if(key == 'IN'):
            if(val == 'before' or val == 'after'):
                important_words += [val]
                sentence_type = 3

    print(important_words)


    print(types_of_sentence[sentence_type], time.get_human())




examples = ["I want to book a cab 20 minutes from now", "Looking to a make reservation for two people day after tomorrow at seven in the evening", "I was working in san francisco for last two years", "Any time after 2 is fine", "Before 5 is good"]


for e in examples:
    #print(timex.tag(e))
    #print(nltk.pos_tag(word_tokenize(e)))
    print(e)
    parse_sentence(e)
    print('==\n')
parse_sentence(input())
print('==\n')



'''
1. I want to book a cab 20 minutes from now - [tStamp]2020 hrs, Thursday, July 20th
2. Looking to a make reservation for two people day after tomorrow at seven in the evening - [tStamp]1900 hrs,Saturday
3. I was working in san francisco for last two years - [tPeriod] - 2013-2015
4. Any timer after 2 is fine - [tTrigger] - start - 0200 hrs,July 21st 2015
5. Before 5 is good - [tTrigger] - start - now, 2000hrs, July 20th, 2015 : end - 0500 hrs, July 21st, 2015
'''

'''
[('I', 'PRP'), ('want', 'VBP'), ('to', 'TO'), ('book', 'NN'),
 ('a', 'DT'), ('cab', 'NN'), ('20', 'CD'), ('minutes', 'NNS'), 
 ('from', 'IN'), ('now', 'RB')]

==

[('Looking', 'VBG'), ('to', 'TO'), ('a', 'DT'), ('make', 'NN'),
 ('reservation', 'NN'), ('for', 'IN'), ('two', 'CD'), ('people', 'NNS'), 
 ('day', 'NN'), ('after', 'IN'), ('tomorrow', 'NN'), ('at', 'IN'), ('seven', 'CD'),
  ('in', 'IN'), ('the', 'DT'), ('evening', 'NN')]

==

[('I', 'PRP'), ('was', 'VBD'), ('working', 'VBG'), ('in', 'IN'),
 ('san', 'JJ'), ('francisco', 'NN'), ('for', 'IN'), ('last', 'JJ'), 
 ('two', 'CD'), ('years', 'NNS')]

==

[('Any', 'DT'), ('time', 'NN'), ('after', 'IN'), ('2', 'CD'),
 ('is', 'VBZ'), ('fine', 'JJ')]
==

[('Before', 'IN'), ('5', 'CD'), ('is', 'VBZ'), ('good', 'JJ')]

==
'''