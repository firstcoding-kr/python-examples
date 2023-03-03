import csv

# CSV 파일 쓰기 (딕셔너리 형식)
with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'Gender']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'John', 'Age': '25', 'Gender': 'Male'})
    writer.writerow({'Name': 'Jane', 'Age': '30', 'Gender': 'Female'})
    writer.writerow({'Name': 'Bob', 'Age': '40', 'Gender': 'Male'})
