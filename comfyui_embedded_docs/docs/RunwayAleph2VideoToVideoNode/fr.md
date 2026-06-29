# Nœud Runway Aleph2 Vidéo vers Vidéo

Ce nœud édite une vidéo à l'aide d'une invite textuelle avec le modèle Aleph2 de Runway. Il transforme votre séquence en restylisant, rééclairant, ajoutant ou supprimant des éléments, ou en modifiant le point de vue tout en préservant le mouvement et le timing d'origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `invite` | Décrit ce qui doit apparaître dans la sortie (1 à 1000 caractères). | STRING | Oui | 1 à 1000 caractères |
| `vidéo` | Vidéo d'entrée à éditer. Doit durer 2 à 30 secondes à 30 ips ou moins. | VIDEO | Oui | Durée de 2 à 30 secondes, 30 ips max |
| `graine` | Graine aléatoire pour la génération (par défaut : 0). | INT | Oui | 0 à 4294967295 |
| `seuil de figure publique` | Modération du contenu pour les personnalités publiques reconnaissables (par défaut : "low"). | COMBO | Oui | "auto"<br>"low" |
| `keyframes` | Images de guidage ancrées à la vidéo d'entrée, provenant des nœuds Aleph2 Keyframe (jusqu'à 5). Utilisez les keyframes ou les images d'invite, pas les deux. | KEYFRAME | Non | Jusqu'à 5 éléments |
| `images d’invite` | Images de guidage ancrées à la vidéo de sortie, provenant des nœuds Aleph2 Prompt Image (jusqu'à 5). Utilisez les keyframes ou les images d'invite, pas les deux. | PROMPT_IMAGE | Non | Jusqu'à 5 éléments |

**Contraintes importantes :**
- La vidéo d'entrée doit durer entre 2 et 30 secondes et avoir une fréquence d'images de 30 ips ou moins.
- Vous pouvez utiliser soit les `keyframes` soit les `prompt_images` pour le guidage, mais pas les deux en même temps.
- Chaque entrée de guidage (keyframes ou images d'invite) prend en charge un maximum de 5 éléments.
- Les horodatages des keyframes et des images d'invite ne doivent pas dépasser la durée de la vidéo d'entrée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `vidéo` | La vidéo éditée générée par le modèle Aleph2. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2VideoToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `bda4d0f49843c1a8f311ddbce5911a2a157cae798a26f7a183b31fe41686d0b7`
