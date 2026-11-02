# BAT-PANEL (sonson)

پنل مدیریتی BAT-PANEL با رابط کاربری فارسی راست‌چین، داشبورد Glassmorphism، تولید کانفیگ پروتکل‌های VPN و API مرکزی.

> **نسخه فعلی: 2.1**  
> داشبورد شیشه‌ای با انیمیشن، ساخت واقعی کانفیگ VLESS / VMess / Trojan / WireGuard / قالب OpenVPN، کنترل خودکار حجم و انقضا، و API گزارش ترافیک Agent پیاده‌سازی شده‌اند.

## نصب سریع (Ubuntu 22.04 / 24.04)

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/batvin/sonson/main/install-v2.sh)
```

نصب‌کننده این موارد را می‌پرسد:
- نام کاربری مدیر (۳ تا ۶۴ کاراکتر)
- رمز عبور مدیر (حداقل ۱۴ کاراکتر)
- پورت پنل (پیش‌فرض `۸۰۰۰`)

### پس از نصب

| مورد | مسیر / آدرس |
|------|-------------|
| داشبورد محلی | `http://127.0.0.1:PORT` |
| مستندات API | `http://SERVER-IP:PORT/api/docs` |
| اطلاعات ورود | `/root/batman-v2-credentials.txt` |
| دستور مدیریت | `bat-panel` |

پنل فقط روی `127.0.0.1` در دسترس است. برای دسترسی از کامپیوتر خود از تونل SSH استفاده کنید:

```bash
ssh -L 8000:127.0.0.1:8000 root@SERVER_IP
```

سپس مرورگر را روی `http://127.0.0.1:8000` باز کنید.

## منوی مدیریت ترمینال

```bash
bat-panel
```

امکانات: وضعیت، restart، stop، start، logs، backup، update از GitHub، تغییر پورت و تغییر مشخصات مدیر.

## قابلیت‌های نسخه ۲.۱

- UI شیشه‌ای (Glassmorphism) با انیمیشن‌های روان
- تولید لینک و کانفیگ **VLESS / VMess / Trojan**
- تولید فایل **WireGuard** واقعی و قالب **OpenVPN**
- قطع خودکار کاربر منقضی یا تمام‌حجم
- دکمه مشاهده و کپی کانفیگ داخل پنل
- API گزارش ترافیک برای Agent

## ساختار پروژه

```
├── install-v2.sh          # نصب‌کننده اصلی
├── v2/
│   ├── backend/           # API و منطق تولید کانفیگ
│   ├── web/               # داشبورد وب فارسی
│   ├── agent/             # Agent مرجع برای نودها
│   ├── scripts/bat-panel  # منوی مدیریتی ترمینال
│   ├── docker-compose.yml
│   └── DEPLOYMENT.md
```

## امنیت

- رمز عبور قوی انتخاب کنید.
- پورت پنل را فقط برای IPهای مورد اعتماد باز کنید.
- برای استفاده عمومی حتماً HTTPS (Nginx/Caddy) فعال کنید.
- فایل `.env` و اطلاعات ورود را محرمانه نگه دارید.

## پشتیبانی

تلگرام: [@shocavpnadmin](https://t.me/shocavpnadmin)

---
**BAT-PANEL** · ریپازیتوری: [batvin/sonson](https://github.com/batvin/sonson)
