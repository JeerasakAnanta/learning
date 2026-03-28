public class Empleoyee {
    private String name;
    private float salary;

    // Constructor
    public Empleoyee(String name, float salary) {
        this.name = name;
        this.salary = salary;
    }

    // getters method
    public String getName() {
        return name;
    }

    public float getSalary() {
        return salary;
    }

    // setters mehod
    public void setName(String name) {
        this.name = name;
    }

    public void setSalary(float salary) {
        this.salary = salary;
    }

    // instance mehod
    public void displayDetatils() {
        System.out.println("Emplyee : " + name);
        System.out.println("Salary  : " + salary);
    }

    public static void main(String[] args) {
        System.out.println("this is Class  ");

        Empleoyee emp = new Empleoyee("Jeerasak", 25000.f);
        emp.displayDetatils();
    }
}
