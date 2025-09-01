import Data.List (intercalate)

-- Структура данных для описания параметров инструмента
data FrezeInfo = FrezeInfo
    { manufacturerName :: String              -- Производитель
    , frezePrice :: Double                    -- Цена фрезы
    , toolLife :: Int                         -- Срок службы (детали)
    , cuttingSpeed :: Double                  -- Скорость резания
    , productionCostPerPiece :: Double        -- Себестоимость детали
    , productSellingPrice :: Double           -- Цена реализации детали
    , additionalCosts :: Double               -- Дополнительные расходы
    , equipmentAmortization :: Double         -- Амортизация оборудования
    , hourlyWage :: Double                    -- Зарплата работника за час
    , timePerPiece :: Double                  -- Время обработки детали
    , leasingPayment :: Double                -- Платеж по лизингу
    , leaseTermMonths :: Int                  -- Срок лизинга (мес.)
    } deriving Show

-- Функция для расчета рентабельности
calculateRoi :: FrezeInfo -> Double
calculateRoi FrezeInfo{..} =
    let totalRevenue = fromIntegral toolLife * productSellingPrice                 -- Доход
        laborCost = fromIntegral toolLife * timePerPiece * hourlyWage              -- Трудозатраты
        leasingTotal = leasingPayment * fromIntegral leaseTermMonths               -- Суммарные лизинговые платежи
        totalCosts = frezePrice + additionalCosts + laborCost + equipmentAmortization + leasingTotal + fromIntegral toolLife * productionCostPerPiece
        profit = totalRevenue - totalCosts
        roi = (profit / frezePrice) * 100
    in roi

-- Удобный способ печати информации о конкретном инструменте
showFrezeInfo :: FrezeInfo -> IO ()
showFrezeInfo fi@FrezeInfo{..} = do
    putStrLn $ intercalate ", "
        ["Производитель: " ++ manufacturerName
        ,"Фреза стоимостью: " ++ show frezePrice
        ,"Скорость резки: " ++ show cuttingSpeed
        ,"Срок службы: " ++ show toolLife
        ,"Цена изделия: " ++ show productSellingPrice
        ,"Производительность: " ++ show productionCostPerPiece
        ,"Доп. расходы: " ++ show additionalCosts
        ,"Амортизация: " ++ show equipmentAmortization
        ,"Зарплата: " ++ show hourlyWage
        ,"Время на деталь: " ++ show timePerPiece
        ,"Лизинговый платёж: " ++ show leasingPayment
        ,"Срок лизинга: " ++ show leaseTermMonths
        ,"Рентабельность (ROI): " ++ show (calculateRoi fi) ++ "%"]

-- Тестируемые данные
testData :: [FrezeInfo]
testData = [
    FrezeInfo{
        manufacturerName="Производитель А",
        frezePrice=5000,
        toolLife=10000,
        cuttingSpeed=200,
        productionCostPerPiece=10,
        productSellingPrice=50,
        additionalCosts=1000,
        equipmentAmortization=500,
        hourlyWage=200,
        timePerPiece=0.1,
        leasingPayment=1000,
        leaseTermMonths=12
    },
    FrezeInfo{
        manufacturerName="Производитель Б",
        frezePrice=7000,
        toolLife=15000,
        cuttingSpeed=250,
        productionCostPerPiece=12,
        productSellingPrice=55,
        additionalCosts=1500,
        equipmentAmortization=700,
        hourlyWage=220,
        timePerPiece=0.08,
        leasingPayment=1200,
        leaseTermMonths=18
    }]

-- Запуск тестов
main :: IO ()
main = mapM_ showFrezeInfo testData
