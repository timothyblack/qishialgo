package OA_GS;

import java.util.ArrayList;
import java.util.List;

public class CommentI {

    public static void main(String[] args){

        Com c = new Com();

        String[] strs = {"a/*comment", "line", "more_comment*/b"};

        c.removeComments(strs);
    }

}


class Com {
    public List<String> removeComments(String[] source) {

        List<String> res = new ArrayList<>();
        boolean mode = false;
        StringBuilder cur = new StringBuilder();

        for(String str : source){

            for(int i = 0; i < str.length(); i++){

                if(mode){

                    if(str.charAt(i) == '*' && i+1<str.length() &&
                            str.charAt(i+1) == '/'){

                        mode = false;
                        i++;
                    }

                }else{

                    if(str.charAt(i) == '/' && i+1 < str.length() &&
                            str.charAt(i+1) == '*'){

                        mode = true;
                        i++;

                    }else if(str.charAt(i) == '/' && i+1 < str.length() &&
                            str.charAt(i+1) == '/'){

                        break;

                    }else{

                        cur.append( str.charAt(i) );
                    }
                }

            }

            if(!mode && cur.length() > 0){
                res.add(cur.toString());

                cur = new StringBuilder();
            }

        }


        return res;


    }
}