import matplotlib.pyplot as plt
plt.ion()
fig, axes = plt.subplots(figsize=(12,5), layout='constrained')

def plot_the_graph(points, gen):
    axes.clear()
    axes.plot(gen, points, color='red')
    axes.set_title("MACHINE LEARNING EVOLUTION")
    axes.set_xlabel("Generations")
    axes.set_ylabel("Points")
    axes.grid(True)
    plt.draw()
    plt.pause(0.001)