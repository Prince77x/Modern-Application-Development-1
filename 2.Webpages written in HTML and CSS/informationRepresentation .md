### Information representation

- Computer work on 'bits,
    - Binary digit:0 and 1

-   Numbers
    - Place value:binary number :eg=0110

But What about character 'Aa....Zz'?

## ASCII

- Americal Standard code for Information Interchange
- 7-bits:128 different entities
    - 'a' _ 'z'
    - 'A' _ 'z'
    - '0' _ '9'
    - Special character :!@#$%^&*()...

- Why bits ?
- What about other character ? hindi,tamil...
    - 1000s of character needed

## Unicode 
- Allow codes for morer scripts, character 
- How many/
    - All living language ? All extinct language ? All future language?

- "Universal character set" encoding UCS


# 📘 Character Encoding & Representation – Key Topics

## 1. Number Systems & Bits
- **Binary, Octal, Decimal, Hexadecimal** → fundamental for encoding.  
- `n` bits can represent `2^n` unique values.  
- Example: 8 bits → 256 values → used in Extended ASCII.

---

## 2. ASCII (American Standard Code for Information Interchange)
- **7-bit ASCII**: 128 characters (0–127).  
- **8-bit Extended ASCII**: 256 characters (0–255).  
- Still widely used for English text, programming.  
- Example: `'A' = 65`, `'a' = 97`.

---

## 3. Unicode & UCS
- Unicode is a universal standard for encoding characters of all languages.  
- Encodings:  
  - **UCS-2**: 16 bits, fixed length, 65,536 chars (BMP only).  
  - **UCS-4**: 32 bits, fixed length, ~4 billion chars (but wasteful).  
  - **UTF-8**: Variable length (1–4 bytes), backward compatible with ASCII.  
  - **UTF-16**: Variable length (2 or 4 bytes), extends UCS-2 using surrogates.  

📌 **UTF-8 is the most popular today (web, databases, OS).**

---

## 4. Variable-Length Encoding
- Instead of fixed bits, common symbols get shorter codes.  
- Examples:  
  - **Huffman Coding** (prefix codes).  
  - **UTF-8** → ASCII chars = 1 byte, others up to 4 bytes.  
- Used for efficient compression and storage.

---

## 5. Control Characters
- ASCII includes non-printable codes (0–31) like:  
  - 10 → Line Feed (LF)  
  - 13 → Carriage Return (CR)  
  - 9 → Tab  
- Important in file formats and networking.

---

## 6. Storage Calculations
- Formula:  
Total Bits = Number of Characters × Bits per Character

- Example: 1000 characters in UCS-4 → `1000 × 32 = 32,000 bits`.  
- Helps estimate file size, memory use.

---

## 7. Code Pages
- Early computers used different encodings (ISO-8859, Windows-1252, etc.).  
- Problem: Same byte → different character in different regions.  
- Unicode solved this with a **single global standard**.

---

## 8. Base Encoding (for Data Transmission)
- **Base64**: Represents binary as text (used in emails, JWT tokens).  
- Increases size (~33%) but ensures safe transfer in text-only systems.  
- **Hex Encoding**: Represents binary as `0–9, A–F`.  

---

## 9. Endianness
- Defines byte order in memory:  
- **Little Endian**: least significant byte first.  
- **Big Endian**: most significant byte first.  
- Important in UCS-2/UTF-16 (BOM = Byte Order Mark indicates order).  

---

## 10. Modern Applications
- **Web Browsers** → Always use UTF-8 now.  
- **Databases** → Support Unicode for internationalization.  
- **Programming Languages** → Strings internally stored in UTF-16 (Java, JavaScript) or UTF-8 (Python 3, Go, Rust).  
- **Operating Systems** → Windows uses UTF-16, Linux uses UTF-8.  

---

# 📊 Summary Table

| Encoding        | Bit Length  | Characters Supported | Notes                              |
|-----------------|-------------|----------------------|------------------------------------|
| ASCII (7-bit)   | 7           | 128                  | English only                       |
| Extended ASCII  | 8           | 256                  | Region-specific                    |
| UCS-2           | 16          | 65,536               | BMP only, outdated                 |
| UTF-8           | 1–4 bytes   | 1.1M                 | Most common today, ASCII-compatible|
| UTF-16          | 2 or 4 bytes| 1.1M                 | Used in Windows, Java, JS          |
| UCS-4           | 32          | ~4B                  | Wasteful, not practical            |

---

✅ If you master these 10 areas, you’ll understand **all encoding-related exam questions + modern real world uses


