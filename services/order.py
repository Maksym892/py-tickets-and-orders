from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import QuerySet
from db.models import Order, Ticket

from django.db import transaction
from db.models import Order, Ticket
from services.user import get_user  # <-- Додаємо імпорт функції


@transaction.atomic
def create_order(tickets: list[dict], user_id: int = None, username: str = None, date: str = None) -> Order:
    # Замінюємо прямий запит User.objects.get(...) на виклик функції
    user = get_user(user_id) if user_id else get_user(
        username)  # Або просто get_user(user_id), залежно від твоїх параметрів

    order = Order.objects.create(user=user)

    if date:
        order.created_at = date
        order.save()

    for ticket_data in tickets:
        Ticket.objects.create(
            row=ticket_data["row"],
            seat=ticket_data["seat"],
            movie_session_id=ticket_data["movie_session"],
            order=order
        )

    return order


def get_orders(username: str = None) -> QuerySet:
    if username:
        return Order.objects.filter(user__username=username)
    return Order.objects.all()
