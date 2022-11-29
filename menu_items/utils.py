from Cafe_Project.core.db_manager import session
from Cafe_Project.models.menu_items import MenuItems

# print(hello)
def get_menuitems(cat):
    # with app.app_context():
        users = session.query(MenuItems).filter_by(category=cat).all()
        for q in users:
            yield {
                'name':q.name,
                'price':q.price,
                'imgpath':q.imgpath
            }



