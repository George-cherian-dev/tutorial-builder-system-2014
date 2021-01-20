
import java.io.*;
import java.util.*;
class SearchDir
{
	public static void main(String [] args)
	{
		String directory="D:\\Project Files\\Crawler\\1\\40";
		String fileName="0";
		File dir = new File(directory);

        File[] matchingFiles = dir.listFiles(new FilenameFilter() {
               public boolean accept(File dir, String name) {
					return name.startsWith(fileName);
                }
        });
		for(int i=0;i<matchingFiles.length;i++)
			System.out.println(matchingFiles[i]);
	}
}