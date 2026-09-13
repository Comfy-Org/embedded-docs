# Kling Texte en Vidéo avec Audio

Le nœud Kling Text to Video with Audio génère une courte vidéo à partir d’une description textuelle. Il envoie une requête au service Kling AI, qui traite le prompt et renvoie un fichier vidéo. Le nœud peut également générer un audio d’accompagnement pour la vidéo en fonction du texte.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_name` | Le modèle d’IA spécifique à utiliser pour la génération vidéo. | COMBO | Oui | `"kling-v2-6"` |
| `prompt` | Invite textuelle positive. La description utilisée pour générer la vidéo. Doit comporter entre 1 et 2500 caractères. | STRING | Oui | - |
| `mode` | Le mode opératoire pour la génération vidéo. | COMBO | Oui | `"pro"` |
| `aspect_ratio` | Le rapport largeur-hauteur souhaité pour la vidéo générée. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | La durée de la vidéo en secondes. | COMBO | Oui | `5`<br>`10` |
| `generate_audio` | Contrôle si un audio est généré pour la vidéo. Lorsqu’activé, l’IA crée du son en fonction du prompt (par défaut : `True`). | BOOLEAN | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoWithAudio/fr.md)

---
**Source fingerprint (SHA-256):** `ddd2f3c1799abac067a05f3f5d6442ad4fe023d2f4f9afbde2894ca66854977e`
