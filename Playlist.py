from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    if self.__first_song == None:
      # Create a new song object with title passed in
      new_song = Song(str(title).title())
      # Assign the new song as the first of the playlist
      self.__first_song = new_song
    else:
      # Create a new song object with title passed in
      new_song = Song(title)
      # Iterate through the list of existing songs until the end is reached
      current_song = self.__first_song
      while current_song.get_next_song() != None:
        current_song = current_song.get_next_song()
      # Assign the new song to the end
      current_song.set_next_song(new_song)
      




  # Create a method called find_song that searches for whether a song exits in the playlist and returns its index. 
  # The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    # Traverse the whole playlist
    current_song = self.__first_song
    song_index = 0
    while current_song != None:
      # Check if each song title matches a Title Cased version of the input parameter
      if current_song.get_title() == str(title).title():
        return song_index
      current_song = current_song.get_next_song()
      song_index += 1
    return -1


  # Create a method called remove_song that removes a song from the playlist. 
  # This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    # Check the first song before traversing the list because it has a special pointer
    current_song = self.__first_song
    if current_song.get_title() == str(title).title():
      self.__first_song = current_song.get_next_song()
      return
    # Check the rest of the playlist
    while current_song.get_next_song() != None:
      # If the song is found, then link the previous song to the song after the target song
      if current_song.get_next_song().get_title() == str(title).title():
        current_song.set_next_song(current_song.get_next_song().get_next_song())
        return
    # End the function so that the program continues running if the title searched was not found
    return f"{title.title()} was not found in the playlist."



  # Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    # Traverse the list while keeping count with each iteration
    current_song = self.__first_song
    counter = 0
    while current_song != None:
      current_song = current_song.get_next_song()
      counter += 1
    return counter


  # Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    # Traverse the list with an index starting at 1
    current_song = self.__first_song
    song_index = 1
    while current_song != None:
      print(f"{song_index}. {current_song.get_title()}")
      current_song = current_song.get_next_song()
      song_index += 1

  