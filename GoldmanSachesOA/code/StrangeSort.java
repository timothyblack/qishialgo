package OA_GS;

import java.util.*;

public class StrangeSort {

    public static void main(String[] args){

        List<String> nums = Arrays.asList("990","332","32");
        List<Integer> lookup = Arrays.asList(3,5,4,6,2,7,9,8,0,1);

        List<String> output = helper(nums, lookup);

        System.out.println(output.toString());

    }


    private static List<String> helper(List<String> nums, List<Integer> lookup){

        // number : index
        Map<Integer, Integer> lookupMap = new HashMap<>();
        List<String> finalResult = new ArrayList<>();
        List<Two> newNums = new ArrayList<>();

        for(int i = 0; i < lookup.size(); i++){

            lookupMap.put(lookup.get(i), i);
        }

        for(int i = 0; i < nums.size(); i++){

            String current = nums.get(i);
            StringBuilder sb = new StringBuilder();

            for(int j = 0; j<current.length(); j++){

                sb.append( (char)( '0' + lookupMap.get( (int)(current.charAt(j)-'0') ) ) );
            }


            Two t = new Two();
            t.oldOne = current;
            t.newOne = sb.toString();
            newNums.add(t);
        }

        // sort newNums using newOne field

        Collections.sort(newNums, new Comparator<Two>(){

            @Override
            public int compare(Two t1, Two t2){

                int n1 = Integer.parseInt(t1.newOne);
                int n2 = Integer.parseInt(t2.newOne);

                return n1 - n2;
            }
        });



        for(int i = 0; i < nums.size(); i++){

            finalResult.add(newNums.get(i).oldOne);
        }

        return finalResult;

    }

    static class Two{

        public String oldOne;
        public String newOne;
    }
}
