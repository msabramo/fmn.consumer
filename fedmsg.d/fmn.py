import socket
hostname = socket.gethostname().split('.')[-1]


config = {
    # Consumer stuff
    "fmn.consumer.enabled": True,
    "fmn.sqlalchemy.uri": "sqlite:////var/tmp/fmn-dev-db.sqlite",
    "fmn.autocreate": True,  # Should new packagers auto-get accounts?

    # Some configuration for the rule processors
    "fmn.rules.utils.use_pkgdb2": False,
    "fmn.rules.utils.pkgdb2_api_url": "http://209.132.184.188/api/",
    "fmn.rules.cache": {
        "backend": "dogpile.cache.dbm",
        "expiration_time": 300,
        "arguments": {
            "filename": "/var/tmp/fmn-cache.dbm",
        },
    },

    # Colors:
    "irc_color_lookup": {
        "fas": "light blue",
        "bodhi": "green",
        "git": "red",
        "tagger": "brown",
        "wiki": "purple",
        "logger": "orange",
        "pkgdb": "teal",
        "buildsys": "yellow",
        "planet": "light green",
        "fmn": "purple",
    },

    ## Backend stuff ##

    # This is the list of enabled backends (so we can turn one off globally)
    #"fmn.backends": ['email', 'irc', 'android'],
    "fmn.backends": ['email', 'irc'],

    # Email
    "fmn.email.mailserver": "127.0.0.1:25",
    "fmn.email.from_address": "notifications@fedoraproject.org",

    # IRC
    "fmn.irc.network": "irc.freenode.net",
    "fmn.irc.nickname": "threebot",
    "fmn.irc.port": 6667,
    "fmn.irc.timeout": 120,

    # GCM - Android notifs
    "fmn.gcm.post_url": "wat",
    "fmn.gcm.api_key": "wat",

    # Confirmation urls:
    "fmn.base_url": "http://localhost:5000/",
    "fmn.acceptance_url": "http://localhost:5000/confirm/accept/{secret}",
    "fmn.rejection_url": "http://localhost:5000/confirm/reject/{secret}",
    "fmn.support_email": "notifications@fedoraproject.org",

    # Generic stuff
    "endpoints": {
        "fmn.%s" % hostname: [
            "tcp://127.0.0.1:3041",
            "tcp://127.0.0.1:3042",
        ],
    },
    "logging": dict(
        loggers=dict(
            fmn={
                "level": "DEBUG",
                "propagate": False,
                "handlers": ["console"],
            },
        ),
    ),
}
