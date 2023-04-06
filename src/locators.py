from selenium.webdriver.common.by import By


class PageLocators:

    FULL_NAME_INPUT = (By.CSS_SELECTOR, '#fullName')
    TAB_FIELD = (By.CSS_SELECTOR, '#join')
    GET_ATTR_FIELD = (By.CSS_SELECTOR, '#getMe')
    CLEAR_FIELD = (By.CSS_SELECTOR, '#clearMe')
    DISABLED_FIELD = (By.CSS_SELECTOR, '#noEdit')
    READONLY_FIELD = (By.CSS_SELECTOR, '#dontwrite')

    GO_TO_HOME_BUTTON = (By.CSS_SELECTOR, '#home')
    COORDINATES_BUTTON = (By.CSS_SELECTOR, '#position')
    COLOR_BUTTON = (By.CSS_SELECTOR, '#color')
    SEIZE_BUTTON = (By.CSS_SELECTOR, '#property')
    DISABLED_BUTTON = (By.CSS_SELECTOR, 'button[title="Disabled button"][id="isDisabled"]')
    HOLD_BUTTON = (By.CSS_SELECTOR, 'button[id="isDisabled"][class="button is-primary"]')

    FRUITS_SELECTOR = (By.CSS_SELECTOR, '#fruits')
    NOTIFICATION = (By.CSS_SELECTOR, 'p[class="subtitle"]')
    SUPERHEROES_SELECTOR = (By.CSS_SELECTOR, '#superheros')
    PROG_LANGUAGE_SELECTOR = (By.CSS_SELECTOR, '#lang')
    SELECTIONS_OPTIONS = (By.TAG_NAME, 'option')
    COUNTRY_SELECTOR = (By.CSS_SELECTOR, '#country')
    OPTION_INDIA = (By.CSS_SELECTOR, 'option[value="India"]')

    SIMPLE_ALERT = (By.CSS_SELECTOR, '#accept')
    CONFIRM_ALERT = (By.CSS_SELECTOR, '#confirm')
    PROMPT_ALERT = (By.CSS_SELECTOR, '#prompt')
    PROMPT_NOTIFICATION = (By.CSS_SELECTOR, '#myName')
    SWEET_ALERT = (By.CSS_SELECTOR, '#modern')
    SWEET_ALERT_CONTENT = (By.CSS_SELECTOR, 'p[class="title"]')
    SWEET_ALERT_CLOSE = (By.CSS_SELECTOR, 'button[aria-label="close"]')

    FIRST_FRAME = (By.CSS_SELECTOR, '#firstFr')
    INNER_FRAME = (By.CSS_SELECTOR, "iframe[src='innerFrame']")
    FIRST_NAME = (By.CSS_SELECTOR, 'input[name="fname"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[name="lname"]')
    EMAIL_NAME = (By.CSS_SELECTOR, 'input[name="email"]')
    INPUT_RESULT = (By.CSS_SELECTOR, 'p[class="title has-text-info"]')

    YES_RADIOBUTTON = (By.CSS_SELECTOR, '#yes')
    RADIOBUTTONS = (By.CSS_SELECTOR, 'input[name="one"]')
    ONE_RADIOBUTTON = (By.CSS_SELECTOR, '#one')
    TWO_RADIOBUTTON = (By.CSS_SELECTOR, '#two')
    NOBUG_RADIOBUTTON = (By.CSS_SELECTOR, '#nobug')
    BUG_RADIOBUTTON = (By.CSS_SELECTOR, '#bug')
    BAR_RADIOBUTTON = (By.CSS_SELECTOR, '#notfoo')
    MAYBE_RADIOBUTTON = (By.CSS_SELECTOR, '#maybe')
    REMEMBER_ME_CHECKBOX = (By.XPATH, '/html/body/app-root/app-radio-check/section[1]/div/div/div[1]/div/div/div['
                                      '6]/label[2]/input')
    TERMS_AND_CONDITIONS_CHECKBOX = (By.XPATH, '/html/body/app-root/app-radio-check/section[1]/div/div/div['
                                               '1]/div/div/div[7]/label[2]/input')
