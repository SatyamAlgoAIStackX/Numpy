import numpy as np
months = np.array(["jan", "fab", 'mar','apr',"may", "june", "july", "aug", "sept", "oct", "nov","dec"])
sales=[]
print("Enter product sales per month in $: ")
for month in months:
    value = float(input(f"{month}: "))
    sales.append(value)
sales=np.array(sales)
print("\n---Company Sales Annalysis---")
print("Total sales of the year: ",np.sum(sales),"$")
print("Average Monthly sales: ",np.mean(sales), "$")
print("Maximmum Sales; ",np.max(sales), "$")
print("Mimimum Sales: ",np.min(sales),"$")

best_month= months[np.argmax(sales)]
worst_month= months[np.argmin(sales)]
print("Best Month: ",best_month)
print("Worst Month: ",worst_month)

above_avg= months[sales>np.mean(sales)]
below_avg= months[sales<np.mean(sales)]
print("Above Average MOnth: ",above_avg)
print("Below Average Month: ",below_avg)