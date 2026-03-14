"""
fetch_rates.py
──────────────
Fetches live exchange rates from the free ExchangeRate-API
and saves them to rates.json, which index.html reads automatically.

HOW TO USE:
  1. Install requests:   pip install requests
  2. Run this script:    python fetch_rates.py
  3. Open index.html in your browser — it now shows live rates!

You can also run this on a schedule (e.g. once a day) to keep
your rates up to date.

API used: https://open.er-api.com (free, no API key needed)
"""

import json
import requests
from datetime import datetime


# ── Currencies we care about ──────────────────────────────────────────────────
CURRENCIES = ["USD", "TJS", "RUB", "UZS", "KZT", "AFN", "AZN", "EUR", "GBP", "TRY", "AED", "SAR", "INR", "CNY", "JPY"]

# ── Free API endpoint (USD base, no key needed) ───────────────────────────────
API_URL = "https://open.er-api.com/v6/latest/USD"


def fetch_rates():
    """Fetch live rates from the API and return as a dict."""
    print("Fetching live exchange rates...")

    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("result") != "success":
            print("API returned an error:", data)
            return None

        all_rates = data["rates"]

        # Filter to only the currencies we need
        filtered = {}
        for currency in CURRENCIES:
            if currency in all_rates:
                filtered[currency] = all_rates[currency]
                print(f"  ✓ {currency}: {all_rates[currency]}")
            else:
                print(f"  ✗ {currency}: not found in API response")

        # Add a timestamp so the app can show "last updated"
        filtered["_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M UTC")

        return filtered

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection.")
        return None
    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def save_rates(rates, filename="rates.json"):
    """Save rates dict to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(rates, f, indent=2, ensure_ascii=False)
    print(f"\nSaved to {filename} ✓")


def main():
    print("=" * 48)
    print("  Central Asia Currency Converter")
    print("  Rate Fetcher")
    print("=" * 48)
    print()

    rates = fetch_rates()

    if rates:
        save_rates(rates)
        print(f"\nTimestamp : {rates['_updated']}")
        print(f"Currencies: {len(rates) - 1} loaded")
        print()
        print("Done! Open index.html in your browser to see live rates.")
    else:
        print("\nFailed to fetch rates. Check your internet connection.")
        print("The app will use its built-in fallback rates instead.")


if __name__ == "__main__":
    main()
