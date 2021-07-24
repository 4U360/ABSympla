from absympla.sympla import ABSympla

ab = ABSympla()
#print(ab.events.get_event(event_id=1019432).data)
#exit(0)
for event in ab.events.list_events():
    print(event.name)