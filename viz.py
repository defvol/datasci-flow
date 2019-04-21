# Visualization tools for our notebooks
# Some plot helpers come from kaggle.com/helgejo/an-interactive-data-science-tutorial
import seaborn as sns
import matplotlib.pyplot as plt

def plot_categories(df, cat, target, **kwargs):
    row = kwargs.get('row', None)
    col = kwargs.get('col', None)
    facet = sns.FacetGrid(df, row=row, col=col)
    facet.map(sns.barplot, cat, target)
    facet.add_legend()

def plot_correlation_map(df):
    corr = df.corr()
    _ , ax = plt.subplots(figsize=(12, 10))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    _ = sns.heatmap(
        corr,
        cmap=cmap,
        square=True,
        cbar_kws={'shrink': .9},
        ax=ax,
        annot=True,
        annot_kws={'fontsize': 12}
    )

def plot_distribution(df, var, target, **kwargs):
    """
    Fit and plot a univariate or bivariate kernel density estimate.
    """
    row = kwargs.get('row', None)
    col = kwargs.get('col', None)
    facet = sns.FacetGrid(df, hue=target, aspect=4, row=row, col=col)
    facet.map(sns.kdeplot, var, shade=True)
    facet.set(xlim=(0, df[var].max()))
    facet.add_legend()

def plot_histogram(df, var, **kwargs):
    row = kwargs.get('row', None)
    col = kwargs.get('col', None)
    facet = sns.FacetGrid(df, aspect=4, row=row, col=col)
    facet.map(sns.distplot, var, hist=True)
    facet.set(xlim=(0, df[var].max()))
    facet.add_legend()

def plot_histograms(df, variables, n_rows, n_cols):
    fig = plt.figure(figsize=(16, 12))
    for i, var_name in enumerate(variables):
        ax=fig.add_subplot(n_rows, n_cols, i+1)
        df[var_name].hist(bins=10, ax=ax)
        ax.set_title('Skew: ' + str(round(float(df[var_name].skew()), )) + ' - ' + var_name)
        ax.set_xticklabels([], visible=True)
        ax.set_yticklabels([], visible=True)
    fig.tight_layout()
    plt.show()
