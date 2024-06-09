from audioop import add
import english_dict
import random
import requests

WORD_LEN = 5
TRIES = 6
API = 'https://wordle-api.vercel.app/api/wordle' # An API to a clone of the wordle game

all_words = english_dict.get_all_n_letters_words(WORD_LEN)

def post_guess(guess):
  body_obj = {'guess': guess}
  res = requests.post(API, json = body_obj).json()

  return res

def main():
  current_word = 'roate'
  wrong_letters = [] # contains strings
  correct_letters_idx = [] # contains dicts (string:int)
  not_correct_letter_idx = [] # contains dicts (string:int)
  is_correct = False
  guess_num = 1

  while guess_num <= TRIES and not is_correct:
    guess_num += 1
    res = post_guess(current_word)
    was_correct = res['was_correct']

    if was_correct:
      print('Success! the word is:',current_word)
      is_correct = True
    else:
      char_info = res['character_info']

      for i in range(len(char_info)):   
        char = char_info[i] 
        char_name = char['char']
        char_in_word = char['scoring']['in_word']
        char_correct_idx = char['scoring']['correct_idx']

        if not char_in_word:
          wrong_letters.append(char_name)
        else:
          if not char_correct_idx:
            not_correct_letter_idx.append({char_name:i})
          else:
            if all(char_name not in d for d in correct_letters_idx):
              correct_letters_idx.append({char_name:i})  
      all_words_after_filter = english_dict.get_all_words_after_filters(WORD_LEN,not_correct_letter_idx,correct_letters_idx,wrong_letters)
      current_word = random.choice(all_words_after_filter)
      print(current_word)

if __name__ == '__main__':
    main()
