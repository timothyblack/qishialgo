package OA_GS;

public class SecondSmall {

    public static void main(String[] args){

        Sol s = new Sol();



        System.out.println( s.second(new int[] {1,4,2,3,-1}) );

    }
}

class Sol{

    public int second(int[]arr){


        // corner case: arr.length < 2 pr == null
        // max()
        int min = Integer.MAX_VALUE;
        int second = Integer.MAX_VALUE;

        for(int i: arr){

            if(i < second){

                second = i;

                if(i < min){

                    second = min;
                    min = i;

                }

            }
        }

        // say, negative one stands for no secondary small value
        return second == Integer.MAX_VALUE ? -1: second;
    }
}
