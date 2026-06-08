Voici la traduction en français de la documentation du nœud Moonvalley Marey Text to Video :

Le nœud Moonvalley Marey Texte vers Vidéo génère un contenu vidéo à partir de descriptions textuelles en utilisant l'API Moonvalley. Il prend une invite textuelle et la convertit en vidéo avec des paramètres personnalisables pour la résolution, la qualité et le style. Le nœud gère l'ensemble du processus, de l'envoi de la demande de génération au téléchargement de la vidéo finale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Description textuelle du contenu vidéo à générer | STRING | Oui | - |
| `negative_prompt` | Texte de l'invite négative (par défaut : liste étendue d'éléments exclus comme synthétique, coupure de scène, artefacts, bruit, etc.) | STRING | Non | - |
| `resolution` | Résolution de la vidéo de sortie (par défaut : "16:9 (1920 x 1080)") | STRING | Non | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)"<br>"21:9 (2560 x 1080)" |
| `prompt_adherence` | Échelle de guidage pour le contrôle de la génération (par défaut : 4.0) | FLOAT | Non | 1.0-20.0 |
| `seed` | Valeur de la graine aléatoire (par défaut : 9) | INT | Non | 0-4294967295 |
| `steps` | Étapes d'inférence (par défaut : 33) | INT | Non | 1-100 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo générée en sortie à partir de l'invite textuelle | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyTxt2VideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `3654043567d7aca3af741d706ee07a8d2e28dbeb4b5b8755514b790aa7c1bd41`
