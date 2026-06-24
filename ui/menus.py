from data.assistants import assistant_types
def get_assistant_type():

    print("\n" + "=" * 50)
    print("AVAILABLE ASSISTANTS")
    print("=" * 50)

    for key, assistant in assistant_types.items():
        print(f"\n{key}. {assistant['name']}")
        print(f"   {assistant['description']}")

    while True:

        choice = input(
            "\nChoose assistant type: "
        ).strip()

        if choice in assistant_types:

            selected = assistant_types[choice]

            print("\nSelected:")
            print(f"{selected['name']}")
            print(f"{selected['description']}")

            return selected

        print("Invalid selection. Try again.")




def get_temperature():

    print("\n" + "=" * 50)
    print("TEMPERATURE GUIDE")
    print("=" * 50)

    print("0.0 - 0.3  -> Deterministic")
    print("0.4 - 0.8  -> Balanced")
    print("0.9 - 1.5  -> Creative")
    print("1.6 - 2.0  -> Highly Random")

    while True:

        try:

            temp = float(
                input("\nEnter temperature (0-2): ")
            )

            if 0 <= temp <= 2:

                print(
                    f"Temperature set to: {temp}"
                )

                return temp

            print(
                "Temperature must be between 0 and 2."
            )

        except ValueError:

            print(
                "Please enter a valid number."
            )

