import java.util.Scanner;

public class MakarovTask5 {
    public static void main(String[] args) {
//Задача 5
            Scanner sc = new Scanner(System.in);
            System.out.print("Введите предложение: ");
            String sentence = sc.nextLine();
            sc.close();
            String[] words = sentence.split("[\\s.,!?]+");
            String longWord = words[0];
            String shortWord = words[0];
            for (int i = 1; i < words.length; i++) {
                if (words[i].length() > longWord.length()) {
                    longWord = words[i];
                }
                if (words[i].length() < shortWord.length()) {
                    shortWord = words[i];
                }
            }
            System.out.println("Самое длинное слово: " + longWord + " длина: " + longWord.length());
            System.out.println("Самое короткое слово: " + shortWord + " длина: " + shortWord.length());
    }
}
