import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(color_codes=True)

client_df=pd.read_csv('./client_data (1).csv')
price_df=pd.read_csv('./price_data (1).csv')

print(client_df.head(3))
print(price_df.head(3))

client_df.info()
price_df.info()

print(client_df.describe())
print(price_df.describe())

def plot_stacked_bars(dataframe,title_,size_=(18,20),rot_=0,legend_="upper right"):
    ax=dataframe.plot(
        kind='bar',
        title=title_,
        rot=rot_,
        figsize=size_,
        stacked=True
    )

    annotate_stacked_bars(ax,textsize=14)
    plt.legend(["Retention","Churn"],loc=legend_)
    plt.ylabel("company base(%)")
    plt.show()
def annotate_stacked_bars(ax,pad=0.99,textsize=13,color="white"):
    for p in ax.patches:
        value=str(round(p.get_height(),1))
        if value==0.0:
            continue
        ax.annotate(
            value,
                ((p.get_x()+ p.get_width()/2)*pad-0.05, (p.get_y()+p.get_height()/2)*pad),
            color=color,
            size=textsize
        )
def plot_distribution(dataframe,column,ax,bins_=50):
    temp= pd.DataFrame({
        "Retention":dataframe[dataframe["churn"]==0][column],
        "churn":dataframe[dataframe["churn"]==1][column]
    })
    temp[["Retention","churn"]].plot(kind='hist',stacked=True,bins=bins_,ax=ax)
    ax.set_xlabel(column)
    ax.ticklabel_format(style='plain',axis='x')

churn=client_df[['id','churn']]
churn.columns=['companies','churn']
churn_total=churn.groupby(churn['churn']).count()
churn_percentage=churn_total/churn_total.sum()*100
plot_stacked_bars(churn_percentage.transpose(),"churning status",(5,5),legend_=("lower right"))

consumption = client_df[['id', 'cons_12m', 'cons_gas_12m', 'cons_last_month', 'imp_cons', 'has_gas', 'churn']]

fig, axs = plt.subplots(nrows=1, figsize=(18, 5))

plot_distribution(consumption, 'cons_12m', axs)