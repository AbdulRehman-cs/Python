import qrcode

def generate_qr(data, filename="qrcode.png"):
    img = qrcode.make(data)
    img.save(filename)
    print(f"QR Code saved as {filename}")
    img.show()

if __name__ == "__main__":
    user_input = input("Enter the data or URL for the QR code: ")
    generate_qr(user_input)
