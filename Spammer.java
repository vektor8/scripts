import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class Spammer {
    public static void main(String[] args) throws InterruptedException, FileNotFoundException {
        Map<String, Object> prefs = new HashMap<>();
        prefs.put("profile.default_content_setting_values.notifications", 2);
        ChromeOptions options = new ChromeOptions();
        options.setExperimentalOption("prefs", prefs);
        System.setProperty("webdriver.chrome.driver", "C:\\Program Files (x86)\\chromedriver.exe");
        WebDriver driver = new ChromeDriver(options);
        //in the next line you will insert the link to the person you're trying to spam and it should look like the one below
        driver.get("https://www.facebook.com/messages/t/100002347463714");
        WebElement acceptButton = driver.findElement(By.xpath("/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]"));
        acceptButton.click();

        WebElement usernameBox = driver.findElement(By.id("email"));
        WebElement passwordBox = driver.findElement(By.name("pass"));
        FileReader fr = null;
        try {
            File f = new File("fbpassword.txt");
            //you should have your facebook access credentials in this txt file: 1st line your email and on the second line your password
            fr = new FileReader(f);
        } catch (Exception e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
        Scanner sc = new Scanner(fr);
        usernameBox.sendKeys(sc.nextLine());
        passwordBox.sendKeys(sc.nextLine());
        passwordBox.sendKeys(Keys.RETURN);
        TimeUnit.SECONDS.sleep(10);
        FileReader fr1 = null;
        try {
            File f = new File("lyrics.txt");
            fr1 = new FileReader(f);
        } catch (Exception e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
        Scanner sc1 = new Scanner(fr1);
        while(sc1.hasNextLine()){
            String s = sc1.nextLine();
            String[] arr = s.split(" ");
            for(String ss:arr){
                WebElement textBox = driver.findElement(By.xpath("//*[@data-editor]"));
                textBox.click();
                textBox.sendKeys(ss);
                System.out.println(ss);
                textBox.sendKeys(Keys.RETURN);
            }
        }
        driver.quit();
    }
}