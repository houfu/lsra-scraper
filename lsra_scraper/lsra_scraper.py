import dataclasses
import os

import click
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


@click.command()
@click.option('--site', '-s', help='Url to LSRA search page',
              default='https://eservices.mlaw.gov.sg/lsra/search-lawyer-or-law-firm')
@click.option('--output', '-o', help='Output format. Accepts either "csv" or "excel"',
              type=click.Choice(['csv', 'excel'], case_sensitive=False),
              default='csv')
@click.option('--out-file', '-O',
              help='Location of output file. If empty, default file name in root directory will be used',
              type=click.Path(), default=None)
@click.option('--root', '-r', help='Root directory for downloading of output files. Ignored if out-file is set.',
              type=click.Path(file_okay=False), default=os.getcwd())
@click.argument('search_type', default='firms')
def lsra_scraper(site, search_type, root, output, out_file):
    if root:
        os.chdir(root)
    if search_type.lower() == 'lawyers':
        print("Lawyers scraping is not supported at this moment.")
        return
    driver = setup_web_driver()
    result = scrape(driver, site, search_type)
    if output == 'csv':
        output_path = save_csv(result, out_file, root, search_type)
        print('CSV file saved at {}'.format(output_path))
        return


def setup_web_driver():
    print('Setting up web driver')
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(150)
    return driver


def get_site(site, search_type='firm'):
    if search_type.lower() == 'lawyers':
        payload = {'searchType': 1}
    else:
        payload = {'searchType': 0}
    r = requests.get(site, params=payload)
    return r.url


def scrape(driver, site, search_type):
    try:
        print("Begin scraping process.")
        driver.get(get_site(site, search_type))
        pass_captcha(driver)
        result = process_pages(driver, search_type=search_type)
    finally:
        print("End scraping process.")
        driver.quit()
    return result


def pass_captcha(driver: webdriver.Chrome):
    from selenium.webdriver.common.keys import Keys
    passed_captcha = False
    captcha = driver.find_element_by_id('txtCaptchCode')
    captcha.send_keys(Keys.END)
    print('In order to continue, you need to enter the captcha code on the web page.')
    code = input('Input the code in your screen now:')
    captcha.send_keys(code)
    driver.find_element_by_id('btnSearch').click()
    while not passed_captcha:
        element = driver.find_element_by_id('showValidationError')
        if element.is_displayed():
            code = input('Validation failed. Please re-enter')
            driver.find_element_by_id('txtCaptchCode').send_keys(code)
            driver.find_element_by_id('btnSearch').click()
            break
        else:
            print('Captcha passed')
            passed_captcha = True
            driver.minimize_window()


def process_pages(driver: webdriver.Chrome, search_type='firm') -> list:
    result = []
    end_of_query = False
    while not end_of_query:
        table_element = driver.find_element_by_id('Tbl_Search').get_attribute('outerHTML')
        if search_type.lower() == 'lawyers':
            parse_lawyers_table(table_element, result)
        else:
            parse_firms_table(table_element, result)
        paging_footer = driver.find_element_by_id('pagingFooter')
        next_page = paging_footer.find_element_by_id('next')
        if 'disabledLink' in next_page.get_attribute('class'):
            end_of_query = True
        else:
            driver.execute_script("arguments[0].click();", next_page)
    return result


def parse_lawyers_table(table, result):
    # TODO: A lawyer's table if there is demand.
    print("Lawyers scraping is not supported.")


def parse_firms_table(table, result):
    soup = BeautifulSoup(table, features="html5lib")
    main_table = soup.body.table.tbody
    rows = [item for item in main_table.children]
    for row in rows:
        item = Firm()
        body = row.table.tbody
        descendants = [item for item in body.descendants]
        item.name_of_law_practice = descendants[7].get_text()
        item.type_of_law_practice = descendants[13].get_text()
        item.key_practice_areas = parse_key_practice_areas(descendants[21].get_text())
        item.size_of_law_practice = descendants[28].get_text()
        item.telephone_no = descendants[34].get_text()
        item.website = descendants[41].get_text()
        item.email = descendants[47].get_text()
        item.address = descendants[54].get_text().replace('\n\n', " ")
        result.append(item)


def parse_key_practice_areas(text):
    if text == 'N.A.':
        return []
    else:
        return text.split(', ')


def save_csv(results, outfile, root, search_type):
    import csv
    import dataclasses
    fields = ['name_of_law_practice', 'type_of_law_practice', 'key_practice_areas', 'size_of_law_practice',
              'telephone_no', 'website', 'email', 'address']
    if not outfile:
        outfile = get_save_file_path(root, search_type, 'csv')
    with open(outfile, 'w', newline='', encoding='utf-8') as outf:
        writer = csv.DictWriter(outf, fieldnames=fields)
        writer.writeheader()
        results_dict = [dataclasses.asdict(result) for result in results]
        writer.writerows(results_dict)
    return outfile


def get_save_file_path(root, search_type, ext):
    import datetime
    return os.path.join(root, "{} {}.{}".format(search_type, datetime.date.today(), ext))


@dataclasses.dataclass
class Firm:
    name_of_law_practice: str = ''
    type_of_law_practice: str = ''
    key_practice_areas: list = dataclasses.field(default_factory=list)
    size_of_law_practice: str = ''
    telephone_no: str = ''
    website: str = ''
    email: str = ''
    address: str = ''


@dataclasses.dataclass
class Lawyer:
    name: str
    registration_type: str = ''
    job_title: str = ''
    date_of_admission: str = ''
    key_practice_areas: list = dataclasses.field(default_factory=list)
    name_of_law_practice: str = ''
    telephone_no: str = ''
    website: str = ''
    email: str = ''
    address: str = ''


if __name__ == '__main__':
    lsra_scraper()
