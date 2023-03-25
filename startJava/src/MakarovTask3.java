import java.util.Scanner;

public class MakarovTask3 {
    public static void main(String[] args) {
        //Задача 3
        Scanner sc = new Scanner(System.in);
        System.out.print("Введите значение a: ");
        double a = sc.nextDouble();
        System.out.print("Введите значение b: ");
        double b = sc.nextDouble();
        System.out.print("Введите значение c: ");
        double c = sc.nextDouble();
        sc.close();
        double D = b * b - 4 * a * c;
        if (a == 0) {
            System.out.println("a не может быть равно 0");
        } else if (D > 0) {
            double root1 = (-b + Math.sqrt(D)) / (2 * a);
            double root2 = (-b - Math.sqrt(D)) / (2 * a);
            System.out.println("Корни уравнения: " + root1 + " и " + root2);
        } else if (D == 0) {
            double root = -b / (2 * a);
            System.out.println("Корень уравнения: " + root);
        } else {
            System.out.println("Корней нет");
        }
    }
}
