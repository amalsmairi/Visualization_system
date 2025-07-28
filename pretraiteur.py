import pandas as pd

def load_excel(uploaded_file):
    return pd.read_excel(uploaded_file)

def sort_months(df, month_col):
    df['Month_dt'] = pd.to_datetime(df[month_col], format='%b %Y')
    df = df.sort_values('Month_dt').drop(columns='Month_dt')
    return df

def compute_mttr(df):
    df['Created At'] = pd.to_datetime(df['Created At'], errors='coerce')
    df['complete_time'] = pd.to_datetime(df['complete_time'], errors='coerce')
    df = df.dropna(subset=['Created At', 'complete_time'])

    df['Resolution Time (hours)'] = (df['complete_time'] - df['Created At']).dt.total_seconds() / 3600
    df['Month'] = df['complete_time'].dt.strftime('%b %Y')

    mttr = df.groupby('Month')['Resolution Time (hours)'].mean().reset_index()
    mttr.rename(columns={'Resolution Time (hours)': 'MTTR (h)'}, inplace=True)

    return sort_months(mttr, 'Month')

def compute_mtta(df):
    df['Created At'] = pd.to_datetime(df['Created At'], errors='coerce')
    df['Updated At'] = pd.to_datetime(df['Updated At'], errors='coerce')
    df = df.dropna(subset=['Created At', 'Updated At'])

    df['Acknowledge Time (hours)'] = (df['Updated At'] - df['Created At']).dt.total_seconds() / 3600
    df['Month'] = df['Updated At'].dt.strftime('%b %Y')

    mtta = df.groupby('Month')['Acknowledge Time (hours)'].mean().reset_index()
    mtta.rename(columns={'Acknowledge Time (hours)': 'MTTA (h)'}, inplace=True)

    return sort_months(mtta, 'Month')

def compute_mttc(df):
    df = df[df['Current Phase'].str.lower() == 'close']
    df = df.dropna(subset=['Created At', 'complete_time'])

    df['Created At'] = pd.to_datetime(df['Created At'], errors='coerce')
    df['complete_time'] = pd.to_datetime(df['complete_time'], errors='coerce')

    df['Closure Time (hours)'] = (df['complete_time'] - df['Created At']).dt.total_seconds() / 3600
    df['Month'] = df['complete_time'].dt.strftime('%b %Y')

    mttc = df.groupby('Month')['Closure Time (hours)'].mean().reset_index()
    mttc.rename(columns={'Closure Time (hours)': 'MTTC (h)'}, inplace=True)

    return sort_months(mttc, 'Month')
