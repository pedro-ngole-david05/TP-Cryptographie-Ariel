def hachage_ariel(message):
    """
    Algorithme de hachage personnalisé - TP Cryptographie
    Signature : Ariel
    """
    # 1. État initial (Offset FNV)
    h = 0x811C9DC5
    PREMIER = 0x01000193
    
    for caractere in message:
        # Transformation en valeur numérique
        valeur_char = ord(caractere)
        
        # Mixage (XOR)
        h = h ^ valeur_char
        
        # Diffusion par multiplication
        h = (h * PREMIER) % (2**64)
        
        # Décalage circulaire (Rotation de 5 bits vers la gauche)
        h = ((h << 5) | (h >> 59)) % (2**64)

    return f"{h:016x}"

# --- ZONE DE TEST / SCAN ---
if __name__ == "__main__":
    print("--- Bienvenue dans l'outil de hachage d'Ariel ---")
    texte_utilisateur = input("Entrez la chaîne de caractères à hacher : ")
    
    resultat = hachage_ariel(texte_utilisateur)
    
    print("-" * 45)
    print(f"Texte : {texte_utilisateur}")
    print(f"Hash  : {resultat}")
    print("-" * 45)
