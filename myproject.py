
class product:
    product_company = "RioTinto"
    def __init__(self,prdid,prdname,prdqty):
        self.prdid = prdid
        self.prdname = prdname
        self.prdqty = prdqty
        self.price = 50


    def show(self):
        print("Product_Id::",self.prdid)
        print("Product_Name::",self.prdname)
        print("Product_Qty::",self.prdqty)
        print("Product_Price::",self.price)
        print("Product_price_change::",self.price_change())
        tqpc = self.total_qty_price_cal(self.prdqty,self.price)
        print("TQPC::",tqpc)
        print("company name before change::",product.product_company)
        self.product_name_cal()
        print("company name after change::", product.product_company)

    @classmethod
    def product_name_cal(cls):
        cls.product_company = "Infosys"


    def price_change(self):
        self.price = 100
        return self.price

    @staticmethod
    def total_qty_price_cal(price,qty):
        qty_price =price * qty
        return qty_price

    def t1(self):
        self.show()

obj = product(201,'copper',222)
obj.t1()


