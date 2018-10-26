import java.util.Scanner;

public class ScriptMe2 {

	public static String sum(String oneF, String twoF)
	{
		int count = 1;
		int oneMax = 1;
		int twoMax = 1;
		for(int i = 0; i < oneF.length(); i++)
		{
			if(oneF.charAt(i) == '(' )
			{
				count++;
				if(count >oneMax)
					oneMax = count;
			}
			else
			{
				count--;
			}
		}
		
		count = 1;
		for(int i = 0; i < twoF.length(); i++)
		{
			if(twoF.charAt(i) == '(' )
			{
				count++;
				if(count > twoMax)
					twoMax = count;
			}
			else
			{
				count--;
			}
		}
		String fin =null;
		if(oneMax == twoMax)
		{
			fin= oneF + twoF;
		}
		if(oneMax > twoMax)
		{
			fin= oneF.substring(0, oneF.length()-1) +  twoF + oneF.substring(oneF.length()-1, oneF.length());
		}
		if(twoMax > oneMax)
		{
			fin= twoF.substring(0, 1) + oneF + twoF.substring(1, twoF.length());
		}
		return fin;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String in = sc.nextLine();
		String[] inArr = in.split(" ");

		String fin = sum(inArr[0],inArr[2]);
		
		for(int i = 4; i < inArr.length; i+=2)
		{
			fin = sum(fin,inArr[i]);
		}
		System.out.print(fin);

	}

}