package OA_GS;

public class CapLock {

    public static String CapLock(String str){


        StringBuilder res = new StringBuilder();

        boolean capOn = false;

        for(int i = 0; i < str.length(); i++){

            char cur = str.charAt(i);

            if(!Character.isLetter(cur)){

                res.append(cur);

            }else {

                if (str.charAt(i) != 'a') {

                    if (capOn) {

                        res.append( (char)(str.charAt(i) + ('A' - 'a')) );

                    } else {

                        res.append(str.charAt(i));
                    }

                } else {

                    if (!capOn) {

                        capOn = true;

                    }else{

                        capOn = false;
                    }
                }

            }
        }

        return res.toString();
    }

    public static void main(String[] args){

//        String res = CapLock.CapLock("\"Baa, Baa!\", said the sheep!");

        String res = CapLock.CapLock("my keyboard is broken!");
        System.out.println(res);

    }


}
