# -*- coding:UTF-8 -*-
import json,urllib,datetime
from xml.etree.ElementTree import parse
#tree=parse(urllib.urlopen('http://miniunit.imbc.com/Schedule'))
mbc=[[4, '2014-09-02', 90], [6, '2006-10-14', 2880], [7, '2014-09-02', 90], [8, '2006-01-01', 106], [8, '2014-09-02', 90], [9, '2014-09-02', 90], [10, '2014-09-02', 90], [11, '2014-09-02', 90], [12, '2013-09-07', 450], [19, '2006-01-01', 3256], [20, '2008-10-03', 2160], [21, '2006-01-01', 3256], [22, '2009-04-01', 2070], [23, '2006-01-01', 3256], [24, '2009-04-01', 1260], [25, '2006-01-01', 3256], [26, '2008-04-06', 2430], [27, '2006-01-01', 3256], [28, '2006-04-17', 1800], [29, '2006-01-01', 1546], [30, '2007-04-12', 1080], [31, '2007-04-12', 1260], [32, '2007-04-12', 1260], [36, '2010-03-27', 1260], [39, '2011-03-22', 1080], [42, '2006-10-14', 2970], [48, '2006-01-01', 3256], [49, '2012-09-12', 720], [50, '2012-09-12', 810], [53, '2013-09-07', 450], [54, '2006-10-14', 2970], [56, '2014-09-02', 90], [84, '2014-09-02', 90], [85, '2014-09-02', 90], [86, '2013-03-11', 180], [86, '2014-09-02', 90], [87, '2014-11-18', 13]]
_mbc=[[4,'2014-09-02',90],
[6,'2006-10-14',2880],
[7,'2014-09-02',90],
[8,'2006-01-01',106],
[8,'2014-09-02',90],
[9,'2014-09-02',90],
[10,'2014-09-02',90],
[11,'2014-09-02',90],
[12,'2013-09-07',450],
[19,'2006-01-01',3256],
[20,'2008-10-03',2160],
[21,'2006-01-01',3256],
[22,'2009-04-01',2070],
[23,'2006-01-01',3256],
[24,'2009-04-01',1260],
[25,'2006-01-01',3256],
[26,'2008-04-06',2430],
[27,'2006-01-01',3256],
[28,'2006-04-17',1800],
[29,'2006-01-01',1546],
[30,'2007-04-12',1080],
[31,'2007-04-12',1260],
[32,'2007-04-12',1260],
[36,'2010-03-27',1260],
[39,'2011-03-22',1080],
[42,'2006-10-14',2970],
[48,'2006-01-01',3256],
[49,'2012-09-12',720],
[50,'2012-09-12',810],
[53,'2013-09-07',450],
[54,'2006-10-14',2970],
[56,'2014-09-02',90],
[84,'2014-09-02',90],
[85,'2014-09-02',90],
[86,'2013-03-11',180],
[86,'2014-09-02',90],
[87,'2014-09-02',90],]
_mbc=[[4,'2014-09-02',90],
[6,'2006-10-14',2880],
[7,'2014-09-02',90],
[8,'2006-01-01',106],
[8,'2014-09-02',90],
[9,'2014-09-02',90],
[10,'2014-09-02',90],
[11,'2014-09-02',90],
[12,'2013-09-07',450],
[19,'2006-01-01',3256],
[20,'2008-10-03',2160],
[21,'2006-01-01',3256],
[22,'2009-04-01',2070],
[23,'2006-01-01',3256],
[24,'2009-04-01',1260],
[25,'2006-01-01',3256],
[26,'2008-04-06',2430],
[27,'2006-01-01',3256],
[28,'2006-04-17',1800],
[29,'2006-01-01',1546],
[30,'2007-04-12',1080],
[31,'2007-04-12',1260],
[32,'2007-04-12',1260],
[36,'2010-03-27',1260],
[39,'2011-03-22',1080],
[42,'2006-10-14',2970],
[48,'2006-01-01',3256],
[49,'2012-09-12',720],
[50,'2012-09-12',810],
[53,'2013-09-07',450],
[54,'2006-10-14',2970],
[56,'2014-09-02',90],
[84,'2014-09-02',90],
[85,'2014-09-02',90],
[86,'2013-03-11',180],
[86,'2014-09-02',90],
[87,'2014-09-02',90],]
def do_mbc(mbc):
    f=open('mbc.save','ab')
    oneday=datetime.timedelta(days=1)
    while mbc != []:
        gid,_start_date,days=mbc.pop()
        print gid,_start_date,days
        y,m,d=map(int,_start_date.split('-'))
        date=datetime.datetime(y,m,d)
        try:
            while days!=0:
                bdate='%d-%d-%d'%(date.year,date.month,date.day)
                songs=get_mbc_song(gid,bdate)
                if songs!=-1:
                    for artist,song_title in songs:
                        artist=artist.replace("'","''")
                        song_title=song_title.replace("'","''")
                        tmp='%d\t%d\t%d\t%d\t%s\t%s\n'%(gid,date.year,date.month,date.day,artist,song_title)
                        #print tmp[:-1]
                        f.write(tmp.encode('utf8'))
                days-=1
                date=date+oneday
        except:
            mbc.append([gid,bdate,days])
            print repr(mbc)
            f.close()
            return -1
    f.close()

def get_mbc_song(gid,bdate):
    songs=[]
    url='http://miniunit.imbc.com/list/musicitemlist?rtype=jsonp&gid=%d&bdate=%s'
    url=url%(gid,bdate)
    try:
        js=json.load(urllib.urlopen(url))
    except:
        return -1
    if js ==[]:
        return -1
    else:
        for j in js:
            songs.append([j['ArtistName'],j['TrackTitle']])
    return songs

def get_sbs_song():
    pass

def get_kbs_song():
    pass#real pass

do_mbc(mbc)