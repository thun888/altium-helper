import os
import sys
import random
import string

head2 = '''|ISBOC=T|RECORD=31|VISIBLEGRIDON=T|VISIBLEGRIDSIZE=10|DISPLAY_UNIT=4|CUSTOMY=950|BORDERON=T|HOTSPOTGRIDON=T|CUSTOMX=1500|CUSTOMMARGINWIDTH=20|SIZE1=10|SHEETNUMBERSPACESIZE=4|CUSTOMYZONES=4|USEMBCS=T|FONTIDCOUNT=1|SNAPGRIDSIZE=10|SHEETSTYLE=8|SYSTEMFONT=1|HOTSPOTGRIDSIZE=4|FONTNAME1=Times New Roman|TITLEBLOCKON=T|AREACOLOR=16317695|SNAPGRIDON=T|CUSTOMXZONES=6
|RECORD=41|ISHIDDEN=T|NAME=CurrentTime|OWNERPARTID=-1|COLOR=8388608|TEXT=*|READONLYSTATE=1|UNIQUEID=WFYPTBEC|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=CurrentDate|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=1|COLOR=8388608|READONLYSTATE=1|UNIQUEID=KRGPTHWR|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=Time|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=2|COLOR=8388608|READONLYSTATE=1|UNIQUEID=APNVELVY|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=Date|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=3|COLOR=8388608|READONLYSTATE=1|UNIQUEID=DOFGRYNH|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=DocumentFullPathAndName|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=4|COLOR=8388608|READONLYSTATE=1|UNIQUEID=XTILODYM|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=DocumentName|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=5|COLOR=8388608|READONLYSTATE=1|UNIQUEID=CIXOCUKW|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=ModifiedDate|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=6|COLOR=8388608|READONLYSTATE=1|UNIQUEID=CYVLOLHC|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=ApprovedBy|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=7|COLOR=8388608|READONLYSTATE=1|UNIQUEID=UKLMMPSH|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=CheckedBy|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=8|COLOR=8388608|READONLYSTATE=1|UNIQUEID=LGBVFHBI|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=Author|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=9|COLOR=8388608|READONLYSTATE=1|UNIQUEID=NNMPOPVS|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=CompanyName|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=10|COLOR=8388608|READONLYSTATE=1|UNIQUEID=ROXAGALI|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=DrawnBy|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=11|COLOR=8388608|READONLYSTATE=1|UNIQUEID=GSEQEJEE|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=Engineer|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=12|COLOR=8388608|READONLYSTATE=1|UNIQUEID=NMEAIFPG|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=Organization|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=13|COLOR=8388608|READONLYSTATE=1|UNIQUEID=CHTRTWQS|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=Address1|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=14|COLOR=8388608|READONLYSTATE=1|UNIQUEID=SLYDDXDR|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=Address2|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=15|COLOR=8388608|READONLYSTATE=1|UNIQUEID=JNHWHKQI|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=Address3|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=16|COLOR=8388608|READONLYSTATE=1|UNIQUEID=MIQKOJUC|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=Address4|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=17|COLOR=8388608|READONLYSTATE=1|UNIQUEID=TBHPRINX|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=Title|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=18|COLOR=8388608|READONLYSTATE=1|UNIQUEID=JRIVAVFH|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=DocumentNumber|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=19|COLOR=8388608|READONLYSTATE=1|UNIQUEID=SJJFVEJY|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=Revision|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=20|COLOR=8388608|READONLYSTATE=1|UNIQUEID=TPPALWNV|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=SheetNumber|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=21|COLOR=8388608|READONLYSTATE=1|UNIQUEID=IXCDWQOY|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=SheetTotal|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=22|COLOR=8388608|READONLYSTATE=1|UNIQUEID=WLJMRBEM|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=Rule|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=23|COLOR=8388608|READONLYSTATE=1|UNIQUEID=SGMPJKTU|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=ImagePath|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=24|COLOR=8388608|READONLYSTATE=1|UNIQUEID=CDHEMVMP|FONTID=1
|RECORD=41|ISHIDDEN=T|NAME=ProjectName|TEXT=*|OWNERPARTID=-1|INDEXINSHEET=25|COLOR=8388608|READONLYSTATE=1|UNIQUEID=FMWVHCEF|FONTID=1
'''

def main():
    Component_overname =input("输入元件位号(eg:U)：")
    Component_name = input("输入设元件名称(eg:3PIN)：")
    Component_pin = int(input("输入元件pin数量(eg:30)："))
    Component_size = input("输入元件宽度(eg:5)：")
    Component_rightpin = input("是否使用右侧引脚(y/n)：")
    #如果执行文件后有 test,则设为默认值
    if Component_size == '':
        Component_size = 5
    if Component_rightpin == '':
        Component_rightpin = 'y'
    if Component_rightpin == "y" or Component_rightpin == "Y":
        Component_rightpin = "y"
        Component_pintype=input("选择放置类型И/凵/Z(输1为И，2为凵，3为Z)：")
        if Component_pintype != "1" and Component_pintype != "2" and Component_pintype != "3":
            print("输入错误，请重新输入")
            Component_pintype = input("选择放置类型И/凵(输1为И，2为凵)：")
    if Component_pin >= 35:
        Constants = 930
    else:
        Constants = 450
    x1 = Constants-int(Component_size)*10
    if Component_rightpin == "y" :
        y = Constants+Component_pin*5+10
    else:
        y = Constants+Component_pin*10+10
    #print(x1)
    #print(y)
    body1 = '|RECORD=1|PARTIDLOCKED=T|COLOR=128|SOURCELIBRARYNAME=thisprogrambythun888.SchLib|OWNERPARTID=-1|DISPLAYMODECOUNT=1|INDEXINSHEET=26|DESIGNITEMID='+str(Component_name)+'|PARTCOUNT=2|LIBREFERENCE='+str(Component_name)+'|LIBRARYPATH=*|LOCATION.X='+str(x1)+'|AREACOLOR=11599871|TARGETFILENAME=*|CURRENTPARTID=1|LOCATION.Y='+str(Constants)+'|UNIQUEID='+str(uniqueid())+'\n'
    body2 ='|RECORD=14|ISNOTACCESIBLE=T|LOCATION.X='+str(Constants)+'|CORNER.Y='+str(Constants)+'|ISSOLID=T|OWNERPARTID=1|OWNERINDEX=27|CORNER.X='+str(x1)+'|COLOR=128|AREACOLOR=11599871|LOCATION.Y='+str(y)+'\n'
    body3 =''
    for i in range(Component_pin):
        pin_num = i+1
        pin_name = input("输入第"+str(pin_num)+"个pin的名称(eg:TX)：")
        if pin_name =="":
            pin_name = pin_num
        pin_y = y-pin_num*10
        index = i*2+27
        if Component_rightpin == "y":
            if Component_pintype =="1":
                if pin_num<= Component_pin/2:
                    body3 = body3+'|DESIGNATOR='+str(pin_num)+'|RECORD=2|NAME='+str(pin_name)+'|LOCATION.X='+str(x1)+'|PINLENGTH=20|OWNERPARTID=1|PINCONGLOMERATE=58|ELECTRICAL=4|OWNERINDEX=27|FORMALTYPE=1|LOCATION.Y='+str(pin_y)+'\n'
                    body3 = body3+'|ISHIDDEN=T|RECORD=41|LOCATION.X='+str(Constants)+'|NAME=PinUniqueId|OWNERPARTID=-1|OWNERINDEX='+str(index)+'|TEXT='+str(uniqueid())+'|COLOR=8388608|LOCATION.Y='+str(pin_y)+'|FONTID=1\n'
                else:
                    pin_y = delete_extra_zero(pin_y+Component_pin/2*10)
                    #print(pin_y)
                    body3 = body3+'|DESIGNATOR='+str(pin_num)+'|RECORD=2|NAME='+str(pin_name)+'|LOCATION.X='+str(Constants)+'|PINLENGTH=20|OWNERPARTID=1|PINCONGLOMERATE=56|ELECTRICAL=4|OWNERINDEX=27|FORMALTYPE=1|LOCATION.Y='+str(pin_y)+'\n'
                    body3 = body3+'|ISHIDDEN=T|RECORD=41|LOCATION.X='+str(Constants)+'|NAME=PinUniqueId|OWNERPARTID=-1|OWNERINDEX='+str(index)+'|TEXT='+str(uniqueid())+'|COLOR=8388608|LOCATION.Y='+str(pin_y)+'|FONTID=1\n'                
            elif Component_pintype =="2":
                if pin_num<= Component_pin/2:
                    body3 = body3+'|DESIGNATOR='+str(pin_num)+'|RECORD=2|NAME='+str(pin_name)+'|LOCATION.X='+str(x1)+'|PINLENGTH=20|OWNERPARTID=1|PINCONGLOMERATE=58|ELECTRICAL=4|OWNERINDEX=27|FORMALTYPE=1|LOCATION.Y='+str(pin_y)+'\n'
                    body3 = body3+'|ISHIDDEN=T|RECORD=41|LOCATION.X='+str(Constants)+'|NAME=PinUniqueId|OWNERPARTID=-1|OWNERINDEX='+str(index)+'|TEXT='+str(uniqueid())+'|COLOR=8388608|LOCATION.Y='+str(pin_y)+'|FONTID=1\n'
                else:
                    pin_y = delete_extra_zero(y-Component_pin/2*10+(pin_num-Component_pin/2-1)*10)
                    #print(pin_y)
                    body3 = body3+'|DESIGNATOR='+str(pin_num)+'|RECORD=2|NAME='+str(pin_name)+'|LOCATION.X='+str(Constants)+'|PINLENGTH=20|OWNERPARTID=1|PINCONGLOMERATE=56|ELECTRICAL=4|OWNERINDEX=27|FORMALTYPE=1|LOCATION.Y='+str(pin_y)+'\n'
                    body3 = body3+'|ISHIDDEN=T|RECORD=41|LOCATION.X='+str(Constants)+'|NAME=PinUniqueId|OWNERPARTID=-1|OWNERINDEX='+str(index)+'|TEXT='+str(uniqueid())+'|COLOR=8388608|LOCATION.Y='+str(pin_y)+'|FONTID=1\n'
            
            elif Component_pintype =="3":
                if (pin_num & 1) == 0: 
                    pin_y = y-pin_num*5 #/2*10
                    body3 = body3+'|DESIGNATOR='+str(pin_num)+'|RECORD=2|NAME='+str(pin_name)+'|LOCATION.X='+str(Constants)+'|PINLENGTH=20|OWNERPARTID=1|PINCONGLOMERATE=56|ELECTRICAL=4|OWNERINDEX=27|FORMALTYPE=1|LOCATION.Y='+str(pin_y)+'\n'
                    body3 = body3+'|ISHIDDEN=T|RECORD=41|LOCATION.X='+str(x1)+'|NAME=PinUniqueId|OWNERPARTID=-1|OWNERINDEX='+str(index)+'|TEXT='+str(uniqueid())+'|COLOR=8388608|LOCATION.Y='+str(pin_y)+'|FONTID=1\n'
                else:
                    pin_y = y-(pin_num+1)*5 #/2*10
                    body3 = body3+'|DESIGNATOR='+str(pin_num)+'|RECORD=2|NAME='+str(pin_name)+'|LOCATION.X='+str(x1)+'|PINLENGTH=20|OWNERPARTID=1|PINCONGLOMERATE=58|ELECTRICAL=4|OWNERINDEX=27|FORMALTYPE=1|LOCATION.Y='+str(pin_y)+'\n'
                    body3 = body3+'|ISHIDDEN=T|RECORD=41|LOCATION.X='+str(x1)+'|NAME=PinUniqueId|OWNERPARTID=-1|OWNERINDEX='+str(index)+'|TEXT='+str(uniqueid())+'|COLOR=8388608|LOCATION.Y='+str(pin_y)+'|FONTID=1\n'
        
        else:
            body3 = body3+'|DESIGNATOR='+str(pin_num)+'|RECORD=2|NAME='+str(pin_name)+'|LOCATION.X='+str(x1)+'|PINLENGTH=20|OWNERPARTID=1|PINCONGLOMERATE=58|ELECTRICAL=4|OWNERINDEX=27|FORMALTYPE=1|LOCATION.Y='+str(pin_y)+'\n'
            body3 = body3+'|ISHIDDEN=T|RECORD=41|LOCATION.X='+str(x1)+'|NAME=PinUniqueId|OWNERPARTID=-1|OWNERINDEX='+str(index)+'|TEXT='+str(uniqueid())+'|COLOR=8388608|LOCATION.Y='+str(pin_y)+'|FONTID=1\n'
        head1 = '|HEADER=Protel for Windows - Schematic Capture Ascii File Version 5.0|WEIGHT='+str(index+10)+'\n'
    body4='|RECORD=34|LOCATION.X='+str(Constants)+'|NAME=Designator|TEXT='+str(Component_overname)+'|OWNERINDEX=27|OWNERPARTID=-1|COLOR=8388608|INDEXINSHEET=-1|READONLYSTATE=1|LOCATION.Y='+str(Constants)+'|FONTID=1\n'
    body5 = '|RECORD=41|LOCATION.X='+str(Constants)+'|NAME=Comment|TEXT='+str(Component_name)+'|OWNERINDEX=27|OWNERPARTID=-1|COLOR=8388608|INDEXINSHEET=-1|UNIQUEID='+str(uniqueid())+'|LOCATION.Y='+str(Constants-10)+'|FONTID=1\n'
    body6= '''|OWNERINDEX=27|RECORD=44
|HEADER=Icon storage
|HEADER=Protel for Windows - Schematic Capture Ascii File Version 5.0
    '''
    allofthem = head1+head2+body1+body2+body3+body4+body5+body6
    filename = Component_name+".SchDoc"
    with open(filename,"w") as f:
        f.write(allofthem)
    print("生成成功，文件名为"+filename)
    os.system("start "+filename)
    return filename




def uniqueid():
    """生成8位随机大写字母=>uniqueid!"""
    return ''.join(random.sample(string.ascii_uppercase, 8))
def delete_extra_zero(n):
    """删除小数点后多余的0"""
    n = '{:g}'.format(n)
    n = float(n) if '.' in n else int(n)  # 含小数点转float否则int
    return n

if __name__ == "__main__":
    os.system("start "+main())
    sys.exit()