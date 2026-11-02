# استقرار BAT-PANEL V2

## پیش‌نیاز

- Ubuntu 22.04 یا 24.04، amd64
- Docker و Docker Compose
- دسترسی root

## نصب

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/batvin/sonson/main/install-v2.sh)
```

پنل فقط روی 127.0.0.1 در دسترس است. از تونل SSH استفاده کنید:

```bash
ssh -L 8000:127.0.0.1:8000 root@SERVER_IP
```
