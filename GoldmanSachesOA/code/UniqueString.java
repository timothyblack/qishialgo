package OA_GS;

import java.util.*;

public class UniqueString {

    public static void main(String[] args){

        Solution sol = new Solution();

        String str = "caaab";


        System.out.println(Arrays.toString( sol.unique(str, 2) ));


    }
}


class Solution{

    public String[] unique(String str, int k){

        int start = 0;
        int end = start + k;
        List<String> res = new ArrayList<>();

        Set<String> set = new HashSet<>();


        while( end <= str.length() ){

            String cur = str.substring(start, end);

            if( set.add(cur) ){

                res.add(cur);
            }

            start++;
            end = start + k;
        }

        Collections.sort(res);

        String[] output = new String[res.size()];

        for(int i = 0; i< res.size(); i++){

            output[i] = res.get(i);
        }

        return output;


    }
}
