from pages.pages_letcode import InputPage, ButtonPage, DropdownPage, AlertPage, FramePage, RadioAndCheckbox


class TestInputField:

    def test_full_name_input(self, driver):
        page = InputPage(driver, 'https://letcode.in/edit')
        page.open()
        page.check_input_full_name()

    def test_tab_key_pressed(self, driver):
        page = InputPage(driver, 'https://letcode.in/edit')
        page.open()
        page.check_tab_key_pressed()

    def test_get_field_attr(self, driver):
        page = InputPage(driver, 'https://letcode.in/edit')
        page.open()
        page.check_field_attr()

    def test_clear_input_field(self, driver):
        page = InputPage(driver, 'https://letcode.in/edit')
        page.open()
        page.check_clear_text_field()

    def test_field_is_disabled(self, driver):
        page = InputPage(driver, 'https://letcode.in/edit')
        page.open()
        page.check_field_is_disabled()

    def test_field_is_readonly(self, driver):
        page = InputPage(driver, 'https://letcode.in/edit')
        page.open()
        page.check_field_is_readonly()


class TestButtonPage:

    def test_go_to_home_button(self, driver):
        page = ButtonPage(driver, 'https://letcode.in/buttons')
        page.open()
        page.check_go_to_home_button()

    def test_button_coordinates(self, driver):
        page = ButtonPage(driver, 'https://letcode.in/buttons')
        page.open()
        page.check_button_coordinates()

    def test_button_color(self, driver):
        page = ButtonPage(driver, 'https://letcode.in/buttons')
        page.open()
        page.check_button_color()

    def test_button_size(self, driver):
        page = ButtonPage(driver, 'https://letcode.in/buttons')
        page.open()
        page.check_button_size()

    def test_button_is_disabled(self, driver):
        page = ButtonPage(driver, 'https://letcode.in/buttons')
        page.open()
        page.check_button_is_disabled()


class TestDropdownPage:

    def test_select_by_visible_text(self, driver):
        page = DropdownPage(driver, 'https://letcode.in/dropdowns')
        page.open()
        page.check_select_by_visible_text()

    def test_multiple_selector_option(self, driver):
        page = DropdownPage(driver, 'https://letcode.in/dropdowns')
        page.open()
        page.check_selection_is_multiple()

    def test_selection_options(self, driver):
        page = DropdownPage(driver, 'https://letcode.in/dropdowns')
        page.open()
        page.check_selection_options()

    def test_selection_by_value(self, driver):
        page = DropdownPage(driver, 'https://letcode.in/dropdowns')
        page.open()
        page.check_selection_by_value()


class TestAlert:

    def test_accept_the_alert(self, driver):
        page = AlertPage(driver, 'https://letcode.in/alert')
        page.open()
        page.check_accept_the_alert()

    def test_dismiss_the_alert(self, driver):
        page = AlertPage(driver, 'https://letcode.in/alert')
        page.open()
        page.check_dismiss_the_alert()

    def test_prompt_input(self, driver):
        page = AlertPage(driver, 'https://letcode.in/alert')
        page.open()
        page.check_prompt_input()

    def test_modern_alert(self, driver):
        page = AlertPage(driver, 'https://letcode.in/alert')
        page.open()
        page.check_modern_alert()


class TestFrame:

    def test_first_frame_interaction(self, driver):
        page = FramePage(driver, 'https://letcode.in/frame')
        page.open()
        page.check_first_frame_interaction()

    def test_second_frame_interaction(self, driver):
        page = FramePage(driver, 'https://letcode.in/frame')
        page.open()
        page.check_second_frame_interaction()


class TestRadioAndCheckbox:

    def test_radiobutton_selection(self, driver):
        page = RadioAndCheckbox(driver, 'https://letcode.in/radio')
        page.open()
        page.check_radiobutton_selection()

    def test_only_one_radiobutton_can_be_selected(self, driver):
        page = RadioAndCheckbox(driver, 'https://letcode.in/radio')
        page.open()
        page.check_only_one_radiobutton_can_be_selected()

