def get_number_of_words(text):
  words_list = text.split()
  return len(words_list)

def character_count(text):
  unique_characters = {}
  text = text.lower()
  for n in text:
    if n in unique_characters:
      unique_characters[n] += 1
    else:
      unique_characters[n] = 1
  
  return unique_characters

def sorted_char_count(char_count):
  sorted_list = []
  for char in char_count:
    sorted_list.append({"character": char, "count": char_count[char]})
  sorted_list.sort(reverse = True, key = lambda dict: dict["count"])
  return sorted_list
