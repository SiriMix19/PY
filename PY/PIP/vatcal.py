def cal_total_price(price, vat_percent):
    vat = price * vat_percent / 100
    t_price = price + vat
    return vat, t_price


def main():
    price = 100
    vat_percent = 7
    vat, t_price = cal_total_price(price, vat_percent)
    print("Vat 7%: ", vat, "บาท")
    print("เงินที่ต้องจ่าย: ", t_price, "บาท")


if __name__ == "__main__":
    main()
