from selene import be, have, command
from selene.support.shared import browser
from pathlib import Path


def test_form_filling():
    browser.open('/automation-practice-form')

    # First Name/ Last Name/ Email
    browser.element('#firstName').should(be.visible).type('Liza')
    browser.element('#lastName').should(be.visible).type('Koss')
    browser.element('#userEmail').should(be.visible).type('lizakoss.demoqa.v1@mailinator.com')

    # Gender
    browser.element('[for="gender-radio-2"]').click()

    browser.element('#userNumber').type('4564978762')

    # DOB
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker').should(be.visible)
    browser.element('.react-datepicker__month-select').click()
    browser.all('.react-datepicker__month-select option').element_by(have.exact_text('March')).click()
    browser.element('.react-datepicker__year-select').click()
    browser.all('.react-datepicker__year-select option').element_by(have.exact_text('2000')).click()
    browser.element('.react-datepicker__day--015:not(.react-datepicker__day--outside-month)').click()

    # Subjects
    browser.element('#subjectsInput').type('Chemistry').press_enter()

    # Hobbies
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    # Upload file
    file_path = (Path(__file__).parents[1] / 'resources' / 'cat.png').resolve()
    browser.element('#uploadPicture').set_value(str(file_path))

    # Address
    browser.element('#currentAddress').type('Sevastopol,Test str., 1')

    # State/City.
    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.element('div[class$="-menu"]').should(be.visible)
    browser.all('[id^="react-select-3-option-"]').element_by(have.exact_text('Haryana')).click()

    browser.element('#city').click()
    browser.element('div[class$="-menu"]').should(be.visible)
    browser.all('[id^="react-select-4-option-"]').element_by(have.exact_text('Karnal')).click()

    # Submit
    browser.element('#submit').perform(command.js.click)

    # Verifying sent test data
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    summary = browser.element('.table-responsive')
    summary.should(have.text('Liza Koss'))
    summary.should(have.text('lizakoss.demoqa.v1@mailinator.com'))
    summary.should(have.text('Female'))
    summary.should(have.text('4564978762'))
    summary.should(have.text('15 March,2000'))
    summary.should(have.text('Chemistry'))
    summary.should(have.text('cat.png'))
    summary.should(have.text('Reading, Music'))
    summary.should(have.text('Haryana Karnal'))
    summary.should(have.text('Sevastopol,Test str., 1'))