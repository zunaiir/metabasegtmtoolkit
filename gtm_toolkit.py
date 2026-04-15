#!/usr/bin/env python3
"""
Metabase GTM Toolkit
Your personal AI-powered go-to-market assistant.


USAGE:
  python3 gtm_toolkit.py
"""

import os
import sys


# ─── Helpers ──────────────────────────────────────────────────────────────────

def check_api_key():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("\n⚠️  ANTHROPIC_API_KEY not set.")
        print("   Get your key at: https://console.anthropic.com")
        print("   Then run: echo 'export ANTHROPIC_API_KEY=your_key' >> ~/.zshrc && source ~/.zshrc\n")
        sys.exit(1)

def print_header():
    print("\n╔══════════════════════════════════════╗")
    print("║        Metabase GTM Toolkit          ║")
    print("╚══════════════════════════════════════╝")

def print_menu():
    print("\nWhat would you like to do?\n")
    print("  1  →  Pre-Call Research Brief")
    print("  2  →  Personalized Cold Email Writer   (coming soon)")
    print("  3  →  Call Notes → CRM Summary         (coming soon)")
    print()
    print("  q  →  Quit")
    print()


# ─── Tools ────────────────────────────────────────────────────────────────────

def run_brief_generator():
    """Run the pre-call research brief tool."""
    try:
        from brief_generator import generate_brief, save_as_docx
    except ImportError:
        print("\n❌ Could not find brief_generator.py — make sure it's in the same folder as this file.\n")
        return

    print("\n── Pre-Call Research Brief ──────────────────\n")

    company_name  = input("Company name:   ").strip()
    if not company_name:
        print("Company name is required.")
        return

    website_url   = input("Website URL:    ").strip()
    contact_name  = input("Contact name:   ").strip()
    contact_title = input("Contact title:  ").strip()

    print(f"\n⏳ Researching {company_name}...")
    print("   → Generating brief with Claude...\n")

    try:
        brief = generate_brief(company_name, website_url, contact_name, contact_title)
    except Exception as e:
        print(f"❌ Error: {e}\n")
        return

    print("─" * 50)
    print(brief)
    print("─" * 50)

    desktop     = os.path.join(os.path.expanduser("~"), "Desktop")
    safe_name   = company_name.replace("/", "").strip()
    folder_path = os.path.join(desktop, safe_name)
    os.makedirs(folder_path, exist_ok=True)

    filepath = os.path.join(folder_path, "brief.docx")
    save_as_docx(brief, filepath)

    print(f"\n✅ Saved to Desktop → {safe_name} → brief.docx")
    print("   Open it in Word or drag it into Google Docs.\n")


def coming_soon(tool_name):
    print(f"\n🚧  {tool_name} is coming soon.\n")


# ─── Main loop ────────────────────────────────────────────────────────────────

def main():
    check_api_key()
    print_header()

    while True:
        print_menu()
        choice = input("Enter a number: ").strip().lower()

        if choice == "1":
            run_brief_generator()
        elif choice == "2":
            coming_soon("Personalized Cold Email Writer")
        elif choice == "3":
            coming_soon("Call Notes → CRM Summary")
        elif choice in ("q", "quit", "exit"):
            print("\nGo make data accessible. 📊\n")
            break
        else:
            print("\n  Please enter 1, 2, 3, or q.\n")

        input("Press Enter to return to the menu...")
        print_header()


if __name__ == "__main__":
    main()
