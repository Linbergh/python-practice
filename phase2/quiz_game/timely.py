import datetime as dt


def get_time():
    return dt.datetime.now()


start = get_time()
print(f"Time started at {start}")
while True:
    choice = input("> ")

    if choice == "logout":
        break

end = get_time()
print(f"Time stoped at {end}")
print(f"You were online for {end - start}")
