from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.animation import Animation
from kivy.graphics import Color, RoundedRectangle, Rectangle

# 9-B sinfining 109-maktab uchun to'liq dars jadvali
DARS_JADVALI = {
    "Dushanba": [
        ("1-soat", "08:15 - 09:00", "Fizika (Karimov N.Q.)", "Fizika (Karimov N.Q.)"),
        ("2-soat", "09:05 - 09:50", "Ona tili (Namozova M.K.)", "Ona tili (Namozova M.K.)"),
        ("3-soat", "09:55 - 10:40", "Informatika (SALAYEVA Z.M.)", "Informatika (Ahmadjonov A.A.)"),
        ("4-soat", "11:00 - 11:45", "Tarbiya (Pulatov A.T.)", "Tarbiya (Pulatov A.T.)"),
        ("5-soat", "11:50 - 12:35", "Biologiya (Botirova N.A.)", "Biologiya (Botirova N.A.)"),
        ("6-soat", "12:40 - 13:25", "Ingliz tili (Tuychiyev I.)", "Ingliz tili (QOBULOV A.I.)"),
    ],
    "Seshanba": [
        ("1-soat", "08:15 - 09:00", "Algebra (Mallayev O.)", "Algebra (Mallayev O.)"),
        ("2-soat", "09:05 - 09:50", "Geometriya (Mallayev O.)", "Geometriya (Mallayev O.)"),
        ("3-soat", "09:55 - 10:40", "Kimyo (Musayeva N.Q.)", "Kimyo (Musayeva N.Q.)"),
        ("4-soat", "11:00 - 11:45", "Adabiyot (Namozova M.K.)", "Adabiyot (Namozova M.K.)"),
        ("5-soat", "11:50 - 12:35", "Informatika (SALAYEVA Z.M.)", "Informatika (Ahmadjonov A.A.)"),
        ("6-soat", "12:40 - 13:25", "Ingliz tili (Tuychiyev I.)", "Ingliz tili (QOBULOV A.I.)"),
    ],
    "Chorshanba": [
        ("1-soat", "08:15 - 09:00", "Fizika (Karimov N.Q.)", "Fizika (Karimov N.Q.)"),
        ("2-soat", "09:05 - 09:50", "O'zb. tarixi (Nabiyeva G.N.)", "O'zb. tarixi (Nabiyeva G.N.)"),
        ("3-soat", "09:55 - 10:40", "Ona tili (Namozova M.K.)", "Ona tili (Namozova M.K.)"),
        ("4-soat", "11:00 - 11:45", "Iqtisod (Ermazarov I.)", "Iqtisod (Ermazarov I.)"),
        ("5-soat", "11:50 - 12:35", "Ingliz tili (Tuychiyev I.)", "Ingliz tili (QOBULOV A.I.)"),
    ],
    "Payshanba": [
        ("1-soat", "08:15 - 09:00", "Jismoniy t. (Mallayev I.A.)", "Jismoniy t. (Jurrayev R.B.)"),
        ("2-soat", "09:05 - 09:50", "Huquq (Nabiyev Z.N.)", "Huquq (Nabiyev Z.N.)"),
        ("3-soat", "09:55 - 10:40", "Algebra (Mallayev O.)", "Algebra (Mallayev O.)"),
        ("4-soat", "11:00 - 11:45", "Algebra (Mallayev O.)", "Algebra (Mallayev O.)"),
        ("5-soat", "11:50 - 12:35", "Rus tili (Qobilov A.U.)", "Rus tili (Naruva M.I.)"),
        ("6-soat", "12:40 - 13:25", "Biologiya (Botirova N.A.)", "Biologiya (Botirova N.A.)"),
    ],
    "Juma": [
        ("1-soat", "08:15 - 09:00", "Rus tili (Naruva M.I.)", "Rus tili (Qobilov A.U.)"),
        ("2-soat", "09:05 - 09:50", "Texnologiya (Mirzayeva N.X.)", "Texnologiya (Chorsiyev U.M.)"),
        ("3-soat", "09:55 - 10:40", "Ingliz tili (Tuychiyev I.)", "Ingliz tili (QOBULOV A.I.)"),
        ("4-soat", "11:00 - 11:45", "Kimyo (Musayeva N.Q.)", "Kimyo (Musayeva N.Q.)"),
        ("5-soat", "11:50 - 12:35", "Adabiyot (Namozova M.K.)", "Adabiyot (Namozova M.K.)"),
        ("6-soat", "12:40 - 13:25", "Jahon Tarix (Nabiyeva G.N.)", "Jahon Tarix (Nabiyeva G.N.)"),
    ],
    "Shanba": [
        ("1-soat", "08:15 - 09:00", "Biologiya (Botirova N.A.)", "Biologiya (Botirova N.A.)"),
        ("2-soat", "09:05 - 09:50", "Fizika (Karimov N.Q.)", "Fizika (Karimov N.Q.)"),
        ("3-soat", "09:55 - 10:40", "Ona tili (Namozova M.K.)", "Ona tili (Namozova M.K.)"),
        ("4-soat", "11:00 - 11:45", "Kimyo (Musayeva N.Q.)", "Kimyo (Musayeva N.Q.)"),
        ("5-soat", "11:50 - 12:35", "O'zb. tarixi (Nabiyeva G.N.)", "O'zb. tarixi (Nabiyeva G.N.)"),
        ("6-soat", "12:40 - 13:25", "Geometriya (Mallayev O.)", "Geometriya (Mallayev O.)"),
    ]
}

class LessonCard(BoxLayout):
    """Har bir dars uchun shaffof, qavariq burchakli zamonaviy karta"""
    def __init__(self, soat, vaqt, fan1, fan2, **kwargs):
        super(LessonCard, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = 110
        self.padding = 12
        self.spacing = 5
        self.opacity = 0

        with self.canvas.before:
            Color(0.12, 0.16, 0.26, 0.9)  # Premium to'q shaffof fon
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[18])
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Soat va Vaqt qatori
        top_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=25)
        s_lbl = Label(text=f"📌 {soat}", bold=True, color=(1, 0.8, 0.2, 1), font_size=15, halign='left')
        s_lbl.bind(size=s_lbl.setter('text_size'))
        v_lbl = Label(text=f"⏰ {vaqt}", color=(0.7, 0.75, 0.85, 1), font_size=13, halign='right')
        v_lbl.bind(size=v_lbl.setter('text_size'))
        top_box.add_widget(s_lbl)
        top_box.add_widget(v_lbl)
        self.add_widget(top_box)

        # Fanlar va o'qituvchilar
        if fan1 == fan2:
            f_lbl = Label(text=f"📖 {fan1}", font_size=14, color=(1, 1, 1, 1), halign='left')
            f_lbl.bind(size=f_lbl.setter('text_size'))
            self.add_widget(f_lbl)
        else:
            g1_lbl = Label(text=f"👥 1-guruh: {fan1}", font_size=13, color=(0.3, 0.85, 1, 1), halign='left')
            g1_lbl.bind(size=g1_lbl.setter('text_size'))
            g2_lbl = Label(text=f"👥 2-guruh: {fan2}", font_size=13, color=(1, 0.4, 0.7, 1), halign='left')
            g2_lbl.bind(size=g2_lbl.setter('text_size'))
            self.add_widget(g1_lbl)
            self.add_widget(g2_lbl)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def animate_in(self):
        anim = Animation(opacity=1, duration=0.35)
        anim.start(self)


class WelcomeScreen(Screen):
    """1-EKRAN: Maktab va Sinf haqida vizual karta hamda Boshlash tugmasi"""
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        with self.canvas.before:
            Color(0.06, 0.08, 0.14, 1) # Asosiy fon
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        # Yuqori ma'lumot boks
        center_box = BoxLayout(orientation='vertical', spacing=12, padding=15)
        
        with center_box.canvas.before:
            Color(0.12, 0.15, 0.24, 0.8)
            self.info_rect = RoundedRectangle(size=center_box.size, pos=center_box.pos, radius=[22])
        center_box.bind(size=self._update_info_rect, pos=self._update_info_rect)

        m_label = Label(text="🏫 109-MAKTAB", font_size=26, bold=True, color=(0.2, 0.75, 1, 1))
        s_label = Label(text="📚 9-'B' SINFI", font_size=22, bold=True, color=(1, 1, 1, 1))
        o_label = Label(text="👩‍🏫 Sinf rahbari:\nNamozova M.K.", font_size=17, halign='center', color=(0.8, 0.85, 0.95, 1))

        center_box.add_widget(m_label)
        center_box.add_widget(s_label)
        center_box.add_widget(o_label)

        main_layout.add_widget(center_box)

        # Pastki BOSHLASH tugmasi
        btn_start = Button(
            text="🚀 BOSHLASH",
            font_size=20,
            bold=True,
            size_hint=(1, None),
            height=65,
            background_normal='',
            background_color=(0.1, 0.6, 0.95, 1)
        )
        btn_start.bind(on_press=self.go_to_schedule)
        main_layout.add_widget(btn_start)

        self.add_widget(main_layout)

    def _update_bg(self, instance, value):
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos

    def _update_info_rect(self, instance, value):
        self.info_rect.size = instance.size
        self.info_rect.pos = instance.pos

    def go_to_schedule(self, instance):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'schedule'


class ScheduleScreen(Screen):
    """2-EKRAN: Dushanbadan Shanbagacha tugmalar va Jadval ekrani"""
    def __init__(self, **kwargs):
        super(ScheduleScreen, self).__init__(**kwargs)
        
        root = BoxLayout(orientation='vertical', padding=12, spacing=10)

        with self.canvas.before:
            Color(0.06, 0.08, 0.14, 1)
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        # Yuqori sarlavha va Kunlar tugmalari gridi
        self.header_label = Label(
            text="📅 KUNNI TANLANG",
            font_size=18,
            bold=True,
            size_hint_y=None,
            height=35,
            color=(0.3, 0.8, 1, 1)
        )
        root.add_widget(self.header_label)

        # Dushanbadan Shanbagacha tugmalar (Horizontal scroll yoki Boks)
        days_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=45, spacing=6)
        
        self.day_buttons = {}
        kunlar = ['Dush', 'Sesh', 'Chor', 'Pay', 'Jum', 'Shan']
        to_full_day = {
            'Dush': 'Dushanba', 'Sesh': 'Seshanba', 'Chor': 'Chorshanba',
            'Pay': 'Payshanba', 'Jum': 'Juma', 'Shan': 'Shanba'
        }

        for short_day in kunlar:
            full_day = to_full_day[short_day]
            btn = Button(
                text=short_day,
                font_size=13,
                bold=True,
                background_normal='',
                background_color=(0.15, 0.2, 0.3, 1),
                color=(0.9, 0.9, 0.9, 1)
            )
            btn.bind(on_press=lambda b, fd=full_day: self.select_day(fd))
            days_box.add_widget(btn)
            self.day_buttons[full_day] = btn

        root.add_widget(days_box)

        # Darslar ro'yxati (Scrollview - butun ekranni pastgacha egallaydi)
        self.scroll = ScrollView(size_hint=(1, 1), effect_cls='ScrollEffect')
        self.schedule_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10, padding=[0, 5, 0, 10])
        self.schedule_layout.bind(minimum_height=self.schedule_layout.setter('height'))
        
        self.scroll.add_widget(self.schedule_layout)
        root.add_widget(self.scroll)

        # Pastki ORTGA tugmasi
        btn_back = Button(
            text="⬅ ORTGA",
            font_size=16,
            bold=True,
            size_hint=(1, None),
            height=50,
            background_normal='',
            background_color=(0.8, 0.2, 0.3, 1)
        )
        btn_back.bind(on_press=self.go_back)
        root.add_widget(btn_back)

        self.add_widget(root)
        self.current_selected_day = 'Dushanba'

    def _update_bg(self, instance, value):
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos

    def on_enter(self):
        # Ekran ochilganda Dushanba jadvalini avtomatik yuklash
        self.select_day('Dushanba')

    def select_day(self, day):
        self.current_selected_day = day
        self.header_label.text = f"📅 {day.upper()} JADVALI"
        
        # Tugmalar rangini faollashtirish
        for d_name, btn in self.day_buttons.items():
            if d_name == day:
                btn.background_color = (0.1, 0.6, 0.95, 1)
            else:
                btn.background_color = (0.15, 0.2, 0.3, 1)

        # Jadvalni yangilash
        self.schedule_layout.clear_widgets()
        darslar = DARS_JADVALI.get(day, [])
        
        for soat, vaqt, fan1, fan2 in darslar:
            card = LessonCard(soat, vaqt, fan1, fan2)
            self.schedule_layout.add_widget(card)
            card.animate_in()

    def go_back(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'welcome'


class UltimateScheduleApp(App):
    def build(self):
        self.title = "109-maktab 9-B Jadval"
        
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(ScheduleScreen(name='schedule'))
        
        return sm

if __name__ == '__main__':
    UltimateScheduleApp().run()
