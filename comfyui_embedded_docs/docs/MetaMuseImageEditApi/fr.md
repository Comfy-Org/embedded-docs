# Meta Muse - Édition d’image

Modifie ou combine jusqu'à 10 images de référence à l'aide d'un prompt textuel et du modèle Muse Image de Meta. Décrivez la modification souhaitée dans le prompt et, si nécessaire, faites référence aux images de référence sous la forme `@Image1`, `@Image2`, etc. Le nœud téléverse les images de référence, appelle l'API Meta Muse Image et renvoie le résultat modifié sous forme d'image.

## Entrées

Le nœud est contrôlé par un sélecteur `model`. Les entrées propres au modèle décrites ci-dessous apparaissent lorsqu'un modèle est sélectionné, et les images de référence que vous connectez peuvent être ajoutées ou supprimées selon vos besoins.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser. | DYNAMIC_COMBO | Oui | "muse-image-1.0" |

### Entrées muse-image-1.0

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Instructions de modification. Prend en charge les références de style `@Image1` aux images d'entrée. Valeur par défaut : chaîne vide. Le prompt doit contenir au moins un caractère. | STRING | Oui | Tout texte d'une longueur minimale de 1 caractère |
| `aspect_ratio` | Rapport d'aspect de la sortie. Les images sont rendues à environ 2,5 mégapixels (1:1 correspond à 1600x1600, 16:9 à 2048x1152) ; "auto" conserve le rapport d'aspect de l'entrée. | COMBO | Oui | "auto"<br>"1:1"<br>"3:2"<br>"2:3"<br>"4:3"<br>"3:4"<br>"5:4"<br>"4:5"<br>"16:9"<br>"9:16"<br>"21:9"<br>"9:21"<br>"2:1"<br>"1:2" |
| `reasoning_strength` | Dans quelle mesure le modèle réfléchit, planifie et s'auto-améliore avant le rendu. | COMBO | Oui | "high"<br>"low" |
| `enable_web_search` | Permet au modèle de rechercher sur le web des faits et des informations en direct pendant la planification de l'image. Valeur par défaut : true. | BOOLEAN | Oui | true ou false (valeur par défaut : true) |
| `enable_image_search` | Permet au modèle de rechercher des images de référence pendant la planification de l'image. Valeur par défaut : true. | BOOLEAN | Oui | true ou false (valeur par défaut : true) |
| `enable_shell` | Permet au modèle d'exécuter du code pendant la planification, pour des mises en page, des graphiques et des diagrammes précis ; lorsqu'il est désactivé, les quantités et l'alignement sont approximatifs. Valeur par défaut : true. | BOOLEAN | Oui | true ou false (valeur par défaut : true) |
| `seed` | Graine pour déterminer si le nœud doit être réexécuté ; l'API n'a pas de graine, donc les résultats réels sont non déterministes quelle que soit cette valeur. Valeur par défaut : 42. | INT | Oui | 0 à 2147483647 (pas de 1) |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Emplacement extensible : connectez 1 à 10 images de référence (`image_1` à `image_10`) à modifier ou à combiner. Référez-vous à elles dans le prompt sous la forme `@Image1`, `@Image2`, ..., numérotées dans l'ordre d'entrée ; une entrée par lot compte une fois par image. | IMAGE | Oui | 1 à 10 images de référence |

Remarque : le prompt ne peut pas être vide, et chaque référence `@ImageN` qu'il contient doit correspondre à l'une des images connectées dans l'ordre d'entrée (par exemple, `@Image1` est la première image de référence connectée). Si le prompt référence un numéro d'image qui n'est pas connecté, ou si plus de 10 images de référence sont connectées, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image modifiée ou combinée renvoyée par le modèle Muse Image. Si l'API renvoie plusieurs images, elles sont renvoyées sous forme de lot. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MetaMuseImageEditApi/fr.md)

---
**Source fingerprint (SHA-256):** `5c009ca45199f9c70465f12d48a46b685abebd0194c3d437121b9df0636dbea7`
