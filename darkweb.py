import pyfiglet
from colorama import Fore, Back, init
import time
import webbrowser
import subprocess 

init(autoreset=True)

# Text to display
big_text = "MABESTE UNITED"
small_text = "Home of powerful scripts"
loading_text = "Loading..."
welcome_text = "Welcome"
please = 'SUPPORT US BY SUBSCRIBING TO OUR YOUTUBE CHANNEL'
subscribe_text = "Thank you for subscribing"
questions_text = "If you have any questions please join our group"
join_text = "Thank you for joining"
IG = "https://instagram.com/thee_mastercard"
darkweb_message = "Hi Hoodmaster, I'm using your social script. I need the darkweb key."
admin_number = "+254759492914"
whats = f"https://wa.me/{admin_number}?text={darkweb_message}"
#darkweb_message = "Hi Hoodmaster, im using your social script i need the darkweb key."
#admin_number = "+254759492914"
# Define gradient colors
colors = [Fore.BLUE, Fore.RED, Fore.LIGHTMAGENTA_EX]

# Function to print text with gradient colors
def print_gradient_text(text):
    color_step = 0
    for char in text:
        color = colors[color_step % len(colors)]
        print(f"{color}{char}", end="")
        color_step += 1
    print()

def wait_for_enter():
    input("Press Enter to continue...")

# Display the gradient text for "MABESTE UNITED"
print_gradient_text(big_text)


# Display the small text in green color
print(f"{Fore.GREEN}{small_text}")


# Loading animation
for _ in range(3):
    for _ in range(3):
        print(loading_text, end="\r")
        time.sleep(0.3)
    loading_text = " " + loading_text  # Shift the loading animation


# Display "Welcome"
print(f"{Fore.YELLOW}{welcome_text}")


# Display "Thank you for subscribing"
print(f"{Fore.CYAN}{subscribe_text}")

print(f'{Fore.RED}{please}')
# Opening a YouTube channel link
channel_link = "https://www.youtube.com/channel/UCnEoXr6-aJcJxbkuZVPxhNA"
webbrowser.open(channel_link)
subprocess.run(["bash", "-c", f"xdg-open '{channel_link}'"])

# Animated text for "Thank you for subscribing"
for _ in range(3):
    print(f"\r{subscribe_text}", end="")
    time.sleep(0.5)
    print(f"\r{' ' * len(subscribe_text)}", end="")
    time.sleep(0.5)
wait_for_enter()

# Display "If you have any questions please join our group"
print(f"{Fore.LIGHTMAGENTA_EX}{questions_text}")


# Loading animation
for _ in range(3):
    for _ in range(3):
        print(loading_text, end="\r")
        time.sleep(0.3)
    loading_text = " " + loading_text  # Shift the loading animation
    

# Open WhatsApp group link
whatsapp_link = "https://chat.whatsapp.com/CXBUcpY05gS9y3cAEAem3V"
webbrowser.open(whatsapp_link)
wait_for_enter()
subprocess.run(["bash", "-c", f"xdg-open '{whatsapp_link}'"])

# Display "Thank you for joining"
print(f"{Fore.MAGENTA}{join_text}")



import requests
import pyfiglet
from colorama import Fore, init
import webbrowser

init(autoreset=True)  # Initialize colorama

# Replace with your actual API key
api_key = None

# Mabeste United SMM API URL
api_url = "https://smmstore.com/api/v2"

# Function to open a URL in the browser
def open_url(url):
    webbrowser.open(url)

# Function to register or retrieve the API key
def get_api_key():
    global api_key
    if api_key is None:
        print(f'{Fore.RED}Welcome to Mabeste United SOCIAL MEDIA HACKING Services!')
        print(f"{Fore.BLUE}DARK WEB KEY NEEDED")
        print(f"{Fore.YELLOW}GET THE DARKWEB KEY FROM ADMIN CONTACT HIM NOW.")
        open_url("https://instagram.com/thee_mastercard")
        subprocess.run(["bash", "-c", f"xdg-open '{whats}'"])
        wait_for_enter()
        subprocess.run(["bash", "-c", f"xdg-open '{IG}'"])
        api_key = input("Enter your DARKWEB key: ")
        print("Thank you for registering! Your DARKWEB key has been saved for future use.")
        print('IF YOU DIDNT SIGNUP AND DONT HAVE A DARKWEB KEY IT WONT WORK CONTACT HOODMASTER TO OBTAIN A KEY')
        # xdg-open https://wa.me/+254759492914?text=Hi Hoodmaster I need the darkweb key for mabeste script
        subprocess.run(["bash", "-c", f"xdg-open '{whats}'"])
       #whats = "https://wa.me/254759492914?text=Hi%20Hoodmaster%2C%20I'm%20using%20your%20social%20script%20and%20I%20need%20the%20darkweb%20auth%20key%20%E2%80%93%20can%20you%20help%3F"


# Function to send an API request
def make_api_request(action, data=None):
    params = {"key": api_key, "action": action}
    if data:
        params.update(data)
    
    response = requests.get(api_url, params=params)
    return response.json()

# Function to retrieve a list of services
def retrieve_services():
    services = make_api_request("services")
    for service in services:
        print(f"Service ID: {service['service']}, Name: {service['name']}, Type: {service['type']}, Rate: ${service['rate']}")

# Function to add an order
def add_order():
    print('it can be found on the pdf or press 0 to see the list')
    print('its quite big i suggest you use the pdf instead')
    service_id = input("Enter the service ID: ")
    if service_id == '0':
        retrieve_services()
    link = input("Enter the link: ")
    quantity = input("Enter the quantity: ")
    runs = input("Enter the runs (optional): ")
    interval = input("Enter the interval in minutes (optional): ")
    
    data = {
        "service": service_id,
        "link": link,
        "quantity": quantity,
    }
    
    if runs:
        data["runs"] = runs
    
    if interval:
        data["interval"] = interval
    
    response = make_api_request("add", data)
    if "order" in response:
        print(f"Order placed successfully. Order ID: {response['order']}")

# Function to check the status of an order
def check_order_status():
    order_id = input("Enter the order ID: ")
    data = {"order": order_id}
    response = make_api_request("status", data)
    if "charge" in response:
        print(f"Order ID: {order_id}, Charge: ${response['charge']}, Status: {response['status']}, Remains: {response['remains']} {response['currency']}")

# Function to check the status of multiple orders
def check_multiple_order_status():
    order_ids = input("Enter order IDs separated by commas: ").split(',')
    data = {"orders": ",".join(order_ids)}
    responses = make_api_request("status", data)
    
    for order_id, response in responses.items():
        if "charge" in response:
            print(f"Order ID: {order_id}, Charge: ${response['charge']}, Status: {response['status']}, Remains: {response['remains']} {response['currency']}")
        else:
            print(f"Order ID: {order_id}, Error: {response['error']}")

# Function to create a refill for an order
def create_refill():
    order_id = input("Enter the order ID for the refill: ")
    data = {"order": order_id}
    response = make_api_request("refill", data)
    if "refill" in response:
        print(f"Refill created successfully. Refill ID: {response['refill']}")

# Function to get the refill status
def get_refill_status():
    refill_id = input("Enter the refill ID: ")
    data = {"refill": refill_id}
    response = make_api_request("refill_status", data)
    if "status" in response:
        print(f"Refill ID: {refill_id}, Status: {response['status']}")

# Function to check the user's balance
def check_user_balance():
    response = make_api_request("balance")
    if "balance" in response:
        print(f"Your balance: {response['balance']} {response['currency']}")
    else:
        print("Error: Internal error")

# Function to display the banner
def display_banner():
    banner = Fore.GREEN + pyfiglet.figlet_format("Mabeste United", font="slant")
    print(banner)

# Main menu
def main_menu():
    print(f"{Fore.RED}CHOOSE YOUR POISON🔥🔥🔥:")
    print("1. retrieve HackingIDs🔄")
    print("2. start Hacking ")
    print("3. Check the status of on going hacking")
    print("4. Check the status of multiple hackings")
    print("5. Create a refill for a hacking")
    print("6. Get the refill status")
    print("7. Check your balance")
    choice = input("Enter the option (1-7): ")
    print(f"{Fore.RED}WISE CHOICE😈😈")
    return choice

if __name__ == "__main__":
    display_banner()
    get_api_key()
    
    while True:
        choice = main_menu()
        if choice == '1':
            retrieve_services()
        elif choice == '2':
            add_order()
        elif choice == '3':
            check_order_status()
        elif choice == '4':
            check_multiple_order_status()
        elif choice == '5':
            create_refill()
        elif choice == '6':
            get_refill_status()
        elif choice == '7':
            check_user_balance()
        else:
            print("Invalid choice.Please enter a valid optioN")
