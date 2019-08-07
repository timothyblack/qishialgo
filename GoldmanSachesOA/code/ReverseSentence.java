package OA_GS;

public class ReverseSentence {

    public static void main(String[] args){

        String str = "Abc, k3e love";
        String res = reverse(str);

        System.out.println(res);
    }


    public static String reverse(String str){

        char[] arr = str.toCharArray();

        reversePart(arr, 0, arr.length-1);

        int s = 0;
        int f = 0;

        while(f < arr.length){

            if(arr[f] == ' '){

                reversePart(arr, s, f-1);
                s = f+1;
            }else if(f == arr.length-1){

                reversePart(arr, s, f);
            }

            f++;
        }

        return new String(arr);

    }

    private static void reversePart(char[] arr, int left, int right){

        while(left < right){

            char temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            left ++;
            right --;
        }

    }
}
