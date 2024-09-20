from flask import Blueprint, render_template
import plugin.tools as tools

admin_route = Blueprint('admin', __name__)

# test
@admin_route.route('/test', methods=['GET'])
def test():
    return tools.to_json()
