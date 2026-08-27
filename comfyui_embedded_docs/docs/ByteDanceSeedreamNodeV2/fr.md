# ByteDance Seedream 4.5 & 5.0

Ce nœud génère ou modifie des images à l’aide des modèles Seedream de ByteDance (versions 4.0, 4.5, 5.0 Lite et 5.0 Pro). Il offre une génération texte-image unifiée et une édition d’image précise à partir d’une phrase unique, jusqu’à une résolution 4K. Il s’agit de la version héritée (V2) du nœud Seedream.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `modèle` | La version du modèle Seedream à utiliser pour la génération. Chaque modèle a des capacités et une tarification différentes. | DYNAMIC_COMBO | Oui | `"seedream 5.0 pro"`<br>`"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` |
| `prompt` | Invite textuelle pour créer ou modifier une image (par défaut : chaîne vide). | STRING | Oui | N/A |
| `graine` | Graine à utiliser pour la génération (par défaut : 0). | INT | Oui | 0 à 2147483647 |
| `filigrane` | Indique s’il faut ajouter un filigrane « généré par IA » à l’image (par défaut : False). | BOOLEAN | Oui | True / False |
| `thinking` | Active le raisonnement d’optimisation de l’invite du modèle (« thinking ») pour une meilleure fidélité. Peut considérablement augmenter le temps de génération — notamment sur Seedream 5.0 Pro. Ne peut être désactivé que pour la génération texte-image (pas lorsque des images de référence sont fournies) (par défaut : True). | BOOLEAN | Non | True / False |

### Entrées `seedream 5.0 pro`

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Choisir une taille recommandée. Sélectionnez Custom pour utiliser la largeur et la hauteur ci-dessous. | COMBO | Oui | Plusieurs préréglages spécifiques au modèle disponibles, y compris `Custom` |
| `width` | Largeur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur `Custom` (par défaut : 2048). | INT | Oui | 1024 à 3136 (pas de 2) |
| `height` | Hauteur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur `Custom` (par défaut : 2048). | INT | Oui | 1024 à 2496 (pas de 2) |

### Entrées `seedream 5.0 lite`

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Choisir une taille recommandée. Sélectionnez Custom pour utiliser la largeur et la hauteur ci-dessous. | COMBO | Oui | Plusieurs préréglages spécifiques au modèle disponibles, y compris `Custom` |
| `width` | Largeur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur `Custom` (par défaut : 2048). | INT | Oui | 1024 à 6240 (pas de 2) |
| `height` | Hauteur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur `Custom` (par défaut : 2048). | INT | Oui | 1024 à 4992 (pas de 2) |
| `max_images` | Nombre maximal d’images à générer. Avec 1, une seule image est produite. Avec >1, le modèle génère entre 1 et max_images images liées (par exemple, scènes narratives, variations de personnages). Le nombre total d’images (entrées + générées) ne peut pas dépasser 15. (par défaut : 1) | INT | Oui | 1 à 14 |
| `fail_on_partial` | Si activé, interrompt l’exécution si des images demandées sont manquantes ou renvoient une erreur. (par défaut : False) | BOOLEAN | Oui | True / False |

### Entrées `seedream-4-5-251128`

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Choisir une taille recommandée. Sélectionnez Custom pour utiliser la largeur et la hauteur ci-dessous. | COMBO | Oui | Plusieurs préréglages spécifiques au modèle disponibles, y compris `Custom` |
| `width` | Largeur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur `Custom` (par défaut : 2048). | INT | Oui | 1024 à 6240 (pas de 2) |
| `height` | Hauteur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur `Custom` (par défaut : 2048). | INT | Oui | 1024 à 4992 (pas de 2) |
| `max_images` | Nombre maximal d’images à générer. Avec 1, une seule image est produite. Avec >1, le modèle génère entre 1 et max_images images liées (par exemple, scènes narratives, variations de personnages). Le nombre total d’images (entrées + générées) ne peut pas dépasser 15. (par défaut : 1) | INT | Oui | 1 à 10 |
| `fail_on_partial` | Si activé, interrompt l’exécution si des images demandées sont manquantes ou renvoient une erreur. (par défaut : False) | BOOLEAN | Oui | True / False |

### Entrées `seedream-4-0-250828`

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Choisir une taille recommandée. Sélectionnez Custom pour utiliser la largeur et la hauteur ci-dessous. | COMBO | Oui | Plusieurs préréglages spécifiques au modèle disponibles, y compris `Custom` |
| `width` | Largeur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur `Custom` (par défaut : 2048). | INT | Oui | 1024 à 6240 (pas de 2) |
| `height` | Hauteur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur `Custom` (par défaut : 2048). | INT | Oui | 1024 à 4992 (pas de 2) |
| `max_images` | Nombre maximal d’images à générer. Avec 1, une seule image est produite. Avec >1, le modèle génère entre 1 et max_images images liées (par exemple, scènes narratives, variations de personnages). Le nombre total d’images (entrées + générées) ne peut pas dépasser 15. (par défaut : 1) | INT | Oui | 1 à 10 |
| `fail_on_partial` | Si activé, interrompt l’exécution si des images demandées sont manquantes ou renvoient une erreur. (par défaut : False) | BOOLEAN | Oui | True / False |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `images` | Emplacement extensible : connectez 1..N éléments (par exemple `image_1`, `image_2`, ...) ; la limite de nombre dépend du modèle sélectionné (voir sections des modèles). Image(s) de référence facultative(s) pour la génération image-à-image ou multi-référence. Sans images de référence, le nœud fonctionne en mode texte-image. | IMAGE | Non | 0 à 10 images (`seedream 5.0 pro`, `seedream-4-5-251128`, `seedream-4-0-250828`)<br>0 à 14 images (`seedream 5.0 lite`) |

### Remarques sur les contraintes

- `width` et `height` ne prennent effet que lorsque `size_preset` est défini sur `Custom`.
- Le nombre total d’images de référence plus les images générées ne peut pas dépasser 15.
- `thinking` ne peut être désactivé que pour la génération texte-image, pas lorsque des images de référence sont fournies.
- Seedream 5.0 Pro ne prend pas en charge la génération par lots : il produit toujours une seule image, donc `max_images` et `fail_on_partial` ne sont pas disponibles pour ce modèle.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `image` | L’image générée ou modifiée sous forme de tenseur. Si plusieurs images ont été demandées, elles sont concaténées dans un seul lot. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `f1a84171d94c602ec5417e43857ddf511ab1e54caa089b1928f740d3a38423f8`
