from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    """ Landing page of website (https://www.galaxycine.vn/) """
    # TODO: To be implemented
    return HttpResponse("Homepage")


def buy_ticket(request):
    """ Page for buying ticket (https://www.galaxycine.vn/lich-chieu) """
    # TODO: To be implemented
    # TODO: Split buying tickets based on movie and based on theater?
    pass


def list_movie_on_air(request):
    """ Display movies that are (or are going to be) on air (https://www.galaxycine.vn/phim-dang-chieu) """
    # TODO: To be implemented
    pass


def list_movie_coming_soon(request):
    """ Display movies that are coming soon (https://www.galaxycine.vn/phim-sap-chieu/) """
    # TODO: To be implemented
    pass


def movie_details(request):
    """ Display movie's details (https://www.galaxycine.vn/dat-ve/captain-marvel) """
    # TODO: To be implemented
    pass


def faqs(request):
    """ Frequent Asked Questions """
    # TODO: To be implemented
    pass


def events_and_promos(request):
    """ Display activate events and promotions """
    # TODO: To be implemented
    pass


def event_promo_details(request):
    """ Display event or promotion's details """
    # TODO: To be implemented
    pass


""" Customer's account related views """
def account_login(request):
    """ Login account """
    # TODO: To be implemented
    pass


def account_signup(request):
    """ Signup account """
    # TODO: To be implemented
    pass


def account_info(request):
    """ Display account information (https://www.galaxycine.vn/thanh-vien) """
    # TODO: To be implemented
    pass


def account_history(request):
    """ Display history transactions (https://www.galaxycine.vn/thanh-vien) """
    # TODO: To be implemented
    pass

