from core.db_manager import session
from models.menu_items import MenuItems


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



