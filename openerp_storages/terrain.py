from lettuce import world
from lettuce.decorators import step
from lettuceterrain import set_root_url


set_root_url('http://127.0.0.1:8000')

LOGIN_ERP = lambda: """
    Given I access url "<root_url>"
    and I fill the field "username" with "%s"
    and I fill the field "password" with "%s"
    and I click on link "Log in"
""" % (world.current_user, world.current_password)


@step('I\'m located in "(.*)"')
def go_to(step, location):
    """
    Global step to access the external storage tab in OpenERP before running a
    scenario
    """
    step.behave_as(LOGIN_ERP)

    if location == "external storage":
        step.behave_as("""
            Then I click on link "Settings"
            and I click on link "Companies"
            and I click on link "External Storage"
        """)
        # By default, we arrive on tab "AWS S3"
    elif location == "attachment":
        step.behave_as("""
            Then I click on link "Settings"
            and I click on link "Attachments"
        """)
