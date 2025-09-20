from selene import be, have, command
from selene.support.shared import browser
from pathlib import Path


def test_form_filling(set_browser):
    browser.open('https://demoqa.com/automation-practice-form')

    b = browser.with_(timeout=10)

    # First Name/ Last Name/ Email
    b.element('#firstName').should(be.visible).type('Liza')
    b.element('#lastName').should(be.visible).type('Koss')
    b.element('#userEmail').should(be.visible).type('lizakoss.demoqa.v1@mailinator.com')

    # Gender
    b.element('[for="gender-radio-2"]').click()

    b.element('#userNumber').type('4564978762')

    # DOB
    b.element('#dateOfBirthInput').click()
    b.element('.react-datepicker').should(be.visible)
    b.element('.react-datepicker__month-select').click()
    b.all('.react-datepicker__month-select option').element_by(have.exact_text('March')).click()
    b.element('.react-datepicker__year-select').click()
    b.all('.react-datepicker__year-select option').element_by(have.exact_text('2000')).click()
    b.element('.react-datepicker__day--015:not(.react-datepicker__day--outside-month)').click()

    # Subjects
    b.element('#subjectsInput').type('Chemistry').press_enter()

    # Hobbies
    b.element('[for="hobbies-checkbox-2"]').click()
    b.element('[for="hobbies-checkbox-3"]').click()

    # Upload file
    b.element('#uploadPicture').set_value(
        str((Path(__file__).parents[1] / 'resources' / 'cat.png').resolve())
    )

    # Address
    b.element('#currentAddress').type('Sevastopol,Test str., 1')

    # State/City.
    b.element('#state').perform(command.js.scroll_into_view).click()
    b.element('div[class$="-menu"]').should(be.visible)
    b.all('[id^="react-select-3-option-"]').element_by(have.exact_text('Haryana')).click()

    b.element('#city').click()
    b.element('div[class$="-menu"]').should(be.visible)
    b.all('[id^="react-select-4-option-"]').element_by(have.exact_text('Karnal')).click()

    # Submit
    b.element('#submit').perform(command.js.click)

    # Verifying sent test data
    b.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    summary = b.element('.table-responsive')
    summary.should(have.text('Liza Koss'))
    summary.should(have.text('lizakoss.demoqa.v1@mailinator.com'))
    summary.should(have.text('Female'))
    summary.should(have.text('4564978762'))
    summary.should(have.text('15 March,2000'))
    summary.should(have.text('Chemistry'))
    summary.should(have.text('Reading, Music'))
    summary.should(have.text('Haryana Karnal'))
    summary.should(have.text('Sevastopol,Test str., 1'))
