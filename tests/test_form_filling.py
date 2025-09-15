from selene import be, have, command
from selene.support.shared import browser
from pathlib import Path

def test_form_filling(set_browser):
    # Имя/Фамилия/Email/Телефон
    browser.element('#firstName').type('Liza')
    browser.element('#lastName').type('Koss')
    browser.element('#userEmail').type('lizakoss.demoqa.v1@mailinator.com')
    browser.element('[for="gender-radio-2"]').should(be.visible).click()
    browser.element('#userNumber').type('4564978762')

    # Дата рождения через виджет
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.all('.react-datepicker__month-select option').element_by(have.exact_text('March')).click()
    browser.element('.react-datepicker__year-select').click()
    browser.all('.react-datepicker__year-select option').element_by(have.exact_text('2000')).click()
    browser.element('.react-datepicker__day--015:not(.react-datepicker__day--outside-month)').click()

    # Subjects — выбрать из подсказки
    browser.element('#subjectsInput').type('Chemistry').press_enter()

    # Hobbies
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    # Upload — без промежуточной переменной
    browser.element('#uploadPicture').set_value(
        str((Path(__file__).parents[1] / 'resources' / 'cat.png').resolve())
    )

    # Address
    browser.element('#currentAddress').type('Sevastopol,Lenina str., 1')

    # Иногда мешают баннер/футер
    browser.execute_script("document.querySelector('#fixedban')?.remove();document.querySelector('footer')?.remove();")

    # State
    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.element('div[class$="-menu"]').should(be.visible)
    browser.all('[id^="react-select-3-option-"]').element_by(have.exact_text('Haryana')).click()

    # City
    browser.element('#city').perform(command.js.scroll_into_view).click()
    browser.element('div[class$="-menu"]').should(be.visible)
    browser.all('[id^="react-select-4-option-"]').element_by(have.exact_text('Karnal')).click()

    # Submit
    browser.element('#submit').perform(command.js.scroll_into_view).click()

    # Проверки (делают это именно тестом)
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    summary = browser.element('.table-responsive')
    summary.should(have.text('Liza Koss'))
    summary.should(have.text('lizakoss.demoqa.v1@mailinator.com'))
    summary.should(have.text('Female'))
    summary.should(have.text('4564978762'))
    summary.should(have.text('15 March,2000'))
    summary.should(have.text('Chemistry'))
    summary.should(have.text('Reading, Music'))
    summary.should(have.text('Haryana Karnal'))
    summary.should(have.text('Sevastopol,Lenina str., 1'))