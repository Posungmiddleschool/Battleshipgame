import matplotlib.pyplot as plt
def graphics():
  fig, ax = plt.subplots(figsize=(7, 7))
  plt.style.use('dark_background')
  ax.set.title('BATTLESHIP GAME')
  ax.set_xticks(range(11))
  ax.set_yticks(range(11))
  ax.set_facecolor('#4166F5')
  
