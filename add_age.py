def main():
    try:
        age_str = input("Enter your age: ").strip()
        age = int(age_str)
    except ValueError:
        print("Invalid input — please enter a whole number for age.")
        return

    total_age = age + 20
    print(f"Total age after adding 20: {total_age}")


if __name__ == "__main__":
    main()
