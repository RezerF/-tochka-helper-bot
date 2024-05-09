from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from secret import YOUR_BOT_TOKEN


# Обработчик команды /start
def start(update, context):
    # Создание клавиатуры с кнопкой "Создать шаблон"
    keyboard = [
        [InlineKeyboardButton("Создать шаблон заказа", callback_data='create_template')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправка сообщения с клавиатурой
    update.message.reply_text('Этот телеграм бот помошник Эковатника":', reply_markup=reply_markup)

# Обработчик нажатия кнопки "Создать шаблон"
def create_template(update, context):
    # Ответ на нажатие кнопки
    query = update.callback_query
    query.answer()

    # Шаблон сообщения
    template = "### Заказ\nАдрес: _________\nТелефон: __________\nДата: __________\nВремя: __________\nЧто сделать(площадь, толщина, насыпь/прокол, для каждого эл-та): __________\nДемонтаж?: __________\nСмета приложена?: __________"

    # Отправка сообщения с шаблоном
    query.message.reply_text(template)

def main():
    # Токен вашего бота
    token = YOUR_BOT_TOKEN

    # Создание объекта для взаимодействия с Telegram API
    updater = Updater(token, use_context=True)

    # Получение диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрация обработчиков команд
    dispatcher.add_handler(CommandHandler("start", start))

    # Регистрация обработчика для нажатия кнопок
    dispatcher.add_handler(CallbackQueryHandler(create_template))

    # Запуск бота
    updater.start_polling()

    # Остановка бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()