from selene.support.shared import browser
from selene import be, have


def test_result_is_found():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Web UI browser tests in'))


def test_result_not_found():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('gehe3453453_notfounderror_354353').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу  ничего не найдено. '))
