from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New group"))
    app.group.modify_first_group(Group(name="Commerce", header="All sales", footer="All sales"))
