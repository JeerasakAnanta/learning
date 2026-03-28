
public class Encapsulation {
    private int id;
    private String name;

    // setter mehtod
    public void setId(int id) {
        this.id = id;

    }

    public void setName(String name) {
        this.name = name;

    }

    public String getname() {
        return name;
    }

    public int getid() {
        return id;
    }

    public static void main(String[] args) {
        System.out.println("Encapsulation");

        Encapsulation encapsulation = new Encapsulation();
        encapsulation.setId((001));
        encapsulation.setName("Jeerasak");

        System.out.println("user ID  :" + encapsulation.getid());
        System.out.println("user Name :" + encapsulation.getname());

    }
}
