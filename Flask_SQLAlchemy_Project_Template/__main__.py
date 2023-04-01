"""__main__.py, run the module $ python -m Flask_SQLAlchemy_Project_Template """

import sys
from os import path
this_dir = path.abspath(path.join(path.dirname("__file__")))
# get root of app, rip off one subdir ... go up
app_root = path.dirname(this_dir)
sys.path.append(path.abspath(app_root))
sys.path.append(path.abspath(this_dir))

from Flask_SQLAlchemy_Project_Template import create_app, setup_database, db_path

port = 5050
if __name__ == "__main__":
    app_factory = create_app(port=port)
    # do not kill db, if exists
    if not path.isfile(db_path):
        setup_database(app_factory)

    # print(app_factory.config)
    app_factory.run(host='localhost', port=port)
