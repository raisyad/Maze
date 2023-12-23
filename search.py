# search.py
# ---------------
# Created by Yaya Wihardi (yayawihardi@upi.edu) on 15/03/2020

# Fungsi search harus me-return path.
# Path berupa list tuples dengan format (row, col) 
# Path merupakan urutan states menuju goal.
# maze merupakan object dari Maze yang merepresentasikan keadaan lingkungan 
# beberapa method dari maze yang dapat digunakan:

# getStart() : return tuple (row, col) -> mendapatkan initial state
# getObjectives() : return list of tuple [(row1, col1), (row2, col2) ...] -> mendapatkan list goal state
# getNeighbors(row, col) : input posisi, return list of tuple [(row1, col1), (row2, col2) ...]
#                          -> mendapatkan list tetangga yg mungkin (expand/sucessor functiom)
# isObjective(row, col) : return true/false -> goal test function

# Edited by : Raisyad Jullfikar 2106238 C2 - 2021

# Import Library queue
import queue

# Temp for put list from initial state to the goal state
path_hasil = []

# Fungsi/Prosedur untuk mengulang (Rekursif) hingga menemukan path dari goal ke initial statenya
def print_route(is_ketemu, parent, initial_state, goal_state):
    # Sebuah kondisi ketika tidak menemukan yang kita tuju, maka return 
    if(not is_ketemu):
        return
    rec_print_route(parent, goal_state, initial_state)

# Fungsi/Prosedur untuk mengulang (Rekursif) hingga menemukan path dari goal ke initial statenya
def rec_print_route(parent, curnode, initial_state):
    
    # Sebuah kondisi ketika node saat ini sudah sampai ke initial statenya, maka fungsi selesai
    if(curnode == initial_state):
        # Menambah node kedalam type list (final_path)
        path_hasil.append(curnode)
        # Mereturn ke fungsi yang sebelumnya
        return
    # Memangggil fungsinya kembali, namun dengan posisi curnode diganti olehh parent dari si current nodenya
    rec_print_route(parent, parent[curnode], initial_state)
    path_hasil.append(curnode)

# Fungsi/Prosedur metode yang dipakai untuk searchnya
def Bfs_Methods(maze):
    Start = maze.getStart()
    # Deklarasi Var fringe sebagai queue
    fringe = queue.Queue()
    fringe.put(Start) # Menginputkan node awal atau initial state, ke fringe
    explored = [] # Var list untuk menyimpan path/node yang sudah terexplore
    parent = {} # Var tupple untuk menampung child dan parentnya

    # Perulangan dibawah akan terus berjalan ketika fringe belum kosong
    while not fringe.empty():   
        current = fringe.get() # Mendapatkan node dari si fringe dan menyimpan kedalam current
        Row = current[0]
        Col = current[1]
        Goal = maze.isObjective(Row, Col)
        EkspandChild = maze.getNeighbors(Row, Col)

        # Ketika node saat ini sudah menemukan goal statenya, maka...
        if (Goal):
            return (True, parent) # Return nilai True dan nilai dari si semua child dan parent nya

        # Cek terlebih dahulu, jika current belum tereksplore, maka..
        if(current not in explored):
            # Lakukan Ekspansi
            
            # Lakukan ekspansi untuk setiap child/node yang bisa dituju oleh node yang sekarang
            for child in EkspandChild:
                fringe.put(child) # Memasukkan value child kedalam fringe

                # Sebelum current dipindahkan kedalam parent, cek dahulu apakah pernah terksplore si childnya, atau belum
                if(child not in explored):
                    # Jika belum, baru masukkan valuenya
                    parent[child] = current
            # Menambah Node sekarang kedalam list explorednya
            explored.append(current)

    return (False, parent) # Mengembalikan nilai False dan semua tupple child dan parent nya

# Fungsi/Prosedur dari searchnya
def search(maze):
    Start = maze.getStart()
    Goal = maze.getObjectives()[0]
    ketemu, parent = Bfs_Methods(maze) # Mengambil value hasil dari Fungsi/Prosedur BFS berupa boolean dan parentnya
    print_route(ketemu, parent, Start, Goal) # Memanggil Fungsi/Prosedur untuk menentukan path yang mana saja yang dibutuhkan untuk mencapai goal state
    return path_hasil # Mengembalikan nilai path yang terdekat dari initial state ke goal state nya