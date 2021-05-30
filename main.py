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
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)

        #缩放倍数
        zoom_x = 2.0
        zoom_y = 2.0
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)

        if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imagePath)          # 若图片文件夹不存在就创建

        pix.writePNG(imagePath + '/' + '%s.png' % pg)  # 将图片写入指定的文件夹内


if __name__ == "__main__":
    pdfPaths = "C:\\Users\\du\\Desktop\\英语"
    imagePath = 'pdfimage'
    for i,pdfPath in enumerate(os.listdir(pdfPaths)):
        print("[{}/{}] {}".format(i,len(os.listdir(pdfPaths)),pdfPath))
        pdfPath_out = pdfPaths+"\\"+pdfPath.split(".")[0]+"_imageonly"+".pdf"
        if os.path.exists(imagePath):
            shutil.rmtree(imagePath)
        os.mkdir(imagePath)
        pdf2image(pdfPaths+"\\"+pdfPath, imagePath)
        image2PDF(pdfPath_out,imagePath)
    shutil.rmtree(imagePath)        #清空处理后的图片文件
    print("恭喜：转换成功！")