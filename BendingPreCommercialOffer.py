from datetime import datetime, date


def name_offer(customer_name: str) -> str:
    this_moment_list = str(datetime.now()).split(" ")
    today = this_moment_list[0].split("-")[::-1]
    this_time = this_moment_list[1].split(":")[:2]
    return f"{customer_name}_({this_time[0]} {this_time[1]})_{today[0]}.{today[1]}.{today[2]}.xlsx"



name_offer("fdsfsd")

