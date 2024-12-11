from app import db

# Основна модель "Телефони"
class Phone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Назва телефону
    description = db.Column(db.Text, nullable=False)  # Опис
    price = db.Column(db.Float, nullable=False)  # Ціна
    added_by = db.Column(db.String(255), nullable=True)

    # Зв'язок з категорією
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref='phones')


# Додаткова модель "Категорії"
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), nullable=False)  # Назва категорії (наприклад смартфони, планшети)


