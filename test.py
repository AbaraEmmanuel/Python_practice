import pandas as pd

# Sample DataFrame
data = {"C1": [1, 2, 3], "C2": ["A", "B", "C"]}
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Edit a particular row (for example, row with index 1)
df.loc[1, "C1"] = 99
df.loc[1, "C2"] = "UpdatedValue"

# Display the modified DataFrame
print("\nModified DataFrame:")
print(df)