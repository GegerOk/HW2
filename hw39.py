import multiprocessing

class WareHouseManager:  # Менеджер склада
    data = {}


    @staticmethod
    def process_request(request):  # Проверяет тип операции и наличие в словаре
        key, opp, value = request
        if opp == 'receipt':
            return WareHouseManager.receipt(key, value)
        elif opp == 'shipment':
            return WareHouseManager.shipment(key, value)

    @classmethod
    def receipt(self,key, value):  # Получение
        if key in self.data:
            self.data[key] += value
        else:
            self.data[key] = value
        return self.data  # Возврат данных после изменения

    @classmethod
    def shipment(self, key, value):

        if key in self.data and self.data[key] >= value:
            self.data[key] -= value
        return self.data  # Возврат данных после изменения

    def run(self, request):
        with multiprocessing.Pool(processes=2) as pool:
            results = pool.map(self.process_request, request)
        return results


if __name__ == '__main__':
    Home = WareHouseManager()
    result = Home.run([
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ])
    print(result)
    print(WareHouseManager.data)

