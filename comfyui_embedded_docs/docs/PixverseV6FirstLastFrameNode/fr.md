# PixVerse V6 Vidéo à partir de la première et de la dernière image

PixVerse V6 First-Last-Frame to Video génère une vidéo qui effectue une transition d'une première image à une dernière image à l'aide de PixVerse, éventuellement avec un son natif. Les deux images fournies sont envoyées à l'API PixVerse, qui produit la vidéo de transition et la renvoie sous forme de fichier vidéo. La sortie conserve le ratio d'aspect de la première image.

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
| `prompt` | Prompt décrivant la transition. | STRING | Oui | Jusqu'à 5000 caractères |
| `quality` | Résolution de sortie. Définit le bord long : 360p est 640px, 540p 1024px, 720p 1280px, 1080p 1920px. (défaut : 720p) | COMBO | Oui | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Durée de la vidéo générée en secondes. (défaut : 5) | INT | Oui | 1 à 15 |
| `generate_audio` | Génère une piste audio native avec la vidéo. (défaut : true) | BOOLEAN | Oui | true<br>false |
| `seed` | Graine (seed) pour la génération vidéo. PixVerse l'enregistre mais ne reproduit pas une exécution à partir de celle-ci. (défaut : 42) | INT | Oui | 0 à 2147483647 |
| `negative_prompt` | Une description textuelle facultative des éléments indésirables dans la vidéo. | STRING | Non | Jusqu'à 2048 caractères |
| `style` | Un style visuel facultatif appliqué à l'ensemble de la vidéo. (défaut : none) | COMBO | Non | Plusieurs options disponibles (défaut : "none") |

Remarque : le prompt ne doit pas être vide après suppression des espaces et est limité à 5000 caractères. Le prompt négatif, s'il est fourni, est limité à 2048 caractères. La durée doit être comprise entre 1 et 15 secondes. La vidéo de sortie conserve le ratio d'aspect de la première image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La vidéo générée qui effectue la transition de la première image à la dernière, incluant une piste audio lorsque `generate_audio` est activé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6FirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `cdb5e45e9de2b429b9d43bbff90b6529af246911ecae8c2809c8abd539101aaa`
