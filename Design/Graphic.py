import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
plt.ion()
fig, axes = plt.subplots(figsize=(12,5), layout='constrained')

def plot_the_graph(points, gen):
    axes.clear()
    axes.plot(gen, points, color='red')
    axes.xaxis.set_major_locator(MaxNLocator(integer=True))
    axes.yaxis.set_major_locator(MaxNLocator(integer=True))
    axes.set_title("MACHINE LEARNING EVOLUTION")
    axes.set_xlabel("Generations")
    axes.set_ylabel("Points")
    axes.grid(True)
    plt.draw()
    plt.pause(1)