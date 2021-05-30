import fitz
import os
import img2pdf
import shutil

def image2PDF(pdfPath,imagePath):
    imageName = os.listdir(imagePath+ '/')

    for i in range(len(imageName)):
        imageName[i] = imagePath+"/"+str(i)+".png"
    with open(pdfPath,"wb") as f:
        f.write(img2pdf.convert(imageName))


def pdf2image(pdfPath, imagePath):
    pdfDoc = fitz.open(pdfPath)
    count = 0
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)

        #缩放倍数
        if(page.get_image_info()[0]["width"]>4000):
            zoom_x = 0.25
            zoom_y = 0.25
        elif(page.get_image_info()[0]["width"]>3000):
            zoom_x = 0.5
            zoom_y = 0.5
        elif(page.get_image_info()[0]["width"]>2000):
            zoom_x = 1
            zoom_y = 1
        else:
            zoom_x = 1.5
            zoom_y = 1.5
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)

        if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imagePath)          # 若图片文件夹不存在就创建

        pix.writePNG(imagePath + '/' + '%s.png' % pg)  # 将图片写入指定的文件夹内
        count+=1
        print(count)


if __name__ == "__main__":
    pdfPaths = "C:\\Users\\du\\Desktop\\圖片pdf"
    imagePath = 'pdfimage'
    for i,pdfPath in enumerate(os.listdir(pdfPaths)):
        print("[{}/{}] {}".format(i+1,len(os.listdir(pdfPaths)),pdfPath))
        pdfPath_out = pdfPaths+"\\"+pdfPath.split(".")[0]+"_imageonly"+".pdf"
        if os.path.exists(imagePath):
            shutil.rmtree(imagePath)
        os.mkdir(imagePath)
        pdf2image(pdfPaths+"\\"+pdfPath, imagePath)
        image2PDF(pdfPath_out,imagePath)
    shutil.rmtree(imagePath)        #清空处理后的图片文件
    print("恭喜：转换成功！")