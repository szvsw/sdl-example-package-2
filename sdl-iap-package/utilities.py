def add_column_to_gdf(gdf, column_name, initial_value):
	if column_name in gdf.columns:
		raise ValueError(f"The column name '{column_name}' cannot be used because the GDF already has a column with that name")
	gdf[column_name] = initial_value