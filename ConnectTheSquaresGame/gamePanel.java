import java.awt.*;
import java.util.ArrayList;
import javax.swing.*;
import java.awt.event.*;
import java.lang.Math.*;

public class GamePanel extends JPanel {
	private Square selectedSquare1;
	private Square selectedSquare2;
	private Square selectedSquare;
	private int r, c;
	private int x, y;
	private ArrayList<Square> squareArr = new ArrayList<Square>();
	private ArrayList<int[]> traveledIdx = new ArrayList<int[]>();
	private Color[] colorArr = {Color.red, Color.cyan, Color.blue, Color.green, Color.orange, Color.pink, Color.darkGray, Color.magenta, Color.yellow};
	public GamePanel(int r, int c) {
		this.r = r;
		this.c = c;
		ArrayList<Integer> colorNum = new ArrayList<Integer>();
		if (r*c/9 % 2 == 0) {
			colorNum.add(r*c/9+r*c-(r*c/9)*9);
			for (int i = 0; i < 8; i++) {
				colorNum.add(r*c/9);
			}
		}
		else {
			for (int i = 0; i < 9; i++) {
				if (i%2==0)
					colorNum.add(r*c/9+1);
				else
					colorNum.add(r*c/9-1);
			}
		}
		int idx;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				idx = (int)(Math.random()*colorArr.length);
				while (colorNum.get(idx) == 0) {
					idx = (int)(Math.random()*colorArr.length);
				}
				colorNum.set(idx, colorNum.get(idx)-1);
				squareArr.add(new Square(35+j*70, 35+i*70, 70, colorArr[idx]));
			}
		}
		addMouseListener(new PanelListener());
	}
	public void paintComponent(Graphics g) {
		super.paintComponent(g);
		for (int i = 0; i < c*r; i++) {
			squareArr.get(i).fill(g);
		}
		if (selectedSquare1!=null) {
			selectedSquare1.draw(g);
		}
		if (selectedSquare2!=null) {
			selectedSquare2.draw(g);
		}
		if (gameEnd()) {
			Font font = new Font("Courier", Font.BOLD, 50);
			g.setFont(font);
			g.drawString("WIN", r*70/2, c*70/2);
		}
		repaint();
	}
	private boolean gameEnd() {
		for (int i=0; i<r*c; i++) {
			if (!squareArr.get(i).getColor().equals(Color.white)) {
				return false;
			}
		}
		return true;
	}
	private class PanelListener extends MouseAdapter {
		public void mousePressed(MouseEvent e) {
			x = e.getX();
			y = e.getY();
			for (int i = 0; i < r*c; i++) {
				if (squareArr.get(i).containsPoint(x, y) && !squareArr.get(i).getColor().equals(Color.white)) {
					selectedSquare = squareArr.get(i);
					if (selectedSquare1 == null) {
						selectedSquare1 = squareArr.get(i);
					}
					else {
						selectedSquare2 = squareArr.get(i);
						if (selectedSquare2.getX()==selectedSquare1.getX() && selectedSquare2.getY()==selectedSquare1.getY()) {
							selectedSquare2 = null;
						}
					}
					break;
				}
			}
		}
		public void mouseReleased(MouseEvent e) {
			if (selectedSquare != null) {
				selectedSquare = null;
			}
			if (selectedSquare1 != null && selectedSquare2 != null) {
				connect();
				repaint();
			}
		}
		public void connect() {
			if (isValidConnection() || isBorderConnection()) {
				selectedSquare1.clear();
				selectedSquare2.clear();
				repaint();
			}
			traveledIdx = new ArrayList<int[]>();
			selectedSquare1 = null;
			selectedSquare2 = null;
		}
		private boolean isBorderConnection() {
			int row1 = (selectedSquare1.getY()-35)/70;
			int col1 = (selectedSquare1.getX()-35)/70;
			int row2 = (selectedSquare2.getY()-35)/70;
			int col2 = (selectedSquare2.getX()-35)/70;
			boolean top = true, bottom = true, right = true, left = true;
			for (int i=row1-1; i>=0; i--) {
				if (!squareArr.get(i*c+col1).getColor().equals(Color.white)) {
					top = false;
				}
			}
			for (int i=row2-1; i>=0; i--) {
				if (!squareArr.get(i*c+col2).getColor().equals(Color.white)) {
					top = false;
				}
			}
			for (int i=row1+1; i<=r-1; i++) {
				if (!squareArr.get(i*c+col1).getColor().equals(Color.white)) {
					bottom = false;
				}
			}
			for (int i=row2+1; i<=r-1; i++) {
				if (!squareArr.get(i*c+col2).getColor().equals(Color.white)) {
					bottom = false;
				}
			}
			for (int i=col1-1; i>=0; i--) {
				if (!squareArr.get(row1*c+i).getColor().equals(Color.white)) {
					left = false;
				}
			}
			for (int i=col2-1; i>=0; i--) {
				if (!squareArr.get(row2*c+i).getColor().equals(Color.white)) {
					left = false;
				}
			}
			for (int i=col1+1; i<=c-1; i++) {
				if (!squareArr.get(row1*c+i).getColor().equals(Color.white)) {
					right = false;
				}
			}
			for (int i=col2+1; i<=c-1; i++) {
				if (!squareArr.get(row2*c+i).getColor().equals(Color.white)) {
					right = false;
				}
			}
			if (squareArr.get((selectedSquare1.getX()-35)/70+(selectedSquare1.getY()-35)/70*c).getColor().equals(squareArr.get((selectedSquare2.getX()-35)/70+(selectedSquare2.getY()-35)/70*c).getColor())) {
				return top || bottom || right || left;
			}
			else {
				return false;
			}
		}
		private boolean isValidConnection() {
			int row1 = (selectedSquare1.getY()-35)/70;
			int col1 = (selectedSquare1.getX()-35)/70;
			int row2 = (selectedSquare2.getY()-35)/70;
			int col2 = (selectedSquare2.getX()-35)/70;
			if (squareArr.get((selectedSquare1.getX()-35)/70+(selectedSquare1.getY()-35)/70*c).getColor().equals(squareArr.get((selectedSquare2.getX()-35)/70+(selectedSquare2.getY()-35)/70*c).getColor())) {
				return searchPath(row1, col1, row2, col2);
			}
			return false;
		}
		private boolean searchPath(int row1, int col1, int row2, int col2) {
			int row = row1;
			int col = col1;
			if (row+1 == row2 && col == col2 || row-1 == row2 && col == col2 || row == row2 && col+1 == col2 || row == row2 && col-1 == col2) {
				return true;
			}
			int[] tmp = {row, col};
			traveledIdx.add(tmp);
			if (col < c-1) {
				if (squareArr.get(row*c+col+1) != null && squareArr.get(row*c+col+1).getColor().equals(Color.white)) {
					int[] nextCoor = {row, col+1};
					if (! inArray(nextCoor, traveledIdx)) {
						col++;
						if (!searchPath(row, col, row2, col2)) {
							col--;
						}
						else {
							return true;
						}
					}
				}
			}
			if (col > 0) {
				if (squareArr.get(row*c+col-1) != null && squareArr.get(row*c+col-1).getColor().equals(Color.white)) {
					int[] nextCoor = {row, col-1};
					if (! inArray(nextCoor, traveledIdx)) {
						col--;
						if(!searchPath(row, col, row2, col2)) {
							col++;
						}
						else {
							return true;
						}
					}
				}
			}
			if (row < r-1) {
				if (squareArr.get((row+1)*c+col) != null && squareArr.get((row+1)*c+col).getColor().equals(Color.white)) {
					int[] nextCoor = {row+1, col};
					if (! inArray(nextCoor, traveledIdx)) {
						row++;
						if(!searchPath(row, col, row2, col2)) {
							row--;
						}
						else {
							return true;
						}
					}
				} 
			}
			if (row > 0) {
				if (squareArr.get((row-1)*c+col) != null && squareArr.get((row-1)*c+col).getColor().equals(Color.white)) {
					int[] nextCoor = {row-1, col};
					if (! inArray(nextCoor, traveledIdx)) {
						row--;
						if(!searchPath(row, col, row2, col2)) {
							row++;
						}
						else {
							return true;
						}
					}
				}
			}
			return false;
		}
		private boolean inArray(int[] coor, ArrayList<int[]> arr) {
			for (int i = 0; i < arr.size(); i++) {
				if (arr.get(i)[0] == coor[0] && arr.get(i)[1] == coor[1]) {
					return true;
				}
			}
			return false;
		}
	}
}