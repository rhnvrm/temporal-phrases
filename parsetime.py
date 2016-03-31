import timex
import nltk

from nltk import pos_tag, word_tokenize

examples = ["Let's go sometime this week", "Tomorrow I'm going to the park.", "I want to book a cab 20 minutes from now", "Looking to a make reservation for two people day after tomorrow at seven in the evening", "Any time after 2 is fine", "Before 5 is good"]


for e in examples:
	print(timex.tag(e))
	print(nltk.pos_tag(word_tokenize(e)))
	print('\n')

'''
1. I want to book a cab 20 minutes from now - [tStamp]2020 hrs, Thursday, July 20th
2. Looking to a make reservation for two people day after tomorrow at seven in the evening - [tStamp]1900 hrs,Saturday
3. I was working in san francisco for last two years - [tPeriod] - 2013-2015
4. Any timer after 2 is fine - [tTrigger] - start - 0200 hrs,July 21st 2015
5. Before 5 is good - [tTrigger] - start - now, 2000hrs, July 20th, 2015 : end - 0500 hrs, July 21st, 2015
'''