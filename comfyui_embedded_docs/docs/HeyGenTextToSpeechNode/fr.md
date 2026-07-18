# HeyGenTextToSpeechNode

Générer un fichier audio de synthèse vocale à partir de texte en utilisant le moteur Starfish TTS de HeyGen. Ce nœud inclut les voix les plus populaires de HeyGen dans 17 langues.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `text` | Texte à synthétiser (jusqu'à 5000 caractères). La parole générée doit durer au moins 1 seconde. | STRING | Oui | 1 à 5000 caractères |
| `voice` | Voix à utiliser (sélectionnée parmi les voix Starfish les plus populaires de HeyGen). | STRING | Oui | Plusieurs options disponibles |
| `custom_voice_id` | Identifiant de voix HeyGen optionnel. Lorsqu'il est défini, remplace la voix sélectionnée ci-dessus. La voix doit prendre en charge le moteur Starfish. | STRING | Non | Tout identifiant de voix HeyGen valide |
| `speed` | Multiplicateur de vitesse de parole (par défaut : 1.0). | FLOAT | Non | 0,5 à 2,0 (pas : 0,05) |
| `ssml` | Traiter le texte comme un balisage SSML (pour les pauses, l'emphase et le contrôle de la prononciation) (par défaut : Faux). | BOOLEAN | Non | Vrai / Faux |
| `seed` | N'est pas envoyé à HeyGen ; modifiez-le pour forcer une nouvelle exécution (par défaut : 42). | INT | Non | 0 à 2147483647 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `AUDIO` | Le fichier audio de synthèse vocale généré à partir du texte d'entrée. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenTextToSpeechNode/fr.md)

---
**Source fingerprint (SHA-256):** `82300626657db8ab16e96ae96b7dfe3291b77bf75efec35971dc772e5123cce7`
