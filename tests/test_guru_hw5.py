import os
from selene import browser, be, have, command

def test_form(browser_options):
    browser.open('/automation-practice-form/')

    #First_name
    browser.element('#firstName').should(be.blank).type('Rodion')

    #Last_name
    browser.element('#lastName').should(be.blank).type('Phil')

    #Email
    browser.element('#userEmail').should(be.blank).type('RodionPhil@gmail.com')

    #Gender
    browser.element('[for="gender-radio-1"]').click()

    #Mobile
    browser.element('#userNumber').should(be.blank).type('89875738562')

    #Date_of_birth
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('[value="11"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="2001"]').click()
    browser.element('.react-datepicker__day--015').click()

    #Subjects
    browser.element('#subjectsInput').click().type("E").press_enter()

    #Hobbies
    browser.element('#hobbies-checkbox-3').click()

    #Picture
    browser.element('#uploadPicture').click().send_keys(os.path.abspath('picture.png'))

    #Address
    browser.element('#currentAddress').should(be.blank).click().type('Antalya')

    #State_City
    browser.element('#react-select-3-input').click().press_enter()
    browser.element('#react-select-4-input').click().press_enter()

    #Submit
    browser.element('#submit').click()

    #Final_window
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.element('.table').all('tr').should(
have.exact_texts('Label Values',
                         'Student Name Rodion Phil',
                         'Student Email RodionPhil@gmail.com',
                         'Gender Male',
                         'Mobile 8987573856',
                         'Date of Birth 15 November,2001',
                         'Subjects English',
                         'Hobbies Music',
                         'Picture picture.png.jpg',
                         'Address Antalya',
                         'State and City NCR Delhi',
                         )
    )
browser.element('#closeLargeModal').should(be.clickable)


