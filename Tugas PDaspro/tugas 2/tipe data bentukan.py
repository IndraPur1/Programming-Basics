#Nama File : Indra Purwanto_24060123140150_TUGAS 3_C2
#Pembuat   : Indra Purwanto
#Tanggal   : 24 september 2023

# DEFINISI TYPE
# type laptopku : <processor:string, graphics:string, display:string, memory:string, storage:string, camera:string, audio:string, battery:string, network:string, weight:string>
# {<processor, graphics, display, memory, storage, camera, audio, battery, network, weight> adalah sebuah laptopku, dengan Processor adalah Processor, graphics adalah graphics, display adalah display, memory adalah memory, storage adalah storage, camera adalah camera, audio adalah audio, battery adalah battery, network adalah network, dan weight adalah weight}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Makelaptopku : 10 string,--> laptopku
#{Makelaptopku(processor, graphics, display, memory, storage, camera, audio, battery, network, weight)membentuk sebuah laptopku dari a, b, c, d, e, f, g, h, i, j dengan a sebagai processor, b sebagai graphics, c sebagai display, d sebagai memory, e sebagai storage, f sebagai camera, g sebagai audio, h sebagai battery, i sebagai network, j sebagai weight}
#Realisasi dalam Phyton
class laptopku:
  def __init__(self,a,b,c,d,e,f,g,h,i,j):
    self.processor = a
    self.graphics = b
    self.display = c
    self.memory = d
    self.storage = e
    self.camera = f
    self.audio = g
    self.battery = h
    self.network = i
    self.weight = j
    
# DEFINISI DAN SPESIFIKASI SELEKTOR
# processor : laptopku --> string
# processor(P) memberikan processor laptopku P
# Realisasi dalam phyton
def processor(P) :
    return P.processor

# graphics : laptopku --> string
# graphics(P) memberikan graphics laptopku P
# Realisasi dalam phyton
def graphics(P) :
    return P.graphics

# display : laptopku --> string
# display(P) memberikan display laptopku P
# Realisasi dalam phyton
def display(P) :
    return P.display

# memory : laptopku --> string
# memory(P) memberikan memory laptopku P
# Realisasi dalam phyton
def memory(P) :
    return P.memory

# storage : laptopku --> string
# storage(P) memberikan storage laptopku P
# Realisasi dalam phyton
def storage(P) :
    return P.storage

# camera : laptopku --> string
# camera(P) memberikan camera laptopku P
# Realisasi dalam Python
def camera(P) :
    return P.camera

# audio : laptopku --> string
# audio(P) memberikan audio laptopku P
# Realisasi dalam Python
def audio(P) :
    return P.audio

# battery : laptopku --> string
# battery(P) memberikan battery laptopku P
# Realisasi dalam Python
def battery(P) :
    return P.battery

# network : laptopku --> string
# network(P) memberikan network laptopku P
# Realisasi dalam Python
def network(P) :
    return P.network

# weight : laptopku --> string
# weight(P) memberikan weight laptopku P
# Realisasi dalam Python
def weight(P) :
    return P.weight

# APLIKASI 
P = laptopku("12th Gen Intel® Core™ i5-12450H Processor 2 GHz","NVIDIA® GeForce RTX™ 3050 Laptop GPU, 4GB GDDR","15.6-inch, Refresh Rate:144Hz","8GB DDR5-4800 SO-DIMM, Max Capacity:32GB, Support dual channel memory","512GB PCIe® 3.0 NVMe™ M.2 SSD","720P HD camera","Dolby Atmos, 2-speaker system","76WHrs, 4S1P, 4-cell Li-ion","Wi-Fi 6 + Bluetooth® 5.2","2.00 Kg")
print(processor(P))
print(graphics(P))
print(display(P))
print(memory(P))
print(storage(P))
print(camera(P))
print(audio(P))
print(battery(P))
print(network(P))
print(weight(P))