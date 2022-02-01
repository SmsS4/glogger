import logging

reset = "\x1b[0m"
FORMATS = {
    logging.DEBUG: "\u001b[38;5;247m",
    logging.WARNING: "\u001b[38;5;11m",
    logging.ERROR: "\u001b[38;5;196m",
    logging.CRITICAL: "\u001b[38;5;52m",
    logging.INFO: "\u001b[38;5;46m",
}
COLORS_INFO = [
    46,
    27,
    44,
    93,
    118,
    128,
    123,
    131,
    134,
    30,
    47,
    64,
    68,
    138,
    141,
    147,
    151,
    155,
    165,
    175,
    183,
    192,
    201,
    210,
]


def paint(name: str, color_scheme: int, text: str) -> str:
    if color_scheme == logging.INFO:
        color = "\u001b[38;5;" + str(COLORS_INFO[hash(name) % len(COLORS_INFO)]) + "m"
    else:
        color = FORMATS[color_scheme]

    return f"{color}{text}{reset}"


class LoggerFormatter(logging.Formatter):
    name_just = 20
    level_just = 40

    def __init__(
        self, spliter: str, show_func: bool = False, emphasize_from: int = logging.ERROR
    ):
        """
        Args:
            spliter: string used to split different part of the log text
                     should be a single character

            show_func: wether or not show function_name in log text
                       its false by default meaning it only shows line number

            emphasize_from: make whole log line colorized should the log_level be greater
                            than `emphasize_from`
        """
        super().__init__()
        self.spliter = spliter
        self.show_func = show_func
        self.emphasize_from = emphasize_from

    def format(self, record: logging.LogRecord) -> str:
        time = self.formatTime(record, self.datefmt)
        split_3 = self.spliter * 3
        log_text = (
            f"{split_3}[{time}]{split_3}[{record.levelname}]".ljust(
                self.level_just, self.spliter
            )
            + f"{split_3}[{record.name}]{split_3}".ljust(self.name_just, self.spliter)
            + f" {record.getMessage()} :: ({record.filename}:"
            + (f"{record.lineno}", record.funcName)[self.show_func]
            + ")"
        )
        if record.levelno >= self.emphasize_from:
            return paint(record.name, record.levelno, log_text)
        return log_text.replace(
            record.levelname, paint(record.name, record.levelno, record.levelname)
        )


def get_logger(
    name: str,
    level: int = logging.INFO,
    split: str = "=",
    show_func: bool = False,
    emphasize_from: int = logging.ERROR,
) -> logging.Logger:
    stdout_h = logging.StreamHandler()
    stdout_h.setLevel(level)
    stdout_h.setFormatter(LoggerFormatter(split, show_func, emphasize_from))

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(stdout_h)

    return logger
