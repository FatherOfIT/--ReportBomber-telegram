import os
import time
import random
from telethon import TelegramClient, events
from telethon.tl.functions.messages import ReportRequest
from telethon.tl.types import InputPeerChannel, InputPeerUser, InputPeerChat
from telethon.errors import FloodWaitError, SessionPasswordNeededError

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = """
    ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗
    ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
    ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   
    ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   
    ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   
    ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
    """
    print("\033[91m" + banner + "\033[0m")
    print("\033[93m" + "=" * 60 + "\033[0m")
    print("\033[92m" + "Telegram Report Bomber v1.0" + "\033[0m")
    print("\033[93m" + "=" * 60 + "\033[0m")
    print("\033[96m" + "Created by: Mohammad Mehdi Haji Vand" + "\033[0m")
    print("\033[93m" + "=" * 60 + "\033[0m\n")

def print_menu():
    menu = """
    [1] API Settings
    [2] Start Report
    [3] Advanced Settings
    [4] Exit
    """
    print("\033[94m" + menu + "\033[0m")

def print_api_settings():
    print("\n\033[93m" + "=" * 60 + "\033[0m")
    print("\033[92m" + "API Settings" + "\033[0m")
    print("\033[93m" + "=" * 60 + "\033[0m")
    print("\033[95m" + "To get API ID and API Hash, visit:" + "\033[0m")
    print("\033[96m" + "https://my.telegram.org" + "\033[0m")
    print("\033[95m" + "1. Log in to your Telegram account" + "\033[0m")
    print("\033[95m" + "2. Go to API development tools" + "\033[0m")
    print("\033[95m" + "3. Create a new application" + "\033[0m")
    print("\033[95m" + "4. Copy your API ID and API Hash" + "\033[0m")
    print("\033[93m" + "=" * 60 + "\033[0m\n")

def print_advanced_settings():
    print("\n\033[93m" + "=" * 60 + "\033[0m")
    print("\033[92m" + "Advanced Settings" + "\033[0m")
    print("\033[93m" + "=" * 60 + "\033[0m")
    print("\033[95m" + "Speed Levels:" + "\033[0m")
    print("1. Ultra Fast (0.1-0.3s delay)")
    print("2. Fast (0.3-0.5s delay)")
    print("3. Normal (0.5-1.0s delay)")
    print("4. Slow (1.0-2.0s delay)")
    print("5. Ultra Slow (2.0-3.0s delay)")
    print("\033[93m" + "=" * 60 + "\033[0m\n")

async def main():
    clear_screen()
    print_banner()
    
    while True:
        print_menu()
        choice = input("\nSelect an option: ")
        
        if choice == "1":
            clear_screen()
            print_banner()
            print_api_settings()
            api_id = input("Enter API ID: ")
            api_hash = input("Enter API Hash: ")
            phone = input("Enter phone number (e.g., +1234567890): ")
            
        elif choice == "2":
            if 'api_id' not in locals():
                print("\033[91m" + "Please set up API settings first!" + "\033[0m")
                continue
                
            clear_screen()
            print_banner()
            print("\n\033[93m" + "=" * 60 + "\033[0m")
            print("\033[92m" + "Start Report" + "\033[0m")
            print("\033[93m" + "=" * 60 + "\033[0m")
            
            target = input("\nEnter target link or ID: ")
            try:
                # Try to convert target to integer if it's a numeric ID
                target = int(target)
            except ValueError:
                # If it's not a numeric ID, keep it as string (username/link)
                pass
            print("""
Select report reason:
1. Spam
2. Violence
3. Pornography
4. Child Abuse
5. Other
            """)
            reason = int(input("Select: "))
            count = int(input("Number of reports: "))
            
            try:
                client = TelegramClient('session_name', api_id, api_hash)
                await client.start(phone=phone)
                
                print(f"\n\033[92mStarting report for {target}\033[0m")
                print("\033[93m" + "=" * 60 + "\033[0m")
                
                entity = await client.get_entity(target)
                
                for i in range(count):
                    try:
                        await client(ReportRequest(
                            peer=entity,
                            reason=reason,
                            message=""
                        ))
                        print(f"\033[92mReport {i+1} of {count} sent successfully\033[0m")
                        time.sleep(random.uniform(1, 3))
                        
                    except FloodWaitError as e:
                        print(f"\033[91mRate limit. Waiting {e.seconds} seconds...\033[0m")
                        time.sleep(e.seconds)
                    except Exception as e:
                        print(f"\033[91mError sending report: {str(e)}\033[0m")
                        time.sleep(5)
                
                print("\n\033[92mOperation completed!\033[0m")
                await client.disconnect()
                
            except Exception as e:
                print(f"\033[91mError: {str(e)}\033[0m")
                
        elif choice == "3":
            clear_screen()
            print_banner()
            print_advanced_settings()
            
        elif choice == "4":
            print("\n\033[92mGoodbye!\033[0m")
            break
            
        else:
            print("\033[91mInvalid option!\033[0m")
        
        input("\nPress Enter to continue...")
        clear_screen()
        print_banner()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main()) 