import java.util.*;

public class waterMelon{
    public static void main(String[] args){
        
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        if(n>2 && n % 2==0){
            System.out.println("yes");
        }
        else{
            System.out.println("No");
        }
    }
}