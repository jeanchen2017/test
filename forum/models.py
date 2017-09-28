from django.db import models
from django.utils import timezone

import nltk
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.parse.stanford import StanfordParser
from collections import Counter
from urlextract import URLExtract

def clean_url(doc):
    extractor = URLExtract()
    urls = list(set(extractor.find_urls(doc)))
    with_url = doc.split()
    remove_url = ' '.join(filter(lambda x: x not in urls, with_url))
    remove_url = remove_url.lower()
    return remove_url

class Post(models.Model):
    def __str__(self):
        return str(self.pk)

    avatar_id = models.IntegerField()
    post_id = models.AutoField(primary_key=True)
    parent_id = models.ForeignKey('self', related_name='parentID', default=0)
    level = models.IntegerField()
    post_subject = models.CharField(max_length=200)
    post_content = models.TextField()
    is_bot = models.BooleanField(default = False)
    is_question = models.BooleanField(default = False)
    timestamp = models.DateTimeField(
            default=timezone.now)

class AverageNumberOfCharactersPerWord(models.Model):
    def average_number_of_characters_per_word(doc):
        remove_url = clean_url(doc)
        filtered = ''.join(filter(lambda x: x not in '".,;!-?', remove_url))
        words = filtered.split()
        average = sum(len(word) for word in words) / len(words)
        return average

class Thoughtfulness_Score(models.Model):
    post_id = models.OneToOneField('Post', primary_key = True)
    post_content = models.TextField()
    thoughtfulness_score = models.FloatField()
    average_number_of_characters_per_word = AverageNumberOfCharactersPerWord()
