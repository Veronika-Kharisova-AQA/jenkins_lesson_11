from pages.practice_form_page import PracticeFormPage


def test_registration_form():
    registration_page = PracticeFormPage()

    registration_page.open() \
        .fill_first_name('Veronika') \
        .fill_last_name('Kharisova') \
        .fill_email('Veronika@example.com') \
        .select_gender('Female') \
        .fill_phone('5643782341') \
        .fill_birth_date('July', '2002', '14') \
        .fill_subject('Maths') \
        .choose_hobby('Sports') \
        .upload_picture('cat.jpg') \
        .fill_address('Russia, Moscow') \
        .select_state('NCR') \
        .select_city('Delhi') \
        .submit() \
        .should_have_registered(
        'Veronika Kharisova',
        'Veronika@example.com',
        'Female',
        '5643782341',
        '14 July,2002',
        'Maths',
        'Sports',
        'cat.jpg',
        'Russia, Moscow',
        'NCR Delhi'
    )