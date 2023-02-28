import bs4, requests, smtplib

toAddress = ['email_address']

#to download page
getPage = requests.get('site name')
getPage.raise_for_status()

#Parse text for vacancy
listing = bs4.BeautifulSoup(getPage.text, 'html.parser')
vacancies = listing.select('.vacancyname')

the_one = 'internship'
flength = len(the_one)
available = False

for vacancy in vacancies:
    for i in range(len(vacancy.text)):
        job = vacancy.text[i:i+flength].lower()
        if job == the_one:
            available = True

if available == True:
  conn = smtplib.SMTP('smtp.gmail.com',587)
  conn.ehlo()
  conn.starttls()
  conn.login('email_address','appkey')
  conn.sendemail('emal_Address', toAddress, 'Subject: Vacancy alert')
  conn.quit()
  print('Sent notification emails for the following recipients: \n')
  for i in range(len(toAddress)):
        print(toAddress[i])
else:
    print('Your preferred vacancy is not available today.')
