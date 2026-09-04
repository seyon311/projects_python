import tkinter as tk
import pandas as pd
from textblob import TextBlob

# Use 3.12 python

try: 
    df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print("Error: the file 'imdb_top_1000.csv' was not found."); raise SystemExit

genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs})

def topwin():
    global toproot, name, genre_entry, mood_entry, rating_entry

    toproot = tk.Tk()
    toproot.title("Genre selection")
    toproot.geometry("800x300")

    name = entername.get()

    msg2 = tk.Label(toproot, text="Great to meet you " + name + " Let's find you the perfect movie!", font=("Arial", 12))
    msg2.pack(pady=20)
    msg3 = tk.Label(toproot, text="Which of these genres would you like? (check your terminal)")
    msg3.pack(pady=20)

    for i, g in enumerate(genres, 1): print(f"{i}. {g}")

    genre_entry = tk.Entry(toproot, width=35)
    genre_entry.pack(pady=10)
    genre_submit = tk.Button(toproot, text="Submit", command=topwin2)
    genre_submit.pack(pady=10)

def topwin2():

    global mood_entry

    msg4 = tk.Label(toproot, text="How are you feeling today? (Describe your mood)", font=("Arial", 12))
    msg4.pack(pady=20)
    mood_entry = tk.Entry(toproot, width=35)
    mood_entry.pack(pady=10)
    mood_submit = tk.Button(toproot, text="Submit", command=topwin3)
    mood_submit.pack(pady=10)

def topwin3():
    global rating_entry

    msg5 = tk.Label(toproot, text="What is your minimum IMDB rating? (7.6-9.3) or type 'skip' to skip this step.", font=("Arial", 12))
    msg5.pack(pady=20)
    rating_entry = tk.Entry(toproot, width=35)
    rating_entry.pack(pady=10)
    rating_submit = tk.Button(toproot, text="Submit", command=topwin4)
    rating_submit.pack(pady=10)

def topwin4():
    genre = genre_entry.get()
    mood = mood_entry.get()
    rating_input = rating_entry.get()

    if rating_input.lower() == "skip":
        rating = None
    else:
        try:
            rating = float(rating_input)
            if not (7.6 <= rating <= 9.3):
                raise ValueError
        except ValueError:
            print("Invalid rating input. Please enter a number between 7.6 and 9.3 or 'skip'.")
            return

    recs = recommend(genre, mood, rating)
    show(recs, name)

def recommend(genre=None, mood=None, rating=None, n=5):
    d = df
    if genre: d = d[d["Genre"].str.contains(genre, case=False, na=False)]
    if rating is not None: d = d[d["IMDB_Rating"] >= rating]
    if d.empty: return "No suitable movie recommendations found."
    d, need_nonneg, out = d.sample(frac=1).reset_index(drop=True), bool(mood), []
    for _, r in d.iterrows():
        ov = r.get("Overview")
        if pd.isna(ov): continue
        pol = TextBlob(ov).sentiment.polarity
        if (not need_nonneg) or pol >= 0:
            out.append((r["Series_Title"], pol))
            if len(out) == n: break
    return out if out else "No suitable movie recommendations found."

def show(recs, name):
    if isinstance(recs, str):
        print(recs)
    else:
        print(f"\n🍿 AI-Analyzed Movie Recommendations for {name}:")
        for i, (t, p) in enumerate(recs, 1):
            print(f"{i}. 🎥 {t} (Polarity: {p:.2f})")

root = tk.Tk()
root.title("Movie recommendations")
root.geometry("900x400")

welcomemsg = tk.Label(root, text="Hello! Welcome to to your personal Movie recommendations centre! Please enter your name down below.", font=("Arial", 12))
welcomemsg.pack(pady=20)

entername = tk.Entry(root, width=35)
entername.pack(pady=10)

submitbtn = tk.Button(root, text="Submit", command=topwin)
submitbtn.pack(pady=10)

root.mainloop()