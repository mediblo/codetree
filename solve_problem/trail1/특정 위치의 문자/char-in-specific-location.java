import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        char[] data = new char[]{'L', 'E', 'B', 'R', 'O', 'S'};
        int num = -1;
        Scanner sc = new Scanner(System.in);
        char inp = sc.next().charAt(0);

        for(int i=0; i<data.length; i++){
            if (data[i] == inp){
                num = i;
                break;
            }
        }

        System.out.print(num != -1 ? num : "None");
    }
}