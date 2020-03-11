from tkinter import *
from tkinter.messagebox import showerror

#Data untuk membuat Barcode sesuai dengan kode 12 angka yang diberi
first_digit = ["LLLLLL",'LLGLGG','LLGGLG','LLGGGL','LGLLGG','LGGLLG','LGGGLL','LGLGLG','LGLGGL','LGGLGL']
l_code = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
g_code = ['0100111','0110011','0011011','0100001','0011101','0111001','0000101','0010001','0001001','0010111']
r_code = ['1110010','1100110','1101100','1000010','1011100','1001110','1010000','1000100','1001000','1110100']


class Gambar_Barcode(Canvas):

    def __init__(self,master):
        self.master = master

        #Judul GUI
        master.title("EAN-13 [by Reynard Adha Ryanda]")

        #Variabel untuk validasi kode dan nama file
        self.kode_valid = False
        self.nama_file_valid = False
        
        #Label sesuai untuk input apa
        self.label1 = Label(master,text="Save barcode to PS file [eg: EAN13.eps]:",font="bold")
        self.label2 = Label(master,text="Enter code (first 12 decimal digits):",font="bold")

        #Menaruh label sesuai tempatnya
        self.label1.grid(row = 0,column=0)
        self.label2.grid(row = 2,column=0)

        #Input kode
        self.kode = StringVar()
        self.tulis_kode = Entry(master,textvariable=self.kode,width=40)

        #Input nama file
        self.nama_file = StringVar()
        self.tulis_nama_file = Entry(master,textvariable=self.nama_file,width=40)

        #Membuat kanvas untuk menggambar barcode
        super().__init__(master,width=300,height=300,bg="white")
        super().grid(row = 4,column=0)

        #Menyambungkan tombol enter dengan command cek
        self.tulis_nama_file.bind("<Return>",self.cek)
        self.tulis_kode.bind("<Return>",self.cek)

        #Menaruh tempat tulis input sesuai tempatnya
        self.tulis_nama_file.grid(row = 1,column=0)
        self.tulis_kode.grid(row = 3,column=0)

    #Command validasi nama file dan kode dilanjutkan dengan penggambaran barcode
    def cek(self,event):

        #Validasi nama file
        nama_file = self.nama_file.get()
        if nama_file[-4:] == '.eps' and " " not in nama_file and len(nama_file)>4:
            self.nama_file_valid = True
        else:
            self.nama_file_valid = False
            self.error1 = showerror(title = "Error Nama File", message = "Nama file tidak valid!")

        #Validasi kode
        kode = self.kode.get()
        if kode.isnumeric() == True and len(kode) == 12:
            self.kode_valid = True
        else:
            self.kode_valid = False
            self.error1 = showerror(title = "Error Kode", message = "Nama kode tidak valid!")

        #Validasi jika kode dan nama file valid
        if self.nama_file_valid == True and self.kode_valid == True:
            self.menggambar()
        else:
            super().delete("all")
    #Command gambar barcode
    def menggambar(self):
        #Menghapus canvas jika mengulang input
        super().delete("all")

        #Variabel kode
        kode_awal = self.kode.get()
        kode = list(kode_awal)
        check_digit = 0

        #Membuat check digit
        for i in range (1,12,2):
            check_digit = (int(kode[i])*3) + check_digit
            
        for j in range (0,12,2):
            check_digit += int(kode[j])

        if check_digit % 10 == 0:
            check_digit = 0
            
        else:
            check_digit = 10 - (check_digit % 10)
            
        #Menambahkan digit terakhir
        kode.append(str(check_digit))

        #Menambahkan tulisan EAN-13 Barcode:
        super().create_text(152,35,fill = "black", font = "Times 17 bold", text = "EAN-13 Barcode:")

        #Membuat Barcode
        super().create_rectangle(51,50,53,185,fill = "blue",width = 0)
        super().create_rectangle(53,50,55,185,fill = "white",width = 0)
        super().create_rectangle(55,50,57,185,fill = "blue",width = 0)

        encoding = first_digit[int(kode[0])]

        x = 0

        for i in range (6):
            if encoding[i] == 'L':
                for j in range (7):
                    if l_code[int(kode[i+1])][j] == '0':
                        super().create_rectangle(57+x,50,59+x,175,fill = "white",width = 0)
                        x += 2
                    elif l_code[int(kode[i+1])][j] == '1':
                        super().create_rectangle(57+x,50,59+x,175,fill = "black",width = 0)
                        x += 2
            elif encoding[i] == 'G':
                for k in range (7):
                    if g_code[int(kode[i+1])][k] == '0':
                        super().create_rectangle(57+x,50,59+x,175,fill = "white",width = 0)
                        x += 2
                    elif g_code[int(kode[i+1])][k] == '1':
                        super().create_rectangle(57+x,50,59+x,175,fill = "black",width = 0)
                        x += 2
                        
        super().create_rectangle(59+x,50,61+x,185,fill = "white",width = 0)
        super().create_rectangle(61+x,50,63+x,185,fill = "blue",width = 0)
        super().create_rectangle(63+x,50,65+x,185,fill = "white",width = 0)
        super().create_rectangle(65+x,50,67+x,185,fill = "blue",width = 0)
        super().create_rectangle(67+x,50,69+x,185,fill = "white",width = 0)

        for i in range (7,13):
            for j in range (7):
                if r_code[int(kode[i])][j] == "0":
                    super().create_rectangle(69+x,50,71+x,175,fill = "white",width = 0)
                    x += 2
                elif r_code[int(kode[i])][j] == "1":
                    super().create_rectangle(69+x,50,71+x,175,fill = "black",width = 0)
                    x += 2

        super().create_rectangle(71+x,50,73+x,185,fill = "blue",width = 0)
        super().create_rectangle(73+x,50,75+x,185,fill = "white",width = 0)
        super().create_rectangle(75+x,50,77+x,185,fill = "blue",width = 0)

        #Membuat angka dibawah barcode dan tulisan check digit
        super().create_text(137,193,fill = "black", font = "Times 14 bold", text = "{}  {}  {}".format(kode[0]," ".join(kode[1:7]),' '.join(kode[7:])))
        super().create_text(137,220,fill = "orange", font = "Times 14 bold", text = "Check Digit: {}".format(check_digit))

        
        #Mengubah Barcode menjadi postscript
        super().postscript(file="{}".format(self.nama_file.get()), colormode='color')
        
def main():
    root = Tk()
    my_barcode = Gambar_Barcode(root)
    root.mainloop()

if __name__ == '__main__':
    main()
