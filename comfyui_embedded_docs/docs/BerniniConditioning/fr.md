# BerniniConditioning

Le nœud BerniniConditioning prépare les données de conditionnement vidéo et image pour le modèle Wan2.2-A14B. Il encode les vidéos sources, les vidéos de référence et les images de référence à l'aide du VAE fourni, puis les attache aux données de conditionnement pour des tâches de génération en contexte.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positif` | Données de conditionnement positives | CONDITIONING | Oui | - |
| `négatif` | Données de conditionnement négatives | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les entrées vidéo et image | VAE | Oui | - |
| `largeur` | Largeur du latent de sortie (par défaut : 832) | INT | Oui | 16 à 8192 (pas : 16) |
| `hauteur` | Hauteur du latent de sortie (par défaut : 480) | INT | Oui | 16 à 8192 (pas : 16) |
| `longueur` | Nombre d'images dans le latent de sortie (par défaut : 81) | INT | Oui | 1 à 8192 (pas : 4) |
| `taille_lot` | Nombre de vidéos à générer en un seul lot (par défaut : 1) | INT | Oui | 1 à 4096 |
| `vidéo_source` | Vidéo source à éditer ou restyler (v2v, rv2v). Redimensionnée à la largeur/hauteur et ajustée à la longueur. | IMAGE | Non | - |
| `vidéo_de_référence` | Vidéo à insérer dans la vidéo source (ads2v). | IMAGE | Non | - |
| `images_de_référence` | Images de référence injectées comme jetons en contexte (r2v, rv2v). Jusqu'à 8 images peuvent être fournies. | IMAGE | Non | 0 à 8 images |
| `ref_max_size` | Taille maximale pour le bord long de reference_video et reference_images. Redimensionné avec conservation du rapport hauteur/largeur et ajusté à 16px (par défaut : 848). | INT | Non | 16 à 8192 (pas : 16) |

**Remarque :** La tâche est déduite des entrées connectées :
- Aucune entrée connectée → texte-vers-vidéo (t2v)
- `source_video` uniquement → vidéo-vers-vidéo (v2v)
- `source_video` + `reference_images` → édition vidéo guidée par référence (rv2v)
- `reference_images` uniquement → référence-vers-vidéo (r2v)
- `source_video` + `reference_video` → insertion d'image/vidéo dans une vidéo (ads2v)

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positif` | Conditionnement positif avec latents de contexte attachés | CONDITIONING |
| `négatif` | Conditionnement négatif avec latents de contexte attachés | CONDITIONING |
| `latent` | Tenseur latent vide dont les dimensions correspondent à la largeur, hauteur, longueur et taille de lot spécifiées | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BerniniConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `3535bbe9a1ae007dc579242b44787ab315479a820eb0da680eab9b870ab60699`
