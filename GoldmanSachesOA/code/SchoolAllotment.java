package OA_GS;

import java.util.*;

public class SchoolAllotment {

//    public static List<Integer> allocateSchools(List<Integer> schoolSeatsArray,
//                                                List<Integer> studentScoreArray,
//                                                List<List<Integer>> studentSchoolPreferencesArray) {
//
//
//
//        Map<Integer, Integer> score2Index = new TreeMap<>(new Comparator<Integer>() {
//            @Override
//            public int compare(Integer o1, Integer o2) {
//                return o2 - o1;
//            }
//        });
//
//        for (int i = 0; i < studentScoreArray.size(); i++) {
//            score2Index.put(studentScoreArray.get(i), i);
//        }
//
//        int studentNoSchool = 0;
//        for (Integer index: score2Index.values()) {
//            List<Integer> perference = studentSchoolPreferencesArray.get(index);
//            int count = 0;
//            for (int p: perference) {
//                if (schoolSeatsArray.get(p) > 0) {
//                    schoolSeatsArray.set(p, schoolSeatsArray.get(p) - 1);
//                    break;
//                } else {
//                    count++;
//                }
//            }
//            if(count >= perference.size()) {
//                studentNoSchool++;
//            }
//        }
//
//        int seatsNoFill = 0;
//        for (Integer seats: schoolSeatsArray) {
//            seatsNoFill += seats;
//        }
//
//        List<Integer> result = new ArrayList<>();
//        result.add(seatsNoFill);
//        result.add(studentNoSchool);
//        return result;
//    }


    public static List<Integer> allocateSchools(List<Integer> schoolSeatsArray,
                                                List<Integer> studentScoreArray,
                                                List<List<Integer>> studentSchoolPreferencesArray){



        Student[] students = new Student[studentScoreArray.size()];

        for(int i = 0; i < studentScoreArray.size() ; i++){

            students[i] = new Student(0, studentScoreArray.get(i), studentSchoolPreferencesArray.get(i));
        }

        Arrays.sort(students, new Comparator<Student>(){

            @Override
            public int compare(Student i1, Student i2){

                if( i1.score == i2.score){

                    return 0;
                }else{

                    return i1.score > i2.score ? -1:1;
                }

            }

        });


        int[] studentUnassigned = {students.length};

        for(Student stu : students){

            if( !updateSchool(stu, schoolSeatsArray, 0, studentUnassigned) ){

                if( !updateSchool(stu, schoolSeatsArray, 1, studentUnassigned) ){

                    updateSchool(stu, schoolSeatsArray, 2, studentUnassigned);

                }

            }
        }


        int count = 0;

        for(Integer seat: schoolSeatsArray){

            count += seat;
        }

        List<Integer> res = new ArrayList<>();
        res.add(count);
        res.add(studentUnassigned[0]);

        return res;
    }

    private static boolean updateSchool(Student stu, List<Integer> schoolSeatsArray, int schoolIdx, int[] studentUnassigned){

        if( schoolSeatsArray.get( stu.preferedSchool.get(schoolIdx) ) > 0) {

            studentUnassigned[0]--;
            schoolSeatsArray.set(stu.preferedSchool.get(schoolIdx),
                    schoolSeatsArray.get( stu.preferedSchool.get(schoolIdx) ) - 1);

            return true;
        }

        return false;
    }


    static class Student{

        int id;
        int score;
        List<Integer> preferedSchool;

        Student(int id, int score, List<Integer> preferedSchool){

            this.id = id;
            this.score = score;
            this.preferedSchool = preferedSchool;
        }
    }


    public static void main(String[] args) {
        List<Integer> schoolSeatsArray = Arrays.asList(1,3,1,2);
        List<Integer> studentScoreArray = Arrays.asList(990,780,830,860,920);
        List<List<Integer>> studentSchoolPrefArray = new ArrayList<>();
        studentSchoolPrefArray.add(Arrays.asList(3,2,1));
        studentSchoolPrefArray.add(Arrays.asList(2,0,0));
        studentSchoolPrefArray.add(Arrays.asList(2,0,1));
        studentSchoolPrefArray.add(Arrays.asList(0,1,3));
        studentSchoolPrefArray.add(Arrays.asList(0,2,3));
        System.out.println(allocateSchools(schoolSeatsArray,studentScoreArray,studentSchoolPrefArray));
    }
}
