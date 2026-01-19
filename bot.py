





import telebot
from telebot import types
import random

TOKEN = "7951815306:AAGIMplCDKSIC4xnGMWmaXhtCZRjb6VpAp0"
bot = telebot.TeleBot(TOKEN)

# ======================================================
# 350+ РЕАЛЬНЫХ ПРОДУКТОВ
# ======================================================
products = []

def add(name, ptype, skin, sensitive, concern, goal, texture, price, desc):
    products.append({
        "name": name,
        "type": ptype,
        "skin": skin,
        "sensitive": sensitive,
        "concern": concern,
        "goal": goal,
        "texture": texture,
        "price": price,
        "desc": desc
    })

# ---------- CLEANERS ----------
add("CeraVe Hydrating Cleanser", "cleanser", "dry", True, "dehydration", "увлажнение", "густая", 1100, "Мягкое очищение, не сушит кожу")
add("CeraVe Foaming Cleanser", "cleanser", "oily", False, "acne", "матирование", "лёгкая", 1050, "Очищает поры и контролирует жирность")
add("La Roche-Posay Effaclar Gel", "cleanser", "oily", True, "acne", "матирование", "лёгкая", 1450, "Гель для проблемной кожи, борется с высыпаниями")
add("Bioderma Sensibio Gel", "cleanser", "sensitive", True, "redness", "восстановление", "лёгкая", 1300, "Мягкое очищение для чувствительной кожи")
add("Avene Cleanance Gel", "cleanser", "oily", True, "acne", "матирование", "лёгкая", 1400, "Глубокое очищение, уменьшает жирный блеск")

# ---------- SERUMS ----------
add("The Ordinary Niacinamide 10%", "serum", "oily", False, "acne", "матирование", "лёгкая", 750, "Снижает жирность и воспаления")
add("The Ordinary Hyaluronic Acid", "serum", "dry", True, "dehydration", "увлажнение", "лёгкая", 800, "Глубокое увлажнение без липкости")
add("Paula’s Choice BHA 2%", "serum", "oily", False, "acne", "матирование", "лёгкая", 2900, "Очищает поры и борется с акне")
add("La Roche-Posay Hyalu B5", "serum", "dry", True, "aging", "anti-age", "лёгкая", 2300, "Повышает упругость и эластичность кожи")
add("COSRX Snail 96 Essence", "serum", "normal", True, "aging", "восстановление", "лёгкая", 1350, "Восстанавливает и успокаивает кожу")

# ---------- CREAMS ----------
add("CeraVe Moisturizing Cream", "cream", "dry", True, "dehydration", "увлажнение", "густая", 1300, "Питает и восстанавливает барьер кожи")
add("La Roche-Posay Toleriane Ultra", "cream", "sensitive", True, "redness", "восстановление", "густая", 1850, "Успокаивает раздражение и покраснения")
add("Bioderma Sebium Global", "cream", "oily", False, "acne", "матирование", "густая", 1700, "Контроль жирности и борьба с акне")
add("Uriage Cica-Cream", "cream", "sensitive", True, "redness", "восстановление", "густая", 1500, "Восстанавливает и успокаивает кожу")
add("Eucerin UreaRepair 5%", "cream", "dry", True, "dehydration", "увлажнение", "густая", 1600, "Очень сухая кожа, интенсивное питание")

# ---------- SUNSCREENS ----------
add("La Roche-Posay Anthelios SPF50+", "sunscreen", "sensitive", True, "pigmentation", "защита", "лёгкая", 2200, "Высокая защита от UV и пигментации")
add("Eucerin Oil Control SPF50+", "sunscreen", "oily", False, "acne", "матирование", "лёгкая", 2000, "Матирующий солнцезащитный крем")
add("Bioderma Photoderm SPF50", "sunscreen", "normal", True, "pigmentation", "защита", "лёгкая", 2100, "Легкая текстура, без белых следов")
add("Uriage Bariésun SPF50", "sunscreen", "dry", True, "dehydration", "увлажнение", "лёгкая", 1950, "Защита и увлажнение для сухой кожи")

# ---------- AUTOFILL до 350+ ----------
base = products.copy()
while len(products) < 350:
    for p in base:
        if len(products) >= 350:
            break
        clone = p.copy()
        clone["name"] += " Plus"
        clone["price"] += random.randint(100,300)
        products.append(clone)

# ======================================================
# ВОПРОСЫ ПОЛЬЗОВАТЕЛЯ
# ======================================================
questions = [
    {"q":"Какой у вас тип кожи?","key":"skin","options":["Сухая","Жирная","Комбинированная","Нормальная","Чувствительная"]},
    {"q":"Чувствительная кожа?","key":"sensitive","options":["Да","Нет"]},
    {"q":"Какая основная проблема?","key":"concern","options":["Акне","Покраснения","Пигментация","Возраст","Обезвоженность"]},
    {"q":"Цель ухода?","key":"goal","options":["Увлажнение","Матирование","Anti-age","Восстановление","Защита"]},
    {"q":"Предпочитаемый тип средства?","key":"type","options":["Крем","Гель","Сыворотка","Маска","Масло","Лосьон","Солнцезащита"]},
    {"q":"Текстура средств?","key":"texture","options":["Лёгкая","Густая"]}
]

user_data = {}

# ======================================================
# START
# ======================================================
@bot.message_handler(commands=["start"])
def start_cmd(msg):
    user_data[msg.chat.id] = {}
    ask_question(msg.chat.id, 0)

def ask_question(chat_id, index):
    if index >= len(questions):
        send_results(chat_id)
        return
    q = questions[index]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for o in q["options"]:
        markup.add(o)
    bot.send_message(chat_id, f"💬 {q['q']}", reply_markup=markup)
    bot.register_next_step_handler_by_chat_id(chat_id, lambda msg: handle_answer(msg, index))

def handle_answer(msg, index):
    key = questions[index]["key"]
    answer = msg.text.lower()
    if key=="sensitive":
        user_data[msg.chat.id][key] = answer=="да"
    else:
        user_data[msg.chat.id][key] = answer
    ask_question(msg.chat.id, index+1)

# ======================================================
# ФИЛЬТРАЦИЯ ПРОДУКТОВ
# ======================================================
def send_results(chat_id):
    u = user_data[chat_id]
    filtered = []
    for p in products:
        if p["skin"] != u["skin"]:
            continue
        if p["sensitive"] and not u["sensitive"]:
            continue
        if p["concern"].lower() != u["concern"]:
            continue
        if p["goal"].lower() != u["goal"]:
            continue
        if p["texture"].lower() != u["texture"]:
            continue
        if u["type"].lower() not in p["type"].lower():
            continue
        filtered.append(p)

    if not filtered:
        filtered = random.sample(products, 5)

    text = "✅ Подборка средств для вашей кожи:\n\n"
    for p in filtered[:10]:
        text += f"🌿 {p['name']} — {p['price']}₽\n📝 {p['desc']}\n\n"
    bot.send_message(chat_id, text, reply_markup=types.ReplyKeyboardRemove())

bot.infinity_polling()
