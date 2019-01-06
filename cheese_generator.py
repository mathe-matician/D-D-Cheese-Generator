import cheese_data
from random import choice

def cheese_generator():
  print(choice(cheese_data.races),
        choice(cheese_data.textures),
        choice(cheese_data.cheese_names),
        "from",
        choice(cheese_data.places))

#if __name__ == "__main__": cheese_generator()
