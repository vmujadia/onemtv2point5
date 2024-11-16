from load_onemt import Translator
import sentencepiece as spm
from oneconfig import *
import random

print (SUBWORD_MODEL_PATH)
print (TRANSLATION_MODEL_FOLDER)

print (TRANSLATION_MODEL_PATH)



s = spm.SentencePieceProcessor(model_file=SUBWORD_MODEL_PATH)

translator = Translator(data_dir=TRANSLATION_MODEL_FOLDER, checkpoint_path=TRANSLATION_MODEL_PATH, batch_size=100)



def split_into_parts(text, num_words=100):
  """Splits text into parts of a given number of words.

  Args:
    text: The text to split.
    num_words: The number of words per part.

  Returns:
    A list of strings, where each string is a part of the text.
  """

  words = text.split()
  parts = []
  current_part = []
  for word in words:
    current_part.append(word)
    if len(current_part) == num_words:
      parts.append(' '.join(current_part))
      current_part = []
  if current_part:
    parts.append(' '.join(current_part))
  return parts


def translate_onemt(text, sl, tl):
    nsl = language_mapping[sl]
    ntl = language_mapping[tl]

    if len(text.split())>100:
        otext = ''
        for p in split_into_parts(text):
            soutput = s.encode(''+nsl+'-to-'+ntl+'%%% '+p, out_type=str)
            out = translator.translate([" ".join(soutput)])
            output = out[0].replace(' ','').replace('▁',' ')
            otext = otext + ' '+output
        return otext.strip()
    else:
        soutput = s.encode(''+nsl+'-to-'+ntl+'%%% '+text, out_type=str)
        out = translator.translate([" ".join(soutput)])
        output = out[0].replace(' ','').replace('▁',' ')

    return output.strip()

