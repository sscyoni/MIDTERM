class Inventory :
    stock  = 0
    def __init__ (self) :
        Inventory.stock +=1
    
        print("새상품이 등록되었습니다")

    
    def add_stock(amount) :
        if amount > 0:
            print(amount,"개가 입고되었습니다")
    def remove_stock(amount) :
        if amount > Inventory.stock :
            print(amount,"개가 출고되었습니다")
        else :
            print("출고불가")

    def get_stock () :
        return Inventory.stock
    
    def set_stock(amount) :
        if amount> 0 :
            a=Inventory.stock + amount
            return (a)
        else :
            return Inventory.stock


item1 = Inventory()
item1.add_stock(10)
item1.remove_stock(3)
print("현재재고수량:",item1.get_stock())

item1.set_stock(20)
print("수정된 재고 수량:",item1.get_stock())
