from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('accuracy.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Race Number', 'Accuracy'])

#Change this n value according to how many tests you want for calculating average accuracy
n = 10

url = f"https://data.typeracer.com/pit/race_history?user=_cephas_&n={n}&startDate=&universe="
page = requests.get(url).text

soup = BeautifulSoup(page, 'lxml')

Table = soup.find('table', class_ = 'scoresTable')
Total_List = []
select = soup.find('select', attrs={'name': 'n'})

for values in Table.find_all('tr')[1:]:
    rows = values.find_all('td')

    Race_Number = rows[0].text.strip()
    Accuracy = rows[2].text.strip()
    Accuracy = Accuracy[:4]
    Acc = float(Accuracy)
    #print(Race_Number, Accuracy)
    Total_List.append(Acc)
    
    csv_writer.writerow([Race_Number, Acc])

sum = 0
for values in Total_List:
    sum += values

avg_accuracy = sum/n
last = "Average Accuracy"

print(f"Your Average accuracy for the past {n} tests is {avg_accuracy}")
csv_writer.writerow([last, avg_accuracy])

csv_file.close()





    
    
    

    
