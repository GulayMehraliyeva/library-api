
def is_book_available(book):
    return book is not None and bool(book["available"])


def has_unpaid_fines(amount_owed):
    return amount_owed > 0


def has_reached_loan_limit(open_loans, limit):
    return open_loans >= limit


def is_loan_returned(loan):
    return bool(loan["returned"])


def is_loan_overdue(loan, days_late):
    return not is_loan_returned(loan) and days_late > 0


def has_exceeded_renewal_limit(loan, max_renewals):
    return loan["renewals"] >= max_renewals


def has_fine_to_pay(loan):
    return loan["fine"] > 0 and not bool(loan["fine_paid"])
