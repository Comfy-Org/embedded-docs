# Kling Début-Fin Image vers Vidéo

Ce nœud crée une séquence vidéo qui effectue une transition entre vos images de début et de fin fournies. Il génère toutes les images intermédiaires pour produire une transformation fluide de la première image à la dernière. Ce nœud appelle l’API image-vers-vidéo mais ne prend en charge que les options d’entrée compatibles avec le champ de requête `image_tail`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `start_frame` | Image de référence — URL ou chaîne encodée en Base64, ne peut pas dépasser 10 Mo, résolution d’au moins 300*300 px, rapport hauteur/largeur entre 1:2.5 et 2.5:1. Le Base64 ne doit pas inclure le préfixe data:image. | IMAGE | Oui | - |
| `end_frame` | Image de référence — Contrôle de l’image finale. URL ou chaîne encodée en Base64, ne peut pas dépasser 10 Mo, résolution d’au moins 300*300 px. Le Base64 ne doit pas inclure le préfixe data:image. | IMAGE | Oui | - |
| `prompt` | Invite de texte positive | STRING | Oui | - |
| `negative_prompt` | Invite de texte négative | STRING | Oui | - |
| `cfg_scale` | Contrôle la force du guidage par l’invite (par défaut : 0.5) | FLOAT | Non | 0.0-1.0 |
| `aspect_ratio` | Le rapport hauteur/largeur de la vidéo générée (par défaut : "16:9") | COMBO | Non | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | La configuration à utiliser pour la génération vidéo au format : mode / durée / nom du modèle. (par défaut : "pro mode / 5s duration / kling-v2-5-turbo"). Toutes les options disponibles utilisent le mode pro avec le modèle kling-v2-5-turbo et ne diffèrent que par la durée de la vidéo. | COMBO | Non | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

**Contraintes d’image :**

- Les deux `start_frame` et `end_frame` doivent être fournis et ne peuvent pas dépasser une taille de fichier de 10 Mo.
- Résolution minimale : 300×300 pixels pour les deux images.
- Le rapport hauteur/largeur de `start_frame` doit être compris entre 1:2.5 et 2.5:1.
- Les images encodées en Base64 ne doivent pas inclure le préfixe "data:image".

**Contraintes d’invite :**

- L’invite positive ne doit pas être vide.
- Les invites positive et négative sont limitées à 500 caractères.
- Si `negative_prompt` est laissé vide, il est omis de la requête.

**Tarification :**

- "pro mode / 5s duration / kling-v2-5-turbo" : $0.35 USD par génération
- "pro mode / 10s duration / kling-v2-5-turbo" : $0.70 USD par génération

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La séquence vidéo générée | VIDEO |
| `video_id` | Identifiant unique de la vidéo générée | STRING |
| `duration` | Durée de la vidéo générée | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `a27977226360a425614255f8330ce7fd8ba94b8c3020eb8fdddc01eb74f035c1`
