import os
from tkinter import Tk, Label, Button, Frame, filedialog, messagebox, font, Menu, Toplevel
from PIL import Image, ImageTk

class ImageHexConverterApp:
    def __init__(self, root):
        """
        앱 초기화 함수
        - 창 기본 설정
        - 폰트 및 상태 변수 초기화
        - 카드 스타일 프레임 및 버튼 배치
        - 메뉴 구성 및 단축키 바인딩
        """

        self.root = root
        self.root.title("HEX Converter")  # 창 제목 설정
        self.root.geometry("600x320")     # 고정 창 크기
        self.root.configure(bg="#E9E9E9") # 배경 색상 설정
        self.root.resizable(False, False)  # 창 크기 조절 비활성화

        self.default_font = font.Font(family="맑은 고딕", size=10)  # 전체 UI에 사용할 기본 글꼴

        # 이미지 상태 관련 변수 초기화
        self.image_path = None
        self.image = None
        self.tk_image = None

        # 다크모드 상태 변수 초기화
        self.dark_mode = False

        # 메뉴 구성
        self.create_menu()

        # 카드 스타일 프레임 구성 (전체 UI 요소를 담는 틀)
        self.card_frame = Frame(self.root, width=500, height=250, bg="#FFFFFF", bd=2, relief="groove")
        self.card_frame.place(x=50, y=35)

        # 이미지 미리보기 라벨 구성
        self.image_label = Label(self.card_frame, bg="#EAEAEA", bd=1, relief="solid")
        self.image_label.place(x=90, y=25, width=320, height=80)

        # 이미지 선택 버튼 구성
        self.select_button = Button(
            self.card_frame, text="이미지 선택", command=self.select_image,
            width=15, height=2, bd=1, relief="solid",
            font=self.default_font, highlightthickness=0,
            bg="#FFFFFF", fg="#000000"
        )
        self.select_button.place(x=130, y=130)

        # HEX 변환 버튼 구성
        self.convert_button = Button(
            self.card_frame, text="HEX로 저장", command=self.convert_image,
            width=15, height=2, bd=1, relief="solid",
            font=self.default_font, highlightthickness=0,
            bg="#FFFFFF", fg="#000000"
        )
        self.convert_button.place(x=260, y=130)

        # 단축키 바인딩 설정
        self.root.bind('<Control-o>', lambda e: self.select_image())  # Ctrl+O: 이미지 열기
        self.root.bind('<Control-s>', lambda e: self.convert_image()) # Ctrl+S: HEX 저장
        self.root.bind('<Escape>', lambda e: self.root.quit())        # ESC: 종료

    def create_menu(self):
        """
        메뉴바 구성 함수
        - 파일: 열기/저장/종료
        - 화면 초기화: 바로 실행
        - 다크모드 전환: 바로 실행
        - 도움말: 단축키 안내/정보
        """
        menubar = Menu(self.root, font=self.default_font)

        # 파일 메뉴
        file_menu = Menu(menubar, tearoff=0, font=self.default_font)
        file_menu.add_command(label="이미지 선택", command=self.select_image)
        file_menu.add_command(label="HEX로 저장", command=self.convert_image)
        file_menu.add_separator()
        file_menu.add_command(label="종료", command=self.root.quit)
        menubar.add_cascade(label="파일", menu=file_menu)

        # 화면 초기화 메뉴 (단일 항목)
        menubar.add_command(label="화면 초기화", command=self.reset_screen)

        # 다크모드 전환 메뉴 (단일 항목)
        menubar.add_command(label="다크모드 전환", command=self.toggle_dark_mode)

        # 도움말 메뉴
        help_menu = Menu(menubar, tearoff=0, font=self.default_font)
        help_menu.add_command(label="단축키 안내", command=self.show_shortcuts)
        help_menu.add_command(label="정보", command=self.show_info)
        menubar.add_cascade(label="도움말", menu=help_menu)

        self.root.config(menu=menubar)

    def show_info(self):
        """ 제작자 및 앱 정보 표시용 팝업 창 """
        info_window = Toplevel(self.root)
        info_window.title("정보")
        info_window.geometry("300x160")
        info_window.resizable(False, False)

        message = (
            "Grayscale BMP to HEX 변환기\n\n"
            "제작: 조정훈\n\n"
            "버전: 1.0"
        )

        Label(info_window, text=message, font=self.default_font, justify="center", padx=20, pady=10).pack(expand=True)

        Button(info_window, text="닫기", command=info_window.destroy, font=self.default_font, width=10, relief="solid", bd=1).pack(pady=(0, 15))

    def show_shortcuts(self):
        """ 단축키 안내 표시용 팝업 창 """
        shortcut_text = (
            "단축키 안내\n\n"
            "Ctrl + O  : 이미지 선택\n"
            "Ctrl + S  : HEX 저장\n"
            "Esc       : 프로그램 종료"
        )

        info_window = Toplevel(self.root)
        info_window.title("단축키 안내")
        info_window.geometry("300x170")
        info_window.resizable(False, False)

        Label(info_window, text=shortcut_text, font=self.default_font, justify="left", padx=20, pady=10).pack(expand=True)

        Button(info_window, text="닫기", command=info_window.destroy, font=self.default_font, width=10, relief="solid", bd=1).pack(pady=(0, 15))

    def reset_screen(self):
        """ 화면을 초기 상태로 되돌림: 이미지 상태 및 라벨 비우기 """
        self.image_path = None
        self.image = None
        self.tk_image = None
        self.image_label.config(image='')  # 이미지 라벨 초기화
        messagebox.showinfo("초기화", "화면이 초기화되었습니다.")

    def toggle_dark_mode(self):
        """ 다크모드와 라이트모드 전환 함수 (배경 + 버튼 색상 포함) """
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.root.configure(bg="#2E2E2E")
            self.card_frame.configure(bg="#3C3C3C")
            self.image_label.configure(bg="#2E2E2E")
            self.select_button.configure(bg="#444444", fg="#FFFFFF")
            self.convert_button.configure(bg="#444444", fg="#FFFFFF")
        else:
            self.root.configure(bg="#E9E9E9")
            self.card_frame.configure(bg="#FFFFFF")
            self.image_label.configure(bg="#EAEAEA")
            self.select_button.configure(bg="#FFFFFF", fg="#000000")
            self.convert_button.configure(bg="#FFFFFF", fg="#000000")

    def select_image(self):
        """ 이미지 파일 선택 다이얼로그 호출 """
        file_path = filedialog.askopenfilename(title="BMP 흑백 이미지 선택", filetypes=[("BMP 파일", "*.bmp")])
        if file_path:
            self.load_image(file_path)

    def load_image(self, file_path):
        """ 선택된 이미지 로드 후 흑백 변환 및 미리보기 라벨에 표시 """
        try:
            image = Image.open(file_path).convert("L")
            image = image.resize((320, 80))
            self.tk_image = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.tk_image)
            self.image_path = file_path
            self.image = image
        except Exception as e:
            messagebox.showerror("오류", f"이미지 불러오기 실패:\n{str(e)}")

    def convert_image(self):
        """ HEX 파일 저장 위치를 사용자에게 묻고 변환 저장 수행 """
        if not self.image or not self.image_path:
            messagebox.showwarning("경고", "이미지를 먼저 선택하세요.")
            return

        try:
            default_name = os.path.splitext(os.path.basename(self.image_path))[0] + "_hex.txt"
            output_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                initialfile=default_name,
                filetypes=[("텍스트 파일", "*.txt")],
                title="HEX 파일 저장 위치 선택"
            )
            if not output_path:
                return

            self.save_hex(self.image, output_path)
            messagebox.showinfo("완료", f"HEX 저장 완료:\n{output_path}")
        except Exception as e:
            messagebox.showerror("오류", f"변환 중 오류 발생:\n{str(e)}")

    def save_hex(self, img, output_txt_path):
        """ 이미지 픽셀 데이터를 HEX 문자열로 변환 후 줄 단위로 저장 """
        width, height = img.size
        with open(output_txt_path, 'w') as f:
            for y in range(height):
                row = []
                for x in range(width):
                    pixel = img.getpixel((x, y))              # 픽셀 값 추출 (0~255)
                    hex_val = f"0x{pixel:02X}"                # 2자리 HEX 문자열 생성
                    row.append(hex_val)
                f.write(" ".join(row) + "\n")                # 한 줄로 저장 후 개행

if __name__ == "__main__":
    root = Tk()
    app = ImageHexConverterApp(root)
    root.mainloop()
