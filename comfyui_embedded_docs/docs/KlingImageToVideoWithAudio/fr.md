# Kling Image (première image) vers vidéo avec audio

Voici la traduction en français de la documentation du nœud ComfyUI :

Le nœud Kling Image (Première image) vers Vidéo avec Audio utilise le modèle d'IA Kling pour générer une courte vidéo à partir d'une seule image de départ et d'une invite textuelle. Il crée une séquence vidéo qui commence par l'image fournie et peut éventuellement inclure un son généré par l'IA pour accompagner les visuels.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model_name` | La version spécifique du modèle d'IA Kling à utiliser pour la génération vidéo. | COMBO | Oui | `"kling-v2-6"` |
| `image_de_départ` | L'image qui servira de première image de la vidéo générée. L'image doit faire au moins 300x300 pixels et avoir un rapport hauteur/largeur compris entre 1:2,5 et 2,5:1. | IMAGE | Oui | - |
| `invite` | Invite textuelle positive. Décrit le contenu vidéo que vous souhaitez générer. L'invite doit contenir entre 1 et 2500 caractères. | STRING | Oui | - |
| `mode` | Le mode opérationnel pour la génération vidéo. | COMBO | Oui | `"pro"` |
| `durée` | La durée de la vidéo à générer, en secondes. | COMBO | Oui | `5`<br>`10` |
| `générer_audio` | Lorsqu'il est activé, le nœud génère un son pour accompagner la vidéo. Lorsqu'il est désactivé, la vidéo sera silencieuse. (par défaut : True) | BOOLEAN | Non | - |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `video` | Le fichier vidéo généré, qui peut inclure du son selon l'entrée `générer_audio`. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageToVideoWithAudio/fr.md)

---
**Source fingerprint (SHA-256):** `f161eedbc5d780805e3d0ca32b6be94cc78afcd2749e065c032ea20991b782fc`
