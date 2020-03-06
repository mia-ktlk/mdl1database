from flask import Markup, url_for
from flask_appbuilder import Model
from flask_appbuilder.filemanager import ImageManager
from flask_appbuilder.models.mixins import ImageColumn
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from flask_appbuilder.models.decorators import renders



class Doctor(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)    
    specialty = Column(String(564))
    street_address = Column(String(564))
    city = Column(String(564))
    state = Column(String(564))
    postal_code = Column(Integer())
    MDL1_class = Column(Date)
    bio = Column(Text())
    photo = Column(ImageColumn(thumbnail_size=(120, 120, True), size=(600, 600, True)))
    personal_phone = Column(String(20))
    email = Column(String(64))
    publications = Column(Text())
    notes = Column(Text())
    work_phone = Column(String(20))

    @renders('address')
    def render_address(self):
        return Markup('<p>'+ self.street_address + '<br>' + self.city + ', ' + self.state + ' ' + str(self.postal_code) + '</p>')

    def photo_img(self):
        im = ImageManager()
        if self.photo:
            return Markup(
                '<a href="' +
                url_for("DoctorModelView.show", pk=str(self.id)) +
                '" class="thumbnail"><img src="' +
                im.get_url(self.photo) +
                '" alt="Photo" class="img-rounded img-responsive"></a>'
            )
        else:
            return Markup(
                '<a href="' +
                url_for("DoctorModelView.show", pk=str(self.id)) +
                '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive">'
                '</a>'
            )

    def photo_img_thumbnail(self):
        im = ImageManager()
        if self.photo:
            return Markup(
                '<a href="' +
                url_for("DoctorModelView.show", pk=str(self.id)) +
                '" class="thumbnail"><img src="' +
                im.get_url_thumbnail(self.photo) +
                '" alt="Photo" class="img-rounded img-responsive"></a>'
            )
        else:
            return Markup(
                '<a href="' +
                url_for("DoctorModelView.show", pk=str(self.id)) +
                '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive">'
                '</a>'
            )

# class Publication(Model):
#     id = Column(Integer, primary_key=True)
#     title = Column(String(150), unique=True, nullable=False)
#     journal = Column(String(564)) 
#     author_id = Column(Integer, ForeignKey('doctor.id'), nullable=False))
#     author = relationship("Author")
#     date = Column(Date)
#     url = Column(String(564))

#     @renders("url")
#     def render_url(self):
#         return Markup('<a href="' + url + '" target="_blank" >' + "Go to link" + "</a>")

#     def __repr__(self):
#         return self.name