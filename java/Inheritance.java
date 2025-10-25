class Animal {
    void eat() {
        System.out.println("Animal is eating...");
    }

    void sleep() {
        System.out.println("Animal is sleeping...");
    }
}

class Dog extends Animal {
    void brake() {
        System.out.println("Dog is barking!");
    }
}

public class Inheritance {
    public static void main(String[] args) {
        /*
         * intheriace is an important pillar of oop (Objct oriented programming)
         * is tis hte mechainsm java by wihc one class is allowed to inherit the
         * feature (files and methods) of anohter calss. we are achiceing
         * inheriace by using extnds keyword inheriace is alos know as "is-a"
         * example Dog cat cow and Derived class of animal ase class
         * Superclass : calss whose features s are inherited is knows asn superclass
         * Subclass : class that inerits the oher class is known as subclass
         * Reuasbility : interitances suports the concept of "reusability" i.e when we
         * want tocreate
         * a new class and sther is already a clss that incudes
         * some of the code
         */
        System.out.println("=========== Inheritance ===========");
        Dog myDog = new Dog();

    }
}
