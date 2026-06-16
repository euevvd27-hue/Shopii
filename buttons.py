# buttons.py
from telethon import Button

# Links
BULLET_GROUP_LINK = "https://t.me/+K47dLZWv3xA5NTdl"
OFFICIAL_GROUP_LINK = "https://t.me/Froxtxchk"
DEV_LINK = "https://t.me/DARK_FROXT_73"

def get_main_keyboard():
    return [
        [
            Button.inline("🚪 Gates", b"gates_menu"),
            Button.inline("📦 Pricing", b"pricing_menu")
        ],
        [
            Button.url("💎 Owner", DEV_LINK),
            Button.inline("🔐 3DS Lookup", b"threeds_menu")
        ],
        [
            Button.url("👥 Official Group", OFFICIAL_GROUP_LINK)
        ]
    ]

def get_back_button(callback_data):
    return [[Button.inline("◀️ Back", callback_data)]]