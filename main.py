from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import BooleanProperty, ListProperty, NumericProperty, StringProperty
from datetime import datetime
import calendar
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import MDTabsBase


TAB_ITEMS = [
    ("input", "tab_input"),
    ("calc", "tab_calc"),
    ("graph", "tab_graph"),
    ("diagram", "tab_diagram"),
    ("total", "tab_total"),
]

I18N = {
    "ru": {
        "app_title": "Калькулятор ипотеки",
        "tab_input": "Ввод",
        "tab_calc": "Расчёт",
        "tab_graph": "График",
        "tab_diagram": "Диаграмма",
        "tab_total": "Итого",
        "form_title": "Параметры ипотеки",
        "loan_hint": "Сумма кредита",
        "loan_help": "Например: 3000000",
        "rate_hint": "Годовая ставка (%)",
        "rate_help": "Например: 12.5",
        "years_hint": "Срок кредита (лет)",
        "years_help": "Например: 20",
        "payment_type_hint": "Тип платежа",
        "start_date": "Дата начала",
        "payment_type": "Тип платежа",
        "payment_annuity": "Аннуитетный",
        "payment_diff": "Дифференцированный",
        "calculate": "Рассчитать",
        "status_default": "Введите параметры и нажмите 'Рассчитать'",
        "status_done": "Расчёт выполнен: график, диаграмма и таблица обновлены.",
        "status_fill": "Заполните все поля: сумма, ставка и срок.",
        "status_invalid": "Проверьте значения: сумма/срок > 0, ставка >= 0.",
        "graph_title": "График динамики платежей",
        "legend_balance": "Синий - Остаток долга",
        "legend_interest": "Красный - Накопленная переплата",
        "legend_principal_paid": "Жёлтый - Погашенное тело",
        "diagram_title": "Диаграмма платежей",
        "principal": "Кредит",
        "interest": "Проценты",
        "total_table_title": "Таблица платежей (строки и столбцы)",
        "metric": "Показатель",
        "value": "Значение",
        "loan_amount": "Сумма кредита",
        "rate": "Ставка",
        "term": "Срок",
        "monthly": "Ежемесячный платёж",
        "total_payment": "Всего выплат",
        "overpayment": "Переплата",
        "total_interest": "Переплата по процентам",
        "effective_rate": "Эффективный %",
        "month": "Мес",
        "no": "№",
        "date": "Дата",
        "payment_col": "Платёж",
        "credit_part": "Кредит",
        "interest_part": "Проценты",
        "balance": "Остаток",
    },
    "kk": {
        "app_title": "Ипотека калькуляторы",
        "tab_input": "Енгізу",
        "tab_calc": "Есеп",
        "tab_graph": "График",
        "tab_diagram": "Диаграмма",
        "tab_total": "Жиыны",
        "form_title": "Ипотека параметрлері",
        "loan_hint": "Несие сомасы",
        "loan_help": "Мысалы: 3000000",
        "rate_hint": "Жылдық мөлшерлеме (%)",
        "rate_help": "Мысалы: 12.5",
        "years_hint": "Несие мерзімі (жыл)",
        "years_help": "Мысалы: 20",
        "payment_type_hint": "Төлем түрі",
        "start_date": "Басталу күні",
        "payment_type": "Төлем түрі",
        "payment_annuity": "Аннуитеттік",
        "payment_diff": "Дифференциалды",
        "calculate": "Есептеу",
        "status_default": "Параметрлерді енгізіп, 'Есептеу' басыңыз",
        "status_done": "Есеп дайын: график, диаграмма және кесте жаңартылды.",
        "status_fill": "Барлық өрістерді толтырыңыз: сома, мөлшерлеме, мерзім.",
        "status_invalid": "Мәндерді тексеріңіз: сома/мерзім > 0, мөлшерлеме >= 0.",
        "graph_title": "Төлем динамикасының графигі",
        "legend_balance": "Көк - Қарыз қалдығы",
        "legend_interest": "Қызыл - Жиналған артық төлем",
        "legend_principal_paid": "Сары - Өтелген негізгі қарыз",
        "diagram_title": "Төлем диаграммасы",
        "principal": "Негізгі қарыз",
        "interest": "Пайыздар",
        "total_table_title": "Төлем кестесі (жолдар мен бағандар)",
        "metric": "Көрсеткіш",
        "value": "Мәні",
        "loan_amount": "Несие сомасы",
        "rate": "Мөлшерлеме",
        "term": "Мерзім",
        "monthly": "Ай сайынғы төлем",
        "total_payment": "Жалпы төлем",
        "overpayment": "Артық төлем",
        "total_interest": "Пайыз бойынша артық төлем",
        "effective_rate": "Тиімді %",
        "month": "Ай",
        "no": "№",
        "date": "Күні",
        "payment_col": "Төлем",
        "credit_part": "Негізгі қарыз",
        "interest_part": "Пайыздар",
        "balance": "Қалдық",
    },
    "en": {
        "app_title": "Mortgage Calculator",
        "tab_input": "Input",
        "tab_calc": "Table",
        "tab_graph": "Graph",
        "tab_diagram": "Chart",
        "tab_total": "Sum",
        "form_title": "Mortgage Parameters",
        "loan_hint": "Loan amount",
        "loan_help": "Example: 3000000",
        "rate_hint": "Annual rate (%)",
        "rate_help": "Example: 12.5",
        "years_hint": "Loan term (years)",
        "years_help": "Example: 20",
        "payment_type_hint": "Payment type",
        "start_date": "Start date",
        "payment_type": "Payment type",
        "payment_annuity": "Annuity",
        "payment_diff": "Differentiated",
        "calculate": "Calculate",
        "status_default": "Enter parameters and press 'Calculate'",
        "status_done": "Calculation complete: graph, diagram and table updated.",
        "status_fill": "Fill all fields: amount, rate and term.",
        "status_invalid": "Check values: amount/term > 0, rate >= 0.",
        "graph_title": "Payment dynamics graph",
        "legend_balance": "Blue - Remaining debt",
        "legend_interest": "Red - Cumulative overpayment",
        "legend_principal_paid": "Yellow - Principal repaid",
        "diagram_title": "Payment Diagram",
        "principal": "Principal",
        "interest": "Interest",
        "total_table_title": "Payment table (rows and columns)",
        "metric": "Metric",
        "value": "Value",
        "loan_amount": "Loan amount",
        "rate": "Rate",
        "term": "Term",
        "monthly": "Monthly payment",
        "total_payment": "Total payment",
        "overpayment": "Overpayment",
        "total_interest": "Total interest",
        "effective_rate": "Effective %",
        "month": "Month",
        "no": "#",
        "date": "Date",
        "payment_col": "Payment",
        "credit_part": "Principal",
        "interest_part": "Interest",
        "balance": "Balance",
    },
}


class NavigationTab(MDBoxLayout, MDTabsBase):
    screen_name = StringProperty("")


class TableRow(MDBoxLayout):
    no = StringProperty("")
    date = StringProperty("")
    payment = StringProperty("")
    interest = StringProperty("")
    principal = StringProperty("")
    balance = StringProperty("")
    bg_color = ListProperty([0.95, 0.95, 0.95, 1])
    text_color = ListProperty([0.08, 0.08, 0.08, 1])
    no_width = NumericProperty(dp(54))
    date_width = NumericProperty(dp(130))
    amount_width = NumericProperty(dp(170))


class LineGraphWidget(Widget):
    balance_points = ListProperty([])
    overpayment_points = ListProperty([])
    principal_paid_points = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            pos=self._redraw,
            size=self._redraw,
            balance_points=self._redraw,
            overpayment_points=self._redraw,
            principal_paid_points=self._redraw,
        )

    def set_data(self, balance_points, overpayment_points, principal_paid_points):
        self.balance_points = balance_points
        self.overpayment_points = overpayment_points
        self.principal_paid_points = principal_paid_points

    @staticmethod
    def _smooth_path(points, samples_per_segment=14):
        if len(points) < 3:
            flat = []
            for x_val, y_val in points:
                flat.extend([x_val, y_val])
            return flat

        ext = [points[0]] + points + [points[-1]]
        smooth = []
        for i in range(1, len(ext) - 2):
            p0 = ext[i - 1]
            p1 = ext[i]
            p2 = ext[i + 1]
            p3 = ext[i + 2]
            for j in range(samples_per_segment):
                t = j / float(samples_per_segment)
                tt = t * t
                ttt = tt * t
                x_val = 0.5 * (
                    (2 * p1[0])
                    + (-p0[0] + p2[0]) * t
                    + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * tt
                    + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * ttt
                )
                y_val = 0.5 * (
                    (2 * p1[1])
                    + (-p0[1] + p2[1]) * t
                    + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * tt
                    + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * ttt
                )
                smooth.extend([x_val, y_val])

        smooth.extend([points[-1][0], points[-1][1]])
        return smooth

    def _redraw(self, *args):
        self.canvas.clear()
        if self.width <= 0 or self.height <= 0:
            return

        left = self.x + dp(24)
        bottom = self.y + dp(20)
        right = self.right - dp(12)
        top = self.top - dp(12)
        graph_w = max(right - left, 1)
        graph_h = max(top - bottom, 1)

        with self.canvas:
            Color(0.88, 0.88, 0.88, 1)
            Rectangle(pos=(self.x, self.y), size=self.size)

            Color(0.82, 0.82, 0.82, 1)
            for i in range(1, 5):
                y_grid = bottom + (graph_h * i / 5)
                Line(points=[left, y_grid, right, y_grid], width=1)
            for i in range(1, 6):
                x_grid = left + (graph_w * i / 6)
                Line(points=[x_grid, bottom, x_grid, top], width=0.8)

            Color(0.2, 0.2, 0.2, 1)
            Line(points=[left, bottom, right, bottom], width=1.2)
            Line(points=[left, bottom, left, top], width=1.2)

        series = []
        if self.balance_points:
            series.append(("balance", self.balance_points, (0.10, 0.42, 0.95, 1)))
        if self.overpayment_points:
            series.append(("overpayment", self.overpayment_points, (0.92, 0.15, 0.15, 1)))
        if self.principal_paid_points:
            series.append(("principal", self.principal_paid_points, (0.94, 0.68, 0.16, 1)))
        if not series:
            return

        max_len = max(len(values) for _, values, _ in series)
        if max_len < 2:
            max_len = 2
        max_value = max(max(values) for _, values, _ in series)
        if max_value <= 0:
            max_value = 1

        for _, values, color in series:
            if len(values) == 1:
                xs = [left, right]
                ys = [bottom + (values[0] / max_value) * graph_h] * 2
                points_xy = list(zip(xs, ys))
            else:
                step = graph_w / (len(values) - 1)
                points_xy = []
                for idx, value in enumerate(values):
                    x_val = left + step * idx
                    y_val = bottom + (value / max_value) * graph_h
                    points_xy.append((x_val, y_val))

            smooth = self._smooth_path(points_xy)
            with self.canvas:
                Color(*color)
                Line(points=smooth, width=2.3)


class PieChartWidget(Widget):
    principal_part = 0.0
    interest_part = 0.0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self._redraw, size=self._redraw)

    def set_parts(self, principal_part, interest_part):
        self.principal_part = max(float(principal_part), 0.0)
        self.interest_part = max(float(interest_part), 0.0)
        self._redraw()

    def _redraw(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(0.94, 0.94, 0.94, 1)
            Rectangle(pos=self.pos, size=self.size)

        size = min(self.width, self.height) - dp(20)
        if size <= 0:
            return
        pos = (self.center_x - size / 2, self.center_y - size / 2)
        total = self.principal_part + self.interest_part

        if total <= 0:
            with self.canvas:
                Color(0.75, 0.75, 0.75, 1)
                Ellipse(pos=pos, size=(size, size))
            return

        principal_angle = 360 * (self.principal_part / total)

        with self.canvas:
            Color(0.1, 0.42, 0.95, 1)
            Ellipse(pos=pos, size=(size, size), angle_start=0, angle_end=principal_angle)
            Color(0.9, 0.1, 0.1, 1)
            Ellipse(pos=pos, size=(size, size), angle_start=principal_angle, angle_end=360)


KV = """
<TableRow>:
    orientation: "horizontal"
    size_hint_y: None
    size_hint_x: None
    width: app.calc_table_width
    height: "46dp"
    spacing: "6dp"
    padding: "10dp", 0
    canvas.before:
        Color:
            rgba: root.bg_color
        Rectangle:
            pos: self.pos
            size: self.size
    MDLabel:
        text: root.no
        size_hint_x: None
        width: root.no_width
        theme_text_color: "Custom"
        text_color: root.text_color
        halign: "center"
        valign: "middle"
        text_size: self.size
    MDLabel:
        text: root.date
        size_hint_x: None
        width: root.date_width
        theme_text_color: "Custom"
        text_color: root.text_color
        halign: "left"
        valign: "middle"
        text_size: self.size
    MDLabel:
        text: root.payment
        size_hint_x: None
        width: root.amount_width
        theme_text_color: "Custom"
        text_color: root.text_color
        halign: "right"
        valign: "middle"
        text_size: self.size
    MDLabel:
        text: root.interest
        size_hint_x: None
        width: root.amount_width
        theme_text_color: "Custom"
        text_color: root.text_color
        halign: "right"
        valign: "middle"
        text_size: self.size
    MDLabel:
        text: root.principal
        size_hint_x: None
        width: root.amount_width
        theme_text_color: "Custom"
        text_color: root.text_color
        halign: "right"
        valign: "middle"
        text_size: self.size
    MDLabel:
        text: root.balance
        size_hint_x: None
        width: root.amount_width
        theme_text_color: "Custom"
        text_color: root.text_color
        halign: "right"
        valign: "middle"
        text_size: self.size

MDScreen:
    md_bg_color: app.screen_color
    MDNavigationLayout:
        MDScreenManager:
            id: screen_manager

            MDScreen:
                name: "input"
                MDBoxLayout:
                    orientation: "vertical"

                    MDTopAppBar:
                        title: app.app_title_text
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["translate", lambda x: app.open_language_menu(x)], ["theme-light-dark", lambda x: app.toggle_theme()]]
                        elevation: 5
                        height: "52dp"
                        md_bg_color: app.toolbar_color
                        specific_text_color: app.toolbar_text_color

                    MDTabs:
                        id: tabs_input
                        on_tab_switch: app.on_tab_switch(*args)
                        allow_stretch: True
                        size_hint_y: None
                        height: "48dp"
                        md_bg_color: app.toolbar_color

                    ScrollView:
                        do_scroll_x: False

                        MDBoxLayout:
                            id: form_card
                            orientation: "vertical"
                            size_hint_y: None
                            height: self.minimum_height
                            md_bg_color: app.card_color
                            padding: "10dp"
                            spacing: "2dp"

                            MDBoxLayout:
                                size_hint_y: None
                                height: "38dp"
                                spacing: "8dp"
                                MDIconButton:
                                    icon: "calendar-month-outline"
                                    theme_text_color: "Hint"
                                    on_release: app.open_date_picker()
                                MDBoxLayout:
                                    orientation: "vertical"
                                    MDLabel:
                                        text: app.start_date_label_text
                                        theme_text_color: "Hint"
                                        font_style: "Caption"
                                    MDTextButton:
                                        text: app.start_date_text
                                        halign: "left"
                                        on_release: app.open_date_picker()

                            MDTextField:
                                id: loan_input
                                hint_text: app.loan_hint_text
                                mode: "line"
                                input_filter: "float"
                                size_hint_y: None
                                height: "40dp"

                            MDTextField:
                                id: years_input
                                hint_text: app.years_hint_text
                                mode: "line"
                                input_filter: "int"
                                size_hint_y: None
                                height: "40dp"

                            MDBoxLayout:
                                size_hint_y: None
                                height: "56dp"
                                spacing: "10dp"
                                MDTextField:
                                    id: rate_input
                                    hint_text: app.rate_hint_text
                                    mode: "line"
                                    input_filter: "float"
                                MDTextField:
                                    id: payment_type_input
                                    hint_text: app.payment_type_label_text
                                    text: app.payment_type
                                    mode: "line"
                                    readonly: True
                                    on_focus: app.open_payment_type_menu(self, self.focus)

                            MDRaisedButton:
                                text: app.calculate_button_text
                                size_hint_y: None
                                height: "40dp"
                                md_bg_color: app.primary_color
                                on_release: app.calculate()

                            MDSeparator:
                                height: "1dp"

                            MDBoxLayout:
                                size_hint_y: None
                                height: "34dp"
                                MDLabel:
                                    text: app._t("monthly")
                                MDLabel:
                                    text: app.monthly_text
                                    halign: "right"

                            MDBoxLayout:
                                size_hint_y: None
                                height: "34dp"
                                MDLabel:
                                    text: app.total_interest_label_text
                                MDLabel:
                                    text: app.overpayment_text
                                    halign: "right"

                            MDBoxLayout:
                                size_hint_y: None
                                height: "34dp"
                                MDLabel:
                                    text: app._t("total_payment")
                                MDLabel:
                                    text: app.total_text
                                    halign: "right"

                            MDBoxLayout:
                                size_hint_y: None
                                height: "34dp"
                                MDLabel:
                                    text: app.effective_rate_label_text
                                MDLabel:
                                    text: app.effective_text
                                    halign: "right"

            MDScreen:
                name: "calc"
                MDBoxLayout:
                    orientation: "vertical"

                    MDTopAppBar:
                        title: app.app_title_text
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["translate", lambda x: app.open_language_menu(x)], ["theme-light-dark", lambda x: app.toggle_theme()]]
                        elevation: 10
                        md_bg_color: app.toolbar_color
                        specific_text_color: app.toolbar_text_color

                    MDTabs:
                        id: tabs_calc
                        on_tab_switch: app.on_tab_switch(*args)
                        allow_stretch: True
                        size_hint_y: None
                        height: "48dp"
                        md_bg_color: app.toolbar_color

                    ScrollView:
                        do_scroll_x: True
                        do_scroll_y: True
                        bar_width: "4dp"
                        MDList:
                            id: calc_table_list
                            size_hint_x: None
                            width: app.calc_table_width

            MDScreen:
                name: "graph"
                MDBoxLayout:
                    orientation: "vertical"

                    MDTopAppBar:
                        title: app.app_title_text
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["translate", lambda x: app.open_language_menu(x)], ["theme-light-dark", lambda x: app.toggle_theme()]]
                        elevation: 10
                        md_bg_color: app.toolbar_color
                        specific_text_color: app.toolbar_text_color

                    MDTabs:
                        id: tabs_graph
                        on_tab_switch: app.on_tab_switch(*args)
                        allow_stretch: True
                        size_hint_y: None
                        height: "48dp"
                        md_bg_color: app.toolbar_color

                    MDCard:
                        id: graph_card
                        orientation: "vertical"
                        md_bg_color: app.card_color
                        radius: [18, 18, 18, 18]
                        elevation: 3
                        padding: "12dp"
                        spacing: "8dp"
                        size_hint: 1, 1
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}

                        MDLabel:
                            text: app.graph_title_text
                            font_style: "H6"
                            halign: "center"
                            size_hint_y: None
                            height: self.texture_size[1] + dp(8)

                        LineGraphWidget:
                            id: graph_widget
                            size_hint_x: 1
                            size_hint_y: 1

                        MDBoxLayout:
                            size_hint_y: None
                            height: "58dp"
                            spacing: "10dp"
                            orientation: "vertical"

                            MDLabel:
                                text: app.legend_balance_text
                                halign: "center"

                            MDLabel:
                                text: app.legend_interest_text
                                halign: "center"

                            MDLabel:
                                text: app.legend_principal_paid_text
                                halign: "center"

            MDScreen:
                name: "diagram"
                MDBoxLayout:
                    orientation: "vertical"

                    MDTopAppBar:
                        title: app.app_title_text
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["translate", lambda x: app.open_language_menu(x)], ["theme-light-dark", lambda x: app.toggle_theme()]]
                        elevation: 10
                        md_bg_color: app.toolbar_color
                        specific_text_color: app.toolbar_text_color

                    MDTabs:
                        id: tabs_diagram
                        on_tab_switch: app.on_tab_switch(*args)
                        allow_stretch: True
                        size_hint_y: None
                        height: "48dp"
                        md_bg_color: app.toolbar_color

                    ScrollView:
                        do_scroll_x: False
                        scroll_y: 1

                        MDCard:
                            id: diagram_card
                            orientation: "vertical"
                            adaptive_height: True
                            md_bg_color: app.card_color
                            radius: [18, 18, 18, 18]
                            elevation: 3
                            size_hint_y: None
                            height: self.minimum_height
                            padding: "16dp"
                            spacing: "10dp"

                            MDLabel:
                                text: app.diagram_title_text
                                font_style: "H6"
                                halign: "center"
                                size_hint_y: None
                                height: self.texture_size[1] + dp(8)

                            PieChartWidget:
                                id: pie_widget
                                size_hint_x: None
                                width: min(root.width - dp(48), dp(320))
                                size_hint_y: None
                                height: "260dp"
                                pos_hint: {"center_x": 0.5}

                            MDBoxLayout:
                                orientation: "vertical"
                                adaptive_height: True
                                spacing: "4dp"
                                size_hint_x: None
                                width: "240dp"
                                pos_hint: {"center_x": 0.5}

                                MDBoxLayout:
                                    orientation: "horizontal"
                                    size_hint_y: None
                                    height: "28dp"
                                    spacing: "8dp"

                                    MDIcon:
                                        icon: "circle-small"
                                        theme_text_color: "Custom"
                                        text_color: (0.1, 0.42, 0.95, 1)
                                        size_hint_x: None
                                        width: "18dp"

                                    MDLabel:
                                        text: app.principal_text + ": " + app.principal_percent_text
                                        halign: "left"
                                        valign: "middle"
                                        text_size: self.size

                                MDBoxLayout:
                                    orientation: "horizontal"
                                    size_hint_y: None
                                    height: "28dp"
                                    spacing: "8dp"

                                    MDIcon:
                                        icon: "circle-small"
                                        theme_text_color: "Custom"
                                        text_color: (0.9, 0.1, 0.1, 1)
                                        size_hint_x: None
                                        width: "18dp"

                                    MDLabel:
                                        text: app.interest_text + ": " + app.interest_percent_text
                                        halign: "left"
                                        valign: "middle"
                                        text_size: self.size

            MDScreen:
                name: "total"
                MDBoxLayout:
                    orientation: "vertical"

                    MDTopAppBar:
                        title: app.app_title_text
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["translate", lambda x: app.open_language_menu(x)], ["theme-light-dark", lambda x: app.toggle_theme()]]
                        elevation: 10
                        md_bg_color: app.toolbar_color
                        specific_text_color: app.toolbar_text_color

                    MDTabs:
                        id: tabs_total
                        on_tab_switch: app.on_tab_switch(*args)
                        allow_stretch: True
                        size_hint_y: None
                        height: "48dp"
                        md_bg_color: app.toolbar_color

                    MDBoxLayout:
                        orientation: "vertical"
                        padding: "12dp"
                        spacing: "8dp"

                        MDLabel:
                            text: app.total_table_title_text
                            font_style: "H6"
                            halign: "center"
                            size_hint_y: None
                            height: self.texture_size[1] + dp(8)

                        ScrollView:
                            MDGridLayout:
                                id: schedule_table
                                cols: 5
                                adaptive_height: True
                                spacing: "6dp"
                                padding: "4dp"

        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation: "vertical"
                padding: "8dp"
                spacing: "8dp"

                MDLabel:
                    text: "MortgageCalculator"
                    font_style: "H6"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: "kivydevelopment@gmail.com"
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: app.nav_input_text
                            on_release: app.switch_screen("input")
                            IconLeftWidget:
                                icon: "form-textbox"

                        OneLineIconListItem:
                            text: app.nav_calc_text
                            on_release: app.switch_screen("calc")
                            IconLeftWidget:
                                icon: "calculator"

                        OneLineIconListItem:
                            text: app.nav_graph_text
                            on_release: app.switch_screen("graph")
                            IconLeftWidget:
                                icon: "chart-line"

                        OneLineIconListItem:
                            text: app.nav_diagram_text
                            on_release: app.switch_screen("diagram")
                            IconLeftWidget:
                                icon: "chart-pie"

                        OneLineIconListItem:
                            text: app.nav_total_text
                            on_release: app.switch_screen("total")
                            IconLeftWidget:
                                icon: "table"
"""


class MortgageCalculatorApp(MDApp):
    language = StringProperty("ru")
    dark_mode = BooleanProperty(True)
    toolbar_color = ListProperty([0.98, 0.98, 0.98, 1])
    toolbar_text_color = ListProperty([0.12, 0.12, 0.12, 1])
    primary_color = ListProperty([0.22, 0.22, 0.22, 1])
    screen_color = ListProperty([0.94, 0.95, 0.97, 1])
    card_color = ListProperty([1, 1, 1, 0.97])
    app_title_text = StringProperty("")
    nav_input_text = StringProperty("")
    nav_calc_text = StringProperty("")
    nav_graph_text = StringProperty("")
    nav_diagram_text = StringProperty("")
    nav_total_text = StringProperty("")
    form_title_text = StringProperty("")
    loan_hint_text = StringProperty("")
    loan_help_text = StringProperty("")
    rate_hint_text = StringProperty("")
    rate_help_text = StringProperty("")
    years_hint_text = StringProperty("")
    years_help_text = StringProperty("")
    payment_type_hint_text = StringProperty("")
    calculate_button_text = StringProperty("")
    graph_title_text = StringProperty("")
    legend_balance_text = StringProperty("")
    legend_interest_text = StringProperty("")
    legend_principal_paid_text = StringProperty("")
    start_date_label_text = StringProperty("")
    start_date_text = StringProperty("31-07-2021")
    payment_type_label_text = StringProperty("")
    total_interest_label_text = StringProperty("")
    effective_rate_label_text = StringProperty("")
    diagram_title_text = StringProperty("")
    total_table_title_text = StringProperty("")
    principal_text = StringProperty("")
    interest_text = StringProperty("")
    status_text = StringProperty("")
    loan_text = StringProperty("—")
    rate_text = StringProperty("—")
    term_text = StringProperty("—")
    monthly_text = StringProperty("—")
    total_text = StringProperty("—")
    overpayment_text = StringProperty("—")
    principal_percent_text = StringProperty("0.00%")
    interest_percent_text = StringProperty("0.00%")
    payment_type = StringProperty("")
    effective_text = StringProperty("—")
    calc_table_width = NumericProperty(dp(640))
    calc_no_width = NumericProperty(dp(44))
    calc_date_width = NumericProperty(dp(92))
    calc_amount_width = NumericProperty(dp(122))

    def build(self):
        self.title = "Mortgage Calculator"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.accent_palette = "BlueGray"
        self._is_syncing_tabs = False
        self._last_schedule = []
        self.payment_menu = None
        self.language_menu = None
        Window.bind(size=self._on_window_resize)
        self._update_calc_table_metrics(Window.width)
        self._apply_language()
        self._apply_theme()
        return Builder.load_string(KV)

    def on_start(self):
        self._populate_tabs()
        self._sync_tabs("input")
        self._setup_menus()
        self._update_calc_table_metrics(Window.width)
        self._populate_calc_table(self._last_schedule)
        Clock.schedule_once(lambda dt: self._animate_screen_content("input"), 0.05)

    def _on_window_resize(self, _window, size):
        width = size[0] if isinstance(size, (tuple, list)) else Window.width
        self._update_calc_table_metrics(width)
        self._populate_calc_table(self._last_schedule)

    def _update_calc_table_metrics(self, viewport_width: float):
        available = max(float(viewport_width) - dp(24), dp(300))
        # Keep horizontal scroll available, but avoid oversized columns on phones.
        self.calc_table_width = max(available, dp(560))
        self.calc_no_width = dp(42)
        self.calc_date_width = dp(88)
        fixed = self.calc_no_width + self.calc_date_width + dp(20) + (dp(6) * 5)
        self.calc_amount_width = max((self.calc_table_width - fixed) / 4.0, dp(100))

    def _t(self, key: str) -> str:
        lang_map = I18N.get(self.language, I18N["ru"])
        return lang_map.get(key, key)

    def _apply_language(self):
        self.app_title_text = self._t("app_title")
        self.nav_input_text = self._t("tab_input")
        self.nav_calc_text = self._t("tab_calc")
        self.nav_graph_text = self._t("tab_graph")
        self.nav_diagram_text = self._t("tab_diagram")
        self.nav_total_text = self._t("tab_total")
        self.form_title_text = self._t("form_title")
        self.loan_hint_text = self._t("loan_hint")
        self.loan_help_text = self._t("loan_help")
        self.rate_hint_text = self._t("rate_hint")
        self.rate_help_text = self._t("rate_help")
        self.years_hint_text = self._t("years_hint")
        self.years_help_text = self._t("years_help")
        self.payment_type_hint_text = self._t("payment_type_hint")
        self.calculate_button_text = self._t("calculate")
        self.graph_title_text = self._t("graph_title")
        self.legend_balance_text = self._t("legend_balance")
        self.legend_interest_text = self._t("legend_interest")
        self.legend_principal_paid_text = self._t("legend_principal_paid")
        self.start_date_label_text = self._t("start_date")
        self.payment_type_label_text = self._t("payment_type")
        self.total_interest_label_text = self._t("total_interest")
        self.effective_rate_label_text = self._t("effective_rate")
        self.diagram_title_text = self._t("diagram_title")
        self.total_table_title_text = self._t("total_table_title")
        self.principal_text = self._t("principal")
        self.interest_text = self._t("interest")
        if not self.status_text:
            self.status_text = self._t("status_default")
        if not self.payment_type:
            self.payment_type = self._t("payment_annuity")
        self.title = self.app_title_text

    def set_language(self, code: str):
        self.language = code
        self._apply_language()
        self._rebuild_tabs_for_language()
        self._setup_menus()
        self._populate_calc_table(self._last_schedule)

    def open_language_menu(self, caller):
        if self.language_menu is None:
            self.language_menu = MDDropdownMenu(
                caller=caller,
                width_mult=2.8,
                items=[
                    {"text": "Русский", "on_release": lambda x="ru": self._set_language_and_close(x)},
                    {"text": "Қазақша", "on_release": lambda x="kk": self._set_language_and_close(x)},
                    {"text": "English", "on_release": lambda x="en": self._set_language_and_close(x)},
                ],
            )
        self.language_menu.caller = caller
        self.language_menu.open()

    def _set_language_and_close(self, code: str):
        self.set_language(code)
        if self.language_menu is not None:
            self.language_menu.dismiss()

    def open_date_picker(self):
        try:
            current = datetime.strptime(self.start_date_text, "%d-%m-%Y")
        except Exception:
            current = datetime.now()
        picker = MDDatePicker(
            year=current.year,
            month=current.month,
            day=current.day,
        )
        picker.bind(on_save=self._on_date_selected)
        picker.open()

    def _on_date_selected(self, _instance, value, _date_range):
        self.start_date_text = value.strftime("%d-%m-%Y")
        self._populate_calc_table(self._last_schedule)

    def _setup_menus(self):
        payment_field = self.root.ids.get("payment_type_input")
        if payment_field is None:
            self.payment_menu = None
        else:
            self.payment_menu = MDDropdownMenu(
                caller=payment_field,
                width_mult=3.5,
                items=[
                    {
                        "text": self._t("payment_annuity"),
                        "on_release": lambda x=self._t("payment_annuity"): self._set_payment_type(x),
                    },
                    {
                        "text": self._t("payment_diff"),
                        "on_release": lambda x=self._t("payment_diff"): self._set_payment_type(x),
                    },
                ],
            )
            payment_field.text = self.payment_type
        if self.status_text == "" or "Введите параметры" in self.status_text or "Enter parameters" in self.status_text:
            self.status_text = self._t("status_default")

    def _set_payment_type(self, value: str):
        self.payment_type = value
        payment_field = self.root.ids.get("payment_type_input")
        if payment_field is not None:
            payment_field.text = value
        if self.payment_menu is not None:
            self.payment_menu.dismiss()

    def open_payment_type_menu(self, field, focused: bool):
        if not focused:
            return
        if self.payment_menu is None:
            self._setup_menus()
        if self.payment_menu is not None:
            self.payment_menu.caller = field
            self.payment_menu.open()

    def _populate_tabs(self):
        tabs_ids = ("tabs_input", "tabs_calc", "tabs_graph", "tabs_diagram", "tabs_total")
        for tabs_id in tabs_ids:
            tabs = self.root.ids.get(tabs_id)
            if tabs is None:
                continue
            if tabs.get_tab_list():
                continue
            for screen_name, tab_key in TAB_ITEMS:
                tabs.add_widget(
                    NavigationTab(
                        title=self._t(tab_key),
                        screen_name=screen_name,
                    )
                )

    def _rebuild_tabs_for_language(self):
        tabs_ids = ("tabs_input", "tabs_calc", "tabs_graph", "tabs_diagram", "tabs_total")
        for tabs_id in tabs_ids:
            tabs = self.root.ids.get(tabs_id)
            if tabs is None:
                continue
            existing = list(tabs.get_tab_list())
            for tab in existing:
                tabs.remove_widget(tab)
            for screen_name, tab_key in TAB_ITEMS:
                tabs.add_widget(NavigationTab(title=self._t(tab_key), screen_name=screen_name))
        current_screen = self.root.ids.screen_manager.current
        self._sync_tabs(current_screen)

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        if self._is_syncing_tabs:
            return
        if not hasattr(instance_tab, "screen_name"):
            return
        self.switch_screen(instance_tab.screen_name, close_drawer=False, sync_tabs=True)

    def _apply_theme(self):
        if self.dark_mode:
            self.theme_cls.theme_style = "Dark"
            self.toolbar_color = [0.06, 0.06, 0.06, 1]
            self.toolbar_text_color = [0.95, 0.95, 0.95, 1]
            # Keep dark mode fully dark to preserve text contrast.
            self.screen_color = [0.10, 0.10, 0.11, 1]
            self.card_color = [0.15, 0.15, 0.16, 1]
            self.primary_color = [0.28, 0.58, 0.92, 1]
        else:
            self.theme_cls.theme_style = "Light"
            self.toolbar_color = [0.98, 0.98, 0.98, 1]
            self.toolbar_text_color = [0.12, 0.12, 0.12, 1]
            self.screen_color = [0.94, 0.95, 0.97, 1]
            self.card_color = [1, 1, 1, 0.97]
            self.primary_color = [0.22, 0.22, 0.22, 1]

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self._apply_theme()
        self._populate_calc_table(self._last_schedule)

    def _sync_tabs(self, screen_name: str):
        tabs_ids = ("tabs_input", "tabs_calc", "tabs_graph", "tabs_diagram", "tabs_total")
        self._is_syncing_tabs = True
        try:
            for tabs_id in tabs_ids:
                tabs = self.root.ids.get(tabs_id)
                if tabs is None:
                    continue
                target_tab = None
                for tab in tabs.get_tab_list():
                    if getattr(tab, "screen_name", None) == screen_name:
                        target_tab = tab
                        break
                if target_tab is not None:
                    tabs.switch_tab(target_tab.title)
        finally:
            self._is_syncing_tabs = False

    def switch_screen(self, screen_name: str, close_drawer: bool = True, sync_tabs: bool = True) -> None:
        root = self.root
        root.ids.screen_manager.current = screen_name
        if close_drawer:
            root.ids.nav_drawer.set_state("close")
        if sync_tabs:
            self._sync_tabs(screen_name)
        Clock.schedule_once(lambda dt: self._animate_screen_content(screen_name), 0.02)

    def _animate_widget(self, widget):
        # Do not animate positional properties for layout-managed widgets.
        # Moving `y` causes clipped cards and broken geometry in Box/Anchor layouts.
        widget.opacity = 0
        Animation.cancel_all(widget)
        Animation(opacity=1, d=0.22, t="out_quad").start(widget)

    def _animate_screen_content(self, screen_name: str):
        ids_by_screen = {
            "input": ["form_card"],
            "calc": ["calc_table_list"],
            "graph": ["graph_card"],
            "diagram": ["diagram_card"],
            "total": ["schedule_table"],
        }
        for widget_id in ids_by_screen.get(screen_name, []):
            widget = self.root.ids.get(widget_id)
            if widget is None:
                continue
            self._animate_widget(widget)

    @staticmethod
    def _fmt_money(value: float) -> str:
        return f"{value:,.2f}".replace(",", " ").replace(".", ",")

    def _read_inputs(self):
        loan_raw = self.root.ids.loan_input.text.strip().replace(" ", "")
        rate_raw = self.root.ids.rate_input.text.strip().replace(",", ".")
        years_raw = self.root.ids.years_input.text.strip()

        if not loan_raw or not rate_raw or not years_raw:
            raise ValueError(self._t("status_fill"))

        loan = float(loan_raw)
        rate = float(rate_raw)
        years = int(years_raw)
        if loan <= 0 or rate < 0 or years <= 0:
            raise ValueError(self._t("status_invalid"))
        return loan, rate, years

    def _build_schedule(self, loan, annual_rate, years):
        months = years * 12
        monthly_rate = annual_rate / 12 / 100

        if monthly_rate == 0:
            monthly_payment = loan / months
        else:
            monthly_payment = loan * monthly_rate / (1 - (1 + monthly_rate) ** (-months))

        balance = loan
        schedule = []
        for month in range(1, months + 1):
            interest_part = balance * monthly_rate
            principal_part = monthly_payment - interest_part

            if month == months:
                principal_part = balance
                monthly_payment = principal_part + interest_part

            balance = max(balance - principal_part, 0.0)
            schedule.append((month, monthly_payment, principal_part, interest_part, balance))
        return schedule

    def _cell(self, text, bold=False):
        return MDLabel(
            text=str(text),
            halign="left",
            bold=bold,
            size_hint_y=None,
            height=dp(28),
        )

    @staticmethod
    def _next_month_date(value: datetime) -> datetime:
        year = value.year
        month = value.month + 1
        if month > 12:
            month = 1
            year += 1
        day = min(value.day, calendar.monthrange(year, month)[1])
        return value.replace(year=year, month=month, day=day)

    def _populate_calc_table(self, schedule=None):
        table = self.root.ids.calc_table_list
        table.clear_widgets()
        header_bg = [0.18, 0.18, 0.18, 1]
        header_text = [0.95, 0.95, 0.95, 1]
        odd_bg = [0.03, 0.03, 0.03, 1]
        odd_text = [0.96, 0.96, 0.96, 1]
        even_bg = [0.92, 0.92, 0.92, 1]
        even_text = [0.10, 0.10, 0.10, 1]

        table.add_widget(
            TableRow(
                no=self._t("no"),
                date=self._t("date"),
                payment=self._t("payment_col"),
                interest=self._t("interest_part"),
                principal=self._t("credit_part"),
                balance=self._t("balance"),
                bg_color=header_bg,
                text_color=header_text,
                no_width=self.calc_no_width,
                date_width=self.calc_date_width,
                amount_width=self.calc_amount_width,
            )
        )

        if not schedule:
            table.add_widget(
                TableRow(
                    no="1",
                    date=self.start_date_text,
                    payment="—",
                    interest="—",
                    principal="—",
                    balance="—",
                    bg_color=even_bg,
                    text_color=even_text,
                    no_width=self.calc_no_width,
                    date_width=self.calc_date_width,
                    amount_width=self.calc_amount_width,
                )
            )
            return

        try:
            current_date = datetime.strptime(self.start_date_text, "%d-%m-%Y")
        except Exception:
            current_date = datetime.now()

        for idx, (_, payment, principal, interest, balance) in enumerate(schedule, start=1):
            is_odd = idx % 2 == 1
            table.add_widget(
                TableRow(
                    no=str(idx),
                    date=current_date.strftime("%d-%m-%Y"),
                    payment=self._fmt_money(payment),
                    interest=self._fmt_money(interest),
                    principal=self._fmt_money(principal),
                    balance=self._fmt_money(balance),
                    bg_color=odd_bg if is_odd else even_bg,
                    text_color=odd_text if is_odd else even_text,
                    no_width=self.calc_no_width,
                    date_width=self.calc_date_width,
                    amount_width=self.calc_amount_width,
                )
            )
            current_date = self._next_month_date(current_date)

    def _populate_schedule_table(self, schedule):
        table = self.root.ids.schedule_table
        table.clear_widgets()

        headers = [
            self._t("month"),
            self._t("monthly"),
            self._t("credit_part"),
            self._t("interest_part"),
            self._t("balance"),
        ]
        for header in headers:
            table.add_widget(self._cell(header, bold=True))

        if not schedule:
            table.add_widget(self._cell("—"))
            table.add_widget(self._cell("—"))
            table.add_widget(self._cell("—"))
            table.add_widget(self._cell("—"))
            table.add_widget(self._cell("—"))
            return

        max_rows = 24
        rows = schedule[:max_rows]
        for month, payment, principal, interest, balance in rows:
            table.add_widget(self._cell(month))
            table.add_widget(self._cell(self._fmt_money(payment)))
            table.add_widget(self._cell(self._fmt_money(principal)))
            table.add_widget(self._cell(self._fmt_money(interest)))
            table.add_widget(self._cell(self._fmt_money(balance)))

        if len(schedule) > max_rows:
            table.add_widget(self._cell("..."))
            table.add_widget(self._cell("..."))
            table.add_widget(self._cell("..."))
            table.add_widget(self._cell("..."))
            table.add_widget(self._cell("..."))
            month, payment, principal, interest, balance = schedule[-1]
            table.add_widget(self._cell(month))
            table.add_widget(self._cell(self._fmt_money(payment)))
            table.add_widget(self._cell(self._fmt_money(principal)))
            table.add_widget(self._cell(self._fmt_money(interest)))
            table.add_widget(self._cell(self._fmt_money(balance)))

    def calculate(self):
        try:
            loan, annual_rate, years = self._read_inputs()
            schedule = self._build_schedule(loan, annual_rate, years)
            self._last_schedule = schedule

            months = years * 12
            total_payment = sum(row[1] for row in schedule)
            overpayment = total_payment - loan
            monthly_payment = schedule[0][1]

            self.loan_text = self._fmt_money(loan)
            self.rate_text = f"{annual_rate:.2f}%"
            self.term_text = f"{years} лет ({months} мес.)"
            self.monthly_text = self._fmt_money(monthly_payment)
            self.total_text = self._fmt_money(total_payment)
            self.overpayment_text = self._fmt_money(overpayment)
            monthly_rate = annual_rate / 12 / 100
            effective_rate = (((1 + monthly_rate) ** 12) - 1) * 100 if monthly_rate > 0 else 0
            self.effective_text = f"{effective_rate:.2f}%"

            principal_pct = (loan / total_payment) * 100 if total_payment else 0
            interest_pct = (overpayment / total_payment) * 100 if total_payment else 0
            self.principal_percent_text = f"{principal_pct:.2f}%"
            self.interest_percent_text = f"{interest_pct:.2f}%"

            graph_rows = schedule
            max_points = 72
            if len(graph_rows) > max_points:
                step = len(graph_rows) / float(max_points)
                sampled = []
                for i in range(max_points):
                    idx = int(round(i * step))
                    if idx >= len(graph_rows):
                        idx = len(graph_rows) - 1
                    sampled.append(graph_rows[idx])
                graph_rows = sampled

            balance_points = [row[4] for row in graph_rows]
            cumulative_overpayment_points = []
            cumulative_principal_points = []
            over_sum = 0.0
            principal_sum = 0.0
            for _, _, principal_part, interest_part, _ in graph_rows:
                over_sum += interest_part
                principal_sum += principal_part
                cumulative_overpayment_points.append(over_sum)
                cumulative_principal_points.append(principal_sum)

            self.root.ids.graph_widget.set_data(
                balance_points, cumulative_overpayment_points, cumulative_principal_points
            )
            self.root.ids.pie_widget.set_parts(loan, overpayment)
            self._populate_calc_table(schedule)
            self._populate_schedule_table(schedule)

            self.status_text = self._t("status_done")
        except Exception as exc:
            self._last_schedule = []
            self.status_text = str(exc)


if __name__ == "__main__":
    MortgageCalculatorApp().run()
