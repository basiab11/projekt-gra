from flask import Flask, render_template, request
import random
app=Flask(__name__)

dzialania=[
    ("1*1", 1),
    ("2*2", 4),
    ("3*3", 9),
    ("4*4", 16),
    ("5*5", 25),
    ("6*6", 36),
    ("7*7", 49),
    ("8*8", 64),
    ("9*9", 81),
    ("10*10", 100),
    ("11*11", 121),
    ("12*12", 144),
    ("13*13", 169),
    ("14*14", 196),
    ("15*15", 225),
    ("16*16", 256),
    ("17*17", 289),
    ("18*18", 324),
    ("19*19", 361),
    ("20*20", 400)
]

dzialania_l = dzialania[:10]
dzialania_s = dzialania[10:20]
dzialania_t = dzialania 


def generuj_karty(lista_par, ilosc_par):
    wybrane=random.sample(lista_par, ilosc_par)

    karty=[]
    idx = 0 

    for para in wybrane:
        dzialanie = para[0]
        wynik = para[1]

        karta_dzialanie = {
            "typ": "dzialanie",
            "tekst": str(dzialanie),
            "id": idx
        }

        karta_wynik = {
            "typ":"wynik",
            "tekst": str(wynik),
            "id":idx
        }

        karty.append(karta_dzialanie)
        karty.append(karta_wynik)

        idx += 1 

    random.shuffle(karty)
    return karty, wybrane
    
def generowanie_kart1(level):
    if level =="latwy":
        pair_count = 4
        size = 4
        pula = dzialania_l
    elif level=="sredni":
        pair_count=6
        size = 6
        pula=dzialania_s
    elif level=="trudny":
        pair_count=8
        size = 8 
        pula=dzialania_t
    else:
        return [],{}, 0
    
    cards, pairs = generuj_karty(pula, pair_count)
    return cards, pairs, size


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        level=request.form.get('difficulty')
        cards, pairs, size = generowanie_kart1(level)
        return render_template("index.html", cards=cards, pairs=pairs, level=level, size = size)
    cards, pairs, size = generowanie_kart1("latwy")
    return render_template("index.html", cards=cards, pairs=pairs, level="latwy")

if __name__ =="__main__":
    app.run(debug=True, port=5002)
