
abstract class Vehicle {
    // Abstract methods (what it can do)
    abstract void accelerate();

    abstract void brake();

    // Concrete method (common to all vehicles)
    void startEngine() {
        System.out.println("Engine started!");
    }
}

class Car extends Vehicle {
    @Override
    void accelerate() {
        System.out.println("Car: Pressing gas pedal...");

    }

    @Override
    void brake() {
        System.out.println("Car: Applying brakes...");
        // Hidden logic: hydraulic pressure, brake pads, etc.
    }
}

public class abstraction {

    public static void main(String[] args) {
        System.out.println("Abstraction");
        Vehicle myCar = new Car();
        myCar.startEngine();
    }
}
