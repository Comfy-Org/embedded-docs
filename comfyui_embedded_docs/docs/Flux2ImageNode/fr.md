# Flux.2 Image

Flux.2 Image

Générez des images à l'aide du modèle Flux.2 [pro] ou Flux.2 [max] à partir d'une invite texte et d'images de référence facultatives. Ce nœud envoie votre requête à l'API BFL, interroge le résultat et renvoie l'image générée sous forme de tenseur.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | La version du modèle Flux.2 à utiliser. La sélection d'un modèle débloque des paramètres supplémentaires pour la largeur, la hauteur et les images de référence facultatives. | DYNAMIC_COMBO | Oui | "Flux.2 [pro]"<br>"Flux.2 [max]" |
| `prompt` | Invite pour la génération ou l'édition d'image (par défaut : chaîne vide). | STRING | Oui | N/A |
| `graine` | La graine aléatoire utilisée pour créer le bruit. Peut être définie pour être randomisée après chaque génération (par défaut : 0). | INT | Oui | 0 à 18446744073709551615 |

### Entrées Flux.2 [pro] et Flux.2 [max]

Partagées par les deux modèles — les ensembles de paramètres sont identiques.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `largeur` | La largeur de l'image générée en pixels (par défaut : 1024). | INT | Oui | 256 à 2048 (step 32) |
| `hauteur` | La hauteur de l'image générée en pixels (par défaut : 768). | INT | Oui | 256 à 2048 (step 32) |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model.images` | Image(s) de référence facultative(s) pour la génération image-à-image. Jusqu'à 8 images. Emplacement extensible : connectez 1 à 8 éléments (`image_1`...`image_8`). | IMAGE | Non | 0 à 8 images |

**Remarque :**
- Le nombre maximal d'images de référence est de 8. Si plus de 8 images sont fournies, une erreur est déclenchée.
- Les valeurs `model.width` et `model.height` affectent le coût de génération. Le coût dépend également du modèle sélectionné et de la présence d'images de référence.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image générée sous forme de tenseur, téléchargée à partir du résultat de l'API BFL. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `2994564757e1c66ac6da7b45d227b27ceb0020ac6fc9e8cbe2b53fe9f70bc195`
