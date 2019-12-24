from app import create_app, db, logger
from app.models import User
app = create_app()

logger.info("服务开启...")


@app.shell_context_processor
def make_shell_contextt():
    return {'db': db, 'User': User}
