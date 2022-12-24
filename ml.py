import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def main():
    l = []
    companies = ['COALINDIA', 'RELIANCE', 'ICICIBANK', 'TITAN', 'ITC', 'WIPRO', 'TCS', 'TATAMOTORS', 'HDFCLIFE', 'INFY']
    for i in range(len(companies)):
        df = yf.download(tickers=companies[i]+'.NS', period='3mo', interval='1d')
        df.to_csv('datasets\\'+companies[i]+'.csv')
        if i == 0:
            df = df.reset_index()
            l.append(df.index)
            l.append(df['Date'])
        l.append(df['Close'])

    #PIVOT DATASET
    df_pivot=pd.DataFrame(l).T
    df_pivot.columns=['Symbol','Date'] + companies
    df_pivot=df_pivot.reset_index(drop=True)
    df_pivot= df_pivot[companies].astype('float64')

    #CORR DATASET
    corr_df = df_pivot.corr(method='pearson')
    corr_df.head(10)

    #CALC RISK
    risk = corr_df.dropna()
    # plt.figure(figsize=(8,5))
    # plt.scatter(risk.mean(),risk.std(),s=25)

    # plt.xlabel('Expected Return')
    # plt.ylabel('Risk')


    #For adding annotatios in the scatterplot
    # for label,x,y in zip(risk.columns,risk.mean(),risk.std()):
    #     plt.annotate(label,xy=(x,y),xytext=(-120,20),textcoords = 'offset points', ha = 'right', va = 'bottom',arrowprops = dict(arrowstyle='->',connectionstyle = 'arc3,rad=-0.5'))
    
    # plt.show()

    #Printing the top 5
    z=pd.DataFrame(columns = ['ticker', 'return', 'risk'])
    for label,x,y in zip(risk.columns,risk.mean(),risk.std()):
        z.loc[len(z)] = [label, x, y]

    z = z.sort_values(by = ['return', 'risk'], ascending = [False, True])
    companies = list(z['ticker'].head(5))
    print(companies)
    split = []
    for i in range(5):
        split.append(z['return'][i] * (1 - z['risk'][i]))
    total = sum(split)
    for i in range(len(split)):
        split[i] = split[i]/total
    return companies, split