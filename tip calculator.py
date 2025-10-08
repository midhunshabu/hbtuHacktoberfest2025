def calculate_tip():
    print("💰 Tip Calculator 💰")
    try:
        bill = float(input("Enter the total bill amount: ₹"))
        tip_percent = float(input("Enter tip percentage (e.g., 10 for 10%): "))
        tip = bill * (tip_percent / 100)
        total = bill + tip
        print(f"\nTip Amount: ₹{tip:.2f}")
        print(f"Total Amount (with tip): ₹{total:.2f}")
    except ValueError:
        print("⚠ Please enter valid numbers.")

calculate_tip()
