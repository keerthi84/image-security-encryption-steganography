# image-security-encryption-steganography
Secure image transmission using AES-256 encryption and LSB steganography with performance analysis
# 🔐 Image Encryption & Steganography (AES-256 + LSB)

## 📌 Overview

This project implements a secure image transmission system using **AES-256 encryption** and **LSB (Least Significant Bit) steganography**.
It ensures both **data confidentiality** and **hidden communication**, protecting sensitive information from unauthorised access.

---

## 🛠️ Tools & Technologies
* Python
* AES-256 Encryption (CBC Mode)
* LSB Steganography
* PyCryptodome / OpenCV / PIL
* Kali Linux / Windows

---

## ⚙️ Methodology

The system follows a dual-layer security approach:

1. Encrypt the secret image using AES-256 (CBC mode)  
2. Embed the encrypted image into a cover image using LSB steganography  
3. Generate the stego image  
4. Extract hidden data from the stego image  
5. Decrypt to recover the original image  
---

## 📊 Results & Analysis

- Achieved **high image quality** after embedding  
- **PSNR up to 58.66 dB**, indicating minimal distortion  
- Histogram analysis shows that encrypted images behave like noise, enhancing security  
- Ensured secure data transmission with minimal visual impact  

---

## 📊 Key Features

* 🔒 Dual-layer security (Encryption + Steganography)
* 🖼️ Secure image-based data hiding
* 🔑 Strong encryption using AES-256
* 📉 Minimal distortion in the output image
* 🛡️ Protection against unauthorised access
* 📈 Performance evaluated using PSNR and histogram analysis

---

## 📁 Project Structure

```
image-security-encryption-steganography/
│
├── encryption.py
├── steganography.py
├── Encryption_Steganography_Report.pdf
├── README.md
│
└── images/
    ├── stego_output.png
    ├── extracted_image.png
    ├── encryption_output.png
    ├── histogram.png
    └── psnr_graph.png
```

---

## 📸 Results (Screenshots)

### 🔹 Stego Image Output

![Stego Output](images/stego_output.png)

### 🔹 Extracted Image

![Extracted Image](images/extracted_image.png)

### 🔹 Encryption Output

![Encryption Output](images/encryption_output.png)

### 🔹 Histogram Analysis

![Histogram](images/histogram.png)

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/yourusername/image-security-encryption-steganography.git
```

2. Navigate to project folder:

```
cd image-security-encryption-steganography
```

3. Run encryption:

```
python encryption.py
```

4. Run steganography:

```
python steganography.py
```

---

## 📌 Conclusion

This project demonstrates how combining **AES encryption** and **LSB steganography** enhances data security.
It provides a reliable solution for secure communication and protection against cyber threats.

---

## 👩‍💻 Author

**Keerthi Krishnan**
Cybersecurity Enthusiast | SOC Analyst Aspirant
📍 UK

---

