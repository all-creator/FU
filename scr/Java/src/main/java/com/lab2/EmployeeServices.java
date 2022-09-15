package com.lab2;

import java.util.HashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;

public class EmployeeServices {
    private static final Set<Employee> employeeList = new HashSet<>();

    public static void addInSetEmployee(Employee employee){
        if (employeeList.size() < 100) employeeList.add(employee);
        else System.out.println("невозможно добавить больше 100 сотрудников");
    }

    public static Set<Employee> getEmployeeList() {
        return employeeList;
    }

    public static Employee getEmployeeById(int id) {
        return employeeList.stream().filter(e -> e.getId() == id).findFirst().orElse(null);
    }

    public static void getEmployeeByIdAndPrint(int id) {
        System.out.println(getEmployeeById(id));
    }

    public static int getEmployeeCosts() {
        return employeeList.stream().reduce(0, (s, e) -> s + e.getSalary(), Integer::sum);
    }

    public static List<Employee> getEmployeeByDate(String date) {
        return employeeList.stream().filter(e -> Objects.equals(e.getDateOfBirth(), date)).toList();
    }

    public static List<Employee> getEmployeeByName(String name) {
        return employeeList.stream().filter(e -> Objects.equals(e.getName(), name)).toList();
    }
}
