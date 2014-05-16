import rumps
import yaml
import logging

default_config = """
targets:
 jachin0.amm.dev
 jachin1.amm.dev
"""


def load_config():
    config = yaml.safe_load(default_config)
    return config


class GitSyncApp(rumps.App):
    def __init__(self):
        super(GitSyncApp, self).__init__("GitSync")

        config = load_config()

        menu_items = ["Preferences", "Silly button", "Say hi"]

        logger.info(menu_items)

        # for target in config['targets']:
        #     menu_items.append(target)

        self.menu = menu_items

    @rumps.clicked("Preferences")
    def prefs(self, _):
        rumps.alert("jk! no preferences available!")

    @rumps.clicked("Silly button")
    def onoff(self, sender):
        sender.state = not sender.state

    @rumps.clicked("Say hi")
    def sayhi(self, _):
        logger.info("hi!")
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")

if __name__ == "__main__":
    logger = logging.getLogger('GitSyncApp')
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    GitSyncApp().run()
