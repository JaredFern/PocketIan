import csv
import requests
import BeautifulSoup
import xml.etree.ElementTree as ET


def main():
    target_url = 'http://www.mccormick.northwestern.edu/eecs/courses/index.html'

    html_text = get_html_text(target_url)

    with open("site.txt", "w") as o:
        o.write(str(html_text))

    with open('courses.csv', "w") as f:
        root = ET.fromstring(html_text)

        ns = {"x": "http://www.w3.org/1999/xhtml"}

        fields = [n.text for n in root.findall(
            ".//x:table[@id='course_list']/*[1]//x:th", namespaces=ns)]

        # only use lineterminator if having problems with extra lines
        w = csv.writer(f, lineterminator='\n')
        w.writerow(fields)

        # XPath = XML path language
        # axis node_test predicate
        # FROM axis SELECt node_test WHERE predicate
        query_string = ".//x:table[@id='course_list']/x:tbody//x:tr"
        for row in root.findall(query_string, namespaces=ns):
            row_text = [" ".join(n.itertext())
                        for n in row.findall(".//x:td", namespaces=ns)]
            # print(row_text)
            w.writerow(row_text)

    with open('courses_2.csv', 'w') as f:
        soup = BeautifulSoup(html_text, "html.parser")

        fields = [f.string for f in soup.find(
            'table', id="course_list").find('thead').find_all('th')]

        # only use lineterminator if having problems with extra lines
        w = csv.writer(f, lineterminator='\n')
        w.writerow(fields)

        for row in soup.find('table', id='course_list').tbody.find_all('tr'):
            row_text = [" ".join(col.stripped_strings) for col in row('td')]
            w.writerow(row_text)


def get_html_text(site_url):
    r = requests.get(site_url)
    return r.text.encode(r.encoding)

if __name__ == '__main__':
    main()
