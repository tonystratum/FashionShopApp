from PIL import Image
import os

basepath = os.path.abspath("fashionshop/static/img/product/Fragrance")


# os.chdir(basepath)
def save_img(img):
    i = Image.open(os.path.join(basepath, img))
    t, f_ext = os.path.splitext(i.filename)
    text = t.replace("-", " ")
    f = text + f_ext
    print('infor:', img, i.format, i.size, i.mode)
    if i.mode == 'RGBA':
        i = i.convert('RGB')
    output = (264, 363)
    i.thumbnail(output, Image.ANTIALIAS)
    # i = i.resize(output, Image.ANTIALIAS)
    i.save(f, "JPEG")
    print('infor changed:', img, i.format, i.size, i.mode)
    pass


for img in os.listdir(basepath):
    save_img(img)


def resultproxy_to_dict(resultproxy):
    """
    Converts SQLAlchemy.engine.result.ResultProxy to a list of rows,
    represented as dicts.
    :param resultproxy: SQLAlchemy.engine.result.ResultProxy
    :return: rows as dicts.
    """
    d, a = {}, []
    for rowproxy in resultproxy:
        # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
        for column, value in rowproxy.items():
            # build up the dictionary
            d = {**d, **{column: value}}
        a.append(d)

    return a


def query_to_dict(db, query):
    """
    Wrapper for raw SQL to dict execution.
    :param db: db object from fashionshop.
    :param query: raw SQL string.
    :return: rows as dicts.
    """
    return resultproxy_to_dict(db.engine.execute(query))
