from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user

from functions import app
from models import User


@app.route('/community', methods=['GET'])
def community():

    login_user(User.query.get(1))

    newest_users = User.get_five_newest_users()


    args = {
            'gift_card_eligible': True,
            'cashout_ok': True,
            'user_below_silver': current_user.is_below_tier('Silver'),
            'table_data': newest_users
    }
    return render_template("community.html", **args)

