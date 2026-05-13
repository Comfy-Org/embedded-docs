> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxTextToVideoNode/fr.md)

Voici la traduction en français de la documentation technique du nœud ComfyUI, en respectant toutes les règles spécifiées :

Génère des vidéos de manière synchrone à partir d'un prompt et de paramètres optionnels via l'API MiniMax. Ce nœud crée un contenu vidéo à partir de descriptions textuelles en se connectant au service texte-vers-vidéo de MiniMax.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt_text` | STRING | Oui | - | Prompt textuel pour guider la génération vidéo |
| `model` | COMBO | Non | "T2V-01"<br>"T2V-01-Director" | Modèle à utiliser pour la génération vidéo (par défaut : "T2V-01") |
| `seed` | INT | Non | 0 à 18446744073709551615 | La graine aléatoire utilisée pour créer le bruit (par défaut : 0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | La vidéo générée à partir du prompt d'entrée |

---
**Source fingerprint (SHA-256):** `bdbd8f9defc4c626f07b36c1ba9859155fa90a2d7ef9a491c30dac4d003d39be`
