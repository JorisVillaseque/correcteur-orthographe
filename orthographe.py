import openai
import pyperclip
import subprocess

# Définissez la clé API OpenAI
openai.api_key = 'votre_clé_api_openai'

def send_notification(title, description):
    try:
        subprocess.run(["osascript", "-e", f'display notification "{description}" with title "{title}"'])
    except Exception as e:
        print(f"Failed to send notification: {e}")

def corriger_texte_avec_gpt3(texte):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": "Tu es un assistant de correction de texte."},
                {"role": "user", "content": f"Corrige l'orthographe et la syntaxe du texte suivant et renvoie-moi seulement le texte corrigé : '{texte}'"}
            ]
        )
    except openai.Error as e:
        print(f"Échec de la génération du texte : {e}")
        return ""
    else:
        return response['choices'][0]['message']['content'].strip()

if __name__ == "__main__":
    # Obtenez le texte du presse-papier
    texte_presse_papier = pyperclip.paste()
    
    if not texte_presse_papier:
        send_notification('Erreur', 'Aucun texte trouvé dans le presse-papier')
    else:
        # Obtenez le texte corrigé
        texte_corrige = corriger_texte_avec_gpt3(texte_presse_papier)
        
        # Mettez le texte corrigé dans le presse-papier
        pyperclip.copy(texte_corrige)
        
        # Affichez une notification de succès
        send_notification('Succès', 'Le texte a été corrigé avec succès')
