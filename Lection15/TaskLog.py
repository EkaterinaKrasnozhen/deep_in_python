import logging
logging.basicConfig(
    filename="log.log", # от текущей директории перейти в log и создать log с расширением log (log/log.log)
    encoding='utf-8', # явно не передали 'w', и по умолчанию будет 'a' дозапись
    format='{asctime} {levelname} {funcName}->{lineno}: {msg}', # дата и время, уровень логирования, функция в котрой вызов был, номер строки в файле, сообщение внутри скобок
    style='{', # формат
    level=logging.WARNING # уровень предупреждения и дальше - ошибки и критичсике
)
