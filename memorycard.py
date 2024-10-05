from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import *

from random import randint, shuffle

app = QApplication([])

app.setStyle( 'Window' )
app.setStyleSheet('.QLabel {font-size: 14pt;}')

class Question():
    ''' содержит вопрос, правильный ответ и три неправильных'''

    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
q1=Question('коли хеллоувін?', '29-30 октебря', '29-30 липня', '29-30 грушня', '29-30 мая')
questions_list.append(q1)
questions_list.append(
    Question('на якому язиці програмування написан цей код?', 'pyhton', 'css+', 'css', 'html')
)
questions_list.append(
    Question('яка най ядовітиша риба у світі?', 'фугу', 'карась', 'акула', 'кит')
)

btn_OK = QPushButton('Відповісти')  # кнопка ответа
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox("Варианты ответов")  # группа вариантов

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

layout_ans1=QVBoxLayout()
layout_ans2=QHBoxLayout()
layout_ans3=QHBoxLayout()

RadioGroup = QButtonGroup()  # это для группировки переключателей
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox("Результат тесту")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('відповідь буде тут!')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 


layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()
# вопрос


QHBoxLayout() # варианты ответов или результат теста QHBoxLayout() # кнопка "Ответить"
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter)) 
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide() # скроем панель с ответом, сначала должна быть видна панель вопро
layout_line3.addStretch (1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большoй
layout_line3.addStretch(1)
layout_card=QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым


def show_result():
    '''показать панель ответов'''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Нступне питання')
def show_question():
    '''показать панель вопросов'''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Відповісти')
    RadioGroup.setExclusive(False) # сняли
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули


answers=[rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    'функция записывает значения вопроса и ответов в соотв при этом варианты ответов распределяются случайным образо'
    shuffle(answers) # перемешали список из кнопок, теперь на answers[0].setText(q.right_answer) # первый элемент списк answers[1].setText(q.wrong1)
    answers[0].setText(q.right_answer) # первый элемент списка заполним правильным ответом, остальные - неверными
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # вопрос 1b_Correct.setText(q.right_answer) # ответ show_question() # показываем панель вопросов
    lb_Correct.setText(q.right_answer) # ответ 
    show_question() # показываем панель вопросов

def show_correct(res):
    'показать результат'
    lb_Result.setText(res) 
    show_result()

def check_answer():
    '''если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        # правильный ответ!
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов:',window.total, 'n-Правильных ответов:', window.total, '\n-правельных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers [2].isChecked() or answers [3].isChecked(): # неправильный ответ!
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')

def next_question():
    ''' задает случайный вопрос из списка '''
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window)
    cur_question = randint(0, len(questions_list) - 1) # нам не нужно старое значение,
    # поэтому можно использовать локал
    # случайно взяли вопрос в пределах списка
    # если внести около сотни слов, то редко будет повторяться
    q = questions_list[cur_question] # взяли вопрос
    ask(q) # спросили

def click_OK():
    ''' определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
    if btn_OK.text() == 'Відповісти':
        check_answer() # проверка ответа
        if window.total==3:
            window.hide()
            finish = QMessageBox()
            finish.setText('Статистика\n-Всього питань: '+str(window.total)+ '\n-Вірних відповідей: '+str(window.score)+
            '\n Рейтинг: '+str(window.score/window.total*100)+ '%')
            finish.show()
            finish.setWindowTitle('Результат тесту')
            finish.exec()
    else:
        next_question() # следующий вопрос
window = QWidget()
window.setWindowTitle('Memo Card')
window.resize(400, 300)
window.setLayout(layout_card)
btn_OK.clicked.connect(click_OK) # по нажатию на кнопку выбираем, что конкретно происходит

window.score = 0
window.total = 0
next_question()
window.show()
app.exec()