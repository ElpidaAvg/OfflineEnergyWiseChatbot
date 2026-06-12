from sentence_transformers import SentenceTransformer, util
import tkinter as tk
from tkinter import scrolledtext

model = SentenceTransformer('all-MiniLM-L6-v2')

qa_pairs = [
    ("hello hi hey greetings",
     "Hello! I can give you smart tips to save electricity and money!"),

    ("save money economy cheaper bill",
     "Small changes in your daily routine can significantly reduce your electricity bill."),

    ("light lights lamp led",
     "LED bulbs consume up to 80% less energy than traditional incandescent bulbs."),

    ("air condition ac cooling heating",
     "Set your air conditioner to 26°C in summer and 20-21°C in winter for better energy savings."),

    ("water heater boiler shower",
     "The water heater usually needs only 15-20 minutes before taking a shower."),

    ("standby tv console charger socket devices",
     "Devices in standby mode continue to consume electricity. Turn off power strips and unplug chargers when not in use."),

    ("washing machine laundry clothes",
     "Prefer washing at 30°C with a full load for lower energy consumption."),

    ("dishwasher",
     "The eco program on a dishwasher uses less electricity and water."),

    ("fridge refrigerator freezer",
     "The ideal refrigerator temperature is 4°C and the freezer should be set to -18°C for efficiency and proper operation."),

    ("oven kitchen cooking",
     "Avoid opening the oven frequently while cooking because heat escapes."),

    ("computer laptop gaming pc",
     "Laptops consume much less electricity than desktop computers."),

    ("charger phone battery charging",
     "Unplug the charger when it is not charging a device."),

    ("night tariff",
     "If you have a night electricity tariff, use energy-intensive appliances during nighttime hours."),

    ("summer heat",
     "Keep shutters and curtains closed during the hottest hours to reduce air conditioning use."),

    ("winter cold heating",
     "Use blankets and proper insulation to reduce heating needs."),

    ("smart tips tricks advice",
     "A power strip with a switch helps you turn off multiple devices at once and save electricity."),

    ("solar panels",
     "Solar panels can significantly reduce electricity costs in the long term."),

    ("thanks thank you",
     "You're welcome! If you'd like, I can give you more energy-saving tips."),

    ("coffee maker espresso",
     "Turn off the coffee machine immediately after use to avoid unnecessary energy consumption."),

    ("iron clothes",
     "Iron multiple clothes at once to avoid repeated heating of the iron."),

    ("microwave microwave oven",
     "A microwave oven usually consumes less energy than a conventional oven for small meals."),

    ("curtains windows",
     "Thick curtains help maintain a stable indoor temperature."),

    ("wifi router internet",
     "If you do not use the internet at night, you can turn off the router to save electricity."),

    ("dryer clothes dryer",
     "Let clothes dry naturally when the weather is good instead of using a dryer."),

    ("eco mode energy saving mode",
     "Eco modes on appliances reduce electricity consumption with little impact on performance."),

    ("vacation holiday away",
     "Before leaving for vacation, unplug devices that do not need to stay connected."),

    ("television netflix youtube tv",
     "Reducing your TV's brightness slightly can help save energy."),

    ("fan",
     "A fan consumes much less electricity than an air conditioner."),

    ("windows open ventilation",
     "Ventilate your home early in the morning or late in the evening to keep it cooler."),

    ("full battery charging",
     "Do not leave devices charging overnight unnecessarily."),

    ("energy class",
     "Energy class A appliances consume less electricity in the long run."),

    ("gaming console playstation xbox",
     "Game consoles consume electricity even in standby mode."),

    ("electric heater fan heater",
     "Electric fan heaters consume a lot of electricity—use them only when necessary."),

    ("smart home automation",
     "Smart plugs help you better monitor and control electricity consumption."),

    ("sun natural light",
     "Take advantage of natural daylight instead of turning on lights."),

    ("freezer ice",
     "Excess frost in the freezer increases electricity consumption."),

    ("door fridge open",
     "Do not leave the refrigerator door open for long periods."),

    ("temperature thermostat",
     "Even a 1°C change on the thermostat can affect your electricity bill."),

    ("led strip rgb lights",
     "Turn off decorative lights when not needed to reduce energy consumption."),

    ("phone brightness",
     "Lower screen brightness on phones and tablets also helps save battery power."),

    ("air fryer",
     "An air fryer usually consumes less electricity than a conventional oven."),

    ("kettle water boiler",
     "Boil only the amount of water you need to avoid wasting energy."),

    ("balcony shade",
     "Awnings and shading help reduce indoor heat during summer."),

    ("dust cleaning filters",
     "Clean filters in air conditioners and appliances help reduce energy consumption."),

    ("sleep mode computer",
     "Put your computer into sleep mode when not using it for an extended period."),

    ("multiple devices",
     "Avoid running multiple high-energy appliances at the same time."),

    ("heater door",
     "Keep room doors closed to better maintain indoor temperature."),

    ("energy monitor",
     "An energy monitor helps identify which appliances consume the most electricity."),

    ("bath shower",
     "A short shower uses less energy and water."),

    ("eco washing economical washing",
     "Eco washing programs take longer but consume less electricity."),

    ("small appliances",
     "Small appliances left permanently plugged in increase electricity consumption."),

    ("kitchen extractor hood",
     "Turn off the kitchen extractor hood as soon as you finish cooking."),

    ("electric oven preheating",
     "A long preheating time is not always necessary for the oven."),

    ("laptop battery",
     "Disconnect the laptop from power once it is fully charged."),

    ("printer",
     "Printers in standby mode continue to consume electricity."),

    ("charger unplug",
     "Even without a phone connected, a charger still draws a small amount of electricity."),

    ("sun drying clothes drying",
     "Drying clothes in the sun reduces the need for a clothes dryer."),

    ("ac maintenance air conditioner maintenance",
     "Proper air conditioner maintenance helps improve efficiency."),

    ("thermos hot water",
     "Use a thermos to keep water hot instead of boiling it repeatedly."),

    ("gaming pc rgb lights",
     "Bright RGB lighting in gaming setups slightly increases electricity consumption."),

    ("refrigerator space full fridge",
     "A properly filled refrigerator maintains its temperature more efficiently."),

    ("fridge hot food",
     "Do not place hot food directly into the refrigerator."),

    ("extension cord power strip",
     "Power strips with switches make it easy to turn off multiple devices."),

    ("desktop computer",
     "Turn off the monitor when you are not using the computer."),

    ("energy saving mode",
     "Enable energy-saving mode on phones and computers."),

    ("water temperature",
     "Excessively high water temperatures unnecessarily increase energy consumption."),

    ("room ventilation",
     "Proper ventilation helps reduce the need for air conditioning."),

    ("induction stove",
     "Induction cooktops are more energy-efficient than older electric stoves."),

    ("freezer organization",
     "Proper freezer organization reduces the time the door stays open."),

    ("smart thermostat",
     "A smart thermostat helps improve control of energy consumption."),

    ("electric car charging",
     "Charging an electric car at night may be more economical."),

    ("window insulation",
     "Good window insulation reduces heat loss."),

    ("old appliances",
     "Very old appliances usually consume more electricity."),

    ("fan cleaning",
     "Clean fans operate more efficiently."),

    ("dishwasher full load",
     "Run the dishwasher only when it is full."),

    ("ac doors windows",
     "Keep doors and windows closed while the air conditioner is running."),

    ("natural cooling",
     "Plants on the balcony can help reduce the surrounding temperature."),

    ("electric toothbrush",
     "Unplug the charging base when it is not needed."),
]

question_texts = [q for q, a in qa_pairs]
question_embeddings = model.encode(question_texts, convert_to_tensor=True)

# Similarity threshold — below this, the bot says it doesn't understand
THRESHOLD = 0.3


# Semantic matching replaces keyword matching
def get_response(user_input):
    input_embedding = model.encode(user_input, convert_to_tensor=True)
    similarities = util.cos_sim(input_embedding, question_embeddings)[0]
    best_idx = similarities.argmax().item()
    best_score = similarities[best_idx].item()

    if best_score < THRESHOLD:
        return best_score, "Sorry, I don't understand. Try asking about pasta, dessert, or vegan recipes!"

    return best_score, qa_pairs[best_idx][1]

class ChatbotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("500x600")
        self.root.configure(bg="#2E2E2E")

        # Title
        tk.Label(
            root, text="Chatbot", font=("Helvetica", 16, "bold"),
            fg="#FFFFFF", bg="#2E2E2E"
        ).pack(pady=10)

        # Chat area (scrollable)
        self.chat_area = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, height=20, width=50, font=("Arial", 11),
            bg="#3C3C3C", fg="#E0E0E0", insertbackground="white"
        )
        self.chat_area.pack(pady=10, padx=10)
        self.chat_area.insert(tk.END,
                              "Welcome to the Chatbot!\n"
                              "Ask about energy tips.\n")
        self.chat_area.config(state='disabled')

        # Input frame
        input_frame = tk.Frame(root, bg="#2E2E2E")
        input_frame.pack(pady=5)

        # Input field
        self.input_field = tk.Entry(
            input_frame, width=40, font=("Arial", 11), bg="#4A4A4A", fg="#FFFFFF",
            insertbackground="white"
        )
        self.input_field.pack(side=tk.LEFT, padx=5)
        self.input_field.bind("<Return>", self.send_message)

        tk.Button(input_frame, text = "Send", command = self.send_message, font = ("Arial", 11), bg = "#4CAF50", fg = "#FFFFFF", activebackground = "#45A049").pack(side = tk.LEFT, padx = 5)
        tk.Button(root, text = "Clear Chat", command = self.clear_chat, font = ("Arial", 11), bg = "#F44336", fg = "#FFFFFF", activebackground = "#D32F2F").pack(pady = 5)

    def send_message(self, event = None):
        user_input = self.input_field.get().strip()
        if not user_input:
            return
        score, response = get_response(user_input)
        self.chat_area.config(state = "normal")
        self.chat_area.insert(tk.END, f"\nYou: {user_input}\n")
        self.chat_area.insert(tk.END, f"Match confidence: {score:.2f}\n")
        self.chat_area.insert(tk.END, f"Bot: {response}\n")
        self.chat_area.config(state = "disabled")
        self.chat_area.see(tk.END)
        self.input_field.delete(0, tk.END)

    def clear_chat(self):
        self.chat_area.config(state = "normal")
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.insert(tk.END, "Welcome to the Chatbot!\n"
                                      "Ask about energy tips.\n")
        self.chat_area.config(state = "disabled")

def main():
    root = tk.Tk()
    app = ChatbotUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
