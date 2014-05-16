import rumps
import yaml
import logging
import os.path
import os

from RumpusGitNotified import RumpusGitNotified
from gitsync.GitSync import GitSync

default_config = {
    'targets': {}
}

def get_config():

    config = {
        'targets': {}
    }

    user_config_path = os.path.expanduser("~/.GitSync")
    if not os.path.isdir(user_config_path):
        os.makedirs(user_config_path)

    for root, dirs, files in os.walk(user_config_path):
        logger.info(files)
        for f in files:
            (root, ext) = os.path.splitext(f)
            if ext == '.yaml':
                stream = open(os.path.join(user_config_path, f), 'r')
                target = yaml.safe_load(stream)
                logger.info(target)
                config['targets'][target['name']] = target


    return config


class GitSyncApp(rumps.App):

    def __init__(self):
        super(GitSyncApp, self).__init__("GitSync", icon='Icon.png')

        config = get_config()

        # None menu items are dividers
        menu_items = ["Help", None, ]

        self.targets = config['targets']
        self.syncs = {}

        for name, target in config['targets'].items():
            menu_items.append(
                rumps.MenuItem(name, callback=self.toggle_sync)
            )

        menu_items.append(None)

        self.menu = menu_items

    @rumps.clicked("Help")
    def prefs(self, _):
        rumps.alert("Talk to Jachin.")

    def toggle_sync(self, sender):
        sender.state = not sender.state

        if not sender.title in self.syncs:
            config = self.targets[sender.title]
            notifier = RumpusGitNotified()
            self.syncs[sender.title] = GitSync(config, notifier)

        git_sync = self.syncs[sender.title]

        if sender.state:
            git_sync.start()
        else:
            git_sync.stop()

    # @rumps.clicked("Silly button")
    # def onoff(self, sender):
    #     sender.state = not sender.state

    # @rumps.clicked("Say hi")
    # def sayhi(self, _):
    #     logger.info("hi!")
    #     rumps.notification(
    #         "Awesome title",
    #         "amazing subtitle",
    #         "hi!!1",
    #         sound=False
    #     )

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
