package OA_GS;

import javax.security.auth.login.AccountException;
import java.util.ArrayList;
import java.util.List;

public class CommentRemoverII {
    public static String commentRemover1(List<String> inputs) {
        if (inputs == null) {
            return null;
        }

        StringBuilder result = new StringBuilder();
        boolean blocked = false;
        StringBuilder blockcomment = new StringBuilder();

        int newLines = 0;

        for (String line: inputs) {
            for (int i = 0; i < line.length(); i++) {

                if (!blocked) { // not in block
                    if (line.charAt(i) == '/' && i != line.length() - 1
                            && line.charAt(i + 1) == '/') {
                        result.append(" ");
                        break;
                    } else if (line.charAt(i) == '/' && i != line.length() - 1
                            && line.charAt(i + 1) == '*') {

                        blockcomment.append(line.charAt(i));
                        blocked = true;
                    } else {
                        result.append(line.charAt(i));
                    }
                } else { //in block
                    if (line.charAt(i) == '*' && i != line.length() - 1
                            && line.charAt(i + 1) == '/') {

                        while(newLines>0){

                            result.append("\n");
                            newLines --;
                        }
                        result.append(" ");

                        blockcomment.setLength(0);
                        blocked = false;
                        i++;
                    } else {
                        blockcomment.append(line.charAt(i));
                        if (i == line.length() - 1) {
                            blockcomment.append("\n");
                            newLines++;
                        }
                    }
                }
            }

            if(!blocked) {
                result.append("\n");
            }

        }

        return result.toString()+blockcomment.toString();
    }

    // this version has minor problem
    public static String commentRemover2(List<String> inputs) {
        if (inputs == null) {
            return null;
        }
        StringBuilder result = new StringBuilder();
        boolean blocked = false;
        StringBuilder blockcomment = new StringBuilder();
        int count = 0;
        for (String line: inputs) {
            for (int i = 0; i < line.length(); i++) {
                if (!blocked) { // not in block
                    if (line.charAt(i) == '/' && i != line.length() - 1
                            && line.charAt(i + 1) == '/') {
                        result.append(" ");
                        result.append("\n");
                        break;
                    } else if (line.charAt(i) == '/' && i != line.length() - 1
                            && line.charAt(i + 1) == '*') {
                        blockcomment.append(line.charAt(i));
                        blockcomment.append(line.charAt(i+1));
                        i++;
                        blocked = true;
                    } else {
                        result.append(line.charAt(i));
                        if(i==line.length()-1) result.append("\n");
                    }
                } else { //in block
                    if (line.charAt(i) == '*' && i != line.length() - 1
                            && line.charAt(i + 1) == '/') {
                        for(int a=count;a>0;a--){
                            result.append("\n");
                        }
                        result.append(" ");
                        blockcomment.setLength(0);
                        blocked = false;
                        count = 0;
                        i++;
                    } else {
                        blockcomment.append(line.charAt(i));
                        if (i == line.length() - 1) {
                            blockcomment.append("\n");
                            count++;
                        }
                    }
                }
            }
        }
        if(blockcomment.length()!=0) result.append(blockcomment);
        return result.toString();
    }

    public static void main(String[] args) {

        String s1 = "public class HelloWorld {";
        String s2 = "//This program will ";
        String s3 = "public static void main(String[] args) {";
        String s4 = "System.out.println(\"Hello/*, World*/\");// a comment";
        String s5 = "/* a sample ";
        String s6 = "spanning multiple ";
        String s7 = "lines*/";
        String s8 = "/*}";
        String s9 = "}";

        List<String> inputs = new ArrayList<>();
        inputs.add(s1);
        inputs.add(s2);
        inputs.add(s3);
        inputs.add(s4);
        inputs.add(s5);
        inputs.add(s6);
        inputs.add(s7);
        inputs.add(s8);
        inputs.add(s9);


        System.out.print(commentRemover2(inputs));
        System.out.print(commentRemover1(inputs));
        System.out.print("finished");


    }
}
