from absympla.sympla import ABSympla
from requests.exceptions import HTTPError

ab = ABSympla()
for event in ab.events.list_events():
    try:
        for p in ab.affiliates.event_affiliates(event_id=event.id):
            print(p)
    except HTTPError as er:
        print(er.response.json())
exit(0)
