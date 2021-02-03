class Song:

  def __init__(self, title):
    # Initialize each Song object with its title
      self.__title = title
      self.__next_song = None


  # Create a getter method for the title attribute, called get_title
  def get_title(self):
    return self.__title
  
  
  # Create a setter method for the next_song attribute, called set_title. Make sure titles are type cased to strings and are Title Cased.
  def set_title(self, title):
    # Use title() method to make the string Title Cased
    self.__title = str(title).title()


  # Create a getter method for the next_song attribute, called get_next_song
  def get_next_song(self):
    return self.__next_song


  # Create a setter method for the next_song attribute, called set_next_song
  def set_next_song(self, next_title):
    # Convert title of input to a string with Title Case
    next_title.__title = str(next_title.__title).title()
    self.__next_song = next_title


  # Using the __str___ dunder method, return a string of the song title.
  def __str__(self):
    return self.get_title()


  # Using the __repr__ dunder method, return a string formatted as the following:'Song Title -> Next Song Title'
  def __repr__(self):
    return f"{self.get_title} -> {self.get_next_song}"
