from config import app
from controller_functions import landing,my_account,login,login_register,logout,clear_session,register,blog
app.add_url_rule("/", view_func=landing)
app.add_url_rule("/my_account",view_func=my_account)
app.add_url_rule("/logout",view_func=logout)
app.add_url_rule("/login/<flag>",view_func=login,methods=['POST'])
app.add_url_rule("/clear_session",view_func=clear_session)
app.add_url_rule('/register/<flag>',view_func=register,methods=['POST'])
app.add_url_rule('/login_register/<flag>',view_func=login_register)
app.add_url_rule('/blog',view_func=blog)