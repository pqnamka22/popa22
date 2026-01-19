import telebot
from telebot import types
import random

TOKEN = "7951815306:AAGORsCd0m14I9sbwEL2_q69AxU6g_Wm2Hk"

bot = telebot.TeleBot(TOKEN)
user_data = {}

# ------------------ БАЗА КОСМЕТИКИ (~150 продуктов) ------------------
# Структура: (Название, Бренд, Описание, Бюджет, Метки)
# Метки: acne, shine, tight, sensitive
COSMETICS = {
    "dry": [
# 70 dry продуктов
("CeraVe Moisturizing Cream", "CeraVe", "Питательный крем для сухой кожи 🌸", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("La Roche-Posay Lipikar Baume AP+", "La Roche-Posay", "Восстанавливает и успокаивает кожу 💧", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Avene Hydrance Riche", "Avene", "Глубокое увлажнение и комфорт ✨", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Bioderma Atoderm Cream", "Bioderma", "Защита кожного барьера 🌼", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Weleda Skin Food", "Weleda", "Плотный крем для очень сухой кожи 🌿", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Eucerin UreaRepair 5%", "Eucerin", "Смягчает и убирает стянутость", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Nivea Soft", "Nivea", "Лёгкий базовый крем", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Clinique Moisture Surge", "Clinique", "Интенсивное увлажнение 💦", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Embryolisse Lait-Creme", "Embryolisse", "Классика для сухой кожи", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Librederm Cerafavit", "Librederm", "Восстанавливает кожу после стресса", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("La Roche-Posay Hydraphase", "La Roche-Posay", "Интенсивное увлажнение без жирности", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("CeraVe Healing Ointment", "CeraVe", "Защита и восстановление кожи", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Avene XeraCalm", "Avene", "Успокаивает раздражённую кожу", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Bioderma Atoderm PP Baume", "Bioderma", "Глубокое восстановление сухой кожи", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Weleda Almond Soothing Cream", "Weleda", "Питает и смягчает кожу", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Avene Hydrance Optimale", "Avene", "Лёгкое увлажнение на день", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Clinique Moisture Cream Rich", "Clinique", "Интенсивное питание кожи", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Eucerin Aquaporin Active", "Eucerin", "Восстанавливает влагу кожи", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Nivea Nourishing Care", "Nivea", "Питательный уход за кожей", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Embryolisse Moisturizer", "Embryolisse", "Крем для сухой кожи и чувствительной кожи 🌸", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("CeraVe Daily Moisturizing Lotion", "CeraVe", "Лёгкий увлажняющий крем", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("La Roche-Posay Nutritic Intense", "La Roche-Posay", "Питание для очень сухой кожи", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Avene Tolerance Extreme", "Avene", "Минимум ингредиентов, максимум увлажнения", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Bioderma Atoderm Intensive Baume", "Bioderma", "Интенсивное питание кожи", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Weleda Calendula Cream", "Weleda", "Успокаивает кожу, питает", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Eucerin Rich Care", "Eucerin", "Глубокое восстановление кожи", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Nivea Creme", "Nivea", "Классический питательный крем", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Clinique Rich Moisture Cream", "Clinique", "Глубокое питание кожи 🌸", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Embryolisse Lait-Creme Concentre", "Embryolisse", "Универсальный крем для сухой кожи", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Avene Rich Cream", "Avene", "Увлажнение и комфорт", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Bioderma Atoderm Shower Cream", "Bioderma", "Мягкое очищение для сухой кожи", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("CeraVe Cream", "CeraVe", "Глубокое питание и восстановление", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("La Roche-Posay Lipikar Stick AP+", "La Roche-Posay", "Защита кожи для сухих участков", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Weleda Skin Food Light", "Weleda", "Лёгкое питание кожи", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Eucerin UreaRepair Plus", "Eucerin", "Интенсивное восстановление", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Nivea Soft Cream", "Nivea", "Лёгкий крем для ежедневного ухода", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Clinique Moisture Surge Intense", "Clinique", "Увлажнение и комфорт", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Embryolisse Rich Cream", "Embryolisse", "Питание и восстановление кожи 🌸", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Avene Hydrance Extra Rich", "Avene", "Глубокое увлажнение", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Bioderma Atoderm Creme Nutritive", "Bioderma", "Питание и мягкость кожи", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("CeraVe Moisturizing Cream Rich", "CeraVe", "Интенсивное питание кожи", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("La Roche-Posay Lipikar Baume Riche", "La Roche-Posay", "Защита и восстановление кожи", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Weleda Almond Cream", "Weleda", "Питание и смягчение кожи", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Eucerin Advanced Repair", "Eucerin", "Глубокое восстановление кожи", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Nivea Nourishing Cream", "Nivea", "Классическое питание сухой кожи", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Clinique Deep Moisture Cream", "Clinique", "Интенсивное увлажнение для сухой кожи", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Embryolisse Nutritive Cream", "Embryolisse", "Питание и комфорт кожи 🌸", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Avene Rich Hydration", "Avene", "Лёгкое питание и увлажнение", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Bioderma Atoderm Creme", "Bioderma", "Мягкое питание кожи", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("CeraVe Daily Cream", "CeraVe", "Увлажнение и восстановление кожи", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("La Roche-Posay Nutritic Cream", "La Roche-Posay", "Питательный уход за сухой кожей", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Weleda Skin Food Original", "Weleda", "Питание и защита кожи", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Eucerin Urea Cream", "Eucerin", "Глубокое восстановление сухой кожи", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Nivea Rich Care", "Nivea", "Питание и мягкость кожи", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Clinique Moisture Rich Cream", "Clinique", "Интенсивное увлажнение и комфорт", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Embryolisse Creme Nutritive", "Embryolisse", "Питание и восстановление кожи 🌸", "💎", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
("Avene Rich Cream Ultra", "Avene", "Увлажнение и питание кожи", "🪙", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Bioderma Atoderm Ultra Cream", "Bioderma", "Питание сухой кожи", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": True}),
],
    "oily": [
("La Roche-Posay Effaclar Duo+", "La Roche-Posay", "Против прыщей и жирного блеска ✨", "💎", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("CeraVe Foaming Cleanser", "CeraVe", "Очищение без пересушивания", "💰", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("COSRX Low pH Cleanser", "COSRX", "Мягкое умывание 🌿", "💰", {"acne": True, "shine": True, "tight": False, "sensitive": True}),
("The Ordinary Niacinamide 10%", "The Ordinary", "Контроль себума и расширенных пор", "💰", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("Bioderma Sebium Gel Moussant", "Bioderma", "Балансирует жирность кожи", "🪙", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("SVR Sebiaclear Gel Moussant", "SVR", "Очищение и матирование кожи", "🪙", {"acne": True, "shine": True, "tight": False, "sensitive": True}),
("Clinique Anti-Blemish Solutions", "Clinique", "Контроль акне и жирности", "💎", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("Avene Cleanance Expert", "Avene", "Сужает поры и уменьшает воспаления", "💎", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("Vichy Normaderm Phytosolution", "Vichy", "Матирующий уход и контроль прыщей", "💰", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("La Roche-Posay Effaclar Mat", "La Roche-Posay", "Матирует и сужает поры ✨", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("CeraVe PM Facial Moisturizing Lotion", "CeraVe", "Лёгкое увлажнение без блеска", "💰", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("COSRX Oil-Free Ultra Moisturizer", "COSRX", "Увлажняет без жирного блеска", "🪙", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("The Ordinary Niacinamide + Zinc", "The Ordinary", "Контроль себума и воспалений", "💎", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("Bioderma Sebium Global", "Bioderma", "Уход против акне и жирности", "💰", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("SVR Sebiaclear Serum", "SVR", "Матирующий и успокаивающий уход", "🪙", {"acne": True, "shine": True, "tight": False, "sensitive": True}),
("Clinique Acne Solutions Clearing Moisturizer", "Clinique", "Увлажнение без жирности", "💎", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("Avene Cleanance Comedomed", "Avene", "Уменьшает прыщи и черные точки", "💰", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("Vichy Normaderm Anti-Age", "Vichy", "Уход против акне и жирного блеска", "💎", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("La Roche-Posay Effaclar Purifying Foaming Gel", "La Roche-Posay", "Очищение и баланс жирной кожи", "💰", {"acne": True, "shine": True, "tight": False, "sensitive": True}),
("CeraVe Foaming Facial Cleanser", "CeraVe", "Мягкое очищение без пересушивания", "🪙", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("COSRX Centella Blemish Cream", "COSRX", "Успокаивает воспаления и акне", "💎", {"acne": True, "shine": False, "tight": False, "sensitive": True}),
("The Ordinary Salicylic Acid 2%", "The Ordinary", "Экспресс-уход против прыщей", "💰", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("Bioderma Sebium Pore Refiner", "Bioderma", "Сужает поры и контролирует блеск", "🪙", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("SVR Sebiaclear Active", "SVR", "Уход для проблемной кожи", "💎", {"acne": True, "shine": True, "tight": False, "sensitive": True}),
("Clinique Clarifying Lotion 2", "Clinique", "Тоник для жирной и проблемной кожи", "💰", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("Avene Cleanance Hydra", "Avene", "Увлажнение без жирного блеска", "🪙", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("Vichy Normaderm Phytosolution Serum", "Vichy", "Сужение пор и контроль блеска", "💎", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("La Roche-Posay Effaclar H", "La Roche-Posay", "Увлажнение для жирной кожи", "💰", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("CeraVe Ultra-Light Moisturizing Lotion", "CeraVe", "Лёгкое увлажнение без блеска", "🪙", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("COSRX AHA/BHA Clarifying Treatment Toner", "COSRX", "Смягчает и обновляет кожу", "💎", {"acne": True, "shine": True, "tight": False, "sensitive": True}),
("The Ordinary Glycolic Acid 7% Toning Solution", "The Ordinary", "Очищение и обновление кожи", "💰", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("Bioderma Sebium Mat Control", "Bioderma", "Матирование и контроль блеска", "🪙", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("SVR Sebiaclear Cream", "SVR", "Успокаивающий крем для проблемной кожи", "💎", {"acne": True, "shine": False, "tight": False, "sensitive": True}),
("Clinique Dramatically Different Oil-Free Gel", "Clinique", "Увлажнение для жирной кожи", "💰", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("Avene Cleanance Mask", "Avene", "Очищение и контроль блеска", "🪙", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("Vichy Normaderm Night Detox", "Vichy", "Восстановление и контроль жирности", "💎", {"acne": True, "shine": True, "tight": False, "sensitive": True}),
("La Roche-Posay Effaclar K+", "La Roche-Posay", "Сужение пор и контроль акне", "💰", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("CeraVe Resurfacing Retinol Serum", "CeraVe", "Контроль прыщей и обновление кожи", "🪙", {"acne": True, "shine": True, "tight": False, "sensitive": True}),
("COSRX Oil-Free Moisturizer", "COSRX", "Увлажнение без блеска", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("The Ordinary Retinol 0.2% in Squalane", "The Ordinary", "Против акне и обновление кожи", "💰", {"acne": True, "shine": True, "tight": False, "sensitive": True}),
("Bioderma Sebium Hydra", "Bioderma", "Увлажнение и контроль блеска", "🪙", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("SVR Sebiaclear Fluid", "SVR", "Лёгкий уход против акне", "💎", {"acne": True, "shine": True, "tight": False, "sensitive": True}),
("Clinique Acne Solutions BB Cream", "Clinique", "Маскирует и ухаживает за кожей", "💰", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("Avene Cleanance Comedomed Cream", "Avene", "Контроль черных точек и блеска", "🪙", {"acne": True, "shine": True, "tight": False, "sensitive": True}),
("Vichy Normaderm Hyaluspot", "Vichy", "Точечный уход против прыщей", "💎", {"acne": True, "shine": True, "tight": False, "sensitive": True}),
("La Roche-Posay Effaclar Duo+ Unifiant", "La Roche-Posay", "Коррекция цвета и контроль акне", "💰", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("CeraVe AM Facial Moisturizing Lotion", "CeraVe", "Дневное увлажнение с SPF", "🪙", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("COSRX BHA Blackhead Power Liquid", "COSRX", "Сужает поры и контролирует блеск", "💎", {"acne": True, "shine": True, "tight": False, "sensitive": True}),
("The Ordinary Azelaic Acid Suspension 10%", "The Ordinary", "Уменьшает акне и воспаления", "💰", {"acne": True, "shine": False, "tight": False, "sensitive": True}),
("Bioderma Sebium Global Cover", "Bioderma", "Матирование и маскировка", "🪙", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("SVR Sebiaclear Toner", "SVR", "Сужает поры и контролирует блеск", "💎", {"acne": True, "shine": True, "tight": False, "sensitive": True}),
("Clinique Acne Solutions Cleansing Foam", "Clinique", "Очищение для жирной и проблемной кожи", "💰", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("Avene Cleanance Spot", "Avene", "Точечный уход против прыщей", "🪙", {"acne": True, "shine": False, "tight": False, "sensitive": True}),
("Vichy Normaderm Detox", "Vichy", "Детокс и контроль жирности кожи", "💎", {"acne": True, "shine": True, "tight": False, "sensitive": True}),
("La Roche-Posay Effaclar Gel", "La Roche-Posay", "Очищение и контроль блеска", "💰", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("CeraVe Resurfacing Cream", "CeraVe", "Контроль прыщей и обновление кожи", "🪙", {"acne": True, "shine": True, "tight": False, "sensitive": True}),
("COSRX Oil-Free Toner", "COSRX", "Увлажнение без блеска", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("The Ordinary Salicylic Acid 2% Cleanser", "The Ordinary", "Очищение и контроль акне", "💰", {"acne": True, "shine": True, "tight": False, "sensitive": True}),
],
    "combo": [
("CeraVe Moisturizing Lotion", "CeraVe", "Баланс для комбинированной кожи 🌸", "💰", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("La Roche-Posay Toleriane", "La Roche-Posay", "Успокаивает чувствительную кожу", "💎", {"acne": False, "shine": False, "tight": False, "sensitive": True}),
("Clinique Dramatically Different", "Clinique", "Поддержка баланса кожи", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("Bioderma Sensibio Light", "Bioderma", "Для чувствительной зоны и нормальной кожи 🌸", "🪙", {"acne": False, "shine": False, "tight": False, "sensitive": True}),
("COSRX Snail Cream", "COSRX", "Восстановление и увлажнение кожи", "💰", {"acne": False, "shine": False, "tight": True, "sensitive": False}),
("Avene Hydrance Light", "Avene", "Лёгкий крем для смешанного типа кожи", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("Vichy Aqualia Thermal", "Vichy", "Увлажнение и баланс 🌿", "🪙", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("SVR Hydraliane Light", "SVR", "Комфорт и баланс кожи", "💰", {"acne": False, "shine": False, "tight": False, "sensitive": True}),
("Librederm Hyaluronic", "Librederm", "Гиалуроновый уход и лёгкое увлажнение", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("Nivea Aqua Effect", "Nivea", "Освежающий крем для комбинированной кожи", "🪙", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("La Roche-Posay Toleriane Sensitive", "La Roche-Posay", "Успокаивает и балансирует кожу", "💰", {"acne": False, "shine": False, "tight": False, "sensitive": True}),
("CeraVe PM Facial Moisturizer", "CeraVe", "Ночной баланс кожи 🌙", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("COSRX Oil-Free Moisturizer", "COSRX", "Увлажнение без блеска", "🪙", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("Clinique Moisture Surge 72H", "Clinique", "Длительное увлажнение и баланс", "💰", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("Avene Hydrance Optimale Light", "Avene", "Лёгкий увлажняющий крем для дня", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("Vichy Aqualia Thermal Light", "Vichy", "Освежение и баланс кожи 🌿", "🪙", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("SVR Hydraliane Gel-Cream", "SVR", "Лёгкий гель для нормальной и комбинированной кожи", "💰", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("Librederm Hyaluronic Gel", "Librederm", "Баланс увлажнения и матирования", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("Nivea Balance Gel-Cream", "Nivea", "Свежесть и комфорт для смешанной кожи", "🪙", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("La Roche-Posay Effaclar Mat", "La Roche-Posay", "Матирование и баланс кожи", "💰", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("CeraVe Facial Moisturizing Lotion", "CeraVe", "Лёгкое увлажнение для дня", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("COSRX Aloe Vera Cream", "COSRX", "Успокаивает и увлажняет кожу", "🪙", {"acne": False, "shine": False, "tight": False, "sensitive": True}),
("Clinique Moisture Surge Intense", "Clinique", "Баланс увлажнения и свежести", "💰", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("Avene Tolerance Extreme Light", "Avene", "Минимум ингредиентов, максимум баланса", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("Vichy Normaderm Phytosolution Light", "Vichy", "Сужение пор и матирование", "🪙", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("SVR Hydraliane Light Gel", "SVR", "Лёгкий гель для комбинированной кожи", "💰", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("Librederm Hyaluronic Light", "Librederm", "Увлажнение и комфорт 🌸", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("Nivea Aqua Effect Gel", "Nivea", "Свежесть и баланс кожи", "🪙", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("La Roche-Posay Toleriane Ultra", "La Roche-Posay", "Баланс и защита чувствительной зоны", "💰", {"acne": False, "shine": False, "tight": False, "sensitive": True}),
("CeraVe Facial Lotion PM", "CeraVe", "Ночной уход с балансом увлажнения", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("COSRX Centella Cream", "COSRX", "Успокаивает и восстанавливает баланс", "🪙", {"acne": False, "shine": False, "tight": False, "sensitive": True}),
("Clinique Dramatically Different Gel", "Clinique", "Баланс для смешанной кожи", "💰", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("Avene Hydrance Optimale Gel", "Avene", "Лёгкий гель для свежести кожи", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("Vichy Aqualia Thermal Gel", "Vichy", "Освежение и баланс 🌿", "🪙", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("SVR Hydraliane Gel Light", "SVR", "Лёгкий гель для нормальной и комбинированной кожи", "💰", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("Librederm Hyaluronic Gel Light", "Librederm", "Баланс и лёгкость увлажнения", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("Nivea Balance Cream Gel", "Nivea", "Свежесть и матирование кожи", "🪙", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("La Roche-Posay Effaclar Duo+", "La Roche-Posay", "Баланс и контроль акне", "💰", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("CeraVe PM Lotion Light", "CeraVe", "Лёгкое ночное увлажнение", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("COSRX Aloe Moisturizer", "COSRX", "Увлажнение и успокоение кожи", "🪙", {"acne": False, "shine": False, "tight": False, "sensitive": True}),
("Clinique Moisture Surge Light", "Clinique", "Баланс и увлажнение кожи", "💰", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("Avene Tolerance Extreme Gel", "Avene", "Лёгкий гель для чувствительной кожи", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("Vichy Normaderm Light Gel", "Vichy", "Матирование и баланс кожи", "🪙", {"acne": True, "shine": True, "tight": False, "sensitive": False}),
("SVR Hydraliane Gel Ultra", "SVR", "Увлажнение и баланс для кожи", "💰", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("Librederm Hyaluronic Cream Light", "Librederm", "Лёгкое увлажнение и свежесть", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("Nivea Aqua Effect Light", "Nivea", "Свежесть и лёгкость кожи", "🪙", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("La Roche-Posay Toleriane Dermo-Cleanser", "La Roche-Posay", "Очищение и баланс кожи", "💰", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("CeraVe Moisturizing Cream Light", "CeraVe", "Лёгкое питание и увлажнение", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("COSRX Aloe Soothing Gel", "COSRX", "Освежает и успокаивает кожу", "🪙", {"acne": False, "shine": False, "tight": False, "sensitive": True}),
("Clinique Dramatically Different Moisturizer Light", "Clinique", "Баланс и уход для смешанной кожи", "💰", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("Avene Hydrance Optimale Intense", "Avene", "Интенсивное лёгкое увлажнение", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("Vichy Aqualia Thermal Light Gel", "Vichy", "Свежесть и баланс кожи 🌿", "🪙", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("SVR Hydraliane Ultra Light", "SVR", "Лёгкое увлажнение и баланс", "💰", {"acne": False, "shine": True, "tight": False, "sensitive": True}),
("Librederm Hyaluronic Light Cream", "Librederm", "Увлажнение и комфорт кожи", "💎", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
("Nivea Balance Gel", "Nivea", "Матирование и баланс кожи", "🪙", {"acne": False, "shine": True, "tight": False, "sensitive": False}),
]



}

# ------------------ СТАРТ ------------------
@bot.message_handler(commands=["start"])
def start(message):
    user_data[message.chat.id] = {}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🌸 Сухая", "✨ Жирная", "🌼 Комбинированная")
    bot.send_message(
        message.chat.id,
        "Привет! 🌷\nДавай подберём косметику 💄\n\nВыбери тип кожи:",
        reply_markup=markup
    )

# ------------------ ВЫБОР ТИПА КОЖИ ------------------
@bot.message_handler(func=lambda m: m.text in ["🌸 Сухая", "✨ Жирная", "🌼 Комбинированная"])
def skin_type(message):
    skin_map = {"🌸 Сухая": "dry", "✨ Жирная": "oily", "🌼 Комбинированная": "combo"}
    user_data[message.chat.id]["skin"] = skin_map[message.text]
    ask_budget(message)

# ------------------ ВЫБОР БЮДЖЕТА ------------------
def ask_budget(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("💰 Бюджет", "🪙 Средний", "💎 Премиум")
    bot.send_message(message.chat.id, "Выбери бюджет 💖:", reply_markup=markup)
    bot.register_next_step_handler(message, budget_selected)

def budget_selected(message):
    text = message.text
    if "💰" in text:
        user_data[message.chat.id]["budget"] = "💰"
    elif "🪙" in text:
        user_data[message.chat.id]["budget"] = "🪙"
    elif "💎" in text:
        user_data[message.chat.id]["budget"] = "💎"
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выбери кнопку 💖")
        ask_budget(message)
        return
    ask_question_1(message)

# ------------------ ВОПРОСЫ ------------------
def yes_no_keyboard():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("✅ Да", "❌ Нет")
    return kb

def ask_question_1(message):
    bot.send_message(message.chat.id, "Есть ли у тебя прыщики? 🌱", reply_markup=yes_no_keyboard())
    bot.register_next_step_handler(message, q1)

def q1(message):
    user_data[message.chat.id]["acne"] = message.text=="✅ Да"
    bot.send_message(message.chat.id, "Кожа часто блестит? ✨", reply_markup=yes_no_keyboard())
    bot.register_next_step_handler(message, q2)

def q2(message):
    user_data[message.chat.id]["shine"] = message.text=="✅ Да"
    bot.send_message(message.chat.id, "Есть чувство стянутости? 🌸", reply_markup=yes_no_keyboard())
    bot.register_next_step_handler(message, q3)

def q3(message):
    user_data[message.chat.id]["tight"] = message.text=="✅ Да"
    bot.send_message(message.chat.id, "Кожа чувствительная? 🌼", reply_markup=yes_no_keyboard())
    bot.register_next_step_handler(message, q4)

def q4(message):
    user_data[message.chat.id]["sensitive"] = message.text=="✅ Да"
    result(message)

# ------------------ РЕЗУЛЬТАТ ------------------
def result(message):
    skin = user_data[message.chat.id]["skin"]
    budget = user_data[message.chat.id]["budget"]
    answers = user_data[message.chat.id]

    # фильтруем по бюджету и меткам
    products = [
        p for p in COSMETICS[skin]
        if p[3]==budget
        and p[4]["acne"]==answers["acne"]
        and p[4]["shine"]==answers["shine"]
        and p[4]["tight"]==answers["tight"]
        and p[4]["sensitive"]==answers["sensitive"]
    ]

    # если меньше 10, добираем случайные того же бюджета
    if len(products)<10:
        others = [p for p in COSMETICS[skin] if p[3]==budget and p not in products]
        random.shuffle(others)
        products += others[:10-len(products)]

    random.shuffle(products)
    text = "✨ *Тебе подойдёт эта косметика:* ✨\n\n"
    for name, brand, desc, _budget, _tags in products[:10]:
        text += f"🌸 *{name}*\n💎 Бренд: {brand}\nОписание: {desc}\n\n"

    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())

# ------------------ ЗАПУСК ------------------
bot.infinity_polling()

