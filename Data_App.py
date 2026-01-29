import pandas as pd

df = pd.read_csv("Studenta_data.csv")

print("****************************************************************************************")
print("Original data set")
print("****************************************************************************************")
print(df)
# df.isnull()
# df.info()
# df.describe()

#Create a new colum by adding two column

df["Total_Marks"] = df["python"] + df["math"]
print("****************************************************************************************")
print("Data set after adding new column")
print("****************************************************************************************")
print(df)



#Print 3 row new file

new_3_row_file = df.head(3).to_csv("new_3_row_file.csv")
df3 = pd.read_csv("new_3_row_file.csv")
print("****************************************************************************************")
print("Getting three rows only")
print("****************************************************************************************")
print(df3)



# print(df.head())
# print(df.tail())
# print(df.sample())


#To Filter a data set, her filtering student who score greater than 90

y = df.loc[df["python"] > 90, ["Student_Name", "python"]]
print("****************************************************************************************")
print("Selecting students who scored over 90")
print("****************************************************************************************")
print(y)



#selecting multiple rows and column, here I am getting name of the student and total marks

z = df.iloc[0:3, [0, -1]]
print("****************************************************************************************")
print("Name of the student and total marks")
print("****************************************************************************************")
print(z)

