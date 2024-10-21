"""validate using pandera following code
from typing import List, Dict, Any
import pandas as pd
import pandera as pa
from pandera import Column, DataFrameSchema, Check

# Define the student data
student_data = [
    {'roll no': 101, 'name': 'Alice', 'father': 'John Doe', 'course': 'BSc Computer Science', 'date of admission': '2021-09-01', 'fee': 5000},
    {'roll no': 102, 'name': 'Bob', 'father': 'Michael Smith', 'course': 'BSc Mathematics', 'date of admission': '2021-09-05', 'fee': 4500},
    {'roll no': 103, 'name': 'Charlie', 'father': 'Robert Brown', 'course': 'BA English', 'date of admission': '2021-09-08', 'fee': 4000},
    {'roll no': 104, 'name': 'David', 'father': 'James Wilson', 'course': 'BBA', 'date of admission': '2021-09-10', 'fee': 5500},
    {'roll no': 105, 'name': 'Eva', 'father': 'William Johnson', 'course': 'BCom', 'date of admission': '2021-09-12', 'fee': 4700},
    {'roll no': 106, 'name': 'Frank', 'father': 'George Clark', 'course': 'BSc Physics', 'date of admission': '2021-09-15', 'fee': 5100},
    {'roll no': 107, 'name': 'Grace', 'father': 'Henry Lewis', 'course': 'BSc Chemistry', 'date of admission': '2021-09-17', 'fee': 4800},
    {'roll no': 108, 'name': 'Hannah', 'father': 'Charles Harris', 'course': 'BBA', 'date of admission': '2021-09-20', 'fee': 5500},
    {'roll no': 109, 'name': 'Ivy', 'father': 'Joseph Martin', 'course': 'BSc Biology', 'date of admission': '2021-09-22', 'fee': 4900},
    {'roll no': 110, 'name': 'Jake', 'father': 'David Thomas', 'course': 'BA History', 'date of admission': '2021-09-25', 'fee': 4600}
]

# Create a DataFrame
student_df = pd.DataFrame(student_data)
student_df['date of admission'] = pd.to_datetime(student_df['date of admission'])

# Define a Pandera schema for validation
schema = pa.DataFrameSchema({
    "roll no": Column(int, [Check.ge(100), Check.le(999)], nullable=False),  # Roll no between 100 and 999
    "name": Column(str, nullable=False),  # Name must be a string
    "father": Column(str, nullable=False),  # Father's name must be a string
    "course": Column(str, Check.isin(["BSc Computer Science", "BSc Mathematics", "BA English", "BBA", "BCom", "BSc Physics", "BSc Chemistry", "BSc Biology", "BA History"]), nullable=False),  # Course must be one of the provided options
    "date of admission": Column(pa.DateTime, nullable=False),  # Valid date format
    "fee": Column(int, [Check.ge(4000), Check.le(6000)], nullable=False)  # Fee between 4000 and 6000
})

# Validate the DataFrame
validated_df = schema.validate(student_df)
print(validated_df)



"""

from typing import List, Dict, Any
import pandas as pd
import pandera as pa
from pandera import Column, DataFrameSchema, Check

# Define the student data

student_data = [
    {'roll no': 101, 'name': 'Alice', 'father': 'John Doe', 'course': 'BSc Computer Science', 'date of admission': '2021-09-01', 'fee': 5000},
    {'roll no': 102, 'name': 'Bob', 'father': 'Michael Smith', 'course': 'BSc Mathematics', 'date of admission': '2021-09-05', 'fee': 4500},
    {'roll no': 103, 'name': 'Charlie', 'father': 'Robert Brown', 'course': 'BA English', 'date of admission': '2021-09-08', 'fee': 4000},
    {'roll no': 104, 'name': 'David', 'father': 'James Wilson', 'course': 'BBA', 'date of admission': '2021-09-10', 'fee': 5500},
    {'roll no': 105, 'name': 'Eva', 'father': 'William' 'course': 'BCom', 'date of admission': '2021-09-12', 'fee': 4700},
    {'roll no': 106, 'name': 'Frank', 'father': 'George Clark', 'course': 'BSc Physics', 'date of admission': '2021-09-15', 'fee': 5100},
    {'roll no': 107, 'name': 'Grace', 'father': 'Henry Lewis', 'course': 'BSc Chemistry', 'date of ad '}

]



     
