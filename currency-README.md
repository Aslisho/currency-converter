# 💱 Central Asia Currency Converter

A fast, clean currency converter focused on **Central Asian currencies** — Tajik Somoni, Russian Ruble, Uzbek Sum, and Kazakh Tenge — alongside USD, EUR, GBP, and CNY.

Built with pure HTML, CSS, JavaScript, and a Python script for fetching live rates.

🌐 **[Live Demo →](https://aslisho.github.io/currency-converter)**

---

## Preview

![Currency Converter Screenshot](screenshot.png)

---

## Features

- 💰 **8 currencies** — TJS, RUB, UZS, KZT, USD, EUR, GBP, CNY
- ⚡ **Instant conversion** — updates as you type
- 🔄 **Swap button** — flip from/to currencies in one click
- 📊 **Rates grid** — see all rates vs USD at a glance
- 🐍 **Python rate fetcher** — run `fetch_rates.py` for live rates
- 📱 **Fully responsive** — works on mobile and desktop
- 🌐 **Works offline** — built-in fallback rates if no internet

---

## Getting Started

### Option 1 — Just open it
Download all files and open `index.html` in your browser.

### Option 2 — Get live rates
```bash
git clone https://github.com/your-username/currency-converter.git
cd currency-converter
pip install requests
python fetch_rates.py
# Then open index.html
```

---

## Project Structure

```
currency-converter/
├── index.html        ← Main app (HTML + CSS + JS)
├── fetch_rates.py    ← Python: fetches live rates → saves rates.json
├── rates.json        ← Exchange rates data
└── README.md         ← This file
```

---

## How It Works

1. `fetch_rates.py` calls a free exchange rate API (open.er-api.com)
2. Saves the 8 currencies we need to `rates.json`
3. `index.html` reads `rates.json` and shows live rates
4. Falls back to built-in rates if offline

---

## Supported Currencies

| Code | Currency       | Region         |
|------|----------------|----------------|
| TJS  | Tajik Somoni   | 🇹🇯 Tajikistan  |
| RUB  | Russian Ruble  | 🇷🇺 Russia      |
| UZS  | Uzbek Sum      | 🇺🇿 Uzbekistan  |
| KZT  | Kazakh Tenge   | 🇰🇿 Kazakhstan  |
| USD  | US Dollar      | 🇺🇸 USA         |
| EUR  | Euro           | 🇪🇺 EU          |
| GBP  | British Pound  | 🇬🇧 UK          |
| CNY  | Chinese Yuan   | 🇨🇳 China       |

---

## Roadmap

- [ ] Auto-refresh rates every hour
- [ ] Conversion history chart
- [ ] More Central Asian currencies (AFN, TMT, AZN)
- [ ] Dark mode toggle
- [ ] PWA support

---

## License

MIT — free to use, modify, and distribute.

*Built by [Aslisho] · Dushanbe, Tajikistan*
