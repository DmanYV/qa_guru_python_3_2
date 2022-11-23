from selene.support.shared import browser
from selene import be, have


def test_google_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('#search').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_google_search_bad_request(open_browser):
    browser.element('[name="q"]').should(be.blank).type('sdfNOSDNgiouBSDoignlkjjdosgn').press_enter()
    browser.element('#res').should(have.text('По запросу sdfNOSDNgiouBSDoignlkjjdosgn ничего не найдено.'))
