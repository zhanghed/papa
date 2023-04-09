import re
# "https://video.pearvideo.com/mp4/adshort/20200601/cont-1677772-15176722_adpkg-ad_hd.mp4"
# "https://image2.pearvideo.com/cont/20200601/cont-1677772-12395438.png"
# "https://video.pearvideo.com/mp4/adshort/20200601/1681022181061-15176722_adpkg-ad_hd.mp4"
# a="https://image2.pearvideo.com/cont/20200601/cont-1677772-12395438.png"
# a = re.findall("cont-.*-", a)[0]
# print(a)

a = "https://image2.pearvideo.com/cont/20200601/cont-1677772-12395438.png"
b = "https://video.pearvideo.com/mp4/adshort/20200601/1681022181061-15176722_adpkg-ad_hd.mp4"

t = re.findall("https.*/", b)[0] + re.findall("cont-.*-", a)[0] + re.findall("-(.*)", b)[0]
print(t)

