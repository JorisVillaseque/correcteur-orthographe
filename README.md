# Correcteur de Texte avec GPT-3 et Python

## Description

Ce projet utilise GPT-3 d'OpenAI pour corriger automatiquement l'orthographe et la syntaxe d'un texte copié dans le presse-papier. Après la correction, le texte est automatiquement replacé dans le presse-papier et une notification est affichée pour indiquer que la correction a été effectuée.

## Prérequis

- Python 3.x
- Clé API OpenAI

## Installation

1. Clonez ce dépôt ou téléchargez-le manuellement sur votre ordinateur.

2. Installez les dépendances Python en utilisant pip :

    ```bash
    pip install openai pyperclip
    ```

3. Placez votre clé API OpenAI dans le script Python, en remplaçant la valeur de `openai.api_key`.

## Utilisation

1. Copiez le texte que vous souhaitez corriger dans le presse-papier.

2. Exécutez le script Python :

    ```bash
    python chemin_vers_le_script/script.py
    ```

3. Le texte corrigé sera automatiquement placé dans le presse-papier.

4. Une notification apparaîtra pour vous informer que le texte a été corrigé.

## Personnalisation

Vous pouvez personnaliser le script pour mieux répondre à vos besoins. Par exemple :

- Utilisez un autre modèle de GPT-3.
- Adaptez le prompt pour des corrections plus spécifiques.
- Intégrez le script dans un workflow automatisé ou attribuez-lui un raccourci clavier.

## Limitations

- Nécessite une connexion Internet pour accéder à l'API GPT-3.
- La confidentialité des données peut être une préoccupation, car le texte est envoyé à un service externe pour correction.

## Licence

Ce projet est sous licence MIT. 

---

N'hésitez pas à contribuer à ce projet ou à ouvrir des issues si vous rencontrez des problèmes.
