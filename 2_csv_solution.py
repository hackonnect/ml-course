import pandas as pd
dataframe = pd.read_csv(r'student_performance.csv')
columns = [
    'gender',
    'A',
    'B',
    'C',
    'D',
    'E',
    'education',
    'lunch',
    'preparation',
    'score'
]
df = pd.DataFrame(0, index = list(range(1000)), columns = columns)

# Solution using a for loop starts here (use this one to help people that are stuck)

education_values = {
    'high school': 1,
    'some high school': 1,
    'associate\'s degree': 2,
    'some college': 3,
    'bachelor\'s degree': 3,
    'master\'s degree': 4
}
for i in range(1000):
    df['gender'][i] = int(dataframe['gender'][i] == 'female')
    df[dataframe['race/ethnicity'][i][-1]][i] = 1
    df['education'][i] = education_values[dataframe['parental level of education'][i]]
    df['lunch'][i] = int(dataframe['lunch'][i] == 'standard')
    df['preparation'][i] = int(dataframe['test preparation course'][i] == 'standard')
    df['score'][i] = dataframe['math score'][i] + dataframe['reading score'][i] + dataframe['writing score'][i]
df.to_csv('df.csv')

# Better solution (significantly faster) starts here
education_values = {
    'high school': 1,
    'some high school': 1,
    'associate\'s degree': 2,
    'some college': 3,
    'bachelor\'s degree': 3,
    'master\'s degree': 4
}
ethnicity_values = {
    'group A': 0,
    'group B': 1,
    'group C': 2,
    'group D': 3,
    'group E': 4
}
df['gender'] = dataframe['gender'].replace({'male': 0, 'female': 1})
ethnicity_columns = pd.get_dummies(dataframe['race/ethnicity'].replace(ethnicity_values))
for i in range(5):
    df['ABCDE'[i]] = ethnicity_columns[i]
df['education'] = dataframe['parental level of education'].replace(education_values)
df['lunch'] = dataframe['lunch'].replace({'free/reduced': 0, 'standard': 1})
df['preparation'] = dataframe['test preparation course'].replace({'none': 0, 'completed': 1})
df['score'] = dataframe['math score'] + dataframe['reading score'] + dataframe['writing score']
df.to_csv('df.csv')