from Flask_SQLAlchemy_Project_Template.database import db
from Flask_SQLAlchemy_Project_Template.models import InternalUse


def add_internal_db(browser, stats, com):
    db.session.add(InternalUse(browser_open=browser, statistics=stats, commercials=com))
    db.session.commit()


def list_internal_db():
    internal_table = InternalUse.query.all()
    internal_dict = {}
    for row in internal_table:
        dict_val = 'browser: ' + str(row.browser_open) + ' ' + \
                   'stats: ' + str(row.statistics) + ' ' + \
                   'com: ' + str(row.commercials)
        internal_dict[row.id] = dict_val
        print(row.id, row.browser_open, row.statistics, row.commercials)
    return internal_dict


def internal_counter_db():
    return str(InternalUse.query.count())
