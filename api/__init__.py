from app import app


## API Routes ##
from api.blueprints.users.views import users_api_blueprint
app.register_blueprint(users_api_blueprint, url_prefix='/api/v1/users')

from api.blueprints.login.views import login_api_blueprint
app.register_blueprint(login_api_blueprint, url_prefix='/api/v1/auth')