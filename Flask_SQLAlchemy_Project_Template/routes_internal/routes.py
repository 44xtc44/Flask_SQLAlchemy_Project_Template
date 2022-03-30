from flask import Blueprint, render_template
import Flask_SQLAlchemy_Project_Template.routes_internal.routes_support as irs

# Blueprint Configuration
internal_bp = Blueprint(
    'internal_bp', __name__,
    template_folder='internal_templates',
    static_folder='internal_static',
    static_url_path='/internal_static'
)


@internal_bp.route('/internal', methods=['GET'])
def internal():
    irs.add_internal_db(0, 67.4, "offer")
    irs.add_internal_db(1, None, "bid")

    internal_dict = irs.list_internal_db()
    html_internal_list = []
    for dict_val in internal_dict.values():
        html_internal_list.append(dict_val)
    internal_counter = irs.internal_counter_db()
    return render_template('internal_bp_content.html', table_dump=html_internal_list, counter=internal_counter)
