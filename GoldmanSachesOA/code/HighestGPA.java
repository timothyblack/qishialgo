package OA_GS;

import java.util.*;

public class HighestGPA {

    public static void main(String[] args){

        AvgGpa sol = new AvgGpa();

        String[][] str = {{"bob","88"},{"jj","100"},{"jj","113"}};


        System.out.println(sol.score(str));


        String[] arr = {"aaa","aa","bb","c","a"};

        Arrays.sort(arr, new Comparator<String>(){

            @Override
            public int compare(String s1, String s2) {

                if (s1.length() == s2.length()) {

                    return s1.compareTo(s2);
                } else {

                    return s1.length() < s2.length() ? -1 : 1;
                }
            }
        });

//        Arrays.sort(arr);

        System.out.println(Arrays.toString(arr));


    }


}


class AvgGpa{

    public double score(String[][] str){

        Map<String, List<String>> map = new HashMap<>();

        for(String[] unit : str){

            String curName = unit[0];

            if( map.containsKey(curName) ){

                map.get(curName).add(unit[1]);
            }else{

                List<String> curScore = new ArrayList<>();
                curScore.add(unit[1]);

                map.put(curName, curScore);
            }
        }

        double maxGpa = Integer.MIN_VALUE;

        for( Map.Entry<String, List<String>> entry : map.entrySet() ){

            List<String> curScore = entry.getValue();

            double curSum = 0;
            for(String s: curScore) {
                curSum += Double.parseDouble(s);
            }

            double curAvg = curSum / curScore.size();

            if(curAvg > maxGpa){

                maxGpa = curAvg;
            }
        }

        return maxGpa;
    }
}