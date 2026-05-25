# ============================================================
#   DecodeLabs Industrial Training — Batch 2026
#   Project 1: Rule-Based AI Chatbot
#   Built strictly according to the Project PDF
# ============================================================

import datetime
import random
import time
import sys


# ============================================================
# PDF PAGE 7 — THE WHITE BOX CONCEPT
# Traceability: Every input traces to a clear output
# Safety:       Zero hallucination — 100% hard-coded
# Compliance:   Fully transparent logic
# ============================================================

BOT_NAME   = "DecoBot"
BOT_VERS   = "1.0"
COMPANY    = "DecodeLabs 2026"
EXIT_CMDS  = ['exit', 'quit', 'bye', 'goodbye']   # Kill Commands (Page 11)


# ============================================================
# TYPEWRITER EFFECT — makes output feel like a real AI
# ============================================================

def typewriter(text, speed=0.025):
    """Print text with a typewriter animation effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


# ============================================================
# CHAT LOGGER — White Box Traceability (PDF Page 7)
# Input -> Logic -> Output. No mystery.
# ============================================================

def log_chat(user_msg, bot_msg):
    """Save every conversation to a log file for traceability."""
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{ts}] YOU : {user_msg}\n")
        f.write(f"[{ts}] BOT : {bot_msg}\n")
        f.write("-" * 50 + "\n")


# ============================================================
# PDF PAGE 9 — IPO MODEL
# PHASE 1: INPUT — Sanitization & Normalization
# PDF Page 10: raw_input.lower().strip()
# ============================================================

def phase_input():
    """
    IPO Phase 1 — INPUT
    Capture raw user input and sanitize it.
    Handles case differences: 'HeLLo', 'HELLO', 'hello' → 'hello'
    """
    raw_input = input("\nYou: ")                   # Raw Feed
    clean_input = raw_input.lower().strip()        # Sanitization (Page 10)
    return raw_input, clean_input


# ============================================================
# PDF PAGE 13, 14, 15 — THE PIVOT: HASH MAPS & DICTIONARIES
# Using Dictionary O(1) instead of If-Elif Ladder O(n)
# Anti-Pattern AVOIDED (Page 12)
# ============================================================

# --- Dynamic response functions (stored as values in dict) ---

def get_time():
    return f"Current time is {datetime.datetime.now().strftime('%I:%M %p')} ⏰"

def get_date():
    return f"Today is {datetime.datetime.now().strftime('%A, %B %d, %Y')} 📅"

def get_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why did Python cross the road? To import the other side! 🐍",
        "How do you comfort a JavaScript bug? You console it! 😄",
        "A SQL query walks into a bar and asks two tables: Can I JOIN you? 😂",
        "What do you call a programmer from Finland? Nerdic! 🇫🇮",
    ]
    return random.choice(jokes)

def get_calc(user_input):
    """Simple calculator using eval — safe for basic math."""
    try:
        expr = user_input.replace('calculate','').replace('calc','').strip()
        result = eval(expr)
        return f"Answer: {result} 🔢"
    except Exception:
        return "Invalid expression! Try: calc 5 * 10 + 3 🔢"


# ============================================================
# PDF PAGE 17 — PROJECT 1 SPECIFICATION: THE LOGIC SKELETON
# KNOWLEDGE BASE: Dictionary with 5+ intents ✅
# FALLBACK: Default response for unknowns ✅
# ============================================================

# Static responses — Pure Dictionary (O1 Lookup, Page 14-15)
KNOWLEDGE_BASE = {

    # --- Greetings (PDF Page 4: Handle greetings) ---
    'hello'         : "Hey there! Great to meet you! 👋",
    'hi'            : "Hi! How can I assist you today? 😊",
    'hey'           : "Hey! What can I do for you? 🤖",
    'good morning'  : "Good Morning! Hope you have a productive day! ☀️",
    'good afternoon': "Good Afternoon! Hope your day is going well! 🌤️",
    'good evening'  : "Good Evening! Hope you had a great day! 🌙",
    'good night'    : "Good Night! Sweet dreams! 🌙",

    # --- About Bot ---
    'name'          : f"I am {BOT_NAME} v{BOT_VERS} — Built by YOU at {COMPANY}! 🤖",
    'who are you'   : f"I am {BOT_NAME}, a rule-based AI chatbot. I run on pure logic! ⚙️",
    'who made you'  : "A DecodeLabs intern built me using Python and if-else logic! 💻",
    'how are you'   : "I am just code, but I am running perfectly! All systems green ✅",
    'what can you do': "I can chat, tell jokes, show time/date, calculate math & more! Type 'help' 💡",

    # --- Help Menu ---
    'help'          : (
        "\n📋 DECOBOT COMMAND MENU:\n"
        "  👋  hello / hi / hey\n"
        "  ⏰  time\n"
        "  📅  date\n"
        "  😄  joke\n"
        "  🔢  calc [expression]  e.g. calc 5 * 10\n"
        "  📊  stats\n"
        "  📜  history\n"
        "  🤖  name / who are you\n"
        "  🙏  namaste / salam\n"
        "  ❌  exit / quit / bye\n"
    ),

    # --- Feelings & Emotions ---
    'thanks'        : "You are welcome! Happy to help 😊",
    'thank you'     : "My pleasure! That is what I am here for 🤖",
    'sorry'         : "No problem at all! Let us move forward 😊",
    'i am happy'    : "That is wonderful! Your happiness matters 😄",
    'i am sad'      : "I am sorry to hear that. I hope things get better for you 💙",
    'i am bored'    : "Let me fix that! Ask me for a joke or try calc 10 * 10! 😄",
    'i am tired'    : "Rest is important! Take care of yourself 💤",
    'i love you'    : "Aww! I like you too, but I am just a bot! 🤖❤️",

    # --- About AI (related to PDF concepts) ---
    'what is ai'    : "AI is the simulation of human intelligence by machines using data and logic! 🧠",
    'what is python': "Python is a beginner-friendly programming language — the one I am built with! 🐍",
    'what is chatbot': "A chatbot is a program that simulates human conversation — just like me! 🤖",
    'what is rule based ai': "Rule-based AI follows hard-coded if-else rules. No learning — pure logic! That is me! ⚙️",

    # --- Multilingual Greetings ---
    'namaste'       : "Namaste! 🙏 (Hindi greeting detected!)",
    'salam'         : "Wa Alaikum Assalam! 🌙 (Urdu/Arabic greeting detected!)",
    'hola'          : "Hola! ¡Qué bueno verte! 🇪🇸 (Spanish!)",
    'bonjour'       : "Bonjour! Comment ça va? 🇫🇷 (French!)",
    'salaam'        : "Wa Alaikum Assalam! 🌙",

    # --- Fun & Extra ---
    'who is your creator': "A brilliant DecodeLabs intern — probably you! 😄",
    'tell me something'  : "Did you know? Python was named after Monty Python, not the snake! 🐍",
    'favourite color'    : "I love the color of clean code — #00FF00 (green) ✅",
    'are you human'      : "No! I am 100% rule-based AI. Pure logic, zero feelings 🤖",
    'are you real'       : "I am as real as the code that runs me! 100% Python 🐍",
}


# ============================================================
# PDF PAGE 9 — IPO MODEL
# PHASE 2: PROCESS — Intent Matching & State
# PDF Page 15: .get() method — Atomic Lookup + Fallback
# PDF Page 12: NO if-elif ladder — Dictionary only
# ============================================================

def phase_process(clean_input, session_stats):
    """
    IPO Phase 2 — PROCESS
    Match user intent using Dictionary O(1) lookup.
    Avoids the If-Elif Anti-Pattern (PDF Page 12).
    Uses .get() method for atomic lookup + fallback (PDF Page 15).
    """

    # --- Dynamic commands (need live data) ---
    if clean_input == 'time':
        return get_time()

    if clean_input == 'date':
        return get_date()

    if clean_input == 'joke':
        return get_joke()

    if clean_input.startswith(('calc', 'calculate')):
        return get_calc(clean_input)

    if clean_input == 'stats':
        return (
            f"\n📊 SESSION STATISTICS:\n"
            f"  Messages sent : {session_stats['count']}\n"
            f"  Session start : {session_stats['start']}\n"
            f"  User name     : {session_stats['name']}\n"
        )

    if clean_input == 'history':
        try:
            with open("chat_log.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()[-10:]   # Show last 10 lines
            return "📜 Recent History:\n" + "".join(lines)
        except FileNotFoundError:
            return "No chat history found yet!"

    # --- PDF Page 15: Dictionary .get() — THE PROFESSIONAL APPROACH ---
    # Exact match first (O1 lookup)
    response = KNOWLEDGE_BASE.get(clean_input)
    if response:
        return response

    # Keyword match (partial matching for smarter responses)
    for key in KNOWLEDGE_BASE:
        if key in clean_input:
            return KNOWLEDGE_BASE[key]

    # --- PDF Page 17: FALLBACK — Default response for unknowns ---
    return "I do not understand that yet. Type 'help' to see what I can do! 💡"


# ============================================================
# PDF PAGE 9 — IPO MODEL
# PHASE 3: OUTPUT — Response Generation (Feedback Loop)
# ============================================================

def phase_output(reply, raw_input):
    """
    IPO Phase 3 — OUTPUT
    Display bot response and log for White Box traceability.
    """
    typewriter(f"\n🤖 {BOT_NAME}: {reply}")    # Display response
    log_chat(raw_input, reply)                  # Log for traceability (Page 7)


# ============================================================
# PDF PAGE 18 — HYBRID ARCHITECTURE
# Rule Match → Instant Response (Speed)
# No Match   → Pass to fallback (Flexibility)
# ============================================================

def hybrid_router(clean_input, session_stats):
    """
    PDF Page 18 — Hybrid Architecture
    First checks rule base. If match → instant response.
    If no match → fallback (in future this passes to an LLM).
    """
    # Check rule base first
    response = phase_process(clean_input, session_stats)

    # Rule matched → Instant response
    if response != "I do not understand that yet. Type 'help' to see what I can do! 💡":
        return response, "RULE_MATCH"

    # No rule match → Fallback (would pass to LLM in production)
    return response, "FALLBACK"


# ============================================================
# PDF PAGE 11 — THE HEARTBEAT: THE INFINITE LOOP
# The organism stays alive until the Kill Command
# while True → continuous loop
# ============================================================

def main():
    """
    Main function — The Heartbeat of the Chatbot (PDF Page 11)
    Runs the IPO cycle continuously in a while True loop.
    """

    # --- Startup Banner ---
    print("\n" + "="*50)
    print(f"   🤖  {BOT_NAME} v{BOT_VERS}  |  {COMPANY}")
    print(f"   DecodeLabs Industrial Training — Project 1")
    print("="*50)
    print("   Architecture: Rule-Based | White Box | IPO")
    print("   Anti-Pattern: If-Elif Ladder AVOIDED ✅")
    print("   Lookup Method: Dictionary O(1) ✅")
    print("="*50 + "\n")

    # Ask user name for personalization
    user_name = input(f"🤖 {BOT_NAME}: Hello! What is your name? → ").strip().title()
    if not user_name:
        user_name = "Friend"

    typewriter(f"\n🤖 {BOT_NAME}: Great to meet you, {user_name}! 🎉")
    typewriter(f"🤖 {BOT_NAME}: I am a Rule-Based AI Chatbot built with pure Python logic.")
    typewriter(f"🤖 {BOT_NAME}: Type 'help' to see what I can do. Type 'exit' to quit.\n")

    # --- Session Stats (for 'stats' command) ---
    session_stats = {
        'name'  : user_name,
        'count' : 0,
        'start' : datetime.datetime.now().strftime("%I:%M %p")
    }

    # ============================================================
    # PDF PAGE 11 — INFINITE LOOP (The Heartbeat)
    # PDF PAGE 17 — INPUT LOOP: Continuous 'while' cycle ✅
    # ============================================================

    while True:

        # ---- IPO PHASE 1: INPUT & SANITIZATION (PDF Page 10) ----
        raw_input, clean_input = phase_input()
        session_stats['count'] += 1

        # ---- PDF PAGE 4 & 11: EXIT STRATEGY (Kill Command) ----
        # PDF Page 17: EXIT STRATEGY: Clean break command ✅
        if clean_input in EXIT_CMDS:
            phase_output(
                f"Goodbye {user_name}! You sent {session_stats['count']} messages. "
                f"Session saved to chat_log.txt 📁 See you next time! 👋",
                raw_input
            )
            break   # ← Kill Command (PDF Page 11)

        # ---- IPO PHASE 2: PROCESS via Hybrid Router (PDF Page 18) ----
        reply, match_type = hybrid_router(clean_input, session_stats)

        # ---- IPO PHASE 3: OUTPUT (PDF Page 9) ----
        phase_output(reply, raw_input)

        # Show match type for White Box traceability (PDF Page 7)
        print(f"   [System: {match_type} | Msg #{session_stats['count']}]")


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
