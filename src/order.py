# 示例：使用 Requests 预定门票
booking_url = 'https://your_booking_url_here'
ticket_details = {'concert_id': '123', 'number_of_tickets': 2}
booking_response = session.post(booking_url, data=ticket_details)
