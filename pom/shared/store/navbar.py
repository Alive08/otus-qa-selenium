from frame.common_locators import *
from frame.node import Node


class navbar(Node):

    link = (css, '#menu')

    class desktops(Node):
        link = (link_text, 'Desktops')
        pc = (plink_text, 'PC')
        mac = (plink_text, 'Mac')
        all = (link_text, 'Show All Desktops')

    class laptops(Node):
        link = (link_text, 'Laptops & Notebooks')
        macs = (plink_text, 'Macs')
        windows = (plink_text, 'Windows')
        all = (link_text, 'Show All Laptops & Notebooks')

    class components(Node):
        link = (link_text, 'Components')
        mice = (plink_text, 'Mice and Trackballs')
        monitors = (plink_text, 'Monitors')
        printers = (plink_text, 'Printers')
        scanners = (plink_text, 'Scanners')
        webcameras = (plink_text, 'Web Cameras')
        all = (link_text, 'Show All Components')

    class tablets(Node):
        link = (link_text, 'Tablets')

    class software(Node):
        link = (link_text, 'Software')

    class phones(Node):
        link = (link_text, 'Phones & PDAs')

    class cameras(Node):
        link = (link_text, 'Cameras')

    class mp3(Node):
        link = (link_text, 'MP3 Players')
