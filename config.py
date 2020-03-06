import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):    
    CSRF_ENABLED = True
    SECRET_KEY = "youwillneverguess"

    OPENID_PROVIDERS = [
        {"name": "Google", "url": "https://www.google.com/accounts/o8/id"},
        {"name": "Yahoo", "url": "https://me.yahoo.com"},
        {"name": "AOL", "url": "http://openid.aol.com/<username>"},
        {"name": "Flickr", "url": "http://www.flickr.com/<username>"},
        {"name": "MyOpenID", "url": "https://www.myopenid.com"},
    ]

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
    # or "sqlite:///" + os.path.join(basedir, "app.db")
    # SQLALCHEMY_DATABASE_URI = 'mysql://myapp@localhost/myapp'

    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_FOLDER = "translations"
    LANGUAGES = {
        "en": {"flag": "gb", "name": "English"},
        "pt": {"flag": "pt", "name": "Portuguese"},
        "es": {"flag": "es", "name": "Spanish"},
        "de": {"flag": "de", "name": "German"},
        "zh": {"flag": "cn", "name": "Chinese"},
        "ru": {"flag": "ru", "name": "Russian"},
    }

    # ------------------------------
    # GLOBALS FOR GENERAL APP's
    # ------------------------------
    UPLOAD_FOLDER = basedir + "/app/static/uploads/"
    IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"
    IMG_UPLOAD_URL = "/static/uploads/"
    IMG_SIZE = (150, 150, True)
    AUTH_TYPE = 1
    AUTH_ROLE_ADMIN = "Admin"
    AUTH_ROLE_PUBLIC = "Public"
    APP_NAME = "Emily’s MDL1 Class"
    # APP_THEME = ""  # default
    # APP_THEME = "cerulean.css"      # COOL
    # APP_THEME = "cerulean.css"      # COOL
    # APP_THEME = "amelia.css"
    # APP_THEME = "cosmo.css"
    # APP_THEME = "cyborg.css"       # COOL
    APP_THEME = "flatly.css"
    # APP_THEME = "journal.css"
    # APP_THEME = "readable.css"
    # APP_THEME = "simplex.css"
    # APP_THEME = "slate.css"          # COOL
    # APP_THEME = "spacelab.css"      # NICE
    # APP_THEME = "united.css"

    # ----------------------------
    FAB_ROLES = {
        "ReadOnly": [
            ["DoctorModelView", "can_list"],
            ["DoctorModelView", "can_show"],
            ["back", "can_show"],
            ["DoctorModelView", "menu_access"],
            ["DoctorModelView", "can_get"],
            ["DoctorModelView", "can_info"],
            ["UserDBModelView", "can_list"],
            ["UserDBModelView", "can_show"],
            ["UserDBModelView", "menu_access"],
            ["UserDBModelView", "can_get"],
            ["UserDBModelView", "can_info"],
            ["UserDBModelView", "can_info"]
        ]
    }
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
