import json
import pandas as pd

df = pd.read_json('research/Spacebudz_Assets.JSON')
# The file path needs to be called from the main folder even though the file is in the same folder 
print(df)

# df = pd.read_json('research/Spacebudz_Assets.JSON')
# df_new = pd.DataFrame(df.features.values.tolist())['Array_Call']