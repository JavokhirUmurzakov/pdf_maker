import qrcode
from fpdf import FPDF

class ShahodatnomaPDF(FPDF):
    def header(self):
        """Sarlavha qo‘shish"""
        self.set_font(family="Times",style='B', size=14)
        self.cell(200, 5, "O'ZBEKISTON RESPUBLIKASI", ln=True, align='C')
        self.cell(200, 5, "REPUBLIC OF UZBEKISTAN", ln=True, align='C')
        self.ln(5)

        self.set_font(family="Arial",style='B', size=14)
        self.cell(200, 5, "TAYANCH O'RTA TA'LIM TO'G'RISIDA", ln=True, align='C')
        self.cell(200, 5, "SHAHODATNOMA", ln=True, align='C')
        self.ln(5)

    def add_content(self):
        """Asosiy matn qo‘shish"""
        self.set_font(family="Times",size=10)

        # Shahodatnoma raqami
        self.cell(200, 5, "N _______", ln=True,align='C')
        self.ln(5)

        # Shaxsiy ma'lumotlar
        self.cell(200, 5, "Ushbu shahodatnoma / This is to certify that", ln=True,align='C')
        self.cell(200, 5, "_______________  yilda tug'ilgan", ln=True,align='C')
        self.cell(200, 5, "(tug'ilgan sanasi)", ln=True, align='C')
        self.ln(10)

        self.cell(200, 5, "_________________________________________________________________________________________________________", ln=True)
        self.ln(5)

        self.cell(200, 5, "________  yilda  ___________________________________________________________________________________________", ln=True)
        self.cell(200, 5, "(ta'lim tashkiloti / educational organization)", ln=True, align='C')
        self.ln(5)

        self.cell(200, 5, "bitirganligi va tayanch o'rta ta'lim olganligini tasdiqlaydi.", ln=True)
        self.ln(10)

    def add_table(self):
        """O‘quv fanlari va baholar jadvali"""
        self.set_font(family="Times",style='B', size=10)
        self.cell(200, 5, "Belgilangan o'quv fanlaridan baholar:", ln=True)
        self.ln(5)

        def add_qr_code(self, qr_data):
            """QR kod yaratish va PDF ga qo‘shish"""
            qr = qrcode.make(qr_data)
            qr.save("qr_code.png")
            self.image("qr_code.png", x=85, y=250, w=40, h=40)

        # Jadval sarlavhalari
        self.set_font(family="Times",size=10)
        self.cell(90, 5, "O'quv fanlari", border=1, align='C')
        self.cell(90, 5, "Baholar", border=1, align='C')
        self.ln()

        # O‘quv fanlari ro‘yxati
        subjects = ["Matematika", "Fizika", "Kimyo", "Biologiya", "Tarix","Iqtisod asoslari","Algebra","Tasviriy san'at","Fransuz tili",
                    "Geografiya", "Adabiyot", "Ingliz tili", "Informatika", "Jismoniy tarbiya","Mehnat","Zoologiya","Jahon tarixi","O'zbekiston tarixi","Rus tili"]
        self.set_font(family="Arial",size=10)
        for subject in subjects:
            self.cell(90, 5, subject, border=1)
            self.cell(90, 5, "", border=1)  # Bo‘sh baho ustuni
            self.ln()

# 📄 PDF yaratish
pdf = ShahodatnomaPDF()
pdf.add_page()
pdf.set_font(family="Times",size=12)

pdf.add_content()
pdf.add_table()

# 📂 PDF faylni saqlash
pdf.output("shahodatnoma.pdf")

print("✅ Shahodatnoma PDF yaratildi!")
