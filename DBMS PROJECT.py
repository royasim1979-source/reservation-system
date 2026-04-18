import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="railway_reservation_system"
)
cursor = conn.cursor()

print("----- Railway Reservation System -----")
print("1 => Book Train Ticket")
print("2 => Display My Records")
choice = int(input("Enter your choice: "))

# ------------------- OPTION 1: BOOK TRAIN -------------------
if choice == 1:
    print("The list of the train is given below:")
    print("1 => ABC")
    print("2 => STU")
    print("3 => UVW")
    print("4 => XYZ")
    print("5 => LMN")

    train = input("Enter the Name of the train you want to book:")
    train1 = train.lower()

    if train1 == "abc":
        print("The train will available only on Sunday")
        L1 = [1011, "Sunday", "Delhi", "Pune", "ABC"]
        str1 = "Insert into Train_List values (%s, %s, %s, %s, %s)"
        Date = "2025-12-01"
        cursor.execute("SELECT * FROM Train_List WHERE TrainNumber=%s", (L1[0],))
        result = cursor.fetchone()
        if not result:
            cursor.execute(str1, L1)
            conn.commit()

    elif train1 == "stu":
        print("The train will available on Monday and Friday.") 
        day = input("Enter the day of train booking:")
        if day == "Monday":
            L1 = [3601, "Monday", "Lucknow", "patna", "STU"]
            Date = "2025-12-21"
        elif day == "Friday":
            L1 = [3601, "Friday", "patna", "Lucknow", "STU"]
            Date = "2025-12-26"
        str1 = "Insert into Train_List values (%s, %s, %s, %s, %s)"
        cursor.execute("SELECT * FROM Train_List WHERE TrainNumber=%s", (L1[0],))
        result = cursor.fetchone()
        if not result:
            cursor.execute(str1, L1)
            conn.commit()

    elif train1 == "uvw":
        print("The train will available on Tuesday and Thursday.") 
        day = input("Enter the day of train booking:")
        if day == "Tuesday":
            L1 = [3770, "Tuesday", "Kharagpur", "Mumbai", "UVW"]
            Date = "2025-11-10"
        elif day == "Thursday":
            L1 = [3770, "Thursday", "Mumbai", "Kharagpur", "UVW"]
            Date = "2025-11-12"
        str1 = "Insert into Train_List values (%s, %s, %s, %s, %s)"
        cursor.execute("SELECT * FROM Train_List WHERE TrainNumber=%s", (L1[0],))
        result = cursor.fetchone()
        if not result:
            cursor.execute(str1, L1)
            conn.commit()

    elif train1 == "xyz":
        print("The train will available on saturday and wednesday.")
        day = input("Enter the day of train booking:")
        if day == "Saturday":
            L1 = [4401, "Saturday", "Kolkata", "chennai", "XYZ"]
            Date = "2025-11-20"
        elif day == "Wednesday":
            L1 = [4401, "Wednesday", "chennai", "kolkata", "XYZ"]
            Date = "2025-11-24"
        str1 = "Insert into Train_List values (%s, %s, %s, %s, %s)"
        cursor.execute("SELECT * FROM Train_List WHERE TrainNumber=%s", (L1[0],))
        result = cursor.fetchone()
        if not result:
            cursor.execute(str1, L1)
            conn.commit() 

    elif train1 == "lmn":
        print("The train will available on Friday and sunday.")
        day = input("Enter the day of train booking:")
        if day == "Friday":
            L1 = [2205, "Friday", "varanasi", "prayagraj", "LMN"]
            Date = "2025-11-30"
        elif day == "Sunday":
            L1 = [2205, "Sunday", "prayagraj", "varanasi", "LMN"]
            Date = "2025-11-25"
        str1 = "Insert into Train_List values (%s, %s, %s, %s, %s)"
        cursor.execute("SELECT * FROM Train_List WHERE TrainNumber=%s", (L1[0],))
        result = cursor.fetchone()
        if not result:
            cursor.execute(str1, L1)
            conn.commit() 
    else:
        print("OOPs...!Wrong choice...!")

    try:
        T_ID = int(open("project.txt").read())
    except:
        T_ID = 100

    T_ID += 1
    open("project.txt", "w").write(str(T_ID))
    Name = input("Enter your name:")
    Age = int(input("Enter your age:"))
    sex = input("Enter your Gender:")
    Address = input("Enter your address:")
    status = input("Enter your conformation of alloted set(Confrim/Hold):")
    category = input("Enter your category(GEN/AC):")
    BookDate = input("Enter the date of ticket booking:")
    l2 = [T_ID, Name, BookDate, Age, sex, Address, status, category]
    str2 = "Insert into passenger values (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(str2, l2)
    conn.commit()

    if category == "GEN":
        print("Your cost of fair is 500 rupees.")
        Fair = 500
    else:
        print("Your cost of fair is 1000 rupees.")
        Fair = 1000

    L3 = [L1[0], Fair]
    str3 = "Insert into Train_record values (%s, %s)"
    cursor.execute(str3, L3)
    conn.commit()

    TrainDate = Date
    if category == "GEN":
        seat = "General"
    else:
        seat = "AC"

    L4 = [L1[0], T_ID, TrainDate, seat]
    str4 = "Insert into train_status values (%s, %s, %s, %s)"
    cursor.execute(str4, L4)
    conn.commit()
    print("Thankyou..! Your booking is successful..")
    print("Your passenger ID is =",T_ID)

# ------------------- OPTION 2: DISPLAY RECORDS -------------------
elif choice == 2:
    passenger_name = input("Enter passenger name to view records: ")
    passenger_ID = input("Enter your Ticket number:")
    query = """
        SELECT p.T_ID, p.Name, p.Age, p.sex, p.Address, p.Status,
               p.Category, p.BookDate, t.TrainNumber, t.TrainName,
               tr.Fair, ts.TrainDate, ts.Seats
        FROM passenger p
        JOIN train_status ts ON p.T_ID = ts.T_ID
        JOIN Train_List t ON ts.TrainNumber = t.TrainNumber
        JOIN Train_record tr ON tr.TrainNumber = t.TrainNumber
        WHERE p.Name = %s and p.T_ID = %s;
    """
    cursor.execute(query, (passenger_name,passenger_ID))
    records = cursor.fetchall()
   # print(records)
    if records:
        print("\n--- Passenger Records ---")
        print("Passenger_ID:",records[0][0],"\nName:",records[0][1],"\nAge:",records[0][2],"\nsex:",records[0][3],"\nAddress:",records[0][4],"\nStatus:",records[0][5],
              "\nCategory:",records[0][6],"\nBookDate:",records[0][7],"\nTrainNumber:",records[0][8],"\nTrainName:",records[0][9],"\nFair:",records[0][10],
              "\nTrainDate:",records[0][11],"\nseat:",records[0][12])
    else:
        print("No records found for this passenger.")

else:
    print("Invalid choice!")

conn.close()

