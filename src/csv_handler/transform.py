from src.csv_handler.load import read_csvs

def transform_df(config):
    compare_cols = config['compare_columns']
    df_target, df_source = read_csvs(config)
    cols_in_both = [col for col in compare_cols if col in df_source.columns and col in df_target.columns]
    df_source = df_source[cols_in_both]
    df_target = df_target[cols_in_both]

    print(df_source, df_target)
