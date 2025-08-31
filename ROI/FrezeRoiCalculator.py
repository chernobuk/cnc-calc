class FrezeRoiCalculator:
    def __init__(self, manufacturer_name, freze_price, tool_life, cutting_speed, production_cost_per_piece, product_selling_price, additional_costs=0, equipment_amortization=0, hourly_wage=0, time_per_piece=0, leasing_payment=0, lease_term=0):
        """
        Конструктор класса калькулятора рентабельности фрез.
        
        :param manufacturer_name: Имя производителя
        :param freze_price: Цена фрезы
        :param tool_life: Стойкость инструмента (общее число обрабатываемых деталей)
        :param cutting_speed: Скорость резания (для оценки эффективности)
        :param production_cost_per_piece: Себестоимость изготовления одной детали
        :param product_selling_price: Продажная цена одной детали
        :param additional_costs: Дополнительные фиксированные расходы (электроэнергия, аренда и др.)
        :param equipment_amortization: Амортизация оборудования за период эксплуатации инструмента
        :param hourly_wage: Среднечасовая оплата труда оператора
        :param time_per_piece: Время обработки одной детали в часах
        :param leasing_payment: Платёж по лизингу оборудования (если применимо)
        :param lease_term: Срок лизинга оборудования в месяцах
        """
        self.manufacturer_name = manufacturer_name
        self.freze_price = freze_price
        self.tool_life = tool_life
        self.cutting_speed = cutting_speed
        self.production_cost_per_piece = production_cost_per_piece
        self.product_selling_price = product_selling_price
        self.additional_costs = additional_costs
        self.equipment_amortization = equipment_amortization
        self.hourly_wage = hourly_wage
        self.time_per_piece = time_per_piece
        self.leasing_payment = leasing_payment
        self.lease_term = lease_term

    def calculate_roi(self):
        """Метод для расчета рентабельности"""
        total_revenue = self.tool_life * self.product_selling_price  # общий доход
        labor_costs = self.tool_life * self.time_per_piece * self.hourly_wage  # затраты на рабочую силу
        leasing_total = self.leasing_payment * self.lease_term  # суммарные выплаты по лизингу
        total_costs = (
            self.freze_price +
            self.additional_costs +
            labor_costs +
            self.equipment_amortization +
            leasing_total +
            (self.tool_life * self.production_cost_per_piece)
        )
        profit = total_revenue - total_costs  # чистая прибыль
        roi = (profit / self.freze_price) * 100 if self.freze_price > 0 else float("inf")
        return round(roi, 2)

    def __repr__(self):
        """Представление объекта в удобочитаемом виде."""
        return f"{self.manufacturer_name}: Фреза стоимостью {self.freze_price}, ROI={self.calculate_roi()}%, Speed={self.cutting_speed}"

# Пример использования:
if __name__ == "__main__":
    manufacturers_data = [
        {
            'manufacturer': 'Производитель А',
            'freze_price': 5000,
            'tool_life': 5,
            'cutting_speed': 200,
            'production_cost_per_piece': 10,
            'product_selling_price': 50,
            'additional_costs': 1000,
            'equipment_amortization': 500,
            'hourly_wage': 200,
            'time_per_piece': 0.1,
            'leasing_payment': 1000,  # месячный платёж по лизингу
            'lease_term': 12          # срок лизинга в месяцах
        },
        {
            'manufacturer': 'Производитель Б',
            'freze_price': 7000,
            'tool_life': 15,
            'cutting_speed': 250,
            'production_cost_per_piece': 12,
            'product_selling_price': 55,
            'additional_costs': 1500,
            'equipment_amortization': 700,
            'hourly_wage': 220,
            'time_per_piece': 0.08,
            'leasing_payment': 1200,  # месячный платёж по лизингу
            'lease_term': 18          # срок лизинга в месяцах
        }
    ]

    for data in manufacturers_data:
        calculator = FrezeRoiCalculator(**data)
        print(calculator)
