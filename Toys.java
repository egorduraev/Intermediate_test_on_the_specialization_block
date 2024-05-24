import java.io.IOException;
import java.util.List;
import java.util.ArrayList;
import java.util.Random;
import java.io.FileWriter;

public class Toys {
    private List<Toy> toys;
    private List<Toy> wonToys;

    public Toys() {
        toys = new ArrayList<>();
        wonToys = new ArrayList<>();
    }

    public void add(int id, String name, int amount, float weight) {
        Toy toy = new Toy(id, name, amount, weight);
        toys.add(toy);
    }

    public void changeWeight(int id, float weight) {
        for (Toy toy : toys) {
            if (toy.getId() == id) {
                toy.setWeight(weight);
                break;
            }
        }
    }

    public void draw() {
        float sum = 0;
        for (Toy toy : toys) {
            sum += toy.getWeight();
        }

        Random rand = new Random();
        float randomNumber = rand.nextFloat() * sum;

        Toy wonToy = null;
        for (Toy toy : toys) {
            if (randomNumber < toy.getWeight()) {
                wonToy = toy;
                break;
            }
            randomNumber -= toy.getWeight();
        }

        if (wonToy != null && wonToy.getAmount() > 0) {
            wonToys.add(wonToy);
            wonToy.setAmount(wonToy.getAmount() - 1);
        }
    }

    public void getWonToy() throws IOException {
        if (wonToys.size() > 0) {
            Toy wonToy = wonToys.remove(0);

            FileWriter writer = new FileWriter("prize_toys.txt", true);
            writer.write(wonToy.getId() + "," + wonToy.getName() + "\n");
            writer.close();
        }
    }
}