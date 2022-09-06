from rich.console import Console
import time

"""
    This function is used to get time formatted to UI
    use in this internal operations. Don't use into
    external code. This request is light, so to
    prevent errors it's better just repeat code.
    
    Returns formatted time: 
    Week day, Month's Day/Month/Year (yyyy)
"""


def get_formatted_time():
    return time.strftime("%a, %d/%m/%Y")


"""
    Format the prefix with [TIME][AGENT][TYPE]
"""


def get_formatted_prefix(f_time="ERROR NO TIME PASSED",
                         f_agent="ERROR NO AGENT PASSED",
                         f_type="ERROR NO TIME PASSED"):
    return f"[{str(f_time)}][{str(f_agent)}][{str(f_type)}]:"


class UI:
    def __init__(self, agent=""):
        self.agent = str(agent)
        self.console = Console()

    def info(self, msg):
        msg = str(msg)
        msg_style = "red"
        msg = f"{get_formatted_prefix(f_time=get_formatted_time(), f_agent=self.agent, f_type='INFO')} {msg}"
        self.console.print(msg, style=msg_style)

    def error(self, msg):
        msg = str(msg)
        msg_style = "red"
        msg = f"{get_formatted_prefix(f_time=get_formatted_time(), f_agent=self.agent, f_type='ERROR')} {msg}"
        self.console.print(msg, style=msg_style)

    def warn(self, msg):
        msg = str(msg)
        msg_style = "yellow"
        msg = f"{get_formatted_prefix(f_time=get_formatted_time(), f_agent=self.agent, f_type='WARN')} {msg}"
        self.console.print(msg, style=msg_style)

    def custom_msg(self, msg=None, color=None, tag=None):
        if msg is not None and color is not None and tag is not None:
            msg = str(msg)
            msg_style = str(color)
            msg = f"{get_formatted_prefix(f_time=get_formatted_time(), f_agent=self.agent, f_type=tag)} {msg}"
            self.console.print(msg, style=msg_style)
        else:
            self.warn("Arguments not defined in custom msg")
