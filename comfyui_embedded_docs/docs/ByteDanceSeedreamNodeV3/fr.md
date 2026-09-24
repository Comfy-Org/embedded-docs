# ByteDance Seedream 4.5 & 5.0

ByteDance Seedream 4.5 & 5.0 génère des images à partir d'une invite textuelle (texte-vers-image) ou génère/modifie des images guidées par des images de référence facultatives, en utilisant les modèles ByteDance Seedream 4.0, 4.5 et 5.0 jusqu'à une résolution 4K. Le nœud envoie l'invite et les éventuelles images de référence à l'API ByteDance, attend la fin de la tâche de génération, puis renvoie le ou les tenseurs d'image résultants.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `prompt` | Invite textuelle pour créer ou modifier une image. Ne doit pas être vide après suppression des espaces blancs. | STRING | Oui | Texte multiligne |
| `modèle` | Sélectionne le modèle Seedream à utiliser. Chaque modèle présente son propre ensemble de sous-paramètres et de limites ci-dessous. | DYNAMIC_COMBO | Oui | "seedream 5.0 pro"<br>"seedream 5.0 flash"<br>"seedream 5.0 lite"<br>"seedream-4-5-251128"<br>"seedream-4-0-250828" |

### Entrées Seedream 5.0 Pro (seedream 5.0 pro)

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `size_preset` | Choisissez une taille recommandée. Sélectionnez Custom pour utiliser la largeur et la hauteur ci-dessous. Défaut : premier préréglage recommandé pour ce modèle. | COMBO | Non | Préréglages de taille recommandés propres au modèle<br>"Custom" |
| `width` | Largeur personnalisée de l'image. La valeur n'est utilisée que si `size_preset` est défini sur `Custom`. Défaut : 2048. | INT | Non | 1024 à 4514 (pas 2) |
| `height` | Hauteur personnalisée de l'image. La valeur n'est utilisée que si `size_preset` est défini sur `Custom`. Défaut : 2048. | INT | Non | 1024 à 4514 (pas 2) |
| `prompt_optimization` | Mode d'optimisation de l'invite lorsque des images de référence sont fournies : 'standard' offre une qualité supérieure, 'fast' un temps de génération plus court. Défaut : "standard". | COMBO | Non | "standard"<br>"fast" |
| `seed` | Graine à utiliser pour la génération. Défaut : 42. | INT | Non | 0 à 2147483647 |
| `watermark` | Indique s'il faut ajouter un filigrane « AI generated » à l'image. Défaut : false. | BOOLEAN | Non | true / false |
| `thinking` | Active le raisonnement d'optimisation de l'invite (« thinking ») du modèle pour un meilleur respect. Peut augmenter considérablement le temps de génération — notamment sur Seedream 5.0 Pro. Ne peut être désactivé que pour la génération texte-vers-image (pas lorsque des images de référence sont fournies). Défaut : true. | BOOLEAN | Non | true / false |

### Entrées Seedream 5.0 Flash (seedream 5.0 flash)

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `size_preset` | Choisissez une taille recommandée. Sélectionnez Custom pour utiliser la largeur et la hauteur ci-dessous. Défaut : premier préréglage recommandé pour ce modèle. | COMBO | Non | Préréglages de taille recommandés propres au modèle<br>"Custom" |
| `width` | Largeur personnalisée de l'image. La valeur n'est utilisée que si `size_preset` est défini sur `Custom`. Défaut : 2048. | INT | Non | 1024 à 4514 (pas 2) |
| `height` | Hauteur personnalisée de l'image. La valeur n'est utilisée que si `size_preset` est défini sur `Custom`. Défaut : 2048. | INT | Non | 1024 à 4514 (pas 2) |
| `seed` | Graine à utiliser pour la génération. Défaut : 42. | INT | Non | 0 à 2147483647 |
| `watermark` | Indique s'il faut ajouter un filigrane « AI generated » à l'image. Défaut : false. | BOOLEAN | Non | true / false |

### Entrées Seedream 5.0 Lite (seedream 5.0 lite)

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `size_preset` | Choisissez une taille recommandée. Sélectionnez Custom pour utiliser la largeur et la hauteur ci-dessous. Défaut : premier préréglage recommandé pour ce modèle. | COMBO | Non | Préréglages de taille recommandés propres au modèle<br>"Custom" |
| `width` | Largeur personnalisée de l'image. La valeur n'est utilisée que si `size_preset` est défini sur `Custom`. Défaut : 2048. | INT | Non | 1024 à 6240 (pas 2) |
| `height` | Hauteur personnalisée de l'image. La valeur n'est utilisée que si `size_preset` est défini sur `Custom`. Défaut : 2048. | INT | Non | 1024 à 4992 (pas 2) |
| `max_images` | Nombre maximal d'images à générer. Avec 1, exactement une image est produite. Avec >1, le modèle génère entre 1 et `max_images` images liées (p. ex., scènes d'histoire, variations de personnage). Le total des images (entrée + générées) ne peut pas dépasser 15. Défaut : 1. | INT | Non | 1 à 14 |
| `fail_on_partial` | Si activé, interrompt l'exécution si des images demandées sont manquantes ou renvoient une erreur. Défaut : false. | BOOLEAN | Non | true / false |
| `seed` | Graine à utiliser pour la génération. Défaut : 42. | INT | Non | 0 à 2147483647 |
| `watermark` | Indique s'il faut ajouter un filigrane « AI generated » à l'image. Défaut : false. | BOOLEAN | Non | true / false |
| `thinking` | Active le raisonnement d'optimisation de l'invite (« thinking ») du modèle pour un meilleur respect. Peut augmenter considérablement le temps de génération — notamment sur Seedream 5.0 Pro. Ne peut être désactivé que pour la génération texte-vers-image (pas lorsque des images de référence sont fournies). Défaut : true. | BOOLEAN | Non | true / false |

### Entrées Seedream 4.5 (seedream-4-5-251128)

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `size_preset` | Choisissez une taille recommandée. Sélectionnez Custom pour utiliser la largeur et la hauteur ci-dessous. Défaut : premier préréglage recommandé pour ce modèle. | COMBO | Non | Préréglages de taille recommandés propres au modèle<br>"Custom" |
| `width` | Largeur personnalisée de l'image. La valeur n'est utilisée que si `size_preset` est défini sur `Custom`. Défaut : 2048. | INT | Non | 1024 à 6240 (pas 2) |
| `height` | Hauteur personnalisée de l'image. La valeur n'est utilisée que si `size_preset` est défini sur `Custom`. Défaut : 2048. | INT | Non | 1024 à 4992 (pas 2) |
| `max_images` | Nombre maximal d'images à générer. Avec 1, exactement une image est produite. Avec >1, le modèle génère entre 1 et `max_images` images liées (p. ex., scènes d'histoire, variations de personnage). Le total des images (entrée + générées) ne peut pas dépasser 15. Défaut : 1. | INT | Non | 1 à 10 |
| `fail_on_partial` | Si activé, interrompt l'exécution si des images demandées sont manquantes ou renvoient une erreur. Défaut : false. | BOOLEAN | Non | true / false |
| `seed` | Graine à utiliser pour la génération. Défaut : 42. | INT | Non | 0 à 2147483647 |
| `watermark` | Indique s'il faut ajouter un filigrane « AI generated » à l'image. Défaut : false. | BOOLEAN | Non | true / false |
| `thinking` | Active le raisonnement d'optimisation de l'invite (« thinking ») du modèle pour un meilleur respect. Peut augmenter considérablement le temps de génération — notamment sur Seedream 5.0 Pro. Ne peut être désactivé que pour la génération texte-vers-image (pas lorsque des images de référence sont fournies). Défaut : true. | BOOLEAN | Non | true / false |

### Entrées Seedream 4.0 (seedream-4-0-250828)

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `size_preset` | Choisissez une taille recommandée. Sélectionnez Custom pour utiliser la largeur et la hauteur ci-dessous. Défaut : premier préréglage recommandé pour ce modèle. | COMBO | Non | Préréglages de taille recommandés propres au modèle<br>"Custom" |
| `width` | Largeur personnalisée de l'image. La valeur n'est utilisée que si `size_preset` est défini sur `Custom`. Défaut : 2048. | INT | Non | 1024 à 6240 (pas 2) |
| `height` | Hauteur personnalisée de l'image. La valeur n'est utilisée que si `size_preset` est défini sur `Custom`. Défaut : 2048. | INT | Non | 1024 à 4992 (pas 2) |
| `max_images` | Nombre maximal d'images à générer. Avec 1, exactement une image est produite. Avec >1, le modèle génère entre 1 et `max_images` images liées (p. ex., scènes d'histoire, variations de personnage). Le total des images (entrée + générées) ne peut pas dépasser 15. Défaut : 1. | INT | Non | 1 à 10 |
| `fail_on_partial` | Si activé, interrompt l'exécution si des images demandées sont manquantes ou renvoient une erreur. Défaut : false. | BOOLEAN | Non | true / false |
| `seed` | Graine à utiliser pour la génération. Défaut : 42. | INT | Non | 0 à 2147483647 |
| `watermark` | Indique s'il faut ajouter un filigrane « AI generated » à l'image. Défaut : false. | BOOLEAN | Non | true / false |
| `thinking` | Active le raisonnement d'optimisation de l'invite (« thinking ») du modèle pour un meilleur respect. Peut augmenter considérablement le temps de génération — notamment sur Seedream 5.0 Pro. Ne peut être désactivé que pour la génération texte-vers-image (pas lorsque des images de référence sont fournies). Défaut : true. | BOOLEAN | Non | true / false |

### Entrées de référence

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `images` | Emplacement extensible : image(s) de référence facultative(s) pour la génération image-vers-image ou multi-références. Connectez 1..N images (p. ex., `image_1`, `image_2`, ...) ; la limite du nombre dépend du modèle (voir notes ci-dessous). Si une image connectée contient un lot d'images, chaque image du lot compte dans la limite. | IMAGE | Non | 0 à 10 (Seedream 5.0 Pro, Seedream 5.0 Flash, Seedream 4.5, Seedream 4.0)<br>0 à 14 (Seedream 5.0 Lite) |

**Notes :**

- Le `prompt` ne doit pas être vide après suppression des espaces blancs.
- Nombre maximal d'images de référence : 10 pour Seedream 5.0 Pro, Seedream 5.0 Flash, Seedream 4.5 et Seedream 4.0 ; 14 pour Seedream 5.0 Lite.
- Chaque image de référence doit avoir un rapport d'aspect compris entre 1:16 et 16:1.
- Lorsque `max_images` est supérieur à 1 (non disponible sur Seedream 5.0 Pro ou Seedream 5.0 Flash), le nombre total d'images de référence plus les images générées ne peut pas dépasser 15.
- `thinking` ne peut être désactivé que pour la génération texte-vers-image. Lorsque des images de référence sont fournies, `thinking` doit être activé. Seedream 5.0 Flash n'a pas d'entrée `thinking`.
- `width` et `height` ne sont utilisés que lorsque `size_preset` est défini sur "Custom".
- `prompt_optimization` n'est disponible que sur Seedream 5.0 Pro.
- `max_images` et `fail_on_partial` ne sont disponibles que sur Seedream 5.0 Lite, Seedream 4.5 et Seedream 4.0 ; Seedream 5.0 Pro et Seedream 5.0 Flash demandent toujours une seule image.
- Contraintes de résolution (largeur x hauteur) :
  - Seedream 5.0 Pro et Seedream 5.0 Flash : entre 0,92 MP (921 600 pixels) et 4,62 MP (4 624 220 pixels).
  - Seedream 5.0 Lite et Seedream 4.5 : au moins 3,68 MP (3 686 400 pixels).
  - Seedream 4.0 : au moins 0,92 MP (921 600 pixels).
  - Seedream 5.0 Lite, Seedream 4.5 et Seedream 4.0 : au plus 16,78 MP (16 777 216 pixels).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | Le tenseur d'image généré. Lorsque plusieurs images sont générées, elles sont concaténées en un seul tenseur IMAGE par lots. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV3/fr.md)

---
**Source fingerprint (SHA-256):** `1c1f40b202ccbb3e0f73cd072170e1c16b833e007f26e63505b54c42b004a8a6`
