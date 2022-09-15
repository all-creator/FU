package com.lab2;

public class Employee {
    int id;
    String name;
    String lastName;
    String dateOfBirth;
    String locationOfBirth;
    int salary;
    boolean isMarried;

    public Employee(int id, String name, String lastName, String dateOfBirth, String locationOfBirth, int salary, boolean isMarried) {
        this.id = id;
        this.name = name;
        this.lastName = lastName;
        this.dateOfBirth = dateOfBirth;
        this.locationOfBirth = locationOfBirth;
        this.salary = salary;
        this.isMarried = isMarried;
    }

    public Employee(int id) {
        this.id = id;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getDateOfBirth() {
        return dateOfBirth;
    }

    public void setDateOfBirth(String dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    public String getLocationOfBirth() {
        return locationOfBirth;
    }

    public void setLocationOfBirth(String locationOfBirth) {
        this.locationOfBirth = locationOfBirth;
    }

    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }

    public boolean isMarried() {
        return isMarried;
    }

    public void setMarried(boolean married) {
        isMarried = married;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Employee employee = (Employee) o;

        return getId() == employee.getId();
    }

    @Override
    public int hashCode() {
        return getId();
    }

    @Override
    public String toString() {
        return "Employee: " +
                "id=" + id +
                ", name='" + name + '\'' +
                ", lastName='" + lastName + '\'' +
                ", dateOfBirth='" + dateOfBirth + '\'' +
                ", locationOfBirth='" + locationOfBirth + '\'' +
                ", salary=" + salary +
                ", isMarried=" + isMarried;
    }
}
