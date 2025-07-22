import sqlite3

def bazani_yarat():
    conn = sqlite3.connect("people.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS people")
    cursor.execute("""
    CREATE TABLE people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ism TEXT,
        familiya TEXT,
        tugilgan_sana TEXT,
        jins TEXT,
        pasport_raqami TEXT,
        telefon TEXT,
        yashash_manzili TEXT,
        kasbi TEXT
    )
    """)
    conn.commit()
    conn.close()
    print("Xush kelibsiz!!!")

def odam_qosh():
    print("\n— Yangi odam ma'lumotlarini kiriting —")
    ism = input("Ism: ").strip()
    familiya = input("Familiya: ").strip()
    tugilgan_sana = input("Tug'ilgan sana (YYYY-MM-DD): ").strip()
    jins = input("Jins (Erkak/Ayol): ").strip()
    pasport_raqami = input("Pasport raqami: ").strip()
    telefon = input("Telefon raqami: ").strip()
    yashash_manzili = input("Yashash manzili: ").strip()
    kasbi = input("Kasbi: ").strip()

    conn = sqlite3.connect("people.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO people (ism, familiya, tugilgan_sana, jins, pasport_raqami, telefon, yashash_manzili, kasbi)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (ism, familiya, tugilgan_sana, jins, pasport_raqami, telefon, yashash_manzili, kasbi))
    conn.commit()
    conn.close()
    print("Odam bazaga qo‘shildi!")

def qidirish(ism_fam):
    parts = ism_fam.strip().split()
    if len(parts) != 2:
        print("Iltimos, ism va familiyani to‘liq kiriting.")
        return
    ism, familiya = parts

    conn = sqlite3.connect("people.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM people WHERE ism=? COLLATE NOCASE AND familiya=? COLLATE NOCASE
    """, (ism, familiya))

    natija = cursor.fetchone()

    if natija:
        print("\n Odam topildi:")
        print(f"ID: {natija[0]}")
        print(f"Ism: {natija[1]}")
        print(f"Familiya: {natija[2]}")
        print(f"Tug‘ilgan sana: {natija[3]}")
        print(f"Jins: {natija[4]}")
        print(f"Pasport raqami: {natija[5]}")
        print(f"Telefon: {natija[6]}")
        print(f"Yashash manzili: {natija[7]}")
        print(f"Kasbi: {natija[8]}")
    else:
        print("\n Ma’lumot topilmadi.")

    conn.close()

if __name__ == "__main__":
    bazani_yarat()

    while True:
        print("\nNimani qilmoqchisiz?")
        print("1 - Yangi odam qo‘shish")
        print("2 - Odam qidirish")
        print("0 - Chiqish")
        tanlov = input("Tanlovingiz: ").strip()

        if tanlov == "1":
            odam_qosh()
        elif tanlov == "2":
            ism_fam = input("Ism va familiyani kiriting: ")
            qidirish(ism_fam)
        elif tanlov == "0":
            print("Dasturdan chiqildi.")
            break
        else:
            print("Noto‘g‘ri tanlov, qaytadan urinib ko‘ring.")
