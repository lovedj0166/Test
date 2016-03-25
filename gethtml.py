#coding=utf-8
import urllib
import re
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg =r'src="(.+\.jpg)"'
    imgre =re.compile(reg)
    imglise = re.findall(imgre,html)
    return imglise



html = getHtml("http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=false&word=%E5%A3%81%E7%BA%B8&pn=0&spn=0&di=0&pi=0&rn=1&tn=baiduimagedetail&istype=&ie=utf-8&oe=utf-8&in=3354&cl=2&lm=-1&st=&cs=3525169332%2C3635106221&os=3454056948%2C4189763449&simid=&adpicid=0&ln=1000&fmq=1378374347070_R&fm=&ic=0&s=0&se=&sme=&tab=&face=&ist=&jit=&statnum=wallpaper&cg=wallpaper&bdtype=-1&oriquery=&objurl=http%3A%2F%2Fe.hiphotos.baidu.com%2Fzhidao%2Fpic%2Fitem%2F78310a55b319ebc40bbc7c3e8326cffc1f171654.jpg&fromurl=http%3A%2F%2Fimage.baidu.com%2Fsearch%2Fdetail%3Fct%3D503316480%26z%3D0%26ipn%3Dd%26word%3D%E9%AB%98%E6%B8%85%E5%A3%81%E7%BA%B8%26pn%3D9%26spn%3D0%26di%3D105820915200%26pi%3D%26rn%3D1%26tn%3Dbaiduimagedetail%26istype%3D%26ie%3Dutf-8%26oe%3Dutf-8%26in%3D3354%26cl%3D2%26lm%3D-1%26st%3D%26cs%3D3635106221%2C3525169332%26os%3D4189763449%2C3454056948%26simid%3D43332147%2C728970372%26adpicid%3D0%26ln%3D1000%26fmq%3D1378374347070_R%26fm%3D%26ic%3D0%26s%3D0%26se%3D%26sme%3D%26tab%3D%26face%3D%26ist%3D%26jit%3D%26statnum%3Dwallpaper%26cg%3D%26bdtype%3D0%26oriquery%3D%26objurl%3Dhttp%3A%2F%2Fe.hiphotos.baidu.com%2Fzhidao%2Fpic%2Fitem%2F78310a55b319ebc40bbc7c3e8326cffc1f171654.jpg%26fromurl%3Dippr_z2C%24qAzdH3FAzdH3Fzit1w5_z%26e3Bkwt17_z%26e3Bv54AzdH3Fq7jfpt5gAzdH3Fccln9n8a0_z%26e3Bip4s%26gsm%3D1e&gsm=0")

print getImg(html)
