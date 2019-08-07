package OA_GS;

public class Compress {


    public static void main(String[] args){

        Comps s = new Comps();

        String res = s.cps("haaaaaaaaaaabb");

        System.out.println(res);

    }

}

class Comps{


    public String cps(String str){


        if(str == null || str.length() == 0){

            return "";
        }

        char[] arr = str.toCharArray();

        int s = 0;
        int f = 0;


        while(f < arr.length){

            int count = 1;
            while(f+1 < arr.length && arr[f+1] == arr[f]){

                count++;
                f++;
            }

            if(count == 1){
                count = 0;
            }

            arr[s++] = arr[f++];


            StringBuilder cur = new StringBuilder();

            for(int i = count; i > 0;i /= 10){

                cur.append( (char)(i%10 + '0') );

            }

            for(int i = cur.length()-1;i>=0;i--){
                arr[s++] = cur.charAt(i);
            }


        }

        return new String(arr,0,s);
    }
}