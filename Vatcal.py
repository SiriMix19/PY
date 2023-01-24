def calculate_total_price(price, vat_percentage):
    vat = price * vat_percentage / 100
    return price + vat

def main():
    price = 100
    vat_percentage = 7
    total_price = calculate_total_price(price, vat_percentage)
    print("Total price: ", total_price)

if __name__ == "__main__":
    main()
