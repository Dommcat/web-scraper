import requests
from bs4 import BeautifulSoup



url_variable = "https://en.wikipedia.org/wiki/Martial_arts"


def get_citations_needed_count(url_variable):
    """
    Takes in wiki page and returns the number of needed citations
    """
    req = requests.get(url_variable)

    # print(req.content)
    markup = req.content
    soup = BeautifulSoup(markup, 'html.parser')
    citation_tags = soup.find_all('sup', {'class': "noprint Inline-Template Template-Fact"})
    # print(citation_tags,len(citation_tags))
    return len(citation_tags)


def get_citations_needed_report(url: str) -> str:
    req = requests.get(url_variable)
    markup = req.text
    soup = BeautifulSoup(markup, 'html.parser')

    citation_tags = soup.find_all('sup', {'class': 'noprint Inline-Template Template-Fact'})
    report = ""
       # Source TH: extract relevant passage and format the report string
    for tag in citation_tags:
        # Extract parent element and its contents
        parent_tag = tag.find_parent()
        passage = parent_tag.get_text().strip()
        report += f'Citation needed for: {passage} [citation needed]\n\n'
    print(report)
    return report
    
with open("citations.txt","w")as outfile :
    outfile.write(get_citations_needed_report(url_variable))
    outfile.write(str(get_citations_needed_count(url_variable)))
get_citations_needed_report(url_variable)
    
# if __name__ == "__main__":
#     url = input("https://en.wikipedia.org/wiki/Martial_arts")
#     print(get_citations_needed_count(url))
#     print(get_citations_needed_report(url))
   