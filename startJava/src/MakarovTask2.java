import java.util.Random;

public class MakarovTask2 {
    public static void main(String[] args) {
//Задача 2
            Random rand = new Random();
            int num = rand.nextInt(21)-10;
            if (num<0){
                num *= -1;
            }
            System.out.println(num);
    }
}
