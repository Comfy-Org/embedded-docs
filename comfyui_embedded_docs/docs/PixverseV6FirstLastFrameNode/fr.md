# PixVerse V6 Vidéo à partir de la première et de la dernière image

PixVerse V6 First-Last-Frame to Video génère une vidéo qui effectue une transition entre une première image et une dernière image à l'aide de PixVerse, avec éventuellement un audio natif. Les deux images fournies sont envoyées à l'API PixVerse, qui produit la vidéo de transition et la renvoie sous forme de fichier vidéo. La sortie conserve le rapport d'aspect de la première image.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `first_frame` | L'image de départ de la vidéo. | IMAGE | Oui | — |
| `last_frame` | L'image de fin de la vidéo. | IMAGE | Oui | — |
| `model` | Modèle et paramètres de génération. Sélectionne le modèle PixVerse et affiche ses paramètres de génération. | DYNAMIC_COMBO | Oui | "PixVerse V6" |

### Entrées PixVerse V6

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite décrivant la transition. | STRING | Oui | Jusqu'à 5000 caractères |
| `quality` | Résolution de sortie. Définit le bord long : 360p correspond à 640px, 540p à 1024px, 720p à 1280px, 1080p à 1920px. (par défaut : 720p) | COMBO | Oui | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Durée de la vidéo générée en secondes. (par défaut : 5) | INT | Oui | 1 à 15 |
| `generate_audio` | Génère une piste audio native avec la vidéo. (par défaut : true) | BOOLEAN | Oui | true<br>false |
| `seed` | Graine pour la génération vidéo. PixVerse l'enregistre mais ne reproduit pas une exécution à partir de celle-ci. (par défaut : 42) | INT | Oui | 0 à 2147483647 |
| `negative_prompt` | Une description textuelle optionnelle des éléments indésirables dans la vidéo. | STRING | Non | Jusqu'à 2048 caractères |
| `style` | Un style visuel optionnel appliqué à l'ensemble de la vidéo. (par défaut : none) | COMBO | Non | Plusieurs options disponibles (par défaut : "none") |

Remarque : L'invite ne doit pas être vide après suppression des espaces, et est limitée à 5000 caractères. L'invite négative, lorsqu'elle est fournie, est limitée à 2048 caractères. La durée doit être comprise entre 1 et 15 secondes. La vidéo de sortie conserve le rapport d'aspect de la première image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée qui effectue la transition entre la première image et la dernière image, incluant une piste audio lorsque `generate_audio` est activé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6FirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `cdb5e45e9de2b429b9d43bbff90b6529af246911ecae8c2809c8abd539101aaa`
