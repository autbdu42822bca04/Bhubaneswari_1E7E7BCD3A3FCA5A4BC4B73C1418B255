class player:
  def play(self):
    print("the player is playing cricket")
class Batsman(player):
  def play(self):
    print("the bast man is batting")
class Bowler(player):
  def play(self):
    print("the bowler is bowling")
bastman=Batsman()
bowler=Bowler()
bastman.play()
bowler.play()


