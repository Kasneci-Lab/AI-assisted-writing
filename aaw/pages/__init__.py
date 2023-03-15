from .input_type import input_type, __inputtypepage__
from .upload_image import upload_image, __uploadpage__
from .feedback import feedback, __feedbackpage__
from .input_text import input_text, __inputtextpage__
from .home import homepage, __homepage__
from .modify_text import modify_text, __modifytextpage__

PAGES = [
    __homepage__,
    __uploadpage__,
    __feedbackpage__,
    __inputtextpage__,
    __inputtypepage__,
    __modifytextpage__,
]
