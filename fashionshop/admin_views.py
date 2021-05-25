from flask import redirect, url_for
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class MyModelView(ModelView):
    """Only admin can see"""

    # column_filters = ['id']

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            # return self.render('login.html')
            return redirect(url_for('home'))


class DashboardView(AdminIndexView):

    def is_visible(self):
        # This view won't appear in the menu structure
        return False

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            # return self.render('login.html')
            return redirect(url_for('home'))
