package OA_GS;

import java.util.HashMap;
import java.util.Map;

public class CountPairsWithGivenSum {


    public static void main(String[] args){

        CPS s = new CPS();

//        int[] arr = {10, 12, 10, 15, -1, 7, 6,
//                5, 4, 2, 1, 1, 1};

        int[] arr = {1,1,1,1};

        int res = s.getPairsCount(arr,2);

        System.out.println(res);

    }
}

class CPS{

    public int getPairsCount(int[] arr, int sum){


        int twiceCount = 0;

        Map<Integer, Integer> map = new HashMap<>();

        for(int i : arr){

            Integer num = map.get(i);

            if(num == null){

                map.put(i,1);

            }else{

                map.put(i, num+1);
            }
        }

        for(int i : arr){

            if( map.containsKey(sum - i) ){

                twiceCount += map.get(sum - i);
            }

            if( sum - i == i){
                twiceCount --;
            }
        }


        return twiceCount/2;
    }


}
