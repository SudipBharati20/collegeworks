
//file handling with try catch
import java.io.File;

public class filehandling {
    public static void main(String[] args) {
        try {
            // Create a new file
            File myFile = new File("example.txt");
            if (myFile.createNewFile()) {
                System.out.println("File created: " + myFile.getName());
            } else {
                System.out.println("File already exists.");
            }

            // Write to the file
            java.io.FileWriter writer = new java.io.FileWriter("example.txt");
            writer.write("Hello, this is a test file.");
            writer.close();
            System.out.println("Successfully wrote to the file.");

            // Read from the file
            java.util.Scanner reader = new java.util.Scanner(myFile);
            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                System.out.println(data);
            }
            reader.close();

            // Delete the file
            if (myFile.delete()) {
                System.out.println("Deleted the file: " + myFile.getName());
            } else {
                System.out.println("Failed to delete the file.");
            }
        } catch (Exception e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}