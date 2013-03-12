from twill.commands import get_browser
from lettuce import world
from lettuce.decorators import step
from lettuce.terrain import before
from lettuceterrain import set_root_url, click_link


set_root_url('http://127.0.0.1:8000')


@step("I'm located in the external storage tag in OpenERP")
def go_to_external_storage(step):
    """
    Global step to access the external storage tab in OpenERP before running a
    scenario
    """
    step.behave_as("""
        Given I access url "<root_url>"
        and I click on link "Settings"
        and I click on link "Companies"
        and I click on link "External Storage"
    """
    # By default, we arrive on tab "AWS S3"


