public class Toy {
    private int id;
    private String name;
    private int amount;
    private float weight;

    public Toy(int id, String name, int amount, float weight) {
        this.id = id;
        this.name = name;
        this.amount = amount;
        this.weight = weight;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getAmount() {
        return amount;
    }

    public double getWeight() {
        return weight;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public void setWeight(float weight) {
        this.weight = weight;
    }
}