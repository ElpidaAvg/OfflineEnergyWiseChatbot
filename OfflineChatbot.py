from sentence_transformers import SentenceTransformer, util
import tkinter as tk
from tkinter import scrolledtext

model = SentenceTransformer('all-MiniLM-L6-v2')

qa_pairs = [
    ("hello hi hey greetings γεια χαρά καλησπέρα",
     "Γεια σας! 💡 Μπορώ να σας δώσω έξυπνες συμβουλές για εξοικονόμηση ρεύματος και χρημάτων!"),

    ("save money economy cheaper bill εξοικονόμηση οικονομία λογαριασμός",
     "Μικρές αλλαγές στην καθημερινότητα μπορούν να μειώσουν σημαντικά τον λογαριασμό ρεύματος."),

    ("light lights lamp led λάμπες φωτισμός",
     "Οι λάμπες LED καταναλώνουν έως και 80% λιγότερη ενέργεια από τις παλιές λάμπες πυρακτώσεως"),

    ("air condition ac cooling heating κλιματιστικό",
     "Ρυθμίστε το κλιματιστικό στους 26°C το καλοκαίρι και 20-21°C τον χειμώνα για καλύτερη οικονομία."),

    ("water heater boiler θερμοσίφωνας μπάνιο",
     "Ο θερμοσίφωνας συνήθως χρειάζεται μόνο 15-20 λεπτά πριν το μπάνιο"),

    ("standby tv console charger πρίζα συσκευές",
     "Οι συσκευές σε standby συνεχίζουν να καταναλώνουν ρεύμα. Κλείνετε πολύπριζα και φορτιστές όταν δεν χρησιμοποιούνται."),

    ("washing machine laundry πλυντήριο ρούχα",
     "Προτιμήστε πλύσιμο στους 30°C και γεμάτο πλυντήριο για χαμηλότερη κατανάλωση."),

    ("dishwasher πλυντήριο πιάτων",
     "Το eco πρόγραμμα στο πλυντήριο πιάτων καταναλώνει λιγότερο ρεύμα και νερό."),

    ("fridge refrigerator ψυγείο κατάψυξη",
     "Η ιδανική θερμοκρασία ψυγείου είναι 4°C και κατάψυξης -18°C για οικονομία και σωστή λειτουργία."),

    ("oven kitchen cooking φούρνος μαγείρεμα",
     "Μην ανοίγετε συχνά τον φούρνο όσο ψήνεται το φαγητό γιατί χάνεται θερμότητα."),

    ("computer laptop gaming pc",
     "Τα laptops καταναλώνουν πολύ λιγότερο ρεύμα από τους σταθερούς υπολογιστές."),

    ("charger phone battery κινητό φόρτιση",
     "Βγάζετε τον φορτιστή από την πρίζα όταν δεν φορτίζει συσκευή"),

    ("night tariff νυχτερινό",
     "Αν έχετε νυχτερινό ρεύμα, χρησιμοποιείτε ενεργοβόρες συσκευές τις βραδινές ώρες."),

    ("summer heat καλοκαίρι ζέστη",
     "Κλείνετε παντζούρια και κουρτίνες τις ζεστές ώρες για να μειώνεται η χρήση κλιματιστικού."),

    ("winter cold χειμώνας θέρμανση",
     "Χρησιμοποιήστε κουβέρτες και σωστή μόνωση για να μειώσετε τη θέρμανση."),

    ("smart tips tricks έξυπνα συμβουλές",
     "Ένα πολύπριζο με διακόπτη βοηθά να κλείνετε πολλές συσκευές μαζί και να γλιτώνετε ρεύμα."),

    ("solar panels φωτοβολταϊκά",
     "Τα φωτοβολταϊκά μπορούν να μειώσουν σημαντικά το κόστος ρεύματος μακροπρόθεσμα"),

    ("thanks thank you ευχαριστώ",
     "Παρακαλώ! Αν θέλετε, μπορώ να σας δώσω κι άλλες συμβουλές εξοικονόμησης."),

    ("coffee maker espresso καφετιέρα",
     "Κλείνετε την καφετιέρα αμέσως μετά τη χρήση για να μην καταναλώνει άσκοπα ρεύμα"),

    ("iron clothes σίδερο ρούχα",
     "Σιδερώνετε πολλά ρούχα μαζί για να αποφεύγετε συνεχές ζέσταμα του σίδερου."),

    ("microwave microwave oven φούρνος μικροκυμάτων",
     "Ο φούρνος μικροκυμάτων καταναλώνει λιγότερη ενέργεια από τον κανονικό φούρνο για μικρά γεύματα."),

    ("curtains windows παράθυρα κουρτίνες",
     "Οι χοντρές κουρτίνες βοηθούν να διατηρείται η θερμοκρασία του σπιτιού σταθερή."),

    ("wifi router internet ρούτερ",
     "Αν δεν χρησιμοποιείτε το internet τη νύχτα, μπορείτε να κλείνετε το router για εξοικονόμηση."),

    ("dryer στεγνωτήριο ρούχων",
     "Αφήστε τα ρούχα να στεγνώσουν φυσικά όταν υπάρχει καλός καιρός αντί για στεγνωτήριο."),

    ("eco mode οικονομική λειτουργία",
     "Οι λειτουργίες Eco στις συσκευές μειώνουν την κατανάλωση ρεύματος χωρίς μεγάλη διαφορά στην απόδοση."),

    ("vacation holiday λείπω διακοπές",
     "Πριν φύγετε διακοπές, βγάλτε από την πρίζα όσες συσκευές δεν χρειάζονται."),

    ("television netflix youtube τηλεόραση",
     "Μειώνοντας λίγο τη φωτεινότητα της τηλεόρασης μπορείτε να εξοικονομήσετε ενέργεια"),

    ("fan ανεμιστήρας",
     "Ο ανεμιστήρας καταναλώνει πολύ λιγότερο ρεύμα από το κλιματιστικό."),

    ("windows open ventilation αερισμός",
     "Αερίζετε το σπίτι νωρίς το πρωί ή αργά το βράδυ για να παραμένει πιο δροσερό."),

    ("full battery charging φόρτιση μπαταρία",
     "Μην αφήνετε συσκευές να φορτίζουν όλη νύχτα χωρίς λόγο."),

    ("energy class ενεργειακή κλάση",
     "Οι συσκευές ενεργειακής κλάσης A καταναλώνουν λιγότερο ρεύμα μακροπρόθεσμα."),

    ("gaming console playstation xbox",
     "Οι κονσόλες καταναλώνουν ρεύμα ακόμα και σε κατάσταση αναμονής."),

    ("electric heater αερόθερμο θερμάστρα",
     "Τα αερόθερμα καταναλώνουν πολύ ρεύμα — χρησιμοποιείτε τα μόνο όταν χρειάζεται."),

    ("smart home automation έξυπνο σπίτι",
     "Οι έξυπνες πρίζες βοηθούν να ελέγχετε καλύτερα την κατανάλωση ρεύματος."),

    ("sun natural light ήλιος φυσικό φως",
     "Εκμεταλλευτείτε το φυσικό φως της ημέρας αντί να ανάβετε λάμπες."),

    ("freezer ice πάγος κατάψυξη",
     "Η πολλή πάχνη στην κατάψυξη αυξάνει την κατανάλωση ρεύματος."),

    ("door fridge open πόρτα ψυγείου",
     "Μην αφήνετε την πόρτα του ψυγείου ανοιχτή για πολλή ώρα."),

    ("temperature thermostat θερμοστάτης",
     "Ακόμα και 1°C διαφορά στον θερμοστάτη μπορεί να επηρεάσει τον λογαριασμό ρεύματος."),

    ("led strip rgb φωτάκια",
     "Κλείνετε τα διακοσμητικά φωτάκια όταν δεν τα χρειάζεστε για να μειώνεται η κατανάλωση."),

    ("phone brightness φωτεινότητα κινητού",
     "Η χαμηλότερη φωτεινότητα σε κινητά και tablets βοηθά και στην οικονομία μπαταρίας"),

    ("air fryer φριτέζα αέρος",
     "Το air fryer συνήθως καταναλώνει λιγότερο ρεύμα από τον μεγάλο φούρνο."),

    ("kettle water boiler βραστήρας",
     "Βράζετε μόνο όσο νερό χρειάζεστε για να μην σπαταλάτε ενέργεια."),

    ("balcony shade σκίαση μπαλκόνι",
     "Οι τέντες και η σκίαση μειώνουν τη θερμότητα μέσα στο σπίτι το καλοκαίρι."),

    ("dust cleaning καθαρισμός φίλτρα",
     "Τα καθαρά φίλτρα σε κλιματιστικά και συσκευές βοηθούν στη χαμηλότερη κατανάλωση."),

    ("sleep mode ύπνος υπολογιστή",
     "Βάλτε τον υπολογιστή σε sleep mode όταν δεν τον χρησιμοποιείτε για αρκετή ώρα."),

    ("multiple devices πολλές συσκευές",
     "Αποφύγετε να λειτουργούν πολλές ενεργοβόρες συσκευές ταυτόχρονα."),

    ("heater door πόρτες θέρμανση",
     "Κλείνετε τις πόρτες στα δωμάτια για να διατηρείται καλύτερα η θερμοκρασία."),

    ("energy monitor μετρητής κατανάλωσης",
     "Ένας μετρητής κατανάλωσης βοηθά να δείτε ποιες συσκευές καίνε περισσότερο ρεύμα."),

    ("bath shower μπάνιο ντους",
     "Ένα σύντομο ντους καταναλώνει λιγότερη ενέργεια και νερό"),

    ("eco washing οικονομικό πλύσιμο",
     "Τα οικολογικά προγράμματα πλύσης διαρκούν περισσότερο αλλά καίνε λιγότερο ρεύμα."),

    ("small appliances μικροσυσκευές",
     "Οι μικροσυσκευές που μένουν μόνιμα στην πρίζα αυξάνουν την κατανάλωση."),

    ("kitchen extractor απορροφητήρας",
     "Κλείνετε τον απορροφητήρα μόλις τελειώσετε το μαγείρεμα."),

    ("electric oven προθέρμανση",
     "Δεν χρειάζεται πάντα μεγάλη προθέρμανση στον φούρνο."),

    ("laptop battery μπαταρία laptop",
     "Αποσυνδέετε το laptop από το ρεύμα όταν έχει φορτίσει πλήρως."),

    ("printer εκτυπωτής",
     "Οι εκτυπωτές σε standby συνεχίζουν να καταναλώνουν ενέργεια."),

    ("charger unplug βγάλτε φορτιστή",
     "Ακόμα και χωρίς κινητό, ο φορτιστής τραβά μικρή ποσότητα ρεύματος."),

    ("sun drying άπλωμα ρούχων",
     "Το άπλωμα ρούχων στον ήλιο μειώνει τη χρήση στεγνωτηρίου"),

    ("ac maintenance συντήρηση κλιματιστικού",
     "Η σωστή συντήρηση του κλιματιστικού βοηθά στην καλύτερη απόδοση."),

    ("thermos hot water θερμός",
     "Χρησιμοποιήστε θερμός για να κρατάτε ζεστό νερό χωρίς επαναλαμβανόμενο βράσιμο."),

    ("gaming pc rgb lights",
     "Τα έντονα RGB φώτα σε gaming setups αυξάνουν ελαφρώς την κατανάλωση."),

    ("refrigerator space ψυγείο γεμάτο",
     "Ένα σωστά γεμάτο ψυγείο διατηρεί καλύτερα τη θερμοκρασία."),

    ("fridge hot food ζεστό φαγητό",
     "Μην βάζετε ζεστό φαγητό απευθείας στο ψυγείο."),

    ("extension cord πολύπριζο",
     "Τα πολύπριζα με διακόπτη βοηθούν να κλείνετε εύκολα πολλές συσκευές."),

    ("desktop computer σταθερός υπολογιστής",
     "Κλείνετε την οθόνη όταν δεν χρησιμοποιείτε τον υπολογιστή."),

    ("energy saving mode λειτουργία εξοικονόμησης",
     "Ενεργοποιήστε τη λειτουργία εξοικονόμησης σε κινητά και υπολογιστές."),

    ("water temperature θερμοκρασία νερού",
     "Η πολύ υψηλή θερμοκρασία νερού αυξάνει άσκοπα την κατανάλωση."),

    ("room ventilation δωμάτιο αερισμός",
     "Ο σωστός αερισμός βοηθά να μειώνεται η ανάγκη για κλιματισμό."),

    ("induction stove επαγωγική εστία",
     "Οι επαγωγικές εστίες είναι πιο αποδοτικές ενεργειακά από τις παλιές ηλεκτρικές."),

    ("freezer organization οργάνωση κατάψυξης",
     "Η σωστή οργάνωση στην κατάψυξη μειώνει τον χρόνο που μένει ανοιχτή."),

    ("smart thermostat έξυπνος θερμοστάτης",
     "Ένας έξυπνος θερμοστάτης βοηθά στον καλύτερο έλεγχο της κατανάλωσης."),

    ("electric car φόρτιση αυτοκινήτου",
     "Η φόρτιση ηλεκτρικού αυτοκινήτου τη νύχτα μπορεί να είναι οικονομικότερη."),

    ("window insulation μόνωση παραθύρων",
     "Η καλή μόνωση στα παράθυρα μειώνει απώλειες θερμότητας."),

    ("old appliances παλιές συσκευές",
     "Οι πολύ παλιές συσκευές καταναλώνουν συνήθως περισσότερο ρεύμα."),

    ("fan cleaning καθάρισμα ανεμιστήρα",
     "Οι καθαροί ανεμιστήρες λειτουργούν πιο αποδοτικά."),

    ("dishwasher full load γεμάτο πλυντήριο",
     "Βάζετε σε λειτουργία το πλυντήριο πιάτων μόνο όταν γεμίσει."),

    ("ac doors windows πόρτες παράθυρα",
     "Κλείνετε πόρτες και παράθυρα όταν λειτουργεί το κλιματιστικό."),

    ("natural cooling φυσική δροσιά",
     "Τα φυτά στο μπαλκόνι βοηθούν να μειώνεται η θερμοκρασία του χώρου"),

    ("electric toothbrush οδοντόβουρτσα",
     "Αποσυνδέετε τη βάση φόρτισης όταν δεν χρειάζεται."),
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
                              "Ask about ... (e.g., '...').\n")
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
                                      "Ask about recipes (e.g., ).\n")
        self.chat_area.config(state = "disabled")

def main():
    root = tk.Tk()
    app = ChatbotUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()