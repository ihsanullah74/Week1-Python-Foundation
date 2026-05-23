#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Student Management System

students = []

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    grade = input("Enter Student Grade: ")
    students.append({"id": student_id, "name": name, "age": age, "grade": grade})
    print("Student added successfully!")

def view_all_students():
    if len(students) == 0:
        print("No students found!")
    else:
        print("\n===== All Students =====")
        for s in students:
            print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']}")

def search_student():
    keyword = input("Enter Student ID or Name to search: ")
    found = False
    for s in students:
        if s['id'] == keyword or s['name'].lower() == keyword.lower():
            print(f"Found → ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']}")
            found = True
    if not found:
        print("Student not found!")

def update_student():
    student_id = input("Enter Student ID to update: ")
    for s in students:
        if s['id'] == student_id:
            s['name'] = input("Enter new name: ")
            s['age'] = int(input("Enter new age: "))
            s['grade'] = input("Enter new grade: ")
            print("Student updated successfully!")
            return
    print("Student not found!")

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    for s in students:
        if s['id'] == student_id:
            students.remove(s)
            print("Student deleted successfully!")
            return
    print("Student not found!")

def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main()


# In[ ]:




