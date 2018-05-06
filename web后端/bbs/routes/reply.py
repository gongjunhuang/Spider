from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)

from routes.index import current_user

from models.reply import Reply


main = Blueprint('reply', __name__)


@main.route("/add", methods=["POST"])
def add():
    form = request.form
    u = current_user()
    print('DEBUG', form)
    m = Reply.new(form, user_id=u.id)
    return redirect(url_for('topic.detail', id=m.topic_id))

