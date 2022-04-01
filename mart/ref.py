from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view


# Category
class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cat_imgs/")

    class Meta:
        verbose_name_plural = '2. Categories'

    def __str__(self):
        return self.title


# Color
class Color(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '4. Colors'

    def color_bg(self):
        return mark_safe('<div style="width:30px; height:30px; background-color:%s"></div>' % (self.color_code))

    def __str__(self):
        return self.title


# Size
class Size(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '5. Sizes'

    def __str__(self):
        return self.title


# Product Model
class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=400)
    detail = models.TextField()
    specs = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '6. Products'

    def __str__(self):
        return self.title


# Product Attribute
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="product_imgs/", null=True)

    class Meta:
        verbose_name_plural = '7. ProductAttributes'

    def __str__(self):
        return self.product.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))


# https://i.ibb.co/0jP2hF1/01new-1.png
# https://i.ibb.co/q7fJt6P/01new-2.png
# https://i.ibb.co/KD6h39d/01new-3.png
# https://i.ibb.co/bRCGD20/01new-4.png
# https://i.ibb.co/tmFXz1K/01new-5.png
# https://i.ibb.co/xYHyxTM/01new-6.png
# https://i.ibb.co/hmTMLDN/01new-7.png
# https://i.ibb.co/L1pNkdY/01new-8.png
# https://i.ibb.co/985Kg9h/01new-9.png
# https://i.ibb.co/7tXd0jb/01new-10.png
# https://i.ibb.co/vm0fyBq/01new-11.png
# https://i.ibb.co/DzBj2X2/01new-12.png
# https://i.ibb.co/cLYbQPG/1.jpg
# https://i.ibb.co/fGRw6SP/1-1001.png
# https://i.ibb.co/23GwS6d/1-1002.jpg
# https://i.ibb.co/WgtL9gs/1-1003.jpg
# https://i.ibb.co/yy36HRc/1-2002.jpg
# https://i.ibb.co/Gvy7Wfp/1-3001.jpg
# https://i.ibb.co/ww8jWbt/1-3002.jpg
# https://i.ibb.co/CPNZrKp/1q-1.jpg
# https://i.ibb.co/3YzJFWN/1q-2.jpg
# https://i.ibb.co/pzfNr8z/1q-3.jpg
# https://i.ibb.co/R65vjqN/1s-1.jpg
# https://i.ibb.co/W3p4WKj/1s-2.jpg
# https://i.ibb.co/NjrZsYc/1s-3.jpg
# https://i.ibb.co/r0tRrPn/1s-4.jpg
# https://i.ibb.co/DwQk2xs/1s-5.jpg
# https://i.ibb.co/CKQSCyY/1s-6.jpg
# https://i.ibb.co/wzSDYbR/2.jpg
# https://i.ibb.co/64vf5V7/2-1001.jpg
# https://i.ibb.co/tZv9PKp/2-1002.jpg
# https://i.ibb.co/jT4DQrt/2-2001.jpg
# https://i.ibb.co/4Jx40d1/2-2002.jpg
# https://i.ibb.co/f9SRNCk/2-3001.jpg
# https://i.ibb.co/sHPWT0T/2-3002.jpg
# https://i.ibb.co/Tc5k7zL/3.jpg
# https://i.ibb.co/zWc4YV2/3.png
# https://i.ibb.co/cCTQPxL/3-1001.jpg
# https://i.ibb.co/ryhyX8H/3-1002.jpg
# https://i.ibb.co/fpdvrp5/3-2001.jpg
# https://i.ibb.co/rbk8TdW/3-2002.jpg
# https://i.ibb.co/prvpkVR/3-3001.jpg
# https://i.ibb.co/xjMPDmz/3-3002.jpg
# https://i.ibb.co/RcLM1BZ/3-4001.jpg
# https://i.ibb.co/YNjdSyp/3-4002.jpg
# https://i.ibb.co/mzkvjpc/4.jpg
# https://i.ibb.co/MsKrvrn/4.webp
# https://i.ibb.co/PwQkFsd/4-1001.jpg
# https://i.ibb.co/d0Zx9sw/4-1002.jpg
# https://i.ibb.co/n3byZ2n/4-2001.jpg
# https://i.ibb.co/FxZ3qxM/4-2002.jpg
# https://i.ibb.co/TWQCQVX/4-3001.jpg
# https://i.ibb.co/TtpYBjN/4-3002.jpg
# https://i.ibb.co/4mzy4qF/4-hover.jpg
# https://i.ibb.co/6XJK2ND/5.jpg
# https://i.ibb.co/rdPQHcc/5-1001.jpg
# https://i.ibb.co/M9hfjW3/5-1002.jpg
# https://i.ibb.co/PFNr405/5-2001.jpg
# https://i.ibb.co/gvmjybn/5-2002.jpg
# https://i.ibb.co/k2gMzcM/5-3001.jpg
# https://i.ibb.co/g39f6y7/5-3002.jpg
# https://i.ibb.co/m0rq0xW/5-hover.jpg
# https://i.ibb.co/LhRzKYL/6.jpg
# https://i.ibb.co/xCD2kv9/6-hover.jpg
# https://i.ibb.co/wzSDYbR/2.jpg
# https://i.ibb.co/2kX1bSt/7-hover.jpg
# https://i.ibb.co/N20hGLY/8.jpg
# https://i.ibb.co/4wkXXGc/8-hover.jpg
# https://i.ibb.co/cLYbQPG/1.jpg
# https://i.ibb.co/NV4b1mS/9-hover.jpg
# https://i.ibb.co/LZYT95N/10.jpg
# https://i.ibb.co/8sjJZ5R/10-hover.jpg
# https://i.ibb.co/9gw1kzp/11.jpg
# https://i.ibb.co/wp9h9m9/11.png
# https://i.ibb.co/ZgbvndW/11-hover.jpg
# https://i.ibb.co/5knzGf6/12.jpg
# https://i.ibb.co/txy5cMT/12.png
# https://i.ibb.co/SmHJ7zG/12-hover.jpg
# https://i.ibb.co/cDRBnBh/13.jpg
# https://i.ibb.co/ZVQNQLy/13.png
# https://i.ibb.co/7KVcG2g/13-hover.jpg
# https://i.ibb.co/RcL1gw9/14.jpg
# https://i.ibb.co/Vj1M7V3/14.png
# https://i.ibb.co/z2JZTRs/14-hover.jpg
# https://i.ibb.co/Jm60qcr/15.jpg
# https://i.ibb.co/pW45mgY/15-hover.jpg
# https://i.ibb.co/Tc5k7zL/3.jpg
# https://i.ibb.co/r7B9fV1/16-hover.jpg
# https://i.ibb.co/L6ZPHqx/17.jpg
# https://i.ibb.co/H7fRydV/17-hover.jpg
# https://i.ibb.co/VTG7YjC/18.jpg
# https://i.ibb.co/kGCJgnM/19.jpg
# https://i.ibb.co/SwG21Hj/20.jpg
# https://i.ibb.co/6W5fVnJ/21.jpg
# https://i.ibb.co/B2xjTNz/22.jpg
# https://i.ibb.co/7nyykPG/23.jpg
# https://i.ibb.co/JpvLs8F/24.jpg
# https://i.ibb.co/Wnh6wzw/24-blog-1.jpg
# https://i.ibb.co/KGqzHBs/24-blog-2.jpg
# https://i.ibb.co/Wcs0Xtt/24-blog-3.jpg
# https://i.ibb.co/ckj6Wjp/24-blog-4.jpg
# https://i.ibb.co/K0HHtyL/24-blog-5.jpg
# https://i.ibb.co/9pH1MYD/24-blog-6.jpg
# https://i.ibb.co/KsCmnrf/24-blog-7.jpg
# https://i.ibb.co/WsbH28c/24-blog-8.jpg
# https://i.ibb.co/wWb4RRz/24-blog-9.jpg
# https://i.ibb.co/zs9q4JF/24-blog-10.jpg
# https://i.ibb.co/XDxryHV/24-blog-11.jpg
# https://i.ibb.co/9sRxjtg/24-blog-12.jpg
# https://i.ibb.co/JHPGc0b/24-blog-13.jpg
# https://i.ibb.co/C9HD3W1/24-blog-14.jpg
# https://i.ibb.co/d6QTsQP/24-blog-15.jpg
# https://i.ibb.co/T40CLc6/24-blog-16.jpg
# https://i.ibb.co/d0nZMt9/24-blog-17.jpg
# https://i.ibb.co/bzjL4dJ/24-blog-18.jpg
# https://i.ibb.co/djV5K6Z/24-blog-19.jpg
# https://i.ibb.co/pzzDSg1/24-blog-20.jpg
# https://i.ibb.co/WKz13Lm/24-blog-21.jpg
# https://i.ibb.co/94PHg1F/24-blog-22.jpg
# https://i.ibb.co/WFxvCNQ/24-blog-23.jpg
# https://i.ibb.co/kyN12Jz/24-blog-24.jpg
# https://i.ibb.co/09qCGtC/24-blog-25.jpg
# https://i.ibb.co/PCzQyK2/24-blog-26.jpg
# https://i.ibb.co/g7mJCVt/24-blog-27.jpg
# https://i.ibb.co/WtcrD8h/24-blog-28.jpg
# https://i.ibb.co/hHpDRB3/24-blog-29.jpg
# https://i.ibb.co/njtr2VN/24-blog-30.jpg
# https://i.ibb.co/gmYFds4/24-blog-31.jpg
# https://i.ibb.co/K67wqjz/24-blog-32.jpg
# https://i.ibb.co/7yvfSWz/25.jpg
# https://i.ibb.co/RTb8SqK/26.jpg
# https://i.ibb.co/Vjbqs9V/44.jpg
# https://i.ibb.co/rkNhgCy/51.jpg
# https://i.ibb.co/xJQKFpN/52.jpg
# https://i.ibb.co/xjFP8KX/53.jpg
# https://i.ibb.co/Zdpqmrx/55.jpg
# https://i.ibb.co/MpDcWt8/61.jpg
# https://i.ibb.co/7tS2SWG/61.webp
# https://i.ibb.co/hB8rvXg/62.jpg
# https://i.ibb.co/J2S9pKh/62.webp
# https://i.ibb.co/tB2pjDp/63.jpg
# https://i.ibb.co/4sNvW5N/63.webp
# https://i.ibb.co/gr8KfyV/71.jpg
# https://i.ibb.co/1LsW9bR/72.jpg
# https://i.ibb.co/kmnW9D6/73.jpg
# https://i.ibb.co/mJBkYhy/74.jpg
# https://i.ibb.co/bJyNqd0/81.jpg
# https://i.ibb.co/WsPDdbF/82.jpg
# https://i.ibb.co/xjFP8KX/53.jpg
# https://i.ibb.co/JyNbzZy/84.jpg
# https://i.ibb.co/kDSj0P2/18483469.jpg
# https://i.ibb.co/PCr2wyS/19502140.jpg
# https://i.ibb.co/D4nJjVd/aa.jpg
# https://i.ibb.co/ctdzLRv/About-icon1.png
# https://i.ibb.co/d4gXSWQ/About-icon2.png
# https://i.ibb.co/86QNY0w/About-icon3.png
# https://i.ibb.co/8bqvrN0/about1.jpg
# https://i.ibb.co/NtJW2d4/about2.jpg
# https://i.ibb.co/3WnCgcJ/about3.jpg
# https://i.ibb.co/g4dxr06/about4.jpg
# https://i.ibb.co/BqhsNpd/about-us-left-image.png
# https://i.ibb.co/jH4ZHRb/about-us-policy-bg.jpg
# https://i.ibb.co/CnQ2wMg/about-us-signature.png
# https://i.ibb.co/z5QrQg4/accessories-category-item.png
# https://i.ibb.co/XYgc3X7/ads.jpg
# https://i.ibb.co/GvMw090/ads2.jpg
# https://i.ibb.co/RgNktp6/alpha.jpg
# https://i.ibb.co/8YRsyn9/apanel.png
# https://i.ibb.co/gtgbyFT/apanel1.png
# https://i.ibb.co/3YYVPws/author.jpg
# https://i.ibb.co/k3pkFhN/a.jpg
# https://i.ibb.co/5GDNYDs/A.png
# https://i.ibb.co/tKJjTR8/background.jpg
# https://i.ibb.co/qx41rRV/baner01.png
# https://i.ibb.co/Y0BS9sw/baner02.png
# https://i.ibb.co/47JM5br/banner.webp
# https://i.ibb.co/wz1m9Yf/banner1.jpg
# https://i.ibb.co/NKgfbvn/banner2.jpg
# https://i.ibb.co/hVVKfrZ/banner3.jpg
# https://i.ibb.co/1ZXvrkg/banner4.jpg
# https://i.ibb.co/ZHTqv6J/banner5.jpg
# https://i.ibb.co/bJCJLvZ/banner6.jpg
# https://i.ibb.co/425cC3c/banner7.jpg
# https://i.ibb.co/6rDYnjz/banner8.jpg
# https://i.ibb.co/TYk5ryX/banner9.jpg
# https://i.ibb.co/K5x5vVQ/banner10.jpg
# https://i.ibb.co/D1sySXV/banner11.jpg
# https://i.ibb.co/gVRsJdD/banner12.jpg
# https://i.ibb.co/QjP2LgW/banner13.jpg
# https://i.ibb.co/zHq1qsB/banner14.jpg
# https://i.ibb.co/z2B0KC8/banner15.jpg
# https://i.ibb.co/v49YwGx/banner-image-1.jpg
# https://i.ibb.co/wL1dPJN/banner-image-2.jpg
# https://i.ibb.co/Q9X7FmG/banner-image-3.jpg
# https://i.ibb.co/b1S8kj3/banner-image-cosmetics-1.jpg
# https://i.ibb.co/z66cVhG/banner-image-cosmetics-2.jpg
# https://i.ibb.co/42T3tV5/banner-image-cosmetics-3.jpg
# https://i.ibb.co/DQLxmfm/banner-image-furniture-1.jpg
# https://i.ibb.co/hKwW6g4/banner-image-furniture-2.jpg
# https://i.ibb.co/K5mHcXg/banner-image-furniture-3.jpg
# https://i.ibb.co/gRbZXCs/big-logo.png
# https://i.ibb.co/8Y1LzKY/blog-next.jpg
# https://i.ibb.co/x6F1Ky8/blog-pre.jpg
# https://i.ibb.co/9ywqky9/blog01.jpg
# https://i.ibb.co/wKm8YV1/blog1.jpg
# https://i.ibb.co/LpbVZ9V/blog-1.png
# https://i.ibb.co/kJFSQ9p/blog02.jpg
# https://i.ibb.co/MNzj82M/blog2.jpg
# https://i.ibb.co/X78Zj3D/blog-2.png
# https://i.ibb.co/3SR3MB7/blog03.jpg
# https://i.ibb.co/hY4TMVs/blog3.jpg
# https://i.ibb.co/KwV0D8Q/blog-3.png
# https://i.ibb.co/mtQ86ST/blog4.jpg
# https://i.ibb.co/gWVGcxH/blog-4.png
# https://i.ibb.co/wKm8YV1/blog1.jpg
# https://i.ibb.co/K75W1Wr/blog6.jpg
# https://i.ibb.co/2YtL12K/blog7.jpg
# https://i.ibb.co/S65W9fZ/blog8.jpg
# https://i.ibb.co/0chC33n/blogads.jpg
# https://i.ibb.co/6r1WTK9/blog-big1.jpg
# https://i.ibb.co/RcF7rJw/blog-big2.jpg
# https://i.ibb.co/z794KRd/blog-big3.jpg
# https://i.ibb.co/j5B77gd/blog-big4.jpg
# https://i.ibb.co/YTt8rhk/blog-big5.jpg
# https://i.ibb.co/wKm8YV1/blog1.jpg
# https://i.ibb.co/K75W1Wr/blog6.jpg
# https://i.ibb.co/MNzj82M/blog2.jpg
# https://i.ibb.co/hY4TMVs/blog3.jpg
# https://i.ibb.co/mtQ86ST/blog4.jpg
# https://i.ibb.co/2YtL12K/blog7.jpg
# https://i.ibb.co/KVQQ13y/blog-post-01.jpg
# https://i.ibb.co/NsT1Yn7/blog-post-02.jpg
# https://i.ibb.co/zR0myX7/blog-post-03.jpg
# https://i.ibb.co/nw0g6dT/bride.jpg
# https://i.ibb.co/xm0svf4/bs-list1.jpg
# https://i.ibb.co/z6yybCw/bs-list2.jpg
# https://i.ibb.co/gmg7Fyd/bs-list3.jpg
# https://i.ibb.co/9H38b9P/b.jpg
# https://i.ibb.co/L9BLSJk/categorie-1.jpg
# https://i.ibb.co/r59mPvM/categorie-2.jpg
# https://i.ibb.co/0mPzrZ6/categorie-3.jpg
# https://i.ibb.co/YQzJQhM/categorie-4.jpg
# https://i.ibb.co/RN4XjG2/category1.jpg
# https://i.ibb.co/xJT0QLz/category2.jpg
# https://i.ibb.co/6v0DLXN/category3.jpg
# https://i.ibb.co/K0bxf9Q/category4.jpg
# https://i.ibb.co/NWSqgJM/category5.jpg
# https://i.ibb.co/nPgVYPn/cmnt01.jpg
# https://i.ibb.co/Bqp6q4J/cmnt02.jpg
# https://i.ibb.co/VqG57Mk/cmnt03.jpg
# https://i.ibb.co/9g7dcKF/code.gif
# https://i.ibb.co/ydmfsx9/comment2.jpg
# https://i.ibb.co/rZHCtp6/comment2-png.jpg
# https://i.ibb.co/ydmfsx9/comment2.jpg
# https://i.ibb.co/pjx7sXM/comment-author-01.jpg
# https://i.ibb.co/25PQp0t/comment-author-02.jpg
# https://i.ibb.co/jM3MVf0/comment-author-03.jpg
# https://i.ibb.co/6P2vcrT/covid.jpg
# https://i.ibb.co/RbLVpGV/cta-bg.jpg
# https://i.ibb.co/XxcymnT/cta-main-homepage-bg.jpg
# https://i.ibb.co/ctnccyj/c.jpg
# https://i.ibb.co/5MZvktZ/dfa.jpg
# https://i.ibb.co/ftV85hq/diallo.png
# https://i.ibb.co/yqcXdhk/download.jpg
# https://i.ibb.co/R2cGFph/entries-01.jpg
# https://i.ibb.co/7pX53Tp/entries-02.jpg
# https://i.ibb.co/TbjPTSC/entries-03.jpg
# https://i.ibb.co/r3FW02Y/farniture-1.jpg
# https://i.ibb.co/q75SHY6/farniture-1-hover.jpg
# https://i.ibb.co/8MT7XPC/farniture-2.jpg
# https://i.ibb.co/8MT7XPC/farniture-2.jpg
# https://i.ibb.co/q75SHY6/farniture-1-hover.jpg
# https://i.ibb.co/r3FW02Y/farniture-1.jpg
# https://i.ibb.co/BTJjn1W/farniture-4.jpg
# https://i.ibb.co/rwVqbgh/farniture-4-hover.jpg
# https://i.ibb.co/mGmW3CP/farniture-5.jpg
# https://i.ibb.co/1TqHFdS/farniture-5-hover.jpg
# https://i.ibb.co/BTJjn1W/farniture-4.jpg
# https://i.ibb.co/BTJjn1W/farniture-4.jpg
# https://i.ibb.co/RzN952R/farniture-7.jpg
# https://i.ibb.co/cwsfRMG/farniture-7-hover.jpg
# https://i.ibb.co/vD7nLm0/farniture-8.jpg
# https://i.ibb.co/CwBK9Kk/farniture-8-hover.jpg
# https://i.ibb.co/pxCMjFd/farniture-9.jpg
# https://i.ibb.co/tPtcQ7B/farniture-9-hover.jpg
# https://i.ibb.co/CwBK9Kk/farniture-8-hover.jpg
# https://i.ibb.co/vD7nLm0/farniture-8.jpg
# https://i.ibb.co/JrVpW2t/farniture-11.jpg
# https://i.ibb.co/1m0yb3d/farniture-11-hover.jpg
# https://i.ibb.co/jGVcDsb/farniture-12.jpg
# https://i.ibb.co/mC295WX/farniture-12-hover.jpg
# https://i.ibb.co/mXQ2Qkx/farniture-13.jpg
# https://i.ibb.co/RS5HLCM/farniture-13-hover.jpg
# https://i.ibb.co/mC295WX/farniture-12-hover.jpg
# https://i.ibb.co/jGVcDsb/farniture-12.jpg
# https://i.ibb.co/8KfCDFt/farniture-15.jpg
# https://i.ibb.co/VjPMsCw/farniture-15-hover.jpg
# https://i.ibb.co/VjPMsCw/farniture-15-hover.jpg
# https://i.ibb.co/8KfCDFt/farniture-15.jpg
# https://i.ibb.co/mtDZFj6/favicon.png
# https://i.ibb.co/hy6f7NT/featured-product-01.png
# https://i.ibb.co/RCcmKRv/featured-product-02.png
# https://i.ibb.co/RBD0KdG/featured-product-03.png
# https://i.ibb.co/0Y26rHc/furniture-featured-product-01.jpg
# https://i.ibb.co/Cs4PTYs/furniture-featured-product-02.jpg
# https://i.ibb.co/zxQNvBk/furniture-featured-product-03.jpg
# https://i.ibb.co/gjWHq0C/furniture-image-01.jpg
# https://i.ibb.co/7tYHBDh/furniture-image-02.jpg
# https://i.ibb.co/k8ttZ95/girl.png
# https://i.ibb.co/VDPQ8cq/header-bg.gif
# https://i.ibb.co/CMt94yy/hot-deals-category-item.png
# https://i.ibb.co/Qm6ZSSf/index-ads1.jpg
# https://i.ibb.co/KVCMnPB/index-ads2.jpg
# https://i.ibb.co/bPzmcYh/index-ads3.jpg
# https://i.ibb.co/jTckGVx/insta-1.jpg
# https://i.ibb.co/QNPbbVz/insta-2.jpg
# https://i.ibb.co/5Mm8LX0/insta-3.jpg
# https://i.ibb.co/jzQVVp6/insta-4.jpg
# https://i.ibb.co/jGw1Bx2/insta-5.jpg
# https://i.ibb.co/GRv7H5r/insta-6.jpg
# https://i.ibb.co/FmB48JP/instaglry01.jpg
# https://i.ibb.co/cQRxy1f/instaglry02.jpg
# https://i.ibb.co/8BMDSbb/instaglry03.jpg
# https://i.ibb.co/vZtK196/instaglry04.jpg
# https://i.ibb.co/Z8fZQ80/instaglry05.jpg
# https://i.ibb.co/qjMT07v/instaglry06.jpg
# https://i.ibb.co/9VwGgzF/instaglry07.jpg
# https://i.ibb.co/nrpvQh1/instaglry08.jpg
# https://i.ibb.co/fn7h1QN/instaglry09.jpg
# https://i.ibb.co/x7C0kTj/instagram-footer-01.jpg
# https://i.ibb.co/Ctk6byW/instagram-footer-02.jpg
# https://i.ibb.co/XsrfxNF/instagram-footer-03.jpg
# https://i.ibb.co/brm9xXY/instagram-footer-04.jpg
# https://i.ibb.co/9g6NZfn/instagram-footer-05.jpg
# https://i.ibb.co/7rNGr7S/instragam1.jpg
# https://i.ibb.co/RHgGF4W/instragam2.jpg
# https://i.ibb.co/P1XvDgL/instragam3.jpg
# https://i.ibb.co/zF5fwW9/instragam4.jpg
# https://i.ibb.co/pJ8Vygt/instragam5.jpg
# https://i.ibb.co/4JJ4FNw/kid-category-item.png
# https://i.ibb.co/ZNhSNGg/lg-1.jpg
# https://i.ibb.co/VvX3zdQ/lg-2.jpg
# https://i.ibb.co/tMyqdGS/lg-3.jpg
# https://i.ibb.co/W36tg6Z/lg-4.jpg
# https://i.ibb.co/NNqPSJ2/log.gif
# https://i.ibb.co/VgYdxRh/login-img.png
# https://i.ibb.co/8NNxv3D/login-logo.png
# https://i.ibb.co/BgxYZN8/logo.png
# https://i.ibb.co/NxXCMxK/logo1.jpg
# https://i.ibb.co/BgxYZN8/logo.png
# https://i.ibb.co/bK4vb5n/logo3.png
# https://i.ibb.co/RHx3fv3/logo4.png
# https://i.ibb.co/k2Nq7C1/logo-icon.png
# https://i.ibb.co/jD8knVN/logo-icon-black.png
# https://i.ibb.co/JcGsHXX/man-category-item.png
# https://i.ibb.co/PNwJYwq/mastercard.png
# https://i.ibb.co/R3bXGLT/me.jpg
# https://i.ibb.co/tLPK850/mid-ads1.jpg
# https://i.ibb.co/9Y7wyCH/mid-ads2.jpg
# https://i.ibb.co/f2CgKLL/mini-blog1.jpg
# https://i.ibb.co/9Nj6yr5/mini-blog2.jpg
# https://i.ibb.co/2njntN4/mvc.png
# https://i.ibb.co/CmJc0jq/MVCdetails.png
# https://i.ibb.co/nRdMg4W/new-arrival-ads.jpg
# https://i.ibb.co/wd8K1Db/new-arrivals-category-item.png
# https://i.ibb.co/C8Ljbhx/news-move1.png
# https://i.ibb.co/hMDpxjM/news-move2.png
# https://i.ibb.co/nDgBDsP/news-move3.png
# https://i.ibb.co/TKxybv9/news-move4.png
# https://i.ibb.co/pjz3Vfm/newsletter-bg.jpg
# https://i.ibb.co/GTQc4fZ/newsletter-image.png
# https://i.ibb.co/cK5SjDR/nfa.png
# https://i.ibb.co/hXdBhrw/niaomi.jpg
# https://i.ibb.co/xmkNsmF/OIP.jpg
# https://i.ibb.co/jTQWK6f/p-4.jpg
# https://i.ibb.co/hC2zFZT/p-5.jpg
# https://i.ibb.co/GpH4q6H/p-6.jpg
# https://i.ibb.co/jVkNV10/p-7.jpg
# https://i.ibb.co/c8hDPnC/page-heading-bg.jpg
# https://i.ibb.co/LrnWNSd/payment1.png
# https://i.ibb.co/hY832dc/payment2.png
# https://i.ibb.co/9NrKbBh/payment3.png
# https://i.ibb.co/FK1xQnT/payment4.png
# https://i.ibb.co/fCx6Kd2/paypal.png
# https://i.ibb.co/tLFHtTj/portfolio-masonry-01.jpg
# https://i.ibb.co/xGCvmVx/portfolio-masonry-02.jpg
# https://i.ibb.co/LCFLmr6/portfolio-masonry-03.jpg
# https://i.ibb.co/FxdXxpD/portfolio-masonry-04.jpg
# https://i.ibb.co/VCRbx7G/portfolio-masonry-05.jpg
# https://i.ibb.co/tx6zgv2/portfolio-masonry-06.jpg
# https://i.ibb.co/k9g8B9Y/portfolio-masonry-07.jpg
# https://i.ibb.co/6RQrSJF/pro1.jpg
# https://i.ibb.co/6ZWztSQ/pro2.jpg
# https://i.ibb.co/hMnyBrL/product1.jpg
# https://i.ibb.co/br5Zmwj/product2.jpg
# https://i.ibb.co/mqTcvM1/product3.jpg
# https://i.ibb.co/gTnFbJY/product4.jpg
# https://i.ibb.co/gv3XBb5/product5.jpg
# https://i.ibb.co/6XtQNyG/product6.jpg
# https://i.ibb.co/qYfFf3K/product7.jpg
# https://i.ibb.co/4Jp7Jw4/product8.jpg
# https://i.ibb.co/rMhPGtJ/product9.jpg
# https://i.ibb.co/7J4B33L/product10.jpg
# https://i.ibb.co/HFxyYFK/product11.jpg
# https://i.ibb.co/QCSgTpM/product12.jpg
# https://i.ibb.co/VxLxVtj/product13.jpg
# https://i.ibb.co/SBXd5c3/product14.jpg
# https://i.ibb.co/Lx66Kwg/product15.jpg
# https://i.ibb.co/SBHKxrx/product16.jpg
# https://i.ibb.co/pz86mVY/product17.jpg
# https://i.ibb.co/s33d3Sp/product18.jpg
# https://i.ibb.co/kqTnN44/product19.jpg
# https://i.ibb.co/CvsT6V4/product20.jpg
# https://i.ibb.co/k08yK4n/product21.jpg
# https://i.ibb.co/gDvrQNJ/product22.jpg
# https://i.ibb.co/bBK1MXN/product23.jpg
# https://i.ibb.co/fM6Sfzh/product24.jpg
# https://i.ibb.co/XF4Zrmg/product25.jpg
# https://i.ibb.co/6ZB240s/product26.jpg
# https://i.ibb.co/0K77hwv/product27.jpg
# https://i.ibb.co/RyFzW4g/product28.jpg
# https://i.ibb.co/cFsvwP6/product29.jpg
# https://i.ibb.co/F7yCgh6/product30.jpg
# https://i.ibb.co/CV70M0w/product31.jpg
# https://i.ibb.co/1Mcq2LP/product32.jpg
# https://i.ibb.co/R0G5PNV/product33.jpg
# https://i.ibb.co/Cn6GtPV/product34.jpg
# https://i.ibb.co/tK5znqm/product35.jpg
# https://i.ibb.co/C9cWzcq/product36.jpg
# https://i.ibb.co/BNKRhny/product37.jpg
# https://i.ibb.co/fH8rNnw/product38.jpg
# https://i.ibb.co/THw05SG/product39.jpg
# https://i.ibb.co/wyRZPdV/product40.jpg
# https://i.ibb.co/j4vfYjK/product41.jpg
# https://i.ibb.co/QHWxwqD/product42.jpg
# https://i.ibb.co/S3B1Jqx/product43.jpg
# https://i.ibb.co/wSy69z9/productbig1.jpg
# https://i.ibb.co/HtxHkTL/productbig2.jpg
# https://i.ibb.co/t2PSgTj/productbig3.jpg
# https://i.ibb.co/B6Zjj9Q/productbig4.jpg
# https://i.ibb.co/9ZSqTNY/project-details-01.jpg
# https://i.ibb.co/PNW6wSC/project-details-02.jpg
# https://i.ibb.co/hBCJs4C/project-details-03.jpg
# https://i.ibb.co/JCkL7BH/pro-single01.jpg
# https://i.ibb.co/JRRbrSh/pro-single02.jpg
# https://i.ibb.co/xSgj6jh/pro-single03.jpg
# https://i.ibb.co/ZTdcvsy/pro-singlethumb01.jpg
# https://i.ibb.co/VwcNWbT/pro-singlethumb02.jpg
# https://i.ibb.co/BPfP3bP/pro-singlethumb03.jpg
# https://i.ibb.co/m03z98X/recent-item-01.jpg
# https://i.ibb.co/r6ggd4t/recent-item-02.jpg
# https://i.ibb.co/kKvqMXw/recent-item-03.jpg
# https://i.ibb.co/P9LHVwV/recent-item-04.jpg
# https://i.ibb.co/CKRfYRB/recent-item-05.jpg
# https://i.ibb.co/QNDDYxG/recent-item-06.jpg
# https://i.ibb.co/3k3RMjx/recent-item-07.jpg
# https://i.ibb.co/qBPH9c5/recent-item-08.jpg
# https://i.ibb.co/HPGv6JK/recent-item-09.jpg
# https://i.ibb.co/7rLWwLm/recent-item-cosmetics-01.jpg
# https://i.ibb.co/nzQwrB0/recent-item-cosmetics-02.jpg
# https://i.ibb.co/5KtHv4b/recent-item-cosmetics-03.jpg
# https://i.ibb.co/wRs1d55/recent-item-cosmetics-04.jpg
# https://i.ibb.co/jZRnhQV/recent-item-cosmetics-05.jpg
# https://i.ibb.co/zQJWpQg/recent-item-cosmetics-06.jpg
# https://i.ibb.co/44nVTxv/recent-post-01.jpg
# https://i.ibb.co/Zdj20mH/recent-post-02.jpg
# https://i.ibb.co/4FLdfzL/recent-post-03.jpg
# https://i.ibb.co/Kx3tPLB/second-cta-bg.jpg
# https://i.ibb.co/ZXR0YFD/shop.jpg
# https://i.ibb.co/qYpXRpv/shop.png
# https://i.ibb.co/dWy5DBY/shopcart01.jpg
# https://i.ibb.co/kXynDgc/shopcart02.jpg
# https://i.ibb.co/QDdPZ7T/shopcart03.jpg
# https://i.ibb.co/Xbbg4kC/shopcart04.jpg
# https://i.ibb.co/f2sBkmT/shopcart05.jpg
# https://i.ibb.co/p0hz1fL/shopping-cart-01.jpg
# https://i.ibb.co/LRwrDpZ/shopping-cart-02.jpg
# https://i.ibb.co/CKK8mJ0/shopping-cart-03.jpg
# https://i.ibb.co/qmhc0jZ/single-product-v1-01.jpg
# https://i.ibb.co/Vm06v8y/single-product-v1-02.jpg
# https://i.ibb.co/fShfP7r/single-product-v1-03.jpg
# https://i.ibb.co/XbcXdJZ/single-product-v1-04.jpg
# https://i.ibb.co/7K43vRW/slide1.jpg
# https://i.ibb.co/Tv4SJ35/slide2.jpg
# https://i.ibb.co/BqfSKLr/slide3.jpg
# https://i.ibb.co/nPb3k0v/slide4.jpg
# https://i.ibb.co/TLT46KV/slide5.jpg
# https://i.ibb.co/Zx32gyW/slide6.jpg
# https://i.ibb.co/6HGktRb/slide7.jpg
# https://i.ibb.co/gzbmcbg/slide8.jpg
# https://i.ibb.co/bKyg0c9/slider1.jpg
# https://i.ibb.co/tZsvt7Y/slider2.jpg
# https://i.ibb.co/JjPt5Vz/slider3.jpg
# https://i.ibb.co/jHfq834/slider4.jpg
# https://i.ibb.co/CBbGRhn/slider5.jpg
# https://i.ibb.co/pbdgCW0/slider6.jpg
# https://i.ibb.co/z5bKQ9v/slider7.jpg
# https://i.ibb.co/LRr0tbp/slider8.jpg
# https://i.ibb.co/QKN2bjR/Spring-MVC.png
# https://i.ibb.co/rw802Sb/spring.png
# https://i.ibb.co/F6CdBxd/ssm-liucheng.png
# https://i.ibb.co/8Mpdm3y/testimonial1.png
# https://i.ibb.co/RjcqMsf/testimonial2.png
# https://i.ibb.co/SPNWm3b/testimonial3.png
# https://i.ibb.co/zS7J0rF/timg.gif
# https://i.ibb.co/hWYdkHM/ts-shap.png
# https://i.ibb.co/hggHwK2/under-banner-01.jpg
# https://i.ibb.co/tBrrjnh/under-banner-02.jpg
# https://i.ibb.co/z21MYPn/under-banner-03.jpg
# https://i.ibb.co/ZJgV79P/visa.png
# https://i.ibb.co/M8NVX5J/web.png
# https://i.ibb.co/HgtT7S0/women-category-item.png
# https://i.ibb.co/Df2Fff6/yang.jpg
# https://i.ibb.co/Dbmn0C6/yanglu.jpg
# https://i.ibb.co/w4QRtWr/image.png
# https://i.ibb.co/LQHXLky/image.png
# https://i.ibb.co/9WVfcZM/image.png

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try:
        tutorial = Tutorial.objects.get(pk=pk)
    except Tutorial.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorial_serializer = TutorialSerializer(tutorial)
        return JsonResponse(tutorial_serializer.data)

    elif request.method == 'PUT':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tutorial.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Tutorial.objects.filter(published=True)

    if request.method == 'GET':
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
