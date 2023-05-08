import java.awt.*;
import javax.swing.JFrame;

public class Main {
    public static void main(String args[]) {
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("连连看");
        frame.setResizable(false);
        frame.setSize(620, 620);
        Container pane = frame.getContentPane();
        GamePanel gp = new GamePanel(8, 8);
        pane.add(gp);
        frame.setVisible(true);
    }
}