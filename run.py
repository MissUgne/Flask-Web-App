from myblog import app
from myblog import db
from myblog.models import User, Post, File, Image
from flask_admin import Admin
from myblog.models import ImageView, PostView, FileView, ModelView, MyAdminIndexView


admin = Admin(app, name='Admin', template_mode='bootstrap3', index_view=MyAdminIndexView())
admin.add_view(ModelView(User, db.session))
admin.add_view(FileView(File, db.session))
admin.add_view(ImageView(Image, db.session))
admin.add_view(PostView(Post, db.session))


if __name__ == '__main__':
    app.run()
