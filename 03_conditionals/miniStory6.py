seat_type = input("Enter seat type(sleeper/AC/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print(f"Sleeper - No AC, beds available")
    case "ac":
        print(f"AC - air conditioned, comfy ride")
    case "general":
        print(f"General - Cheapest option, no reservation")
    case "luxury":
        print(f"Luxury - premium seats with meal included")
    case _:
        print(f"Invalid seat type")