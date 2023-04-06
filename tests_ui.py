import pytest

from pages.pages_letcode import InputPage, ButtonPage, DropdownPage, AlertPage, FramePage, RadioAndCheckbox


class TestInputField:

    def test_full_name_input(self, driver):
        """Test case: Enter your full name."""
        page = InputPage(driver, 'https://letcode.in/edit')
        page.open()
        page.check_input_full_name()

    def test_tab_key_pressed(self, driver):
        """Test case: Append a text and press keyboard tab."""
        page = InputPage(driver, 'https://letcode.in/edit')
        page.open()
        page.check_tab_key_pressed()

    def test_get_field_attr(self, driver):
        """Test case: Get attribute inside the text box."""
        page = InputPage(driver, 'https://letcode.in/edit')
        page.open()
        page.check_field_attr()

    def test_clear_input_field(self, driver):
        """Test case: Clear the text in the field."""
        page = InputPage(driver, 'https://letcode.in/edit')
        page.open()
        page.check_clear_text_field()

    def test_field_is_disabled(self, driver):
        """Test case: Confirm edit field is disabled."""
        page = InputPage(driver, 'https://letcode.in/edit')
        page.open()
        page.check_field_is_disabled()

    def test_field_is_readonly(self, driver):
        """Test case: Confirm text is readonly."""
        page = InputPage(driver, 'https://letcode.in/edit')
        page.open()
        page.check_field_is_readonly()


class TestButtonPage:

    def test_go_to_home_button(self, driver):
        """Test case: check button's directional link."""
        page = ButtonPage(driver, 'https://letcode.in/buttons')
        page.open()
        page.check_go_to_home_button()

    def test_button_coordinates(self, driver):
        """Test case: Get the X & Y co-ordinates of element"""
        page = ButtonPage(driver, 'https://letcode.in/buttons')
        page.open()
        page.check_button_coordinates()

    def test_button_color(self, driver):
        """Test case: Find the color of the button."""
        page = ButtonPage(driver, 'https://letcode.in/buttons')
        page.open()
        page.check_button_color()

    def test_button_size(self, driver):
        """Test case: Find the height & width of the button."""
        page = ButtonPage(driver, 'https://letcode.in/buttons')
        page.open()
        page.check_button_size()

    def test_button_is_disabled(self, driver):
        """Test case: Confirm button is disabled."""
        page = ButtonPage(driver, 'https://letcode.in/buttons')
        page.open()
        page.check_button_is_disabled()


class TestDropdownPage:

    def test_select_by_visible_text(self, driver):
        """Test case: Select the apple using visible text."""
        page = DropdownPage(driver, 'https://letcode.in/dropdowns')
        page.open()
        page.check_select_by_visible_text()

    def test_multiple_selector_option(self, driver):
        """"Test case: Select your superhero's from the list."""
        page = DropdownPage(driver, 'https://letcode.in/dropdowns')
        page.open()
        page.check_selection_is_multiple()

    def test_selection_options(self, driver):
        """Test case: Select the last programming language and print all the options."""
        page = DropdownPage(driver, 'https://letcode.in/dropdowns')
        page.open()
        page.check_selection_options()

    def test_selection_by_value(self, driver):
        """Test case: Select 'India' using value & print the selected value."""
        page = DropdownPage(driver, 'https://letcode.in/dropdowns')
        page.open()
        page.check_selection_by_value()


class TestAlert:

    def test_accept_the_alert(self, driver):
        """Test case: Accept the alert."""
        page = AlertPage(driver, 'https://letcode.in/alert')
        page.open()
        page.check_accept_the_alert()

    def test_dismiss_the_alert(self, driver):
        """Test case: Dismiss the alert & print the alert text."""
        page = AlertPage(driver, 'https://letcode.in/alert')
        page.open()
        page.check_dismiss_the_alert()

    def test_prompt_input(self, driver):
        """Test case: Type your name & accept prompt alert."""
        page = AlertPage(driver, 'https://letcode.in/alert')
        page.open()
        page.check_prompt_input()

    def test_modern_alert(self, driver):
        """Test case: Check presence of modern alert window"""
        page = AlertPage(driver, 'https://letcode.in/alert')
        page.open()
        page.check_modern_alert()


class TestFrame:

    def test_first_frame_interaction(self, driver):
        """Test case: Switching to iframe and interaction with inner input fields."""
        page = FramePage(driver, 'https://letcode.in/frame')
        page.open()
        page.check_first_frame_interaction()

    def test_second_frame_interaction(self, driver):
        """Test case: Switching to inner iframe and interaction with inner input fields."""
        page = FramePage(driver, 'https://letcode.in/frame')
        page.open()
        page.check_second_frame_interaction()


class TestRadioAndCheckbox:

    def test_radiobutton_selection(self, driver):
        """Test case: Select any radiobutton."""
        page = RadioAndCheckbox(driver, 'https://letcode.in/radio')
        page.open()
        page.check_radiobutton_selection()

    def test_only_one_radiobutton_can_be_selected(self, driver):
        """Test case: Confirm you can select only one radio button."""
        page = RadioAndCheckbox(driver, 'https://letcode.in/radio')
        page.open()
        page.check_only_one_radiobutton_can_be_selected()

    @pytest.mark.xfail
    def test_both_radiobuttons_selected_bug(self, driver):
        """Test case: Find the bug (both buttons are selected)."""
        page = RadioAndCheckbox(driver, 'https://letcode.in/radio')
        page.open()
        page.check_both_radiobuttons_selected_bug()

    def test_selected_radiobutton(self, driver):
        """"Test case: Find which radiobutton is selected."""
        page = RadioAndCheckbox(driver, 'https://letcode.in/radio')
        page.open()
        page.check_radiobutton_is_selected()

    def test_field_is_disabled(self, driver):
        """"Test case: Confirm last field is disabled."""
        page = RadioAndCheckbox(driver, 'https://letcode.in/radio')
        page.open()
        page.check_field_is_disabled()

    def test_checkbox_is_selected(self, driver):
        """Test case: Find if the checkbox is selected."""
        page = RadioAndCheckbox(driver, 'https://letcode.in/radio')
        page.open()
        page.check_checkbox_is_selected()

    def test_terms_checkbox_is_selected(self, driver):
        """Test case: Accept the T&C checkbox."""
        page = RadioAndCheckbox(driver, 'https://letcode.in/radio')
        page.open()
        page.check_terms_checkbox_is_selected()
