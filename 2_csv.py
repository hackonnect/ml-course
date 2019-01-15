# Pandas will help us import the CSV file
import pandas as pd

# Import the dataset from 'student_performance.csv'
dataframe = pd.read_csv(r'student_performance.csv')

# Let's print it to see the result we get
print(dataframe)

# Now we know what's inside the CSV file, we can actually retrieve individual columns
print(dataframe['gender'])

# Quick exercise: try to find the number of students that are female
# Solution:
print(sum([x == 'female' for x in dataframe['gender']]))
# Answer: 518

# At this point, go back to the whiteboard and plan out how we are changing the qualitative data into quantitative data
# Explain why 1s and 0s dont matter.
# Gender: Set female to 1 and male to 0.
# Ethnicity: Because ethnicity is not binary, we have to create 5 features and assign 1s or 0s.
# Parental Level of Education: There is progression involved, so some highschool can be set to 1, some highschool can be set to 1, associate's to 2, some college to 3, bachelor's to 3, master's to 4.
# Lunch: Set standard to 1 and reduced to 0.
# Test preparation course: Set completed to 1 and none to 0.
# Combine the three scores for now.

# Let's create a new Data Frame to store this
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

# Now we need to set each column one by one.

for index, gender in enumerate(dataframe['gender']):
    if gender == 'female':
        df['gender'][index] = 1
    else:
        df['gender'][index] = 0

# Let's check this:

print(df)

# Now attempt to do the other rows yourself!
# A sample solution is located in 2_csv_solution.py
# In order to save the result to a new csv file, you can simply do this:
# df.to_csv('<filename>')