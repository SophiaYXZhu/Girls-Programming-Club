import java.awt.*;
import java.lang.Math.*;

public class Square {
	private int centerX, centerY, length;
	private Color color;
	public Square(int x, int y, int w, Color c) {
		centerX = x;
		centerY = y;
		length = w;
		color = c;
	}
	public int getX() {
		return centerX;
	}
	public int getY() {
		return centerY;
	}
	public int getLength() {
		return length;
	}
	public Color getColor() {
		return color;
	}
	public void setX(int x) {
		centerX=x;
	}
	public void setY(int y) {
		centerY=y;
	}
	public void setLength(int w) {
		length=w;
	}
	public void setColor(Color c) {
		color=c;
	}
	public void draw(Graphics g) {
		Color oldColor = g.getColor();
		g.setColor(Color.black);
		g.drawRect(centerX-length/2, centerY-length/2, length, length);
		g.setColor(oldColor);
	}
	public void fill(Graphics g) {
		Color oldColor = g.getColor();
		g.setColor(color);
		g.fillRect(centerX-length/2, centerY-length/2, length, length);
		g.setColor(oldColor);
	}
	public boolean containsPoint(int x, int y) {
		return (x < centerX+length/2) && (x > centerX-length/2) && (y < centerY+length/2) && (y > centerY-length/2);
	}
	public void clear() {
		this.color = Color.white;
	}
}
