import subprocess

def wipe_android_system(ip):
    """يتصل بالجهاز عبر ADB Wi-Fi ويحذف النظام بالكامل"""
    try:
        # التحقق من توفر ADB
        subprocess.run(['adb', 'version'], check=True, capture_output=True)

        # الاتصال بالجهاز عن بعد
        subprocess.run(['adb', 'connect', f"{ip}:5555"], check=True)

        # جعل النظام قابل للكتابة
        subprocess.run(['adb', 'shell', 'su -c "mount -o remount,rw /system"'], check=True)

        # حذف ملفات النظام
        subprocess.run(['adb', 'shell', 'su -c "rm -rf /system/*"'], check=True)

        print(f"✅ تم حذف نظام التشغيل من الجهاز: {ip}")
    except subprocess.CalledProcessError as e:
        print(f"❌ خطأ أثناء التنفيذ: {e}")
    except FileNotFoundError:
        print("❌ لم يتم العثور على ADB! تأكد من تثبيته.")

# تشغيل الحذف مباشرة بمجرد تشغيل السكريبت
wipe_android_system("192.168.1.100")  # ضع IP الجهاز هنا