from tkinter.messagebox import NO
from selenium.webdriver.common.by import By

from frame.node import Node

class product(Node):

    self = (By.CSS_SELECTOR, "#column-left")

    class desktops(Node):
        self = (By.CSS_SELECTOR, "#column-left > * a[href$='desktops']")
        pc = (By.CSS_SELECTOR, "#column-left > * a[href$='desktops/pc']")
        mac = (By.CSS_SELECTOR, "#column-left > * a[href$='desktops/mac']")

    class laptops(Node):
        self = (By.CSS_SELECTOR, "#column-left > * a[href$='laptop-notebook']")
        mac = (By.CSS_SELECTOR, "#column-left > * a[href$='laptop-notebook/macs']")
        win = (By.CSS_SELECTOR, "#column-left > * a[href$='laptop-notebook/windows']")

    class components(Node):
        self = (By.CSS_SELECTOR, "#column-left > * a[href$='component']")
        mice = (By.CSS_SELECTOR, "#column-left > * a[href$='component/mouse']")
        monitors = (By.CSS_SELECTOR, "#column-left > * a[href$='component/monitor']")
        printers = (By.CSS_SELECTOR, "#column-left > * a[href$='component/printer']")
        scanners = (By.CSS_SELECTOR, "#column-left > * a[href$='component/scanner']")
        webcameras = (By.CSS_SELECTOR, "#column-left > * a[href$='component/web-camera']")

    class tablets(Node):
        self = (By.CSS_SELECTOR, "#column-left > * a[href$='tablet']")

    class software(Node):
        self = (By.CSS_SELECTOR, "#column-left > * a[href$='software']")

    class phones(Node):
        self = (By.CSS_SELECTOR, "#column-left > * a[href$='smartphone']")

    class cameras(Node):
        self = (By.CSS_SELECTOR, "#column-left > * a[href$='camera']")

    class mp3players(Node):
        self = (By.CSS_SELECTOR, "#column-left > * a[href$='mp3-players']")
