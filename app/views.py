from flask_appbuilder.charts.views import GroupByChartView
from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import ModelView

from . import appbuilder, db
from .models import Doctor


class DoctorModelView(ModelView):
    datamodel = SQLAInterface(Doctor, db.session)
    list_title = "List Doctors"
    show_title = "Show Doctor"
    add_title = "Add Doctor"
    edit_title = "Edit Doctor"

    # list_widget = ListThumbnail

    label_columns = {
        "photo_img": "Photo",
        "photo_img_thumbnail": "Photo",
    }
    list_columns = [
        "photo_img_thumbnail",
        "name",
        "specialty",
        "location",
        "MDL1_class",
        "email",
    ]

    show_fieldsets = [
        ("Summary", {"fields": ["photo_img", "name", "specialty", 
                    "MDL1_class", "bio",]}),
        (
            "Contact Info",
            {
                "fields": [
                    "email",
                    "work_phone",
                    "personal_phone",
                    "street_address",
                ],
                "expanded": True,
            },
        ),
        (
            "Publications",
            {
                "fields": [
                    "publications",
                ],
                "expanded": True,
            },
        ),
        ("Extra", {"fields": ["notes"], "expanded": False}),
    ]

    add_fieldsets = [
        ("Summary", {"fields": ["name","photo", "specialty","location", 
                    "MDL1_class", "bio",]}),
        (
            "Contact Info",
            {
                "fields": [
                    "email",
                    "work_phone",
                    "personal_phone",
                    "street_address",                    
                ],
                "expanded": True,
            },
        ),
        (
            "Publications",
            {
                "fields": [
                    "publications",
                ],
                "expanded": True,
            },
        ),
        ("Extra", {"fields": ["notes"], "expanded": False}),
    ]

    edit_fieldsets = [
        ("Summary", {"fields": ["name", "photo","specialty","location",
                    "MDL1_class", "bio",]}),
        (
            "Contact Info",
            {
                "fields": [
                    "email",
                    "work_phone",
                    "personal_phone",
                    "street_address",
                ],
                "expanded": True,
            },
        ),
        (
            "Publications",
            {
                "fields": [
                    "publications",
                ],
                "expanded": True,
            },
        ),
        ("Extra", {"fields": ["notes"], "expanded": False}),
    ]





db.create_all()
appbuilder.add_view_no_menu(DoctorModelView())
