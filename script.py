import sys

from tabulate import tabulate

def load_csv_data(filename, delimiter=','):
  lines = []
  fileName = filename
  try:
    with open(fileName) as file:
      for line in file: 
        line = line.strip()
        if line:
          lines.append(line.split(delimiter))
  except FileNotFoundError:
    sys.exit("File doesn't exist")
  return lines

def sort_data(data, column):
  if column >= len(data[0]):
    print("Invalid column index for sorting")
    return data
  else:
    return [data[0]] + sorted(data[1:], key=lambda x: x[column])

def filter_data(data, column, value):
  if column >= len(data[0]): 
    print("Invalid column index for filtering")
    return data 

  filtered = []
  for row in data[1:]:
    print(row[column])
    if row[column].strip() == value:
      filtered.append(row)
  return [data[0]] + filtered

  
if __name__ == "__main__":
  if len(sys.argv) != 2:
    sys.exit("Usage: python script.py filename.csv")
    
  filename = sys.argv[1]

  if not filename.endswith(".csv"):
    print("File is not a csv file")
    sys.exit()

  delimiter = input("Enter the delimiter (default is comma): ")
  if not delimiter:
    delimiter = ','
  
  lines = load_csv_data(filename, delimiter)

  headings = lines[0]

  print(tabulate(lines, headers="firstrow", tablefmt="grid"))

  while True:
    choice = int(input("\nDo you want to:\n"
                   "1. Sort data\n"
                   "2. Filter data\n"
                   "3. Exit\n"
                   "Enter your choice: "))
    
    if choice == 1:
      column = int(input("Enter the column index to sort by: "))    
      lines = sort_data(lines, column)
      print(tabulate(lines, headers="firstrow", tablefmt="grid"))

    elif choice == 2:
      column = int(input("Enter the column index to filter by: "))
      value = input("Enter the value to filter for: ")
      line = filter_data(lines, column, value)
      print(tabulate(line, headers="firstrow", tablefmt="grid"))
      
    elif choice == 3:
        sys.exit()
   
    else:
      print("Invalid choice. Please choose again.")
