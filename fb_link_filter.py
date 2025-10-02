import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# import profile_scrper as page_scrper
import page_scrper
import re

def extract_links(html_file_path, base_url=None, class_names=None):
    # Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all elements with the specified class names
    elements = []
    if class_names:
        for class_name in class_names:
            elements.extend(soup.find_all(class_=class_name))
    else:
        elements = soup.find_all()

    # Extract href attributes and remove duplicates
    unique_links = set()
    for element in elements:
        # links = element.find_all('a')
        # print(len(elements))
        # print(element.get('href'))
        
        href = element.get('href')
        pattern = r"https?://(www\.)?facebook\.com/[A-Za-z0-9_.-]+/?" 
        # print(f'totlal links found {len(href)} ')
        try:
            if re.match(pattern, href):
                    # If a base_url is provided, join it with relative URLs
                if base_url:
                    href = urljoin(base_url, href)
                unique_links.add(href)
        except Exception as e:
            print(f"Error extracting links: {str(e)}")
        
    return list(unique_links)
i = 0
# Example usage
if __name__ == "__main__":
    html_file_path = os.path.join("./facebook_ads_content.html")
    base_url = 'https://www.facebook.com'  # Updated to include https://www.
    class_names = ['xt0psk2']  # Add the class names you want to search for
    
    unique_links = extract_links(html_file_path, base_url, class_names)
    
    # print(f"Found {len(unique_links)} unique links:")
    # for link in unique_links:
    #     print(link)
    m = len(unique_links)
    # Optionally, save the links to a file
    # with open('extracted_links.txt', 'w') as f:
    for link in unique_links:
        # f.write(f"{link}\n")
        i += 1

        try:
            # page_scroller.main(link)
            print(i)

            # profile_path =os.path.join('profile.html')
            page_scrper.main(link)
            print(m-i)
        except Exception as e:
            print(f"Error scraping {link}: {str(e)}")
    print("Links have been saved to 'extracted_links.txt'")
