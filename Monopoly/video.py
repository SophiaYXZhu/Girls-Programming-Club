import cv2
import pygame
from config import *
import sys

class Video:
    def __init__():
        print("This is the Video class")

    @classmethod
    def play_video(self, directory, wn):
        cap = cv2.VideoCapture(directory)
        success, img = cap.read()
        shape = img.shape[1::-1]
        wn = pygame.display.set_mode(shape)
        clock = pygame.time.Clock()
        while success:
            clock.tick(60)
            success, img = cap.read()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    success = False
            try:
                wn.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
            except Exception:
                sys.exit()
            pygame.display.update()
        sys.exit()

if __name__ == "__main__":
    pygame.display.set_caption("大富翁")
    screen = pygame.display.set_mode([1500,800])
    Video.play_video("C:\\Users\\Duality\\Documents\\Sophia+Zhu\\Workplace\\Monopoly\\images\\king.mp4", screen)