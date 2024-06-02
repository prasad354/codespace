def bid_adieu(names):
    if len(names) == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        farewell = ", ".join(names[:-1]) + ", and " + names[-1]
        return f"Adieu, adieu, to {farewell}"

def main():
    print("Enter names (one per line), then press Ctrl-D to bid adieu:")
    names = []
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass
    
    farewell_message = bid_adieu(names)
    print(farewell_message)

if __name__ == "__main__":
    main()
