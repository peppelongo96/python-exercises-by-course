import cImage as image

def taglio(img,win):
    new_pixel=image.Pixel(255,255,255)
    click_1=win.getMouse()
    click_2=win.getMouse()
    click_1_x=click_1[0]
    click_1_y=click_1[1]
    click_2_x=click_2[0]
    click_2_y=click_2[1]
    print(click_1)
    print(click_2)
    for col in range(img.getHeight()):
        for row in range(img.getWidth()):

            if click_1_x  <= click_2_x and click_1_y <= click_2_y:
                if not (click_1_x < row < click_2_x and click_1_y < col < click_2_y):   
                    img.setPixel(row,col,new_pixel)

            if click_1_x >= click_2_x and click_1_y <= click_2_y:
                if not (click_2_x < row < click_1_x and click_1_y < col < click_2_y):
                    img.setPixel(row,col,new_pixel)

            if click_1_x >= click_2_x and click_1_y >= click_2_y:
                if not (click_2_x < row < click_1_x and click_2_y < col < click_1_y):
                   img.setPixel(row,col,new_pixel)

            if click_1_x <= click_2_x and click_1_y >= click_2_y:
                if not (click_1_x < row < click_2_x and click_2_y < col < click_1_y):
                  img.setPixel(row,col,new_pixel)  
    img.draw(win)

def main():
    immagine = image.Image("1.gif")
    win = image.ImageWin(immagine.getHeight(),immagine.getWidth())
    immagine.draw(win)

    taglio(immagine,win)

main()
