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
    browser.element('[for="hobbies-checkbox-2"]').click()  # Reading
    browser.element('[for="hobbies-checkbox-3"]').click()  # Music

    # Upload (без переменных — сразу абсолютный путь)
    browser.element('#uploadPicture').set_value(
        str((Path(__file__).parents[1] / 'resources' / 'cat.png').resolve())
    )

    # Адрес
    browser.element('#currentAddress').type('Sevastopol,Lenina str., 1')

    # Иногда баннер/футер мешают — прибираем
    browser.execute_script("document.querySelector('#fixedban')?.remove();document.querySelector('footer')?.remove();")

    # State / City
    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.element('div[class$="-menu"]').should(be.visible)
    browser.all('[id^="react-select-3-option-"]').element_by(have.exact_text('Haryana')).click()

    browser.element('#city').perform(command.js.scroll_into_view).click()
    browser.element('div[class$="-menu"]').should(be.visible)
    browser.all('[id^="react-select-4-option-"]').element_by(have.exact_text('Karnal')).click()

    # Submit
    browser.element('#submit').perform(command.js.scroll_into_view).click()

    # ПРОВЕРКИ (это делает скрипт — тестом)
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    table = browser.element('.table-responsive')
    table.should(have.text('Liza Koss'))
    table.should(have.text('lizakoss.demoqa.v1@mailinator.com'))
    table.should(have.text('Female'))
    table.should(have.text('4564978762'))
    table.should(have.text('15 March,2000'))
    table.should(have.text('Chemistry'))
    table.should(have.text('Reading, Music'))
    table.should(have.text('Haryana Karnal'))
    table.should(have.text('Sevastopol,Lenina str., 1'))
