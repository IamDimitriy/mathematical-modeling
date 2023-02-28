import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib



def build_a_graph(df):
    matplotlib.rcParams['font.size'] = 18
    sns.set(style="darkgrid")
    matplotlib.rcParams['figure.dpi'] = 200
    fig = sns.kdeplot(df['with CRISPR/Cas'], fill=True, color="r")
    fig = sns.kdeplot(df['no CRISPR/Cas'], fill=True, color="b")
    plt.title('График численности популяций настоящего моделирования')
    plt.xlabel('t, секунды')
    plt.ylabel('количество')
    plt.tight_layout()
    plt.show()
