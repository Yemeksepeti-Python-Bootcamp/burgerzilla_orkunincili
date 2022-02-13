def load_data(obj:object):
    from app.models.serializers import ProductSchema
    product_schema = ProductSchema()
    product = product_schema.dump(obj)
    return product
