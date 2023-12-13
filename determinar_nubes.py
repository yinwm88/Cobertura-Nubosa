def determinar_nube(df):
    COLOR_NUBE = 0.95
    df_nube = df.loc[df['razon'] > COLOR_NUBE]
    return df_nube


