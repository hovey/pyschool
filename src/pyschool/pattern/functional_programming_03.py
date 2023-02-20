def main():
    print("Client data: five examples of client selection, first three valid, second two invalid.")
    choices = ("None", "std", "pca", "something_else", "not_available_option")
    for item in choices:
        print(f"Client logical choice: '{item}'")


    print("\nOriginal Implementation:")
    # process client choices
    for item in choices:
        print(f"Original service processsing client choice: '{item}'")
        if not item == "None":
            if not item == "std" and not item == "pca":
                # raise ValueError("Preprocessing mode must be either 'None', 'std' or 'pca'")
                print("Service will raise a ValueError.")


    print("\nRevised Implementation:")
    options = ("None", "std", "pca")  # make tuple, it is immutable
    for item in choices:
        print(f"Revised service processsing client choice: '{item}'")
        if item not in options:
            # raise ValueError("Preprocessing mode must be either 'None', 'std' or 'pca'")
            print("Service will raise a ValueError.")

if __name__ == "__main__":
    main()
