from absympla.sympla import ABSympla

ab = ABSympla()

event_id = 1019432

for order in ab.orders.event_orders(event_id=event_id):

    for participant in ab.orders.order_participants(event_id=event_id, order_id=order.id):
        for form in participant.custom_form:
            print(form)
        break
    break

exit(0)
