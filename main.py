import flet as ft
import requests

# رابط سيرفر Firebase المجاني الخاص بك والمشغل 24 ساعة
FIREBASE_URL = "https://khouta-server-default-rtdb.firebaseio.com/.json"

def main(page: ft.Page):
    page.title = "تطبيق خُطى"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    # دالة لجلب البيانات من السيرفر عند فتح التطبيق
    def load_data():
        try:
            response = requests.get(FIREBASE_URL)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"Error loading data: {e}")
        return None

    # واجهة التطبيق الفخمة
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("أهلاً بك في رحلتك الروحية", size=16, color=ft.colors.GREEN_700, weight=ft.FontWeight.BOLD),
                    ft.Text("تطبيق خُطى", size=36, color=ft.colors.GREEN_900, weight=ft.FontWeight.BOLD),
                    ft.Text("التاريخ الهجري", size=14, color=ft.colors.AMBER_700),
                    
                    # زر لعرض التوقيت المحلي المباشر
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.icons.CALENDAR_TODAY, color=ft.colors.WHITE),
                                ft.Text("١ ذو الحجة ١٤٤٧ هـ", color=ft.colors.WHITE, size=18, weight=ft.FontWeight.BOLD)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        bgcolor=ft.colors.AMBER_600,
                        padding=10,
                        border_radius=10
                    ),
                    
                    ft.Container(height=20),
                    
                    ft.Container(
                        content=ft.Text("التوقيت المحلي المباشر", color=ft.colors.WHITE, size=16),
                        bgcolor=ft.colors.GREEN_850,
                        padding=15,
                        border_radius=15,
                        alignment=ft.alignment.center
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=30,
            width=350,
            bgcolor=ft.colors.WHITE,
            border_radius=20,
            shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.BLACK12)
        )
    )

ft.app(target=main)
