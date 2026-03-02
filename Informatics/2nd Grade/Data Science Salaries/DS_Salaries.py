import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# from sklearn.model_selection import train_test_split
# from sklearn.decomposition import PCA

def read_dataset() :
    df=pd.read_csv("ds_salaries.csv")
    return df

    # EN - Entry Level
    # MI - Mid Level
    # SE - Senior Level
    # EX - Executive Level

    # CT - Contractor
    # FL - Freelancer
    # FT - Full-time
    # PT - Part-time

def overall_data_check(df) :
    print(df)
    print(100 * "=")
    # print(df.shape)
    # print(10 * "=")
    print(df.info())
    print(100 * "=")
    print(df.describe())
    print(100 * "=")
    print(df.nunique())
    print(100 * "=")
    # print(df.isnull().sum())
    # print(10 * "=")
    print(df.duplicated().any())
    # pd.set_option('display.max_rows', None)
    # print(df[df['job_title']=='Data Scientist'])
    # print(df.loc[df.duplicated()])
    df=df.drop_duplicates()
    df=df.drop(['salary', 'salary_currency'], axis=1)

    # The dataset consists of 3755 rows and 11 columns
    # The target variable is salary_in_usd
    # No missing values

def visualization(df) :
    #Fig 1
    fig, axes = plt.subplots(1, 2, figsize=(16, 5))
    sns.histplot(ax=axes[0], data=df, x='salary_in_usd', kde=True)
    axes[0].set_title("Distribution")
    sns.boxplot(ax=axes[1], data=df, y='salary_in_usd')
    axes[1].set_title("Quantiles")

    #Fig 2
    columns=['work_year', 'experience_level', 'employment_type']
    fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True)
    df2=df.groupby(columns[0])['salary_in_usd'].mean().round(0).reset_index()
    # print(df2)
    sns.lineplot(ax=axes[0], data=df2, x=columns[0], y='salary_in_usd', color='blue')
    axes[0].set_title(f"Average Salary by {columns[0]}", pad=10, fontsize=15)
    axes[0].set_xlabel(f"{columns[0]}", labelpad=20)
    axes[0].set_ylabel("Average Salary (USD)", labelpad=20)
    for i in range(1, len(columns)) :
        df2=df.groupby(columns[i])['salary_in_usd'].mean().round(0).reset_index()
        sns.barplot(ax=axes[i], data=df2, x=columns[i], y='salary_in_usd', color='gray')
        axes[i].set_title(f"Average Salary by {columns[i]}", pad=10, fontsize=15)
        axes[i].set_xlabel(f"{columns[i]}", labelpad=20)
        axes[i].set_ylabel("Average Salary (USD)", labelpad=20)

    #Fig 3
    columns=['job_title', 'company_location']
    fig, axes = plt.subplots(1, 2, figsize=(16, 5))
    for i in range(len(columns)) :
        df2=df.groupby(columns[i])['salary_in_usd'].mean().round(0).reset_index().sort_values(by='salary_in_usd', ascending=False).head(10)
        sns.barplot(ax=axes[i], data=df2, x='salary_in_usd', y=columns[i], color='gray')
        axes[i].set_title(f"Average Salary by {columns[i]}", pad=10, fontsize=15)
        axes[i].set_xlabel("Average Salary (USD)", labelpad=20)
        axes[i].set_ylabel(f"{columns[i]}", labelpad=20)

    #Fig 4
    fig=plt.figure()
    sns.countplot(data=df, x='job_title', order=df['job_title'].value_counts().iloc[:10].index)
    plt.xticks(rotation=45)
    plt.title("Top 10")

    #Fig 5
    fig=plt.figure()
    onsite=0
    remote=0
    hybrid=0
    for i in range(0, len(df['remote_ratio'])) :
        if df['remote_ratio'][i]==0 :
            onsite+=1
        elif df['remote_ratio'][i]==100 :
            remote+=1
        else :
            hybrid+=1
    # print(onsite+remote+hybrid)
    plt.pie([onsite, hybrid, remote], labels=["On-site", "Hybrid", "Remote"], autopct='%.2f')
    plt.title("Percentage of Remote Workers")

    plt.show()

def EDA() :
    df=read_dataset()
    overall_data_check(df)
    visualization(df)

# def prediction() :
#     X_full=read_dataset()
#     X_full=X_full.drop_duplicates()
#     # X_full.dropna(axis=0, subset=['salary_in_usd'], inplace=True)
#     y=X_full['salary_in_usd']
#     # X_full=X_full.drop(['salary_in_usd'], axis=1)
#     X_full.drop(['salary_in_usd'], axis=1, inplace=True)
#     X_train_full, X_valid_full, y_train, y_valid = train_test_split(X_full, y, train_size=0.8, test_size=0.2, random_state=0)
#     categorical_cols=[col for col in X_train_full.columns if X_train_full[col].nunique()<10 and X_train_full[col].dtype=='object']
#     numerical_cols=[col for col in X_train_full.columns if X_train_full[col].dtype in ['int64', 'float64']]
#     cols=categorical_cols+numerical_cols
#     X_train=X_train_full[cols].copy()
#     X_valid=X_valid_full[cols].copy()

EDA()
# prediction()