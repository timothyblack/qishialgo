package OA_GS;

import java.util.HashSet;
import java.util.Set;

public class ReverseEquation {
    public static String reverse2(String s){
        StringBuilder sb = new StringBuilder();
        int j = 0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='+'||(s.charAt(i)=='-'&&(j!=i))||s.charAt(i)=='*'||s.charAt(i)=='/'){
                sb.insert(0,s.substring(j,i));
                j = i+1;
                sb.insert(0,s.charAt(i));
            }
        }
        sb.insert(0,s.substring(j,s.length()));
        return sb.toString();
    }

    public static String reverse(String str){
//        StringBuilder sb = new StringBuilder();

        Set<Character> lookUp = new HashSet<>();
        lookUp.add('*');
        lookUp.add('-');
        lookUp.add('+');
        lookUp.add('/');

        char[] arr = str.toCharArray();

        reverseArr(arr, 0, arr.length-1);

        int s = 0;

        int f = 0;

        for( ; f < arr.length; f++){

            if( lookUp.contains(arr[f]) ){

                if(arr[f] != '-'){

                    reverseArr(arr,s,f-1);

                    s = f+1;

                }else{

                    if(f == arr.length-1 || lookUp.contains( arr[f+1] ) ){

                        reverseArr(arr,s,f);

                        s = f+2;
                    }else{

                        reverseArr(arr,s,f-1);

                        s = f+1;

                    }

                }

            }else if(f>s && f == arr.length-1){

                reverseArr(arr, s, f);
            }

        }



        return new String(arr);
    }

    private static void reverseArr(char[] arr, int left, int right){

        while(left < right){

            char temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            left ++;
            right --;

        }
    }

    public static void main(String[] args) {
        // write your code here
        System.out.println(reverse("a+b*c-d/e"));
        System.out.println(reverse2("a+b*c-d/e"));
//
        System.out.println(reverse("20-3+5*2"));
        System.out.println(reverse2("20-3+5*2"));
//
        System.out.println(reverse("10*-10--20"));
        System.out.println(reverse2("10*-10--20"));

//        System.out.println(reverse("10"));
//        System.out.println(reverse2("10"));

        System.out.println(reverse("-12*2.4+-9.6--23.89"));
        System.out.println(reverse2("-12*2.4+-9.6--23.89"));

    }
}
