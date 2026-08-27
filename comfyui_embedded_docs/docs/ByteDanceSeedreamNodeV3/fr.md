# ByteDanceSeedreamNodeV3

Le nœud ByteDance Seedream 4.5 et 5.0 génère des images à partir d’un prompt texte (text-to-image) ou génère/édite des images guidées par des images de référence facultatives, en utilisant les modèles ByteDance Seedream 4.0, 4.5 et 5.0 jusqu’à une résolution 4K. Le nœud envoie le prompt et les éventuelles images de référence à l’API ByteDance, attend que la tâche de génération soit terminée, puis renvoie le ou les tenseurs d’image résultants.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt texte pour créer ou modifier une image. Ne doit pas être vide après suppression des espaces. | STRING | Oui | Texte multiligne |
| `modèle` | Sélectionne le modèle Seedream à utiliser. Chaque modèle expose son propre ensemble de sous-paramètres et de limites ci-dessous. | DYNAMIC_COMBO | Oui | "seedream 5.0 pro"<br>"seedream 5.0 lite"<br>"seedream-4-5-251128"<br>"seedream-4-0-250828" |

### Entrées Seedream 5.0 Pro (seedream 5.0 pro)

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size_preset` | Choisissez une taille recommandée. Sélectionnez « Custom » pour utiliser la largeur et la hauteur ci-dessous. Par défaut : premier préréglage recommandé pour ce modèle. | COMBO | Non | Préréglages de taille recommandés spécifiques au modèle<br>"Custom" |
| `width` | Largeur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur « Custom ». Par défaut : 2048. | INT | Non | 1024 à 3136 (pas de 2) |
| `height` | Hauteur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur « Custom ». Par défaut : 2048. | INT | Non | 1024 à 2496 (pas de 2) |
| `prompt_optimization` | Mode d’optimisation du prompt lorsque des images de référence sont fournies : « standard » offre une qualité supérieure, « fast » un temps de génération plus court. Par défaut : « standard ». | COMBO | Non | "standard"<br>"fast" |
| `seed` | Seed à utiliser pour la génération. Par défaut : 42. | INT | Non | 0 à 2147483647 |
| `watermark` | Indique s’il faut ajouter un filigrane « AI generated » à l’image. Par défaut : false. | BOOLEAN | Non | true / false |
| `thinking` | Active le raisonnement d’optimisation du prompt du modèle (« thinking ») pour une meilleure adhérence. Peut considérablement augmenter le temps de génération — notamment sur Seedream 5.0 Pro. Ne peut être désactivé que pour la génération text-to-image (pas lorsque des images de référence sont fournies). Par défaut : true. | BOOLEAN | Non | true / false |

### Entrées Seedream 5.0 Lite (seedream 5.0 lite)

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size_preset` | Choisissez une taille recommandée. Sélectionnez « Custom » pour utiliser la largeur et la hauteur ci-dessous. Par défaut : premier préréglage recommandé pour ce modèle. | COMBO | Non | Préréglages de taille recommandés spécifiques au modèle<br>"Custom" |
| `width` | Largeur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur « Custom ». Par défaut : 2048. | INT | Non | 1024 à 6240 (pas de 2) |
| `height` | Hauteur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur « Custom ». Par défaut : 2048. | INT | Non | 1024 à 4992 (pas de 2) |
| `max_images` | Nombre maximal d’images à générer. Avec 1, une seule image est produite. Avec >1, le modèle génère entre 1 et max_images images associées (p. ex., scènes d’histoire, variations de personnages). Le nombre total d’images (entrée + générées) ne peut pas dépasser 15. Par défaut : 1. | INT | Non | 1 à 14 |
| `fail_on_partial` | Si activé, interrompt l’exécution si des images demandées sont manquantes ou renvoie une erreur. Par défaut : false. | BOOLEAN | Non | true / false |
| `seed` | Seed à utiliser pour la génération. Par défaut : 42. | INT | Non | 0 à 2147483647 |
| `watermark` | Indique s’il faut ajouter un filigrane « AI generated » à l’image. Par défaut : false. | BOOLEAN | Non | true / false |
| `thinking` | Active le raisonnement d’optimisation du prompt du modèle (« thinking ») pour une meilleure adhérence. Peut considérablement augmenter le temps de génération — notamment sur Seedream 5.0 Pro. Ne peut être désactivé que pour la génération text-to-image (pas lorsque des images de référence sont fournies). Par défaut : true. | BOOLEAN | Non | true / false |

### Entrées Seedream 4.5 (seedream-4-5-251128)

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size_preset` | Choisissez une taille recommandée. Sélectionnez « Custom » pour utiliser la largeur et la hauteur ci-dessous. Par défaut : premier préréglage recommandé pour ce modèle. | COMBO | Non | Préréglages de taille recommandés spécifiques au modèle<br>"Custom" |
| `width` | Largeur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur « Custom ». Par défaut : 2048. | INT | Non | 1024 à 6240 (pas de 2) |
| `height` | Hauteur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur « Custom ». Par défaut : 2048. | INT | Non | 1024 à 4992 (pas de 2) |
| `max_images` | Nombre maximal d’images à générer. Avec 1, une seule image est produite. Avec >1, le modèle génère entre 1 et max_images images associées (p. ex., scènes d’histoire, variations de personnages). Le nombre total d’images (entrée + générées) ne peut pas dépasser 15. Par défaut : 1. | INT | Non | 1 à 10 |
| `fail_on_partial` | Si activé, interrompt l’exécution si des images demandées sont manquantes ou renvoie une erreur. Par défaut : false. | BOOLEAN | Non | true / false |
| `seed` | Seed à utiliser pour la génération. Par défaut : 42. | INT | Non | 0 à 2147483647 |
| `watermark` | Indique s’il faut ajouter un filigrane « AI generated » à l’image. Par défaut : false. | BOOLEAN | Non | true / false |
| `thinking` | Active le raisonnement d’optimisation du prompt du modèle (« thinking ») pour une meilleure adhérence. Peut considérablement augmenter le temps de génération — notamment sur Seedream 5.0 Pro. Ne peut être désactivé que pour la génération text-to-image (pas lorsque des images de référence sont fournies). Par défaut : true. | BOOLEAN | Non | true / false |

### Entrées Seedream 4.0 (seedream-4-0-250828)

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size_preset` | Choisissez une taille recommandée. Sélectionnez « Custom » pour utiliser la largeur et la hauteur ci-dessous. Par défaut : premier préréglage recommandé pour ce modèle. | COMBO | Non | Préréglages de taille recommandés spécifiques au modèle<br>"Custom" |
| `width` | Largeur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur « Custom ». Par défaut : 2048. | INT | Non | 1024 à 6240 (pas de 2) |
| `height` | Hauteur personnalisée de l’image. La valeur n’est prise en compte que si `size_preset` est défini sur « Custom ». Par défaut : 2048. | INT | Non | 1024 à 4992 (pas de 2) |
| `max_images` | Nombre maximal d’images à générer. Avec 1, une seule image est produite. Avec >1, le modèle génère entre 1 et max_images images associées (p. ex., scènes d’histoire, variations de personnages). Le nombre total d’images (entrée + générées) ne peut pas dépasser 15. Par défaut : 1. | INT | Non | 1 à 10 |
| `fail_on_partial` | Si activé, interrompt l’exécution si des images demandées sont manquantes ou renvoie une erreur. Par défaut : false. | BOOLEAN | Non | true / false |
| `seed` | Seed à utiliser pour la génération. Par défaut : 42. | INT | Non | 0 à 2147483647 |
| `watermark` | Indique s’il faut ajouter un filigrane « AI generated » à l’image. Par défaut : false. | BOOLEAN | Non | true / false |
| `thinking` | Active le raisonnement d’optimisation du prompt du modèle (« thinking ») pour une meilleure adhérence. Peut considérablement augmenter le temps de génération — notamment sur Seedream 5.0 Pro. Ne peut être désactivé que pour la génération text-to-image (pas lorsque des images de référence sont fournies). Par défaut : true. | BOOLEAN | Non | true / false |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Emplacement extensible : image(s) de référence facultative(s) pour la génération image-to-image ou multi-références. Connectez 1..N images (p. ex., `image_1`, `image_2`, ...) ; la limite du nombre d’images dépend du modèle (voir notes ci-dessous). Si une image connectée contient un lot d’images, chaque image du lot compte dans la limite. | IMAGE | Non | 0 à 10 (Seedream 5.0 Pro, Seedream 4.5, Seedream 4.0)<br>0 à 14 (Seedream 5.0 Lite) |

**Remarques :**

- Le `prompt` ne doit pas être vide après suppression des espaces.
- Nombre maximal d’images de référence : 10 pour Seedream 5.0 Pro, Seedream 4.5 et Seedream 4.0 ; 14 pour Seedream 5.0 Lite.
- Chaque image de référence doit avoir un rapport hauteur/largeur compris entre 1:3 et 3:1.
- Lorsque `max_images` est supérieur à 1 (non disponible sur Seedream 5.0 Pro), le nombre total d’images de référence plus les images générées ne peut pas dépasser 15.
- `thinking` ne peut être désactivé que pour la génération text-to-image. Lorsque des images de référence sont fournies, `thinking` doit être activé.
- `width` et `height` ne sont utilisés que lorsque `size_preset` est défini sur « Custom ».
- `prompt_optimization` est uniquement disponible sur Seedream 5.0 Pro.
- `max_images` et `fail_on_partial` sont uniquement disponibles sur Seedream 5.0 Lite, Seedream 4.5 et Seedream 4.0 ; Seedream 5.0 Pro demande toujours une seule image.
- Exigences de résolution (largeur x hauteur) :
  - Seedream 5.0 Pro : entre 0,92 MP (921 600 pixels) et 4,19 MP (4 194 304 pixels).
  - Seedream 5.0 Lite et Seedream 4.5 : au moins 3,68 MP (3 686 400 pixels).
  - Seedream 4.0 : au moins 0,92 MP (921 600 pixels).
  - Tous les modèles non Pro : au maximum 16,78 MP (16 777 216 pixels).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | Le tenseur d’image généré. Lorsque plusieurs images sont générées, elles sont concaténées dans un seul tenseur IMAGE par lots. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV3/fr.md)

---
**Source fingerprint (SHA-256):** `68dd23afdb5720491cef784b22ad66ff0baf80984ea652ea4c13e6c264c029ac`
