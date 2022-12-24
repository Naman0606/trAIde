# trAIde
Algorithmic trading is the use of computer programs to automatically make trades based on predetermined criteria. It allows traders to execute trades faster and more accurately than manual trading, and can be used in a variety of financial markets, including stocks, currencies, and commodities. It can be used to execute trades on behalf of a trader or to manage a portfolio of securities.
In this project we built a web application using Python, Flask, HTML, CSS and Bootstrap to perform Intraday trading. 
Applied statistical analysis to identify the top 5 companies to trade in for each day. The application makes use of a combination of the Simple Moving Average (SMA), the Relative Strength Index (RSI), and the Exponential Moving Average (EMA) combined with the Double Cross Moving Average (DCMA) to make trading decisions and execute trades.  Statistical analysis is used to identify patterns and trends in data, which can be helpful in identifying potential trading opportunities.
Based on the above mentioned technical indicators and the DCMA trading technique the algorithm executes trades by first flagging a crossover and then analysing if the trend is followed. And with the help of multithreading we were able to apply these techniques on 5 companies simultaneously thus diversifying the portfolio.
This technique resulted in a profit of about 15% compounded annually when used to trade in 5 minute interveled historic data of the selected companies.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
