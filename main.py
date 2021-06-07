import os
def merge(left, right):

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right): 
        if left[left_index] < right[right_index]:
            result.append(right[right_index])
            right_index += 1
        else:
            result.append(left[left_index])
            left_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result 


def merge_sort(data):

    if len(data) <= 1: 
        return data

    half = len(data) // 2
    left = merge_sort(data[:half])
    right = merge_sort(data[half:])

    return merge(left, right)

    
def main():
  os.system('cls')
  ops = True
  data = []
  while(ops):
    print("====================================")
    print("NAMA : ALFA SEAN KALAPADANG LONTENG|        ")
    print("NIM  : 20101106067                 |")
    print("====================================\n")
    print("======================================================")
    print("|\t\t  WELCOME TO PROGRAM                 |")
    print("|\t\t      MERGE SORT                     |")
    print("======================================================")
    print("\t  |===========|MENU|===========|")
    print("\t     1. INPUT DATA                       ")
    print("\t     2. BERSIHKAN DATA                   ")
    print("\t     3. MERGE SORT                       ")
    print("\t     4. EXIT                             ")
    print("======================================================")
    choice = int(input("MASUKKAN PILIHAN MENU : "))

    if choice == 1:

      print("==========================\n")
      temp = input("=> MASUKKAN DATA : ")
      temp = temp.split()
      data = list(map(int, temp))
      print("\n============================\n")
      os.system('cls')

    elif choice == 2 and data != []:
      
      print("============================\n")
      del data
      print("=> DATA TELAH DIBERSIHKAN")
      print("\n============================\n")

    elif choice == 3 and data != []:

      print("============================\n")
      print("=> DATA SEBELUM DIURUTKAN")
      print("  ",*data)
      fin = iter(merge_sort(data))

      print("=> DATA SESUDAH DIURUTKAN")
      print("  ",*fin)
      print("\n============================\n")
      

    elif choice == 4:

      ops = False

    else:
      print("\n============================\n")
      print("INPUTAN MENU YANG ANDA MASUKKAN SALAH!!!")
      print("\n============================\n")
      
      
  print("\n============================\n")
  print("TERIMA KASIH :) !!")
  print("\n============================\n")

if __name__=="__main__":
  main()