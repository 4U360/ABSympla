from absympla.sympla import ABSympla

ab = ABSympla()

for request in ab.requests.event_requests(event_id=1019432):
    print(request.invoice_info)

exit(0)
