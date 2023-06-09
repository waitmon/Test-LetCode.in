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

    DRAG_BOX = (By.CSS_SELECTOR, '#sample-box')
    CONTAINER_BOX = (By.CSS_SELECTOR, '[class="example-boundary"]')

    DRAG_BOX_SOURCE = (By.CSS_SELECTOR, '[id="draggable"]')
    DROP_BOX_TARGET = (By.CSS_SELECTOR, '[id="droppable"]')
    
    TO_DO_TASK = (By.XPATH, "//div[text()=' Fall asleep']")
    DONE_TASK = (By.XPATH, "//div[text()=' Walk dog']")
    TASK_LIST = (By.CSS_SELECTOR, '#cdk-drop-list-1')

    SELECTABLE_OPTION = (By.CSS_SELECTOR, '#selectable')

    SLIDER = (By.CSS_SELECTOR, '#generate')
    GET_COUNTRIES_BUTTON = (By.CSS_SELECTOR, '[class="button is-primary"]')
    LIMIT_COUNTER = (By.CSS_SELECTOR, 'h1[class="subtitle has-text-info"]')
    COUNTRY_LIST = (By.CSS_SELECTOR, '[class="has-text-primary-light"]')

    CALORIES_SORT_HEADER = (By.CSS_SELECTOR, 'div[class="mat-sort-header-content ng-tns-c30-1"]')
    CALORIES_LIST = (By.XPATH, "//label[text()='Sortable Tables']/following-sibling::table//tr/td[2]")

    UNIVERSITY_LIST = (By.XPATH, "//table[@id='advancedtable']/tbody/tr/td[2]")
    SHOW_ENTRIES = (By.CSS_SELECTOR, 'select[name="advancedtable_length"]')
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[type="search"]')
    SEARCH_RESULT = (By.XPATH, '//*[@id="advancedtable"]/tbody/tr/td[2]')
    SERIAL_NUMBER_LIST = (By.XPATH, "//table[@id='advancedtable']/tbody/tr/td[1]")
    NEXT_PAGE = (By.XPATH, '//*[@id="advancedtable_next"]')

    FIRST_NAME_FORM = (By.CSS_SELECTOR, '#firstname')
    LAST_NAME_FORM = (By.CSS_SELECTOR, '#lasttname')
    EMAIL_FORM = (By.CSS_SELECTOR, '#email')
    PHONE_NUMBER_FORM = (By.CSS_SELECTOR, '#Phno')
    ADDRESS_LINE_1_FORM = (By.CSS_SELECTOR, '#Addl1')
    ADDRESS_LINE_2_FORM = (By.CSS_SELECTOR, '#Addl2')
    STATE_FORM = (By.CSS_SELECTOR, '#state')
    POSTAL_CODE_FORM = (By.CSS_SELECTOR, '#postalcode')
    GENDER_LIST_FORM = (By.CSS_SELECTOR, 'input[type="radio"][name="gender"]')
    TERMS_CHECKBOX_FORM = (By.XPATH, '/html/body/app-root/app-forms/section[1]/div/div/div[1]/div/div/form/div['
                                     '7]/div/label/input')
    DATE_OF_BIRTH = (By.CSS_SELECTOR, 'input[type="date"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')

    DOWNLOAD_XLS = (By.CSS_SELECTOR, '#xls')
    DOWNLOAD_PDF = (By.CSS_SELECTOR, '#pdf')
    DOWNLOAD_TXT = (By.CSS_SELECTOR, '#txt')
