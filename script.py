# Imports
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define function to retrieve data
def getdata(url):
    r = requests.get(url)
    return r.text

# Get HTML code using parse
def html_code(url):
    # pass the url
    # into getdata function
    htmlData = getdata(url)
    soup = BeautifulSoup(htmlData, 'html.parser')

    # Return html code
    return soup

# Filter job detail using find_all function
def job_detail(soup):
    # find the HTML tag with find()
    # convert to string
    data = soup.find_all('div', class_='column is-half')
    result = []

    for item in data:
        url = item.find('a', class_='card-footer-item', href=True)['href'].strip()
        result.append(url)
    return result

# Filter job title using find_all function
def title(soup):
    #find the html tag with find()
    # convert to string
    data = soup.find_all('div', class_='column is-half')
    result = []

    for item in data:
        title = item.find('h2', class_='title is-5').text.strip().title()
        result.append(title)
    return result

    # result = data.split('\n')

    # res=[]
    # for i in range(1, len(result)):
    #     if len(result[i]) > 1:
    #         res.append(result[i])
    # return(res)

# Filter company name using find_all function
def company_name(soup):
    #find the html tag with find()
    # convert to string
    data = soup.find_all('div', class_="column is-half")
    result = []

    for item in data:
        name = item.find('h3', class_='subtitle is-6 company').text.strip().title()
        result.append(name)
    return result

    # res=[]
    # for i in range(1, len(result)):
    #     if len(result[i]) > 1:
    #         res.append(result[i])
    # return(res)

# Filter company location using find_all function
def company_location(soup):
    #find the html tag with find()
    # convert to string
    data = soup.find_all('div', class_="column is-half")
    result = []

    for item in data:
        location = item.find('p', class_='location').text.strip().title()
        result.append(location)
    return result







# for data in soup.find_all():
#     company = soup.find('h3', class_='subtitle is-6 company')
#     location = soup.find('p', class_='location')
#     job_detail = soup.find()
#     print(data.get_text())

def main():

    # Data for URL
    url = 'https://realpython.github.io/fake-jobs/'
    
    # Pass URL into soup, which returns HTML string
    soup = html_code(url)

    # call job_detail and title
    job_det = job_detail(soup)
    job_title = title(soup)

    # Call company_name and company_location
    name = company_name(soup)
    location = company_location(soup)

    # Empty dataframe to store scraped data 
    job_data = []    

    # Traverse both data
    # temp = 0
    # for i in range(1, len(job_det)):
    #     j = temp
    #     for i in (range(temp, 2+temp)):
    #         print('Job Details and Job Title : ' + job_title[j])

    #         temp = j
    #         print('Job : ' + job_det[i])
    #         print('------------------------------------------------')

    #         print('Company Name : ' + name[i])
    #         print('Company Location : ' + location[i])

    for t, n, l, u in zip(job_title, name, location, job_det) :
        job_data.append({
            'Job Title': job_title,
            'Company': name,
            'Location': location,
            'URL': job_det
        })

    df = pd.DataFrame(job_data)
    print(df)
    df.to_csv('data.csv')

if __name__ == '__main__':
    main()