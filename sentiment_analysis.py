!pip install vaderSentiment
!pip install googletrans

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

sentence1 = 'I get out of bed at half past ten'
sid.polarity_scores(sentence1)

sentence2 = 'I sadly got out of bed at half past ten'
sid.polarity_scores(sentence2)

sentence3 = 'I happily 😊 got out of bed at half past ten!!'
sid.polarity_scores(sentence3)

from googletrans import Translator

translator = Translator()
he_sentence1 = translator.translate('איזה יום שמח לי היום')
sid.polarity_scores(he_sentence1)

he_sentence2 = translator.translate('הייתי שמח הרבה יותר אם זה באמת היה כיף')
sid.polarity_scores(he_sentence2) # Computers don't understand irony
