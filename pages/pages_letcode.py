import random
import string
import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from src.generator import generated_new_user, generated_university
from src.locators import PageLocators


class InputPage(BasePage):
    locators = PageLocators()

    def check_input_full_name(self):
        input_text = ''.join(random.choices(string.ascii_letters.lower(), k=10))
        input_field = self.element_is_present(self.locators.FULL_NAME_INPUT)
        input_field.send_keys(input_text)
        input_result = input_field.get_attribute('value')
        assert input_result != '', 'Input field is empty'

    def check_tab_key_pressed(self):
        input_field = self.element_is_present(self.locators.TAB_FIELD)
        input_field.send_keys(', no doubts')
        initial_input_field_text = input_field.get_attribute('value')
        input_field.send_keys(Keys.TAB)
        next_input_field = self.element_is_present(self.locators.GET_ATTR_FIELD)
        next_input_field_text = next_input_field.get_attribute('value')
        assert initial_input_field_text != next_input_field_text, 'TAB key was not pressed'

    def check_field_attr(self):
        input_field = self.element_is_present(self.locators.GET_ATTR_FIELD)
        field_attribute = input_field.get_attribute('value')
        assert field_attribute == 'ortonikc', 'Field has different value'

    def check_clear_text_field(self):
        input_field = self.element_is_present(self.locators.CLEAR_FIELD)
        input_field.clear()
        input_result = input_field.get_attribute('value')
        assert input_result == '', 'Input field is not empty'

    def check_field_is_disabled(self):
        input_field = self.element_is_present(self.locators.DISABLED_FIELD)
        assert not input_field.is_enabled(), 'The field is enabled'

    def check_field_is_readonly(self):
        input_field = self.element_is_present(self.locators.READONLY_FIELD)
        assert 'readonly' in input_field.get_attribute('value'), 'The field is enabled for interaction'


class ButtonPage(BasePage):
    locators = PageLocators()

    def check_go_to_home_button(self):
        initial_url = self.driver.current_url
        button = self.element_is_present(self.locators.GO_TO_HOME_BUTTON)
        button.click()
        redirection_url = self.driver.current_url
        assert initial_url != redirection_url, 'Go to home button does not redirect to home page'

    def check_button_coordinates(self):
        button = self.element_is_present(self.locators.COORDINATES_BUTTON)
        location = button.location
        assert location is not '', 'Could not extract button X & Y co-ordinates'

    def check_button_color(self):
        button = self.element_is_present(self.locators.COLOR_BUTTON)
        rgb = button.value_of_css_property('background-color')
        button_color = Color.from_string(rgb).hex
        assert "#" in button_color, 'Could not extract button color'

    def check_button_size(self):
        button = self.element_is_present(self.locators.COORDINATES_BUTTON)
        dimensions = button.size
        assert 'height' and 'width' in dimensions, 'Could not extract button size'

    def check_button_is_disabled(self):
        button = self.element_is_present(self.locators.DISABLED_BUTTON)
        assert not button.is_enabled(), 'The button is enabled'

    def check_click_and_hold_button(self):
        button = self.element_is_present(self.locators.HOLD_BUTTON)
        self.scroll_to_element(button)
        action = ActionChains(self.driver)
        action.click_and_hold(button).pause(3).perform()
        button_msg = button.text
        assert button_msg == 'Button has been long pressed', 'Could not reproduce click and hold action'


class DropdownPage(BasePage):
    locators = PageLocators()

    def check_select_by_visible_text(self):
        select = Select(self.element_is_present(self.locators.FRUITS_SELECTOR))
        select.select_by_visible_text('Apple')
        notification_text = self.element_is_visible(self.locators.NOTIFICATION).text
        assert notification_text == 'You have selected Apple', 'Apple option was not selected'

    def check_selection_is_multiple(self):
        selector = self.element_is_present(self.locators.SUPERHEROES_SELECTOR)
        assert selector.get_attribute('multiple')

    def check_selection_options(self):
        select = Select(self.element_is_present(self.locators.PROG_LANGUAGE_SELECTOR))
        select.select_by_index(4)
        for option in select.options:
            print(option.text, option.get_attribute('value'))
        assert select.options != '', 'Could not print all the options'

    def check_selection_by_value(self):
        option_needed = self.element_is_present(self.locators.OPTION_INDIA)
        select = Select(self.element_is_present(self.locators.COUNTRY_SELECTOR))
        select.select_by_value('India')
        print(option_needed.text)
        assert option_needed.is_selected()


class AlertPage(BasePage):
    locators = PageLocators()

    def check_accept_the_alert(self):
        self.element_is_present(self.locators.SIMPLE_ALERT).click()
        time.sleep(0.2)
        alert_window = self.driver.switch_to.alert
        alert_text = alert_window.text
        alert_window.accept()
        assert alert_text == 'Hey! Welcome to LetCode', 'Alert window did not appear'

    def check_dismiss_the_alert(self):
        self.element_is_present(self.locators.CONFIRM_ALERT).click()
        time.sleep(0.2)
        alert_window = self.driver.switch_to.alert
        alert_text = alert_window.text
        alert_window.dismiss()
        print(alert_text)
        assert alert_text == 'Are you happy with LetCode?', 'Alert window did not appear'

    def check_prompt_input(self):
        prompt_text = ''.join(random.choices(string.ascii_letters.lower(), k=7))
        self.element_is_present(self.locators.PROMPT_ALERT).click()
        prompt = self.driver.switch_to.alert
        prompt.send_keys(prompt_text)
        prompt.accept()
        prompt_msg = self.element_is_present(self.locators.PROMPT_NOTIFICATION)
        assert prompt_msg.is_displayed(), 'Prompt window did not appear'

    def check_modern_alert(self):
        self.element_is_present(self.locators.SWEET_ALERT).click()
        assert self.element_is_visible(self.locators.SWEET_ALERT_CONTENT), 'Modern alert window did not appear'


class FramePage(BasePage):
    locators = PageLocators()

    def check_first_frame_interaction(self):
        iframe = self.element_is_present(self.locators.FIRST_FRAME)
        self.driver.switch_to.frame(iframe)
        input_data = next(generated_new_user())
        self.element_is_present(self.locators.FIRST_NAME).send_keys(input_data.first_name)
        self.element_is_present(self.locators.LAST_NAME).send_keys(input_data.last_name)
        input_result = self.element_is_present(self.locators.INPUT_RESULT)
        assert input_result.is_displayed(), 'Driver could not switch to iframe'

    def check_second_frame_interaction(self):
        first_iframe = self.element_is_present(self.locators.FIRST_FRAME)
        self.driver.switch_to.frame(first_iframe)
        second_iframe = self.element_is_present(self.locators.INNER_FRAME)
        self.driver.switch_to.frame(second_iframe)
        input_data = next(generated_new_user())
        email_field = self.element_is_present(self.locators.EMAIL_NAME)
        email_field.send_keys(input_data.email)
        assert email_field != '', 'Driver could not switch to inner iframe'


class RadioAndCheckbox(BasePage):
    locators = PageLocators()

    def check_radiobutton_selection(self):
        radiobutton = self.element_is_present(self.locators.YES_RADIOBUTTON)
        radiobutton.click()
        assert radiobutton.is_selected()

    def check_only_one_radiobutton_can_be_selected(self):
        first_radiobutton = self.element_is_present(self.locators.ONE_RADIOBUTTON)
        second_radiobutton = self.element_is_present(self.locators.TWO_RADIOBUTTON)
        first_radiobutton.click()
        second_radiobutton.click()
        assert second_radiobutton.is_selected() and not first_radiobutton.is_selected(), 'Both radiobuttons are ' \
                                                                                         'selected '

    def check_both_radiobuttons_selected_bug(self):
        first_radiobutton = self.element_is_present(self.locators.NOBUG_RADIOBUTTON)
        second_radiobutton = self.element_is_present(self.locators.BUG_RADIOBUTTON)
        first_radiobutton.click()
        second_radiobutton.click()
        assert not first_radiobutton.is_selected() and second_radiobutton.is_selected(), 'Both radiobuttons are ' \
                                                                                         'selected'

    def check_radiobutton_is_selected(self):
        selected_radiobutton = self.element_is_present(self.locators.BAR_RADIOBUTTON)
        assert 'on' in selected_radiobutton.get_attribute('value'), 'Radiobutton has no selected attribute'

    def check_field_is_disabled(self):
        disabled_radiobutton = self.element_is_present(self.locators.MAYBE_RADIOBUTTON)
        assert not disabled_radiobutton.is_enabled(), 'Radiobutton is enabled for interaction'

    def check_checkbox_is_selected(self):
        selected_checkbox = self.element_is_present(self.locators.REMEMBER_ME_CHECKBOX)
        assert selected_checkbox.is_selected(), 'Checkbox is not selected'

    def check_terms_checkbox_is_selected(self):
        selected_checkbox = self.element_is_present(self.locators.TERMS_AND_CONDITIONS_CHECKBOX)
        selected_checkbox.click()
        assert selected_checkbox.is_selected(), 'Checkbox was not selected'


class DropPage(BasePage):
    locators = PageLocators()

    def check_drag_and_drop(self):
        drag = self.element_is_visible(self.locators.DRAG_BOX_SOURCE)
        drop = self.element_is_visible(self.locators.DROP_BOX_TARGET)
        self.action_drag_and_drop_to_element(drag, drop)
        assert drop.text == 'Dropped!', 'Could not reproduce drag and drop process'


class SelectablePage(BasePage):
    locators = PageLocators()

    def check_selecting_all_elements(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.LEFT_CONTROL).perform()
        selectable_options = self.elements_are_present(self.locators.SELECTABLE_OPTION)
        for option in selectable_options:
            option.click()
        selected_options_quantity = []
        for status in selectable_options:
            selected_options_quantity.append(status.get_attribute('class'))
        assert 'ui-selectable ui-selected' in selected_options_quantity, 'Not all options were not selected'


class SliderPage(BasePage):
    locators = PageLocators()

    def check_slider_interaction(self):
        slider = self.element_is_present(self.locators.SLIDER)
        self.action_drag_and_drop_by_offset(slider, random.randint(0, 50), 0)
        word_limit_value = self.element_is_present(self.locators.LIMIT_COUNTER).text
        self.element_is_present(self.locators.GET_COUNTRIES_BUTTON).click()
        generated_country_list = self.element_is_visible(self.locators.COUNTRY_LIST).text
        country_list = generated_country_list.split(' - ')
        assert len(country_list) == word_limit_value, 'Generated countries are not based on slider values'


class SortableTablesPage(BasePage):
    locators = PageLocators()

    def check_sorting_by_calories_desc(self):
        sort_header = self.element_is_visible(self.locators.CALORIES_SORT_HEADER)
        self.action_move_to_element(sort_header)
        self.action_double_click(sort_header)
        calories_available = self.elements_are_present(self.locators.CALORIES_LIST)
        calories_list_descending_order = []
        for value in calories_available:
            current_value = value.text
            calories_list_descending_order.append(current_value)
        assert calories_list_descending_order == sorted(calories_list_descending_order, reverse=True), \
            'Descending sorting was not reproduced '

    def check_sorting_by_calories_asc(self):
        sort_header = self.element_is_visible(self.locators.CALORIES_SORT_HEADER)
        self.action_move_to_element(sort_header)
        self.action_double_click(sort_header)
        sort_header.click()
        calories_available = self.elements_are_present(self.locators.CALORIES_LIST)
        calories_list_descending_order = []
        for value in calories_available:
            current_value = value.text
            calories_list_descending_order.append(current_value)
        assert calories_list_descending_order == sorted(calories_list_descending_order), 'Ascending ' \
                                                                                         'sorting was not' \
                                                                                         ' reproduced '


class AdvancedTablePage(BasePage):
    locators = PageLocators()

    def check_searching_university_name(self):
        uni_name = random.sample(next(generated_university()).uni_name, k=1)
        search_field = self.element_is_present(self.locators.SEARCH_FIELD)
        search_field.send_keys(uni_name)
        search_request = search_field.get_attribute('value')
        search_result = self.element_is_visible(self.locators.SEARCH_RESULT).text
        assert search_request == search_result, 'Searching request and result did not match'

    def check_selecting_serial_numbers(self):
        show_entries = self.element_is_present(self.locators.SHOW_ENTRIES)
        Select(show_entries).select_by_index(random.randint(0, 2))
        chosen_entries = show_entries.get_attribute('value')
        number_list = self.elements_are_present(self.locators.SERIAL_NUMBER_LIST)
        assert len(number_list) == int(chosen_entries), 'Quality of displayed entries did not match with selected value'


class WaitPage(BasePage):
    locators = PageLocators()

    def check_waiting_for_alert_appearance(self):
        button = self.element_is_present(self.locators.SIMPLE_ALERT)
        button.click()
        WebDriverWait(self.driver, timeout=10).until(EC.alert_is_present())
        alert_window = self.driver.switch_to.alert
        alert_text = alert_window.text
        alert_window.accept()
        assert alert_text == "Finally I'm here, just to say Hi :)"


class FormPage(BasePage):
    locators = PageLocators()

    def check_data_input(self):
        user_info = next(generated_new_user())
        first_name = user_info.first_name
        last_name = user_info.last_name
        email = user_info.email
        phone_number = user_info.phone_number
        first_address_line = user_info.address_line_1
        second_address_line = user_info.address_line_2
        state = user_info.state
        postal_code = user_info.postal_code
        date_of_birth = user_info.date_of_birth
        self.element_is_present(self.locators.FIRST_NAME_FORM).send_keys(first_name)
        self.element_is_present(self.locators.LAST_NAME_FORM).send_keys(last_name)
        self.element_is_present(self.locators.EMAIL_FORM).clear()
        self.element_is_present(self.locators.EMAIL_FORM).send_keys(email)
        self.element_is_present(self.locators.PHONE_NUMBER_FORM).send_keys(phone_number)
        self.element_is_present(self.locators.ADDRESS_LINE_1_FORM).send_keys(first_address_line)
        self.element_is_present(self.locators.ADDRESS_LINE_2_FORM).send_keys(second_address_line)
        self.element_is_present(self.locators.STATE_FORM).send_keys(state)
        self.element_is_present(self.locators.POSTAL_CODE_FORM).send_keys(postal_code)
        self.element_is_present(self.locators.DATE_OF_BIRTH).send_keys(date_of_birth)
        gender_list = self.elements_are_present(self.locators.GENDER_LIST_FORM)
        gender_button = gender_list[random.randint(0, 2)]
        gender_button.click()
        self.element_is_present(self.locators.TERMS_CHECKBOX_FORM).click()
        self.element_is_present(self.locators.SUBMIT_BUTTON).click()


class UploadAndDownloadPage(BasePage):
    locators = PageLocators()

    def check_xls_download(self):
        self.element_is_present(self.locators.DOWNLOAD_XLS).click()
        fileends = "crdownload"
        while "crdownload" == fileends:
            time.sleep(1)
            newest_file = self.latest_download_file()
            if "crdownload" in newest_file:
                fileends = "crdownload"
            else:
                fileends = "none"
        assert '.xls' in self.latest_download_file(), 'XLS file was not downloaded'

    def check_pdf_download(self):
        self.element_is_present(self.locators.DOWNLOAD_PDF).click()
        fileends = "crdownload"
        while "crdownload" == fileends:
            time.sleep(1)
            newest_file = self.latest_download_file()
            if "crdownload" in newest_file:
                fileends = "crdownload"
            else:
                fileends = "none"
        assert '.pdf' in self.latest_download_file(), 'PDF file was not downloaded'

    def check_txt_download(self):
        self.element_is_present(self.locators.DOWNLOAD_TXT).click()
        fileends = "crdownload"
        while "crdownload" == fileends:
            time.sleep(1)
            newest_file = self.latest_download_file()
            if "crdownload" in newest_file:
                fileends = "crdownload"
            else:
                fileends = "none"
        assert '.txt' in self.latest_download_file(), 'TXT file was not downloaded'
