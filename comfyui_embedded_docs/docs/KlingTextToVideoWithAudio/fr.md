# Kling Texte en Vidéo avec Audio

Le nœud Kling Text to Video with Audio génère une courte vidéo à partir d'une description textuelle. Il envoie une requête au service d'IA Kling, qui traite la consigne et renvoie un fichier vidéo. Le nœud peut également générer un fichier audio d'accompagnement pour la vidéo en fonction du texte.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model_name` | Le modèle d'IA spécifique à utiliser pour la génération vidéo. | COMBO | Oui | `"kling-v2-6"` |
| `prompt` | Consigne textuelle positive. La description utilisée pour générer la vidéo. Doit contenir entre 1 et 2500 caractères. | STRING | Oui | - |
| `mode` | Le mode opérationnel pour la génération vidéo. | COMBO | Oui | `"pro"` |
| `aspect_ratio` | Le rapport largeur/hauteur souhaité pour la vidéo générée. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | La durée de la vidéo en secondes. | COMBO | Oui | `5`<br>`10` |
| `generate_audio` | Contrôle si un fichier audio est généré pour la vidéo. Lorsqu'il est activé, l'IA crée un son basé sur la consigne. (par défaut : `True`) | BOOLEAN | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoWithAudio/fr.md)

---
**Source fingerprint (SHA-256):** `eff4549816c347a090e2f6e8ae8ba832bd2c5b7aef7c729b51c9d72b7a814d5a`
