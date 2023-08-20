"""test_delete_first_group"""
from model.group import Group

def test_delete_first_group(app):
    """test_delete_first_group"""
    if app.group.count() == 0:
        app.group.create(Group(name="New group"))
    app.group.delete_first_group()
