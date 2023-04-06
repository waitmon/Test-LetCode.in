import random
import string
import time

from selenium.webdriver import Keys
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from src.generator import generated_new_user
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
