import java.util.*;
class program 
{
    public static void main()
    {
        Scanner sc=new Scanner(System.in);
        String s=sc.nextLine();
        Stack <Character> st=new Stack<>();
        if(sc.hasNextLine()){
           char arr=s.toCharArray();
            for(int i=0;i<arr.length;i++)
            {
                if(arr[i]=='(')
                {
                    st.push(i)
                }else if (arr[i]==')')
                {
                    if(!st.isEmpty())
                    {
                        st.pop();
                    }

                }else{
                    arr[i]='*';
                }
            }
            StringBuilder sb=new StringBuilder();
            for(int i=0;i<arr.length;i++)
                {
                    if(i!='*')
                        sb.append(i);
                }

            System.out.println(sb);
        }
    }
}