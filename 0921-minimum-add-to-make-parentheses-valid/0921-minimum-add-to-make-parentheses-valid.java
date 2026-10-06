class Solution {
    public int minAddToMakeValid(String s) {
        int op = 0;
        int a=0,b=0;
        int on=0;
        for(char i : s.toCharArray())
        {
            System.out.println("i="+i+" A="+a+" B="+b);
            if(i=='(') 
            {
                on=1;
                a++;
            }
            else if (i==')'&& on==1)
            {
                a--;
            }
            else if (i==')'&& on == 0)
            {
                b++;
            }
            if(a<1) on=0;
        }
        if(a<1) a*=-1;
        op = op+a+b;
        return op;
    }
}