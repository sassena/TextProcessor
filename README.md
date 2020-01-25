# TextProcessor
A simple module for basic text preprocessing.
Uses spacy language models.

###Installation
Install the script:
```
python setup.py install
```
Then download spacy language model:
```
python -m spacy download en_core_web_sm
```
###Usage
```
from text_processor import process
p = process.TextProcessor()
s = "Hi Im Josè and Im from Latin America, how are you?"
print(p.preprocess(s))
['hi', 'jose', 'latin', 'america']
```
For usage in other languages, add the correct language model 
to TextProcessor, such as:
```
from text_processor import process
p = process.TextProcessor(language="es_core_news_sm")
```
