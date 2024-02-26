# I want to write program that will sign student into the attended.txt to later grade it.


from datetime import datetime

def signInSheet():
    i = 0  # counter
    attendance_data = []  # List to store attendance data

    def save_attendance():
        nonlocal i, attendance_data
        with open("attended.txt", "a") as file:
            now = datetime.now()
            current_day = now.strftime("%B %d")
            file.write("\n\n" + current_day + "\n")
            for attendance_record in attendance_data:
                i += 1
                file.write(f"{i} {attendance_record['name']} {attendance_record['pittID']} {attendance_record['timestamp']}\n")

    def printAttendanceStatistics():
        nonlocal attendance_data
        if not attendance_data:
            print("No attendance records available.")
            return

        attendance_stats = {}
        for record in attendance_data:
            if record['name'] in attendance_stats:
                attendance_stats[record['name']] += 1
            else:
                attendance_stats[record['name']] = 1

        print("\nAttendance Statistics:")
        for name, count in attendance_stats.items():
            print(f"{name}: {count} times")

    while True:
        try:
            checker = input("If you want to close sign-in sheet, press 0. Otherwise, press 1: ")
            if checker == "0":
                save_attendance()
                break
            elif checker == "1":
                userName = input("Please Enter your name: ")
                pittID = input("Enter your pittID: ")

                # Validate input
                if not userName or not pittID:
                    print("Invalid input. Please enter both name and pittID.")
                    continue

                now = datetime.now()
                current_datetime = now.strftime("%B %d %H:%M")
                print(f"Welcome to the class {userName} at {current_datetime}")

                # Add attendance record to the list
                attendance_data.append({
                    'name': userName,
                    'pittID': pittID,
                    'timestamp': current_datetime
                })

        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    signInSheet()
    printAttendanceStatistics()

