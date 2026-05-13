> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageToVideoWithAudio/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI :

Le nœud Kling Image (Première image) vers Vidéo avec Audio utilise le modèle d'IA Kling pour générer une courte vidéo à partir d'une seule image de départ et d'une invite textuelle. Il crée une séquence vidéo qui commence par l'image fournie et peut éventuellement inclure un son généré par l'IA pour accompagner les visuels.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model_name` | COMBO | Oui | `"kling-v2-6"` | La version spécifique du modèle d'IA Kling à utiliser pour la génération vidéo. |
| `start_frame` | IMAGE | Oui | - | L'image qui servira de première image de la vidéo générée. L'image doit faire au moins 300x300 pixels et avoir un rapport hauteur/largeur compris entre 1:2,5 et 2,5:1. |
| `prompt` | STRING | Oui | - | Invite textuelle positive. Décrit le contenu vidéo que vous souhaitez générer. L'invite doit contenir entre 1 et 2500 caractères. |
| `mode` | COMBO | Oui | `"pro"` | Le mode opérationnel pour la génération vidéo. |
| `duration` | COMBO | Oui | `5`<br>`10` | La durée de la vidéo à générer, en secondes. |
| `generate_audio` | BOOLEAN | Non | - | Lorsqu'il est activé, le nœud génère un son pour accompagner la vidéo. Lorsqu'il est désactivé, la vidéo sera silencieuse. (par défaut : True) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `video` | VIDEO | Le fichier vidéo généré, qui peut inclure du son selon l'entrée `generate_audio`. |

---
**Source fingerprint (SHA-256):** `f161eedbc5d780805e3d0ca32b6be94cc78afcd2749e065c032ea20991b782fc`
