


import pandas as pd

schools = pd.read_csv("schools.csv")

first_case = schools[["school_name" , "borough"]].sort_values("school_name" , ascending= True).sort_index()
print(first_case.head(10))

second_case = schools[["school_name" , "percent_tested" , "borough"]].sort_values("percent_tested").sort_index()
print(second_case.head(10))


to_merge = first_case.merge(second_case , on = "borough")
to_merge1 = second_case.merge(first_case , on = "school_name")

print("The first merge case: " , to_merge.head(50) ,
       "\nThe second merge case: " , to_merge1.head(50))


