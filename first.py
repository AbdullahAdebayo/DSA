import pandas as pd

data = pd.read_csv("sample1.csv")
# print(data.head(90))


by_name = data.sort_values(by=["Country" , "Name" , "IQ"])

new_list = by_name.drop(columns=['Education', 'Awards', 'Influence','Achievements','Notable Works'])

first_300 = new_list[by_name['Country'].isin(['USA','UK','Germany'])]
print(first_300.head(300))


Field_Of_Expertise = new_list[by_name['Field of Expertise'].isin(['Mathematics', 'Physics', 'Chemistry'])]
print(Field_Of_Expertise.head(300))

filtered_iq = new_list[by_name['IQ'] >= 170]
print(filtered_iq.head(500))

birth_year = new_list[by_name['Birth Year'].between(1900, 1940)]
print(birth_year.head(500))


male = [new_list['Gender'] == 'Male']
male1 = new_list[by_name['Gender'] == "Male"]
female = [new_list['Gender'] == 'Female']
female2 = [new_list[by_name['Gender'] == "Female"]]

print(male)
print(male1)
print(female)
print(female2)