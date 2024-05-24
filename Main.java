import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Toys toys = new Toys();
        toys.add(1, "Doll", 10, 20);
        toys.add(2, "Teddy Bear", 5, 10);
        toys.add(3, "Blocks", 20, 65);
        toys.add(4, "Lego", 3, 5);
        toys.changeWeight(2, 40);
        
        for (int i = 0; i < 10; i++) {
            toys.draw();
            toys.getWonToy();
        }
        
    }
}