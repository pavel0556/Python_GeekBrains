def lucky_ticket (ticket_number):
    left = 0
    rigt = 0
    res = "Выигрыш"
    if (len(str(ticket_number)))== 6:
        for digit in str(ticket_number)[0:3:1]:
            left = left + int(digit)
            for digit in str(ticket_number)[3:6:1]:
                rigt = rigt + int(digit)
    if (left == rigt) and ((left != 0) or (rigt != 0)):
        res = "Выигрыш"
    return res



print(lucky_ticket(1231238))



