package OA_GS;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class WholeMinuteDilamma {
    public static int wholeMinDilamma(List<Integer> inputs) {
        if (inputs == null || inputs.size() <= 1) {
            return 0;
        }

        Map<Integer, Integer> map = new HashMap<>();
        for (Integer time: inputs) {
            int remainder = time % 60;
            if (remainder != 0) {
                if (map.containsKey(remainder)) {
                    map.put(remainder, map.get(remainder) + 1);
                } else {
                    map.put(remainder, 1);
                }
            }
            else{
                map.put(0,map.getOrDefault(0,0)+1);
            }
        }

        int count = 0;
        for (Integer key: map.keySet()) {
            if(key==0){
                if(map.get(0)>1){
                    count += (map.get(0)-1)*map.get(0);
                }
            }
            else{
                int subset = 60 - key;
                if (map.get(subset) != null) {
                    int num = map.get(subset);
                    if (subset == key) {
                        num--;
                    }
                    count += map.get(key)*num;
                }
            }
        }
        return count / 2;
    }

    public static void main(String[] args) {
        List<Integer> input = Arrays.asList(10,20,60,50,40,30,30,30);
        int output = wholeMinDilamma(input);
        System.out.println(output);

    }
}
