# Automatic extraction of online homework results.

## ONLY NEED TO DO THIS ONCE.
Instructions:
1. Go to https://moseskonto.tu-berlin.de/moses/tutorium/
2. Click "Ergebnisse"
3. For all of your tutoriums, please click on them and download the respective csv file
4. Copy all students from your tutoriums into ONE csv file. Name it "students_list.csv".
5. The first line of this csv file has to be:
Name	Vorname	Matr.-Nr.	Studiengang	E-Mail	Ordnungsmerkmal	Tutorium	Tutor	Hausaufgabenkriterium
6. Save it in the same folder as this file, i.e., "main.py".
7. Close the csv file.
8. You now have a CSV file with the names and, more importantly, the email addresses of your students in it.


## THIS NEEDS TO BE DONE FOR EVERY NEW HOMEWORK ASSIGNMENT.
1. Next, download the Online Hausaufgaben results from isis. Again, as a csv file. Save the results as "ha.csv"
Put the file "ha.csv" in the same folder as this python repository.
2. Run this file. If you want to do it via commandline, navigate to this repo and execute the command python3 main.py
3. The console should now output the results of your students in a clean fashion. You no longer have to go through
the entire list manually.