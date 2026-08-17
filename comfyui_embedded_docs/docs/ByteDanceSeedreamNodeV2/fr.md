# ByteDance Seedream 4.5 & 5.0

Ce nœud crée ou modifie des images à l’aide des modèles Seedream de ByteDance (4.0, 4.5, 5.0 Lite et 5.0 Pro). Il génère de nouvelles images à partir d’un prompt texte et peut modifier des images existantes en s’appuyant sur des images de référence et une instruction en une phrase, avec une prise en charge de résolutions allant jusqu’à 4K.

## Entrées

Le sélecteur `model` détermine quelles entrées spécifiques au modèle sont disponibles. Les tableaux ci-dessous listent les entrées communes, les entrées pour chaque modèle et les emplacements extensibles d’images de référence.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | La version du modèle Seedream à utiliser pour la génération. Chaque modèle possède des capacités, des limites et des tarifs différents. | DYNAMIC_COMBO | Oui | `"seedream 5.0 pro"`<br>`"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` |
| `prompt` | Prompt texte pour créer ou modifier une image. | STRING | Oui | Tout texte (non vide) |
| `seed` | Graine à utiliser pour la génération (par défaut : 0). | INT | Oui | 0 à 2147483647 |
| `watermark` | Indique s’il faut ajouter un filigrane « AI generated » à l’image (par défaut : False). | BOOLEAN | Oui | True / False |
| `thinking` | Active le raisonnement d’optimisation du prompt du modèle (« thinking ») pour une meilleure adhésion. Peut augmenter considérablement le temps de génération, notamment sur Seedream 5.0 Pro. Ne peut être désactivé que pour la génération texte-à-image (pas lorsque des images de référence sont fournies). (par défaut : True) | BOOLEAN | Non | True / False |

### Entrées de seedream 5.0 pro

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size_preset` | Choisissez une taille recommandée. Sélectionnez Custom pour utiliser la largeur et la hauteur ci-dessous. | COMBO | Oui | Préréglages spécifiques au modèle (y compris Custom) |
| `width` | Largeur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur Custom (par défaut : 2048). | INT | Oui | 1024 à 3136 (pas de 2) |
| `height` | Hauteur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur Custom (par défaut : 2048). | INT | Oui | 1024 à 2496 (pas de 2) |

### Entrées de seedream 5.0 lite

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size_preset` | Choisissez une taille recommandée. Sélectionnez Custom pour utiliser la largeur et la hauteur ci-dessous. | COMBO | Oui | Préréglages spécifiques au modèle (y compris Custom) |
| `width` | Largeur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur Custom (par défaut : 2048). | INT | Oui | 1024 à 6240 (pas de 2) |
| `height` | Hauteur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur Custom (par défaut : 2048). | INT | Oui | 1024 à 4992 (pas de 2) |
| `max_images` | Nombre maximal d’images à générer. Avec 1, une seule image est produite. Avec >1, le modèle génère entre 1 et max_images images associées (par exemple, des scènes d’histoire, des variations de personnages). Le nombre total d’images (en entrée + générées) ne peut pas dépasser 15. (par défaut : 1) | INT | Oui | 1 à 14 |
| `fail_on_partial` | Si activée, l’exécution est interrompue si des images demandées sont manquantes ou renvoient une erreur. (par défaut : False) | BOOLEAN | Oui | True / False |

### Entrées de seedream-4-5-251128

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size_preset` | Choisissez une taille recommandée. Sélectionnez Custom pour utiliser la largeur et la hauteur ci-dessous. | COMBO | Oui | Préréglages spécifiques au modèle (y compris Custom) |
| `width` | Largeur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur Custom (par défaut : 2048). | INT | Oui | 1024 à 6240 (pas de 2) |
| `height` | Hauteur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur Custom (par défaut : 2048). | INT | Oui | 1024 à 4992 (pas de 2) |
| `max_images` | Nombre maximal d’images à générer. Avec 1, une seule image est produite. Avec >1, le modèle génère entre 1 et max_images images associées (par exemple, des scènes d’histoire, des variations de personnages). Le nombre total d’images (en entrée + générées) ne peut pas dépasser 15. (par défaut : 1) | INT | Oui | 1 à 10 |
| `fail_on_partial` | Si activée, l’exécution est interrompue si des images demandées sont manquantes ou renvoient une erreur. (par défaut : False) | BOOLEAN | Oui | True / False |

### Entrées de seedream-4-0-250828

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size_preset` | Choisissez une taille recommandée. Sélectionnez Custom pour utiliser la largeur et la hauteur ci-dessous. | COMBO | Oui | Préréglages spécifiques au modèle (y compris Custom) |
| `width` | Largeur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur Custom (par défaut : 2048). | INT | Oui | 1024 à 6240 (pas de 2) |
| `height` | Hauteur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur Custom (par défaut : 2048). | INT | Oui | 1024 à 4992 (pas de 2) |
| `max_images` | Nombre maximal d’images à générer. Avec 1, une seule image est produite. Avec >1, le modèle génère entre 1 et max_images images associées (par exemple, des scènes d’histoire, des variations de personnages). Le nombre total d’images (en entrée + générées) ne peut pas dépasser 15. (par défaut : 1) | INT | Oui | 1 à 10 |
| `fail_on_partial` | Si activée, l’exécution est interrompue si des images demandées sont manquantes ou renvoient une erreur. (par défaut : False) | BOOLEAN | Oui | True / False |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Image(s) de référence facultative(s) pour la génération image-à-image ou multi-références. Emplacement extensible : connectez 1..N éléments (`image_1`, `image_2`, ..., `image_N`) ; le nombre maximal dépend du modèle sélectionné (10 pour seedream 5.0 pro, seedream-4-5-251128 et seedream-4-0-250828 ; 14 pour seedream 5.0 lite). | IMAGE | Non | 0 à 10<br>0 à 14 (seedream 5.0 lite) |

### Remarques

- Les valeurs personnalisées `width` et `height` ne sont prises en compte que lorsque `size_preset` est défini sur Custom.
- Limites de résolution (basées sur la largeur × la hauteur) :
  - seedream 5.0 pro : minimum 0,92 MP, maximum 4,19 MP.
  - seedream 5.0 lite et seedream-4-5-251128 : minimum 3,68 MP.
  - seedream-4-0-250828 : minimum 0,92 MP.
  - seedream 5.0 lite, seedream-4-5-251128 et seedream-4-0-250828 : maximum 16,78 MP.
- Les images de référence doivent avoir un ratio d’aspect compris entre 1:3 et 3:1.
- Lorsque `max_images` est supérieur à 1 (disponible sur seedream 5.0 lite, seedream-4-5-251128 et seedream-4-0-250828), le nombre total d’images (images de référence plus images générées) ne peut pas dépasser 15.
- `thinking` ne peut être désactivé que pour la génération texte-à-image ; il doit être activé lorsque des images de référence sont fournies.
- seedream 5.0 pro génère toujours une seule image et n’affiche pas les entrées `max_images` ni `fail_on_partial`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L’image générée ou modifiée. Si plusieurs images ont été demandées avec `max_images`, elles sont renvoyées concaténées en un seul lot. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `b57e0d85a586aaeb7cf02ceaaddcd2d36cdac20f5251cba48de602a979420f1c`
