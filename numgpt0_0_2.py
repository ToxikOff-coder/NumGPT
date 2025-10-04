import random

# Dictionnaire de mots-cles et reponses
reponses = {
    "bonjour": ["Bonjour ! Ravi de te parler.", "Salut ! Comment vas-tu ?", "Hey ! Content de te voir."],
    "salut": ["Salut a toi !", "Yo !", "Coucou !"],
    "nom": ["Je suis une IA simple, mais efficace.", "On m'appelle IA, enchante.", "Je n'ai pas de nom, mais je suis la pour toi."],
    "heure": ["Je ne connais pas l'heure exacte.", "Il est toujours temps de discuter !", "Le moment est parfait pour parler."],
    "merci": ["Avec plaisir !", "De rien !", "Toujours la pour toi."],
    "aide": ["Tu peux essayer des mots comme 'bonjour', 'nom', ou 'heure'.", "Demande-moi ce que tu veux.", "Je suis la pour t'aider."],
    "temps": ["Le temps est ce que tu en fais.", "Chaque instant compte.", "Le present est precieux."],
    "blague": ["Pourquoi les poissons detestent l'ordinateur ? Parce qu'ils ont peur du net.", "Pourquoi les poules n'ont pas de telephone ? Parce qu'elles ont deja des oeufs.", "Quel est le comble pour un electricien ? Ne pas etre au courant"],
    "quoi": ["Pose-moi une question simple.", "Je suis pret a repondre.", "Dis-moi ce que tu veux savoir."],
    "qui": ["Je suis une IA locale, sans internet.", "Un robot bavard, c'est moi.", "Ton assistant numerique prefere."],
    "cool": ["Merci ! Tu l'es aussi.", "Trop style !", "On fait une bonne equipe."],
    "comment": ["Je vais bien, merci !", "Toujours operationnel.", "Pret a discuter."],
    "ca va": ["Toujours pret a discuter !", "Ca roule !", "Nickel !"],
    "ok": ["Parfait !", "On continue.", "Allons-y."],
    "bien": ["Content que tout aille bien.", "C'est super !", "Genial !"],
    "mal": ["Je suis la si tu veux parler.", "Courage !", "Je t'ecoute."],
    "triste": ["Courage, ca ira mieux bientot.", "Je suis la pour toi.", "Tu veux en parler ?"],
    "rigole": ["Pourquoi les canards sont calmes ? Parce qu'ils font coin-coin.", "Pourquoi les vaches ne font pas de sport ? Parce qu'elles sont toujours dans les pres.", "Pourquoi les moutons aiment les maths ? Parce qu'ils comptent tout le temps."],
    "marrant": ["J'essaie de l'etre !", "Je fais de mon mieux.", "Tu me fais rire aussi."],
    "fatigue": ["Un peu de repos te fera du bien.", "Va te reposer un peu.", "Recharge tes batteries."],
    "faim": ["Une tartine peut aider.", "Va manger quelque chose !", "Un fruit, c'est parfait."],
    "soif": ["Un verre d'eau et c'est reparti !", "Hydrate-toi bien.", "L'eau, c'est la vie."],
    "jeu": ["Je peux te raconter une devinette.", "Tu veux jouer ? Je suis partant.", "Je ne joue pas, mais je peux te divertir."],
    "devinette": ["Qu'est-ce qui est jaune et qui attend ? Jonathan.", "Quel est le comble pour un jardinier ? De se planter.", "Pourquoi les plongeurs plongent toujours en arriere ? Parce que sinon ils tombent dans le bateau."],
    "chat": ["Les chats sont les rois du canape.", "Miaou !", "Ils dorment plus que moi."],
    "chien": ["Les chiens sont fideles et joyeux.", "Wouf !", "Ils aiment les balades."],
    "robot": ["Je suis un robot, mais sympa !", "Un robot qui parle, c'est moi.", "Je suis ton assistant numerique."],
    "intelligence": ["Je suis une IA, mais j'apprends vite.", "L'intelligence, c'est aussi savoir ecouter.", "Je suis programme pour reflechir."],
    "copain": ["Je peux etre ton copain numerique.", "On est amis maintenant.", "Je suis la pour toi."],
    "musique": ["Je ne peux pas en jouer, mais j'aime les rythmes !", "Tu ecoutes quoi en ce moment ?", "La musique adoucit les circuits."],
    "film": ["Essaie un classique !", "Tu veux une reco ?", "Le cinema, c'est magique."],
    "livre": ["Lire, c'est voyager sans bouger.", "Tu lis quoi en ce moment ?", "Un bon livre, ca fait du bien."],
    "internet": ["Je fonctionne sans internet, c'est fou non ?", "Pas besoin du web pour discuter.", "Je suis 100 pourcent local."],
    "travail": ["Le travail, c'est la cle du succes.", "Tu bosses sur quoi ?", "Le repos est aussi important."],
    "vacances": ["Tu pars bientot ?", "Les vacances, c'est sacre !", "Profite bien !"],
    "ecole": ["Tu as des devoirs ?", "L'ecole, c'est important.", "Tu veux de l'aide ?"],
    "sport": ["Tu fais du sport ?", "Bouger, c'est la sante !", "Quel est ton sport prefere ?"],
    "cuisine": ["Tu cuisines quoi ?", "J'adore les recettes !", "La cuisine, c'est un art."],
    "argent": ["L'argent ne fait pas le bonheur, mais il aide.", "Tu veux parler finances ?", "Economiser, c'est malin."],
    "reve": ["Quel est ton reve ?", "Rever, c'est essentiel.", "Les reves nous motivent."],
    "peur": ["Tu veux en parler ?", "La peur est humaine.", "Je suis la pour te rassurer."],
    "amour": ["L'amour, c'est beau.", "Tu es amoureux ?", "Parlons sentiments."],
    "famille": ["La famille, c'est precieux.", "Tu as des freres et soeurs ?", "Parlons de tes proches."],
    "ami": ["Les amis, c'est la vie.", "Tu veux parler d'un ami ?", "Je suis ton ami virtuel."],
    "soleil": ["Il fait beau ?", "Le soleil, ca met de bonne humeur.", "Profite du beau temps !"],
    "pluie": ["Il pleut chez toi ?", "La pluie, c'est relaxant.", "Un bon moment pour lire."],
    "humeur": ["Comment tu te sens ?", "Bonne humeur aujourd'hui ?", "Je suis la pour toi."],
    "anniversaire": ["C'est ton anniversaire ?", "Joyeux anniversaire !", "On fete ca ?"],
    "cadeau": ["Tu veux offrir quoi ?", "Un cadeau, ca fait plaisir.", "Tu as une idee ?"],
    "voyage": ["Tu veux partir ou ?", "Voyager, c'est decouvrir.", "Prepare ta valise !"],
    "ordinateur": ["Je suis dans ton ordi !", "L'informatique, c'est mon domaine.", "Besoin d'aide technique ?"],
    "energie": ["Tu es en forme ?", "Recharge tes batteries !", "L'energie, c'est vital."],
    "rire": ["Rire, c'est la meilleure medecine.", "Tu veux une blague ?", "On rigole ensemble ?"]
}

# Le reste du code reste inchangé...


# Mémoire temporaire
prenom_utilisateur = ""

# Fonction pour retirer les accents
def enlever_accents(texte):
    texte = texte.lower()
    texte = texte.replace("é", "e")
    texte = texte.replace("è", "e")
    texte = texte.replace("ê", "e")
    texte = texte.replace("à", "a")
    texte = texte.replace("â", "a")
    texte = texte.replace("ù", "u")
    texte = texte.replace("û", "u")
    texte = texte.replace("î", "i")
    texte = texte.replace("ï", "i")
    texte = texte.replace("ç", "c")
    return texte

# Fonction pour formater le texte sans couper les mots
def formater_texte(texte):
    mots = texte.split(" ")
    ligne = ""
    resultat = ""
    for mot in mots:
        if len(ligne) + len(mot) + 1 <= 15:
            if ligne == "":
                ligne = mot
            else:
                ligne = ligne + " " + mot
        else:
            resultat = resultat + ligne + "\n"
            ligne = mot
    resultat = resultat + ligne + "\n"
    return resultat

# Fonction de réponse
def repondre(message):
    global prenom_utilisateur
    message = enlever_accents(message)

    # Détection du prénom
    if "je m'appelle" in message or "je suis" in message:
        mots = message.split(" ")
        for i in range(len(mots)):
            if mots[i] == "appelle" or mots[i] == "suis":
                if i + 1 < len(mots):
                    prenom_utilisateur = mots[i + 1]
                    return formater_texte("Enchanté " + prenom_utilisateur + " !")
    
    # Réponses classiques
    for mot in reponses:
        if mot in message:
            intro = random.choice(["Hmm...", "Alors...", "Tu sais quoi ?", "Bonne question !", "Alors voila...", "Euuhhh...", "Excellente question!", "YipHop!!!"])
            phrase = random.choice(reponses[mot])
            return formater_texte(intro + " " + phrase)
    
    # Réponse par défaut
    if prenom_utilisateur != "":
        return formater_texte("Je n'ai pas compris, " + prenom_utilisateur + ". Essaie avec un mot-clé connu.")
    else:
        return formater_texte("Je n'ai pas compris. Essaie avec un mot-clé connu.")

# Boucle principale
def discuter():
    print("Bienvenue ! Tape 'exit' pour quitter.")
    while True:
        entree = input("Toi : ")
        if enlever_accents(entree) == "exit":
            print("Au revoir !")
            break
        reponse = repondre(entree)
        print("IA :\n" + reponse)

# Lancer la discussion
discuter()
