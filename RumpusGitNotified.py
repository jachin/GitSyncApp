import rumps

class RumpusGitNotified:

    def __init__(self):
        self

    def sync_failed(self):
        rumps.notification("GitSync", "Sync Failed", 'Sorry.')

    def sync_start(self, local_path, remote_path, remote_host):
        rumps.notification(
            "GitSync",
            "Starting",
            "Syncing %s and %s on %s" % (
                local_path,
                remote_path,
                remote_host,
            )
        )

    def sync_done(self, local_path, remote_path, remote_host):
        rumps.notification(
            "GitSync",
            "Completed",
            "Sync of %s and %s on %s" % (
                local_path,
                remote_path,
                remote_host,
            )
        )
