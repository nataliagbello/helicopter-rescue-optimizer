import math
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


def mergeSort(lifeboatStack):
    results = []
    n = len(lifeboatStack)
    if n <= 1:
        return lifeboatStack
    middle = n // 2
    leftHalf = lifeboatStack[:middle]
    rightHalf = lifeboatStack[middle:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)
    leftIndex = 0 
    rightIndex = 0 

    while leftIndex < len(sortedLeft) and rightIndex < len(sortedRight):
        if sortedLeft[leftIndex][1] >= sortedRight[rightIndex][1]:
            results.append(sortedLeft[leftIndex])
            leftIndex += 1
        else:
            results.append(sortedRight[rightIndex])
            rightIndex += 1
    results.extend(sortedLeft[leftIndex:])
    results.extend(sortedRight[rightIndex:])

    return results



def lifeboatsRescue(lifeboatStack, D): # lifeboat = (number of people, distance, risk) , D = helicopter fuel
    priorityStack = []
    rescuedStack=[]
    totalPeople = 0
    peopleRescued = 0
    i = 0
    print('')
    print('')
    print('============================================')
    print('========== Initializing Lifeboats ==========')
    print('============================================')
    for lifeboat in lifeboatStack:
        i += 1 # lifeboats identification
        people = lifeboat[0]
        totalPeople += people
        fuelCost = float(2*lifeboat[1]) # twice the distance - one round trip
        urgencyFactor = float((lifeboat[0]*lifeboat[2])/fuelCost) # max amount of people for the least amount of fuel
        distance = lifeboat[1]
        priorityStack.append([i,urgencyFactor,fuelCost,distance, people])
        
        print(f'Lifeboat index: {i}')
        print(f'Fuel cost {i}: {fuelCost}')
        print(f'Urgency factor of lifeboat {i}: {urgencyFactor}')
        print(f'Number of people in lifeboat {i}: {people}')
        print('============================================')
    # sorting priorityStack based on urgencyFactor to determine rescue sequence 
    print('')
    print('')
    print('============================================')
    print('STACKS:')
    print(f'Priority Stack: {priorityStack}')
    sortedPriorityStack = mergeSort(priorityStack)
    print(f'Sorted Priority Stack: {sortedPriorityStack}')
    print('============================================')
    print('')
    print('')

    print('============================================')
    print('============== Rescue Sequence =============')
    print('============================================')
    print('')
    print (f' - Initial fuel: {D}')
    for lifeboat in sortedPriorityStack:
        if lifeboat[2] <= D:
            print('')
            print('============================================')
            print('+1 Rescue')
            rescuedStack.append(lifeboat)
            D -= lifeboat[2]
            peopleRescued += lifeboat[0]
            print(f' - Current Rescue: {rescuedStack}')
            print(f' - Updated fuel: {D}')
            print(f' - Remaining Sorted Priority Stack: {sortedPriorityStack}')
        else:
            pass
    print('')
    print('============================================')
    print('')
    print('')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('Out of fuel!')
    print('')
    print(f' - Remaining fuel: {D}')
    print(f' - Rescued lifeboats Stack: {rescuedStack}')
    print('')
    print('END OF RESCUE MISSION')
    return (priorityStack, rescuedStack, D, totalPeople, peopleRescued)


def tkinterMap(priorityStack, rescuedStack, totalPeople, peopleRescued, D):
    window = tk.Tk()
    window.title('Helicopter rescue mission - Algorithm')
    canvas = tk.Canvas(window, width = 1500, height = 800, bg = 'lightblue')
    canvas.pack()
    rescuedCount = len(rescuedStack)

    # Caixinha
    hud = canvas.create_rectangle(10, 10, 270, 270, fill="#ffffff", outline="black")
    hud_text = canvas.create_text(20, 20, anchor="nw", text="Lifeboat Rescue", font=("Arial", 15, "bold"), fill="black")
    hud_text = canvas.create_text(20, 60, anchor="nw", text="~ Green Lifeboat - rescued", font=("Arial", 12, "bold"), fill="green")
    hud_text = canvas.create_text(20, 80, anchor="nw", text="~ Red Lifeboat - abandoned", font=("Arial", 12, "bold"), fill="red")
    hud_text = canvas.create_text(20, 110, anchor="nw", text= f'- Helicopter Fuel:{D}\n' f"\n" f"- Total People: {totalPeople}\n" f"\n" f"- People Rescued: {peopleRescued}\n" f"\n" f"- Lifeboats Rescued: {rescuedCount}",
    font=("Arial", 12),
    fill="black")


    baseX = 320
    baseY = 380

    #Helicopter
    canvas.create_rectangle(baseX - 10, baseY - 10, baseX + 10, baseY + 10, fill = "yellow", outline = "black")
    canvas.create_text(baseX, baseY - 20, text = "HELIPAD", font = ("Arial", 12))

    fatorX = 100
    fatorY = 200

    for lifeboat in priorityStack: # [[i, urgencyFactor, cost, distance],...]
        lifeboatId, urgencyFactor, fuelCost, distance, people = lifeboat

        x = baseX + distance * fatorX
        y = baseY + math.sin(lifeboatId * 1.3) * fatorY

        rescued = any(s[0] == lifeboatId for s in rescuedStack)
        color = 'green' if rescued else 'red'

        canvas.create_oval(x - 14, y - 14, x + 14, y + 14, fill = color)
        canvas.create_text(x, y - 22, text = f"Lifeboat {lifeboatId}", font = ("Arial", 12))
        canvas.create_text(x + 10, y + 35, text = f"Urgency: {urgencyFactor:.1f}\n" f'Number of people: {people}', font = ("Arial", 8))

        canvas.create_line(baseX, baseY, x, y, fill="black")
        mx = (baseX + x)/2
        my = (baseY + y)/2
        canvas.create_text(mx + 10, my - 10, text = f"{distance} km", font = ("Arial", 12, 'bold'), fill = "black")

    window.mainloop()







# ==================================== TEST ====================================

stack = [[2,2,2],[1,3,6],[4,7,10]]
D = 10
priorityStack, rescuedStack, D, totalPeople, rescuedPeople = lifeboatsRescue(stack, D)
tkinterMap(priorityStack, rescuedStack, totalPeople, rescuedPeople, D)
