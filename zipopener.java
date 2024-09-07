import net.lingala.zip4j.ZipFile;
import net.lingala.zip4j.exception.ZipException;
import net.lingala.zip4j.model.FileHeaders;
import net.lingala.zip4j.model.ZipParameters;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ZipCracker {

    public static void main(String[] args) {
        String zipFilePath = "protected.zip";  // Path to your ZIP file
        String passwordList = "passwords.txt"; // Path to your password dictionary file

        try {
            crackZip(zipFilePath, passwordList);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void crackZip(String zipFilePath, String passwordList) throws IOException {
        ZipFile zipFile = new ZipFile(zipFilePath);

        try (BufferedReader reader = new BufferedReader(new FileReader(passwordList))) {
            String password;
            while ((password = reader.readLine()) != null) {
                password = password.trim();
                if (tryPassword(zipFile, password)) {
                    System.out.println("Password found: " + password);
                    return;
                }
            }
            System.out.println("Password not found.");
        }
    }

    public static boolean tryPassword(ZipFile zipFile, String password) {
        try {
            if (zipFile.isEncrypted()) {
                zipFile.setPassword(password.toCharArray());
            }
            // Try to extract to check if the password is correct
            zipFile.extractAll("output_folder");  // Extract to a folder
            return true;
        } catch (ZipException e) {
            // Wrong password or issue with extraction
            return false;
        }
    }
}
