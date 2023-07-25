class Phone:
    IMEI = None      # 序列号
    producer = "HM"  # 厂商

    def call_by_4g(self):
        print("4g通话")


class Phone2022(Phone):
    face_id = "1001"

    def call_by_5g(self):
        print("5g通话")


phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
















