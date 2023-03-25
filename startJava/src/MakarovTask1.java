import java.util.Scanner;

public class MakarovTask1 {
    public static void main(String[] args) {
//Задача 1
        Scanner sc = new Scanner(System.in);
        System.out.print("Введите длину стороны a: ");
        double a = sc.nextDouble();
        sc.close();
        double area = (Math.sqrt(3) / 4) * a * a;
        double perimeter = 3 * a;
        System.out.println("Площадь треугольника: " + area);
        System.out.println("Периметр треугольника: " + perimeter);
    }
}
