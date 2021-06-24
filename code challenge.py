# At ABC Company, each year every employee is given a percentage based increment to their salaries based on the departments they belong to. You have to write a script(s) using a scripting language (for example Python) to read from flat_data.csv and store into employees and department DB tables in the schema below. Furthermore you need to read tables from the database, calculate the updated salaries and write them back. Please note that you will need to create these tables using script or DDL and provide your code.

# The database contains the following schemas:

# employee: id :: UUID, first_name::Text, last_name::Text, salary::numeric, department_id::UUID
# department: id::UUID, name::Text, salary_increment::numeric
# The salary_increment column in department contains the percentage value for calculating the salary. The output of the process should be the following table

# updated_salaries: employee_id, updated_salary
# All the tables must be created by script and have the necessary key relationships between them.

# Completion
# When you are finished (or out of time) you will push up the application to a git repo. Then please notify Rais Mohammad via email (rais@pumpjackdataworks.com) with the subject Pumpjack Data Analyst Code Challenge and the link to the github repo.


import pandas as pd

data = pd.read_csv(
    'flat_data.csv', 
    header=None,
    skiprows=1
    )
df = pd.DataFrame(data[0].str.split(',').tolist())
df[2] = pd.to_numeric(df[2])
df[4] = pd.to_numeric(df[4])
df["updated_salaries"]= df[2] + df[4]
df["updated_salaries"] = ((df[2] * (df[4] / 100)) + df[2] ).astype(int)
df.rename(index=str, columns={0: "first_name", 1:"last_name", 2:"salary", 3:"dept_name",4:"salary_increment"})
