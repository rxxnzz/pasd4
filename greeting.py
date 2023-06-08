import datetime

def greeting():
    current_time = datetime.datetime.now()
    current_hour = current_time.hour

    if current_hour < 11:
        waktu = "Pagi"
    elif current_hour < 15:
        waktu = "Siang"
    elif current_hour < 18 :
        waktu = "Sore"
    else:
        waktu = "Malam"

    return waktu