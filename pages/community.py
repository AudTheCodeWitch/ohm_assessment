from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user

from functions import app
from models import User


@app.route('/community', methods=['GET'])
def community():

    login_user(User.query.get(1))

    # I haven't figured out how connect to MySQL, so I'm using dummy data for the time being
    # topfive = conn.execute("SELECT display_name, tier, point_balance FROM user ORDER BY create_time DESC LIMIT 2;")
    newest_users = [
        {"display_name": "Justin Bieber",
         "tier": "Silver",
         "point_balance": 0
         },
        {"display_name": "Elvis Presley",
         "tier": "Carbon",
         "point_balance": 0
         },
        {"display_name": "Chuck Norris",
         "tier": "Carbon",
         "point_balance": 5000
         },
        {"display_name": "Rachel Carson",
         "tier": "Platinum",
         "point_balance": 12000
         },
        {"display_name": "Jane Goodall",
         "tier": "Gold",
         "point_balance": 8000
         }
    ]

    args = {
            'gift_card_eligible': True,
            'cashout_ok': True,
            'user_below_silver': current_user.is_below_tier('Silver'),
            'table_data': newest_users
    }
    return render_template("community.html", **args)

