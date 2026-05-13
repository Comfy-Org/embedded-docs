> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ImageNode/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI, en respectant vos règles :

## Aperçu

Générez des images en utilisant le modèle Flux.2 [pro] ou Flux.2 [max] à partir d'une invite textuelle et d'images de référence optionnelles. Ce nœud envoie votre requête à l'API BFL, interroge le résultat et renvoie l'image générée sous forme de tenseur.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Invite pour la génération ou l'édition d'image (par défaut : chaîne vide). |
| `model` | COMBO | Oui | `"Flux.2 [pro]"`<br>`"Flux.2 [max]"` | La version du modèle Flux.2 à utiliser. La sélection d'un modèle déverrouille des paramètres supplémentaires pour la largeur, la hauteur et les images de référence optionnelles. |
| `seed` | INT | Oui | 0 à 18446744073709551615 | La graine aléatoire utilisée pour créer le bruit. Peut être définie pour se randomiser après chaque génération (par défaut : 0). |

**Paramètres supplémentaires (déverrouillés par la sélection du `model`) :**

Lorsque vous sélectionnez un modèle, les paramètres suivants deviennent disponibles :

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model.width` | INT | Oui | 256 à 1440 | La largeur de l'image générée en pixels. |
| `model.height` | INT | Oui | 256 à 1440 | La hauteur de l'image générée en pixels. |
| `model.images` | IMAGE | Non | 0 à 8 images | Images de référence optionnelles pour guider la génération. Un maximum de 8 images est pris en charge. |

**Contraintes :**
- Le nombre maximum d'images de référence est de 8. Si plus de 8 images sont fournies, une erreur sera générée.
- Les valeurs `model.width` et `model.height` affectent le coût de la génération (voir la logique du badge de prix dans le code source).

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `image` | IMAGE | L'image générée sous forme de tenseur, téléchargée depuis le résultat de l'API BFL. |

---
**Source fingerprint (SHA-256):** `664ddf45d42f64e4882cc959018f7874915325f2d46519c6bb9a0c5a501228f7`
