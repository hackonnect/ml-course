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

# Solution starts here
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