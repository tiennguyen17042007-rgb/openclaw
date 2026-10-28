import json
import os

FILE = "products.json"


def load_products():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_products(products):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)


def main():
    products = load_products()

    while True:
        print("\n===== SALE OFF =====")
        print("1. Them san pham")
        print("2. Xem danh sach")
        print("3. Tim san pham")
        print("0. Thoat")

        choice = input("Chon chuc nang: ")

        if choice == "1":
            name = input("Ten san pham: ")
            price = float(input("Gia goc: "))
            discount = float(input("Phan tram giam gia: "))

            final_price = price * (100 - discount) / 100

            products.append({
                "name": name,
                "price": price,
                "discount": discount,
                "final_price": final_price
            })

            save_products(products)
            print("Da them san pham!")

        elif choice == "2":
            if not products:
                print("Chua co san pham.")
            for p in products:
                print(
                    p["name"],
                    "- Gia goc:", p["price"],
                    "- Giam:", str(p["discount"]) + "%",
                    "- Con:", round(p["final_price"], 2)
                )

        elif choice == "3":
            keyword = input("Nhap ten can tim: ").lower()
            for p in products:
                if keyword in p["name"].lower():
                    print(p)

        elif choice == "0":
            break

        else:
            print("Lua chon khong hop le.")


if __name__ == "__main__":
    main()
