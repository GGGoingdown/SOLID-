class ParentClass:
    def method_a(self, par1, par2):
        print(f"Par1 - {par1}::Par2 - {par2}")

    def method_b(self, par1):
        print(f"Par1 - {par1}")


class BadSubClass(ParentClass):
    # Breaking rules
    """
    mathod_a 再父類別有兩個parameters (par1 and par2)
    但是子類別在override父類別的方法時
    參數的數量不同了
    """

    def method_a(self, par1):
        print(f"Par1 - {par1}")


class GoodSubClass(ParentClass):
    def method_a(self, par1, par2):
        print(f"[Subclass]Par1 - {par1}:: Par2 - {par2}")


if __name__ == "__main__":
    # bs1 = BadSubClass()
    # bs1.method_a("p1")
    gs1 = GoodSubClass()  # 更改為ParentClass依然可以運作
    gs1.method_a("hello", "world")
