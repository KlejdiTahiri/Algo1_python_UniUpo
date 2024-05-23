def calculate_anagrams(word):
  anagrams = set()
  recursive_anagrams("",word,anagrams)
  return anagrams


def recursive_anagrams(partial, characters, anagrams):
  if len(characters) == 0:
    anagrams.add(partial)
  else:
    for index, ch in enumerate(characters):
      #new tentative
      partial += ch
      new_characters = characters[:index] + characters[index+1 :]
      #recursive call
      recursive_anagrams(partial, new_characters, anagrams)
      #backtraking
      #BEWARE: I don't need to fix characters, because I've created a new list (new_characters)
      # strings are immutable -> I need to create a new list
      partial = partial[0:len(partial)-1]


print(calculate_anagrams("dog"))
