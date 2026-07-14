
import csv
import os
from datetime import datetime

FILE = "expenses.csv"
HEADERS = ["id","date","description","amount","category"]

def ensure_file():
    if not os.path.exists(FILE):
        with open(FILE,"w",newline="") as f:
            csv.writer(f).writerow(HEADERS)

def next_id():
    ensure_file()
    with open(FILE,"r") as f:
        rows=list(csv.reader(f))
    return len(rows)

def add_expense():
    desc=input("Description: ").strip()
    cat=input("Category: ").strip()
    amt=input("Amount: ").strip()
    if desc=="" or cat=="":
        print("Description/Category cannot be empty")
        return
    try:
        amt=float(amt)
    except:
        print("Amount must be numeric")
        return
    row=[next_id(),datetime.now().strftime("%Y-%m-%d"),desc,f"{amt:.2f}",cat.title()]
    with open(FILE,"a",newline="") as f:
        csv.writer(f).writerow(row)
    print("Expense Added Successfully")

def view_all():
    ensure_file()
    with open(FILE,"r") as f:
        rows=list(csv.reader(f))
    if len(rows)==1:
        print("No expenses found")
        return
    print("\nID\tDATE\t\tDESCRIPTION\tAMOUNT\tCATEGORY")
    print("-"*60)
    total=0
    count=0
    for r in rows[1:]:
        print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}")
        total+=float(r[3]); count+=1
    print("-"*60)
    print("Total Records:",count)
    print("Total Amount:",round(total,2))

def search_category():
    cat=input("Enter Category: ").lower()
    ensure_file()
    with open(FILE,"r") as f:
        rows=list(csv.reader(f))[1:]
    total=0
    found=False
    for r in rows:
        if r[4].lower()==cat:
            found=True
            print(r)
            total+=float(r[3])
    if found:
        print("Category Total:",round(total,2))
    else:
        print("No Record Found")

def monthly_total():
    month=input("Enter Month (YYYY-MM): ")
    ensure_file()
    with open(FILE,"r") as f:
        rows=list(csv.reader(f))[1:]
    total=0
    for r in rows:
        if r[1].startswith(month):
            total+=float(r[3])
    print("Monthly Total:",round(total,2))

def delete_id():
    did=input("Enter ID: ")
    ensure_file()
    with open(FILE,"r") as f:
        rows=list(csv.reader(f))
    new=[rows[0]]
    found=False
    for r in rows[1:]:
        if r[0]==did:
            found=True
        else:
            new.append(r)
    with open(FILE,"w",newline="") as f:
        csv.writer(f).writerows(new)
    if found:
        print("Expense Deleted")
    else:
        print("ID Not Found")

def run():
    ensure_file()
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All")
        print("3. Search by Category")
        print("4. Monthly Total")
        print("5. Delete by ID")
        print("6. Exit")
        ch=input("Enter Choice: ")
        if ch=="1":
            add_expense()
        elif ch=="2":
            view_all()
        elif ch=="3":
            search_category()
        elif ch=="4":
            monthly_total()
        elif ch=="5":
            delete_id()
        elif ch=="6":
            print("Thank You")
            break
        else:
            print("Invalid Choice")

if __name__=="__main__":
    run()
