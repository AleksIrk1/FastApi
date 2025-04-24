import enum

class StatusOrder(str, enum.Enum):
    in_progress = 'В процессе'
    sending = 'Отправлен'
    delivered = 'Доставлен'
    closed = 'Закрыт'
    cancelled = 'Отменен'

    
