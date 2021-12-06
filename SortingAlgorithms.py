# Colby Austin
# Sorting Algorithm demo
#
# I am still adding all of the algorithms
#######################################################################
from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort
from quickSort import quick_sort
from mergeSort import merge_sort
from insertionSort import insertion_sort
# from selectionSort import selection_sort
# from heapSort import heap_sort
# from shellSort import shell_sort
# from combSort import comb_sort
# from executionSort import execution_sort
# from countingSort import counting_sort
# from bucketSort import bucket_sort
# from radixSort import radix_sort
# from blockSort import block_sort
# from exchangeSort import exchange_sort
# from treeSort import tree_sort
# from cycleSort import cycle_sort
# from librarySort import library_sort
# from gnomeSort import gnome_sort
# from cocktailshakerSort import cocktailshaker_sort
# from tournamentSort import tournament_sort
# from patienceSort import patience_sort
# from shellSort import shell_sort
# from pancakeSort import pancake_sort
# from beadSort import bead_sort


root = Tk()
root.title('Sorting Algorithm Demo')
root.maxsize(1500,1000)
root.config(bg='black')
root.columnconfigure(2)
root.rowconfigure(2)

# variables
Right_Sorting_alg = StringVar()
Left_Sorting_alg = StringVar()


def drawData(data, canvas, colorArray):
    canvas.delete("all")
    c_height = 400
    c_width = 590
    x_width = c_width / (len(data) + 1)
    offset = 0
    spacing = 0
    height_adjusted = [i/max(data) for i in data]
    for i, height in enumerate(height_adjusted):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 380
        # bottom right
        x1 = (i+1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    root.update_idletasks()


def Generate():
    global right_data
    global left_data

    data = []
    try:
        size = int(sizeEntry.get())
    except:
        size = 100
    for n in range(size):
        data.append(n+1)
    random.shuffle(data)
    right_data = data
    left_data = data
    drawData(data, LeftSortingDemo, ['red' for x in range(len(data))])
    drawData(data, RightSortingDemo, ['red' for x in range(len(data))])

def Start():
    global right_data
    global left_data
    speed = SpeedScale.get()
    canvas = [LeftSortingDemo, RightSortingDemo]
    sorting_alg = [Left_Sorting_alg.get(), Right_Sorting_alg.get()]
    data_list = [left_data, right_data]
    for i in range(len(canvas)):
        if sorting_alg[i] == 'quick sort':
            quick_sort(data_list[i], 0, len(data_list[i]) - 1, drawData, canvas[i], speed)
        elif sorting_alg[i] == 'bubble sort':
            bubble_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'merge sort':
            merge_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'insertion sort':
            insertion_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'selection sort':
            selection_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'heap sort':
            heap_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'shell sort':
            shell_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'comb sort':
            comb_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'execution sort':
            execution_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'counting sort':
            counting_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'bucket sort':
            bucket_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'radix sort':
            radix_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'block sort':
            block_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'exchange sort':
            exchange_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'tree sort':
            tree_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'cycle sort':
            cycle_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'library sort':
            library_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'gnome sort':
            gnome_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'cocktail shaker sort':
            cocktailshaker_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'tournament sort':
            tournament_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'patience sort':
            patience_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'shell sort':
            shell_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'pancake sort':
            pancake_sort(data_list[i], drawData, canvas[i], speed)
        elif sorting_alg[i] == 'bead sort':
            bead_sort(data_list[i], drawData, canvas[i], speed)

        drawData(data_list[i], canvas[i], ['green' for x in range(len(data_list[i]))])


# Frame/base Layout
UI_frame = Frame(root, width=1190, height=300, bg='grey')
LeftSortingDemo = Canvas(root, width=590, height=400, bg='grey')
RightSortingDemo = Canvas(root, width=590, height=400, bg='grey')


UI_frame.grid(row=1, columnspan=2, padx=5, pady=5)
LeftSortingDemo.grid(row=0, column=0, padx=5, pady=5)
RightSortingDemo.grid(row=0, column=1, padx=5, pady=5)


# User Interface area
UI_frame.columnconfigure(8)
UI_frame.rowconfigure(4)

# Row[0]
Label(UI_frame, text='Algorithm: ', bg='grey').grid(row=0, column=0, padx=5, pady=5)
algMenu = ttk.Combobox(UI_frame, textvariable=Left_Sorting_alg, values=["bubble sort", "quick sort", "insertion sort", "selection sort", "merge sort", "heap sort", "shell sort", "comb sort", "execution sort", "counting sort", "bucket sort", "radix sort", "block sort", "exchange sort", "tree sort", "cycle sort", "library sort", "gnome sort", "cocktail shaker sort", "tournament sort", "patience sort", "shell sort", "pancake sort", "bead sort"])
algMenu.grid(row=0, column=1, columnspan=3, padx=5, pady=5)
algMenu.current(0)
algMenu = ttk.Combobox(UI_frame, textvariable=Right_Sorting_alg, values=["bubble sort", "quick sort", "insertion sort", "selection sort", "merge sort", "heap sort", "shell sort", "comb sort", "execution sort", "counting sort", "bucket sort", "radix sort", "block sort", "exchange sort", "tree sort", "cycle sort", "library sort", "gnome sort", "cocktail shaker sort", "tournament sort", "patience sort", "shell sort", "pancake sort", "bead sort"])
algMenu.grid(row=0, column=7, columnspan=3, padx=5, pady=5)
algMenu.current(0)

# Row[1]
Label(UI_frame, text='Average: ', bg='grey').grid(row=1, column=0, padx=5, pady=5)
Label(UI_frame, text='value ', bg='grey').grid(row=1, column=1, padx=5, pady=5)
Label(UI_frame, text='Average: ', bg='grey').grid(row=1, column=5, padx=5, pady=5)
Label(UI_frame, text='value ', bg='grey').grid(row=1, column=6, padx=5, pady=5)

# Row[2]
Label(UI_frame, text='Best: ', bg='grey').grid(row=2, column=0, padx=5, pady=5)
Label(UI_frame, text='value', bg='grey').grid(row=2, column=1, padx=5, pady=5)
Label(UI_frame, text='Worst: ', bg='grey').grid(row=2, column=2, padx=5, pady=5)
Label(UI_frame, text='value ', bg='grey').grid(row=2, column=3, padx=5, pady=5)
Label(UI_frame, text='Best: ', bg='grey').grid(row=2, column=5, padx=5, pady=5)
Label(UI_frame, text='value', bg='grey').grid(row=2, column=6, padx=5, pady=5)
Label(UI_frame, text='Worst: ', bg='grey').grid(row=2, column=7, padx=5, pady=5)
Label(UI_frame, text='value ', bg='grey').grid(row=2, column=8, padx=5, pady=5)

# Row[3]
Label(UI_frame, text='Size: ', bg='grey').grid(row=3, column=0, padx=5, pady=5)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=3, column=1, columnspan=3, padx=5, pady=5)

# Row[4]
Button(UI_frame, text="Generate", command=Generate, bg='grey').grid(row=4, column=0, padx=5, pady=5)
SpeedScale = Scale(UI_frame, from_=0.05, to=1, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed")
SpeedScale.grid(row=4, column=1, columnspan=4, padx=5, pady=5)
Button(UI_frame, text="Start", command=Start, bg='grey').grid(row=4, column=6, padx=5, pady=5)

#main begin
if __name__ == '__main__':
    root.mainloop()
    print("done")

