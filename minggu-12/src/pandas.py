import pandas as pd
#creating a dictionary of series
d = {'Name':pd.Series(['Alfrick','Michael','Wendy','Paul','Dusan','George','Andreas',
   'Irene','Sagar','Simon','James','Rose']),
   'Years of Experience':pd.Series([5,9,1,4,3,4,7,9,6,8,3,1]),
   'Programming Language':pd.Series(['Python','JavaScript','PHP','C++','Java','Scala','React','Ruby','Angular','PHP','Python','JavaScript'])
    }

#Create a DataFrame
df = pd.DataFrame(d)
print(df)