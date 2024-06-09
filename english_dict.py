DICT_FILE = 'words_alpha.txt'

def get_all_n_letters_words(n):
    with open(DICT_FILE, 'r') as f:
        lines = f.readlines()
    lines = [line[:-1] for line in lines] # remove newline char
    return [word for word in lines if len(word) == n]

# Get list of words without the not correct index char and with the correct index char
def get_all_words_after_filters(n,not_correct_index_list,correct_index_list,wrong_letters):
  with open(DICT_FILE, 'r') as f:
        lines = f.readlines()
  lines = [line[:-1] for line in lines] # remove newline char
  all_words = [word for word in lines if len(word) == n]
  all_words_after_filters = []

  for word in all_words:
    if not any(char in word for char in wrong_letters):
      is_letters_in_correct_idx = True

      for dic in correct_index_list:
        if(list(dic.keys())[0] not in word or
             word[list(dic.values())[0]] != list(dic.keys())[0]):
            is_letters_in_correct_idx = False

      if is_letters_in_correct_idx:
        for dic in not_correct_index_list:
          
          if(list(dic.keys())[0] not in word or   
            word[list(dic.values())[0]] == list(dic.keys())[0]):     
            is_letters_in_correct_idx = False

        if is_letters_in_correct_idx:
          all_words_after_filters.append(word)   

  return all_words_after_filters