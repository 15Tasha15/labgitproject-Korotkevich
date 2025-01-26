# main.py


from src.utils import add_numbers, multiply_numbers

def main():
    # Использование функции add_numbers
    a, b = 5, 3
    sum_result = add_numbers(a, b)
    print(f"The sum of {a} and {b} is: {sum_result}")

    # Использование функции multiply_numbers
    product_result = multiply_numbers(a, b)
    print(f"The product of {a} and {b} is: {product_result}")

if __name__ == "__main__":
    main()