import pandas as pd

data = {
    'Name': ['John', 'Mary', 'Robert', 'Emily'],
    'Age': [30, 28, 35, 27],
    'Address': ['New York', 'Los Angeles', 'Chicago', 'San Francisco'],
    'Qualification': ['BSc', 'BA', 'PhD', 'MSc']
}

df = pd.DataFrame(data)

print(df['Address'])
print(df['Address'][0])
