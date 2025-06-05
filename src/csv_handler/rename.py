def rename_columns(df_source, config):
    column_map = config['columns_mapping']

    df_source.rename(columns=column_map['source_to_target'], inplace=True)

    return df_source
