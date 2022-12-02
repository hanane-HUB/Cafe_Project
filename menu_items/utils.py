from core.db_manager import session
from models.menu_items import MenuItems
from models.receipts import Receipt


def get_menuitems(cat):
    # with app.app_context():
        users = session.query(MenuItems).filter_by(category=cat).all()
        for q in users:
            yield {
                'id':q.id,
                'name':q.name,
                'price':q.price,
                'imgpath':q.imgpath
            }


def get_item():
    return session.query(MenuItems).all()


def add_item(name, price, cat, img):
    item = MenuItems(name=name, price=price, cat=cat, img=img)
    session.add(item)
    session.commit()