import itertools
import matplotlib.pyplot as plt
import seaborn as sns

def reg_resid_plots(data, cmap_name="tab10"):
    num_cols = data.shape[1]
    permutation_count = num_cols * (num_cols - 1)

    fig, ax = plt.subplots(permutation_count, 2, figsize=(15, 4 * permutation_count), squeeze=False)

    cmap = plt.get_cmap(cmap_name)
    colors = [cmap(i % cmap.N) for i in range(permutation_count)]

    for (x, y), axes, color in zip(
        itertools.permutations(data.columns, 2),
        ax,
        colors
    ):
        sns.regplot(x=x, y=y, data=data, ax=axes[0], color=color)
        sns.residplot(x=x, y=y, data=data, ax=axes[1], color=color)

    fig.tight_layout()
    plt.close(fig)
    return fig