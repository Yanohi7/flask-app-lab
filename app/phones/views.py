from flask import render_template, request, redirect, url_for, flash, session
from . import phones_bp
from .models import Phone, Category
from app import db
from .forms import PhoneForm

# Головна сторінка з телефонами
@phones_bp.route('/')
def phone_list():
    # Доступні поля для сортування
    sort_options = {
        'price': Phone.price,
        'name': Phone.name,
    }
    sort_by = request.args.get('sort_by', 'price')  # За замовчуванням сортуємо за ціною
    order = request.args.get('order', 'asc')  # Напрямок сортування

    sort_column = sort_options.get(sort_by, Phone.price)

    # Сортуємо за вибраним напрямком
    if order == 'asc':
        phones = Phone.query.order_by(sort_column).all()
    else:
        phones = Phone.query.order_by(db.desc(sort_column)).all()

    categories = Category.query.all()  # Завантажуємо всі категорії
    return render_template('phone_list.html', phones=phones, categories=categories, sort_by=sort_by, order=order)



@phones_bp.route('/search', methods=['GET', 'POST'])
def search_phone():
    if request.method == 'POST':
        search_query = request.form.get('search', '').strip()  # Пошуковий запит
        category_id = request.form.get('category')  # Вибрана категорія

        # Початковий запит
        query = Phone.query

        # Фільтруємо за назвою, якщо пошук не порожній
        if search_query:
            query = query.filter(Phone.name.ilike(f'%{search_query}%'))

        # Фільтруємо за категорією, якщо вона вибрана
        if category_id:
            query = query.filter(Phone.category_id == category_id)

        phones = query.all()  # Виконання запиту
        categories = Category.query.all()  # Завантажуємо всі категорії

        return render_template('phone_list.html', phones=phones, categories=categories)

    return redirect(url_for('phones.phone_list'))


@phones_bp.route('/<int:id>')
def phone_detail(id):
    phone = db.get_or_404(Phone, id)
    return render_template('phone_detail.html', phone=phone)


# Додавання нового телефону
@phones_bp.route('/add_phone', methods=['GET', 'POST'])
def add_phone():
    form = PhoneForm()
    form.load_categories()  # Завантажуємо категорії з БД

    if form.validate_on_submit():
        # Створюємо новий об'єкт Phone
        new_phone = Phone(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            category_id=form.category.data,  # Вибрана категорія
            added_by = session.get('username')
        )
        db.session.add(new_phone)
        db.session.commit()

        flash('Телефон успішно додано!', 'success')
        return redirect(url_for('phones.phone_list'))

    return render_template('add_phone.html', form=form)

@phones_bp.route('/edit_phone/<int:id>', methods=['GET', 'POST'])
def edit_phone(id):
    phone = db.get_or_404(Phone, id)  # Отримання телефону з БД або 404
    form = PhoneForm(obj=phone)  # Заповнення форми існуючими даними
    form.load_categories()  # Завантаження категорій з БД

    if form.validate_on_submit():
        phone.name = form.name.data
        phone.description = form.description.data
        phone.price = form.price.data
        phone.category_id = form.category.data  # Оновлення категорії
        db.session.commit()  # Збереження змін
        flash('Телефон успішно відредаговано!', 'success')
        return redirect(url_for('phones.phone_list'))

    return render_template('edit_phone.html', form=form, phone=phone)

@phones_bp.route('/delete_phone/<int:id>', methods=['GET', 'POST'])
def delete_phone(id):
    phone = db.get_or_404(Phone, id)
    db.session.delete(phone)
    db.session.commit()
    return redirect(url_for('phones.phone_list'))