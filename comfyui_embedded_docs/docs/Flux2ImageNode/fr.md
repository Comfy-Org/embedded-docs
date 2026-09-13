# Flux.2 Image

Génère des images à l’aide du modèle Flux.2 [pro] ou Flux.2 [max] à partir d’un prompt textuel et d’images de référence facultatives. Le nœud envoie la requête à l’API BFL, interroge régulièrement l’API jusqu’à ce que le résultat soit prêt, puis renvoie l’image générée.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Version du modèle Flux.2 à utiliser. La sélection d’un modèle déverrouille des paramètres supplémentaires pour la largeur, la hauteur et les images de référence facultatives. | DYNAMIC_COMBO | Oui | "Flux.2 [pro]"<br>"Flux.2 [max]" |
| `prompt` | Prompt pour la génération ou l’édition d’image (valeur par défaut : chaîne vide). | STRING | Oui | N/A |
| `seed` | Graine aléatoire utilisée pour créer le bruit (valeur par défaut : 0). Prend en charge l’option de contrôle après génération pour randomiser la valeur après chaque exécution. | INT | Oui | 0 à 18446744073709551615 |

### Entrées Flux.2 [pro] et Flux.2 [max]

Partagées par les deux modèles — les ensembles de paramètres sont identiques.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model.width` | Largeur de l’image générée en pixels (valeur par défaut : 1024). | INT | Oui | 256 à 2048 (pas de 32) |
| `model.height` | Hauteur de l’image générée en pixels (valeur par défaut : 768). | INT | Oui | 256 à 2048 (pas de 32) |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model.images` | Image(s) de référence facultative(s) pour la génération image à image. Jusqu’à 8 images. Emplacement extensible : connectez 1..8 éléments (`image_1`...`image_8`). | IMAGE | Non | 0 à 8 images |

**Remarque :**
- Le nombre maximal d’images de référence est de 8. Si plus de 8 images sont fournies, une erreur est générée. Les images de lot comptent dans cette limite, car chaque image d’un lot est comptée individuellement.
- Les images de référence sont redimensionnées afin que le nombre total de pixels ne dépasse pas 2048 x 2048 avant d’être envoyées à l’API.
- Les valeurs `model.width` et `model.height` affectent le coût de génération. Le coût dépend également du modèle sélectionné et de la présence éventuelle d’images de référence.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L’image générée sous forme de tenseur, téléchargée depuis le résultat de l’API BFL. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `2994564757e1c66ac6da7b45d227b27ceb0020ac6fc9e8cbe2b53fe9f70bc195`
