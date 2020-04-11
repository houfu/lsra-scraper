import pytest
from selenium.common.exceptions import NoSuchElementException

from lsra_scraper import lsra_scraper
from lsra_scraper.lsra_scraper import Firm
from click.testing import CliRunner


def test_setup_web_driver():
    driver = None
    try:
        driver = lsra_scraper.setup_web_driver()
        assert driver
    finally:
        if driver:
            driver.close()


def test_web_site(selenium, site_path):
    selenium.get(site_path)


def test_parse_key_practice_areas():
    assert lsra_scraper.parse_key_practice_areas('N.A.') == []
    assert lsra_scraper.parse_key_practice_areas(
        'ACCIDENT AND PERSONAL INJURY CLAIMS, ADMIRALTY AND SHIPPING LAW, '
        'BANKRUPTCY AND INSOLVENCY LAW, CIVIL AND COMMERCIAL LITIGATION, '
        'CONVEYANCING AND PROPERTY LAW, CORPORATE AND COMMERCIAL LAW, '
        'CRIMINAL LAW, EMPLOYMENT LAW, FAMILY LAW, INSURANCE LAW, '
        'ISLAMIC LAW, LANDLORD AND TENANT LAW, WILLS, '
        'PROBATE AND ADMINISTRATION OF ESTATE, WORKERS’ COMPENSATION CLAIMS') == [
               'ACCIDENT AND PERSONAL INJURY CLAIMS',
               'ADMIRALTY AND SHIPPING LAW',
               'BANKRUPTCY AND INSOLVENCY LAW',
               'CIVIL AND COMMERCIAL LITIGATION',
               'CONVEYANCING AND PROPERTY LAW',
               'CORPORATE AND COMMERCIAL LAW',
               'CRIMINAL LAW', 'EMPLOYMENT LAW', 'FAMILY LAW', 'INSURANCE LAW',
               'ISLAMIC LAW', 'LANDLORD AND TENANT LAW', 'WILLS',
               'PROBATE AND ADMINISTRATION OF ESTATE',
               'WORKERS’ COMPENSATION CLAIMS'
           ]


def test_parse_firms_table():
    test_table = open('tests/firms_table2.html', 'r')
    result = []
    lsra_scraper.parse_firms_table(test_table.read(), result=result)
    assert result == [
        Firm(name_of_law_practice='ABDULLAH SHAIK ABUBAKAR', type_of_law_practice='SINGAPORE LAW PRACTICE',
             key_practice_areas=[], size_of_law_practice='SMALL (1 TO 5 LAWYERS)', telephone_no='90355501',
             website='N.A.', email='abd_bakar@singnet.com.sg',
             address='7 EVERGREEN GARDENS EVERGREEN GARDEN SINGAPORE 468883'),
        Firm(name_of_law_practice='ABRAHAM LOGAN & PARTNERS', type_of_law_practice='SINGAPORE LAW PRACTICE',
             key_practice_areas=[], size_of_law_practice='SMALL (1 TO 5 LAWYERS)', telephone_no='65362119',
             website='http://www.abrahamlogan.com.sg', email='alp@abrahamlogan.com.sg',
             address="101A UPPER CROSS STREET PEOPLE'S PARK CENTRE # 09-07 SINGAPORE 058357"),
        Firm(name_of_law_practice='ABRAHAM TEO & CO', type_of_law_practice='SINGAPORE LAW PRACTICE',
             key_practice_areas=['ACCIDENT AND PERSONAL INJURY CLAIMS', 'BUILDING AND CONSTRUCTION LAW',
                                 'CIVIL AND COMMERCIAL LITIGATION', 'COMPETITION LAW', 'CRIMINAL LAW', 'EMPLOYMENT LAW',
                                 'FAMILY LAW', 'LANDLORD AND TENANT LAW', 'WILLS',
                                 'PROBATE AND ADMINISTRATION OF ESTATE'], size_of_law_practice='SMALL (1 TO 5 LAWYERS)',
             telephone_no='64352933', website='N.A.', email='abrahamteo@singnet.com.sg',
             address="1 PARK ROAD PEOPLE'S PARK COMPLEX # 04-47 SINGAPORE 059108"),
        Firm(name_of_law_practice='ABRAHAMLOW LLC', type_of_law_practice='SINGAPORE LAW PRACTICE',
             key_practice_areas=[], size_of_law_practice='MEDIUM (6 TO 30 LAWYERS)', telephone_no='65356688',
             website='N.A.', email='inquiries@abrahamlow.com.sg',
             address='24 RAFFLES PLACE CLIFFORD CENTRE # 07-02 SINGAPORE 048621'),
        Firm(name_of_law_practice='ACACIA LEGAL LLC', type_of_law_practice='SINGAPORE LAW PRACTICE',
             key_practice_areas=['ACCIDENT AND PERSONAL INJURY CLAIMS', 'ADMINISTRATIVE AND CONSTITUTIONAL LAW',
                                 'ARBITRATION', 'BANKING', 'FINANCE AND SECURITIES LAW',
                                 'BANKRUPTCY AND INSOLVENCY LAW', 'CIVIL AND COMMERCIAL LITIGATION',
                                 'CONVEYANCING AND PROPERTY LAW', 'CORPORATE AND COMMERCIAL LAW', 'CRIMINAL LAW',
                                 'EMPLOYMENT LAW', 'FAMILY LAW', 'IMMIGRATION LAW', 'INSURANCE LAW',
                                 'INTELLECTUAL PROPERTY LAW', 'LANDLORD AND TENANT LAW', 'MEDIA',
                                 'INTERNET AND INFORMATION TECHNOLOGY LAW', 'MEDIATION', 'TRUST LAW', 'WILLS',
                                 'PROBATE AND ADMINISTRATION OF ESTATE', 'WORKERSâ€™ COMPENSATION CLAIMS'],
             size_of_law_practice='SMALL (1 TO 5 LAWYERS)', telephone_no='6683 9908',
             website='http://www.acacialegal.sg', email='contact@acacialegal.sg',
             address='CARPENTER STREET CARPENTER HAUS # 36 SINGAPORE 059915'),
        Firm(name_of_law_practice='ACCLAIM LAW LLC', type_of_law_practice='SINGAPORE LAW PRACTICE',
             key_practice_areas=['BANKRUPTCY AND INSOLVENCY LAW', 'CIVIL AND COMMERCIAL LITIGATION',
                                 'CONVEYANCING AND PROPERTY LAW', 'FAMILY LAW'],
             size_of_law_practice='SMALL (1 TO 5 LAWYERS)', telephone_no='62500884', website='N.A.',
             email='office@acclaimlaw.com.sg', address='331 NORTH BRIDGE ROAD ODEON TOWERS # 03-01 SINGAPORE 188720'),
        Firm(name_of_law_practice='ACHIEVERS LLC', type_of_law_practice='SINGAPORE LAW PRACTICE', key_practice_areas=[],
             size_of_law_practice='SMALL (1 TO 5 LAWYERS)', telephone_no='63924280', website='N.A.',
             email='ibrahimyakub@singnet.com', address='390 VICTORIA STREET GOLDEN LANDMARK # 02-38 SINGAPORE 188061'),
        Firm(name_of_law_practice='ACIES LAW CORPORATION', type_of_law_practice='SINGAPORE LAW PRACTICE',
             key_practice_areas=['ARBITRATION', 'BANKING', 'FINANCE AND SECURITIES LAW',
                                 'BANKRUPTCY AND INSOLVENCY LAW', 'BUILDING AND CONSTRUCTION LAW',
                                 'CIVIL AND COMMERCIAL LITIGATION', 'CORPORATE AND COMMERCIAL LAW', 'CRIMINAL LAW',
                                 'EMPLOYMENT LAW', 'FAMILY LAW', 'LANDLORD AND TENANT LAW', 'MEDIATION'],
             size_of_law_practice='SMALL (1 TO 5 LAWYERS)', telephone_no='65384538', website='http://www.acieslaw.com',
             email='sctan@acieslaw.com', address='78 SHENTON WAY # 31-02 SINGAPORE 079120'),
        Firm(name_of_law_practice='ACTON LAW LLC', type_of_law_practice='SINGAPORE LAW PRACTICE',
             key_practice_areas=['ARBITRATION', 'BANKING', 'FINANCE AND SECURITIES LAW',
                                 'BANKRUPTCY AND INSOLVENCY LAW', 'CIVIL AND COMMERCIAL LITIGATION',
                                 'CORPORATE AND COMMERCIAL LAW', 'INTELLECTUAL PROPERTY LAW', 'MEDIA',
                                 'INTERNET AND INFORMATION TECHNOLOGY LAW'],
             size_of_law_practice='SMALL (1 TO 5 LAWYERS)', telephone_no='+6565098893',
             website='http://www.actonlaw.sg', email='enquiries@actonlaw.sg',
             address='70 SHENTON WAY EON SHENTON # 12-06/07 SINGAPORE 079118'),
        Firm(name_of_law_practice='ACTUS LEGAL LLP', type_of_law_practice='SINGAPORE LAW PRACTICE',
             key_practice_areas=['ACCIDENT AND PERSONAL INJURY CLAIMS', 'ARBITRATION', 'BANKING',
                                 'FINANCE AND SECURITIES LAW', 'BANKRUPTCY AND INSOLVENCY LAW',
                                 'BUILDING AND CONSTRUCTION LAW', 'CIVIL AND COMMERCIAL LITIGATION', 'COMPETITION LAW',
                                 'CONVEYANCING AND PROPERTY LAW', 'CORPORATE AND COMMERCIAL LAW', 'CRIMINAL LAW',
                                 'EMPLOYMENT LAW', 'FAMILY LAW', 'IMMIGRATION LAW', 'INSURANCE LAW',
                                 'INTELLECTUAL PROPERTY LAW', 'ISLAMIC LAW', 'LANDLORD AND TENANT LAW', 'MEDIA',
                                 'INTERNET AND INFORMATION TECHNOLOGY LAW', 'MEDIATION', 'TRUST LAW', 'WILLS',
                                 'PROBATE AND ADMINISTRATION OF ESTATE', 'WORKERSâ€™ COMPENSATION CLAIMS'],
             size_of_law_practice='SMALL (1 TO 5 LAWYERS)', telephone_no='6788 2088', website='http://www.actus.sg',
             email='contactus@actus.sg',
             address="101 UPPER CROSS STREET PEOPLE'S PARK CENTRE # 06-15B SINGAPORE 058357")
    ]


def test_get_save_file_path():
    import datetime
    assert lsra_scraper.get_save_file_path('\\\\Users', 'lawyers',
                                           'csv') == f"\\\\Users\\lawyers {datetime.date.today()}.csv"


def test_search_type_arguments_lawyers(mocker):
    runner = CliRunner()
    driver_mock = mocker.patch('lsra_scraper.lsra_scraper.setup_web_driver')
    runner.invoke(lsra_scraper.lsra_scraper, ['lawyers'])
    driver_mock.assert_not_called()


def test_search_type_arguments_firms(mocker):
    runner = CliRunner()
    driver_mock = mocker.patch('lsra_scraper.lsra_scraper.setup_web_driver')
    runner.invoke(lsra_scraper.lsra_scraper, ['firms'])
    driver_mock.assert_called()


def test_search_type_arguments_default(mocker):
    runner = CliRunner()
    driver_mock = mocker.patch('lsra_scraper.lsra_scraper.setup_web_driver')
    runner.invoke(lsra_scraper.lsra_scraper, [])
    driver_mock.assert_called()


def test_out_file_arguments_default(mocker):
    import os
    runner = CliRunner()
    mocker.patch('lsra_scraper.lsra_scraper.setup_web_driver')
    mocker.patch('lsra_scraper.lsra_scraper.scrape', return_value=[])
    mock_csv = mocker.patch('lsra_scraper.lsra_scraper.save_csv')
    runner.invoke(lsra_scraper.lsra_scraper, [])
    mock_csv.assert_called_with([], None, os.getcwd(), 'firms')


def test_out_file_arguments_outfile(mocker):
    import os
    runner = CliRunner()
    mocker.patch('lsra_scraper.lsra_scraper.setup_web_driver')
    mocker.patch('lsra_scraper.lsra_scraper.scrape', return_value=[])
    mock_csv = mocker.patch('lsra_scraper.lsra_scraper.save_csv')
    runner.invoke(lsra_scraper.lsra_scraper, ['--out-file', 'test.csv'])
    mock_csv.assert_called_with([], 'test.csv', os.getcwd(), 'firms')


def test_get_site(site_path):
    assert lsra_scraper.get_site(
        site=site_path) == 'https://eservices.mlaw.gov.sg/lsra/search-lawyer-or-law-firm?searchType=0'
    assert lsra_scraper.get_site(site=site_path,
                                 search_type='firm') == 'https://eservices.mlaw.gov.sg/lsra/search-lawyer-or-' \
                                                        'law-firm?searchType=0'
    assert lsra_scraper.get_site(site=site_path,
                                 search_type='lawyers') == 'https://eservices.mlaw.gov.sg/lsra/search-lawyer-or-' \
                                                           'law-firm?searchType=1'


def test_parse_lawyers_table():
    lsra_scraper.parse_lawyers_table(open('tests/firms_table2.html', 'r').read(), [])


def test_process_pages(selenium, mocker):
    import os
    import pathlib
    selenium.get(pathlib.Path(os.getcwd() + 'tests/firms_table2.html').as_uri())
    try:
        mock_parse_lawyers_table = mocker.patch('lsra_scraper.lsra_scraper.parse_lawyers_table')
        mock_parse_firms_table = mocker.patch('lsra_scraper.lsra_scraper.parse_firms_table')
        lsra_scraper.process_pages(selenium)
        mock_parse_firms_table.assert_called_once()
        lsra_scraper.process_pages(selenium, search_type='lawyers')
        mock_parse_lawyers_table.assert_called_once()
    except NoSuchElementException:
        pass


def test_save_csv_outfile():
    import os
    test_results = [Firm('ABC', 'DEF', [], '1', '123')]
    outfile = 'test.csv'
    try:
        outfile = lsra_scraper.save_csv(test_results, outfile, os.getcwd(), 'firms')
        assert open(outfile, 'r')
    finally:
        os.remove(outfile)


def test_save_csv_default():
    import os
    test_results = [Firm('ABC', 'DEF', [], '1', '123')]
    outfile = None
    try:
        outfile = lsra_scraper.save_csv(test_results, outfile, os.getcwd(), 'firms')
        assert open(outfile, 'r')
    finally:
        os.remove(outfile)


def test_scrape(mocker, selenium, site_path):
    mocker.patch('lsra_scraper.lsra_scraper.pass_captcha')
    mocker.patch('lsra_scraper.lsra_scraper.process_pages', return_value=['test'])
    assert lsra_scraper.scrape(selenium, site_path, 'firms') == ['test']


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable_gpu')
    return chrome_options


@pytest.fixture
def site_path():
    return 'https://eservices.mlaw.gov.sg/lsra/search-lawyer-or-law-firm'
