package OA_GS;

import java.util.Arrays;
import java.util.Comparator;

public class Chartiy {

    public static void main(String[] args){

        CC c = new CC();

        String[] res = c.cc(new int[]{25,8,2,35,15,120,55,42});

        System.out.println( Arrays.toString(res) );
    }
}

class CC{

    public String[] cc(int[] arr){

        Entity a = new Entity(0,"A");
        Entity b = new Entity(0,"B");
        Entity c = new Entity(0,"C");

        Entity[] all = new Entity[3];
        all[0] = a;
        all[1] = b;
        all[2] = c;


        String[] res = new String[arr.length];


        for(int i = 0; i < arr.length; i++){

            sort(all);

            System.out.print(all[0].name+'\t');
            System.out.println(all[0].money);

            all[0].money += arr[i];

            res[i] = all[0].name;

        }

        return res;


    }

    public void sort(Entity[] all){

        Arrays.sort(all, new Comparator<Entity>(){

            @Override
            public int compare(Entity e1, Entity e2){

                if(e1.money == e2.money){

                    return e1.name.compareTo(e2.name);

                }else{

                    return e1.money < e2.money ? -1:1 ;
                }
            }
        });
    }

    class Entity{

        int money = 0;
        String name;

        Entity(int money, String name){

            this.name = name;
            this.money = money;

        }

    }
}
