# PixVerse V6 Image en vidéo

Ce nœud anime une image d'entrée avec le modèle PixVerse V6 et renvoie une vidéo, éventuellement accompagnée d'une piste audio native. La vidéo de sortie conserve le rapport d'aspect de l'image d'entrée.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `image` | L'image d'entrée à animer. | IMAGE | Oui | Image unique |
| `modèle` | Modèle et paramètres de génération. | DYNAMIC_COMBO | Oui | "PixVerse V6" |

### Entrées PixVerse V6

Ces paramètres apparaissent lorsque le modèle « PixVerse V6 » est sélectionné.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `prompt` | Prompt pour la génération de la vidéo (par défaut : vide). | STRING | Oui | 1 à 5000 caractères |
| `quality` | Résolution de sortie. Définit le grand côté : 360p correspond à 640px, 540p à 1024px, 720p à 1280px, 1080p à 1920px (par défaut : "720p"). | COMBO | Oui | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Durée de la vidéo générée en secondes (par défaut : 5). | INT | Oui | 1 à 15 |
| `generate_audio` | Générer une piste audio native avec la vidéo (par défaut : true). | BOOLEAN | Oui | true ou false |
| `multi_clip` | Laisser le modèle découper la vidéo en plusieurs plans au lieu d'une prise continue (par défaut : false). | BOOLEAN | Oui | true ou false |
| `seed` | Graine pour la génération de la vidéo. PixVerse l'enregistre mais ne reproduit pas une exécution à partir de celle-ci (par défaut : 42, le contrôle après génération est activé). | INT | Oui | 0 à 2147483647 |
| `negative_prompt` | Description textuelle facultative des éléments indésirables dans la vidéo (par défaut : vide). | STRING | Non | Jusqu'à 2048 caractères |
| `style` | Style visuel facultatif appliqué à toute la vidéo (par défaut : aucun). | COMBO | Non | Options multiples disponibles (préréglages de style PixVerse V6) |

Remarque : le prompt doit contenir au moins un caractère non blanc et au plus 5000 caractères ; le prompt négatif, s'il est fourni, doit comporter au plus 2048 caractères. La vidéo de sortie correspond toujours au rapport d'aspect de l'image d'entrée, donc aucun réglage de rapport d'aspect n'est nécessaire. Une seule image d'entrée est acceptée. PixVerse peut rejeter une requête lorsque la modération du contenu échoue, lorsque le compte du fournisseur n'a plus de crédits ou lorsque le nombre maximal de générations simultanées est déjà en cours d'exécution.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée, incluant la piste audio native lorsque `generate_audio` est activé. Le rapport d'aspect correspond à celui de l'image d'entrée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6ImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `6ecf958e510e7afc43f5f0e4e5dfd2b789aea02bec882d928326732501cee7b3`
