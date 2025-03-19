print("What tinmes did you run in the 110 hurdles each meet? \n")

times = []

while True:
    time = input("Enter your times (type 'done' whne you have completed all times): ")

    if time == "done":
        break

    times.append(time)
    print(f"{time.lower()} has been added to your time list")

    if times:
        print("\n These are your Times from all the meets this year:")

        for time in times:
            print(f"~ {time.title()}")

    else:
        print("You have had no meets yet this year")