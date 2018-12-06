from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse

INDEED_DEFAULT_URL = "https://ca.indeed.com/jobs?as_and="

parser = argparse.ArgumentParser()
parser.add_argument("--city", help="City Location",type=str, default="Victoria")
parser.add_argument("--province", help="Province (2-chars)",type=str, default="BC")
parser.add_argument("--job", help="Job title",type=str, default="Software Developer")
parser.add_argument("--radius", help="Radius from city",type=str, default="50")
parser.add_argument("--limit", help="Number of jobs",type=str, default="50")
parser.add_argument("--keywords", help="Keywords in job posting",type=str, default="python")
args = parser.parse_args()

city = args.city
province = args.province
limit = args.limit
radius = args.radius
job_title = args.job

job_search= "+".join(job_title.split(" "))
location = "{},+{}".format(city, province)

indeed_url = "{}{}&radius={}&l={}&limit={}".format(INDEED_DEFAULT_URL, job_search, radius, location, limit)

page = urlopen(indeed_url)
soup = BeautifulSoup(page,'html.parser')

all_postings = []
jobs = soup.find_all("h2", {"class": "jobtitle"})

for job in soup.find_all("h2", {"class": "jobtitle"}):
    job_posting = "https://www.indeed.ca{}".format(job.a["href"])
    all_postings.append(job_posting)

page = urlopen(all_postings[0])
soup = BeautifulSoup(page,'html.parser')

for post in all_postings:
    page = urlopen(post)
    soup = BeautifulSoup(page, 'html.parser')
    print ("Company: " + soup.find_all("h4")[0].text.strip())
    print ("Job Title " + soup.find_all("div", {"class":"icl-u-lg-mr--sm icl-u-xs-mr--xs"})[0].text.strip())
    try:
        print ("Rating: {}".format(round(float(soup.find("meta",{"itemprop":"ratingValue"})["content"]),2)))
    except:
        print ("No Rating")
    print ("Posting: {}".format(all_postings[0]))
    print ("")
