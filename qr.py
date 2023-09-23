# Retrieve QR code data for a specific patient (replace with actual patient ID)
patient_id_to_retrieve = "12345"
patient_qr_data = db.qrcodes.find_one({"patient_id": patient_id_to_retrieve})

if patient_qr_data:
    img_data = patient_qr_data["qr_code_image"]

    # Generate dynamic HTML
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>QR Code Display</title>
    </head>
    <body>
        <h1>QR Code Display</h1>
        <p>Scan the QR code below:</p>
        <img src="data:image/png;base64,{img_data.decode('utf-8')}" alt="QR Code">
    </body>
    </html>
    """

    # Write HTML to a file
    with open("qrcode_display.html", "w") as html_file:
        html_file.write(html_content)

    print("HTML file generated.")
else:
    print("Patient not found.")