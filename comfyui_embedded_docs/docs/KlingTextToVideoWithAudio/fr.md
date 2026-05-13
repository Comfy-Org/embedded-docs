> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoWithAudio/fr.md)

Le nœud Kling Text to Video with Audio génère une courte vidéo à partir d'une description textuelle. Il envoie une requête au service d'IA Kling, qui traite la consigne et renvoie un fichier vidéo. Le nœud peut également générer un fichier audio d'accompagnement pour la vidéo en fonction du texte.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model_name` | COMBO | Oui | `"kling-v2-6"` | Le modèle d'IA spécifique à utiliser pour la génération vidéo. |
| `prompt` | STRING | Oui | - | Consigne textuelle positive. La description utilisée pour générer la vidéo. Doit contenir entre 1 et 2500 caractères. |
| `mode` | COMBO | Oui | `"pro"` | Le mode opérationnel pour la génération vidéo. |
| `aspect_ratio` | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Le rapport largeur/hauteur souhaité pour la vidéo générée. |
| `duration` | COMBO | Oui | `5`<br>`10` | La durée de la vidéo en secondes. |
| `generate_audio` | BOOLEAN | Non | - | Contrôle si un fichier audio est généré pour la vidéo. Lorsqu'il est activé, l'IA crée un son basé sur la consigne. (par défaut : `True`) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | Le fichier vidéo généré. |

---
**Source fingerprint (SHA-256):** `eff4549816c347a090e2f6e8ae8ba832bd2c5b7aef7c729b51c9d72b7a814d5a`
