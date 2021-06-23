from absympla.sympla import ABSympla

ab = ABSympla()
for p in ab.participants.event_participants(event_id=1019432):
    print(p.data)
exit(0)
