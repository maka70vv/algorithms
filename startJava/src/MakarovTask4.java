import java.util.Scanner;

public class MakarovTask4 {
    public static void main(String[] args) {
//Задача 4
            Scanner sc = new Scanner(System.in);
            System.out.print("Введите строку: ");
            String str = sc.nextLine();
            System.out.print("Введите подстроку, которую нужно заменить: ");
            String oldSubstr = sc.nextLine();
            System.out.print("Введите новую подстроку: ");
            String newSubstr = sc.nextLine();
            sc.close();
            String newStr = str.replaceAll(oldSubstr, newSubstr);
            System.out.println("Результат: " + newStr);
    }
}
