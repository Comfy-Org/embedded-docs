# Magnific Améliorateur de Peau d’Image

Voici la traduction en français de la documentation du nœud Magnific Image Skin Enhancer :

Le nœud Magnific Image Skin Enhancer applique un traitement IA spécialisé aux portraits afin d'améliorer l'apparence de la peau. Il propose trois modes distincts pour différents objectifs d'amélioration : créatif pour des effets artistiques, fidèle pour préserver l'aspect original, et flexible pour des améliorations ciblées comme l'éclairage ou le réalisme. Le nœud télécharge l'image vers une API externe pour le traitement et renvoie le résultat amélioré.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | Le portrait à améliorer. | IMAGE | Oui | - |
| `sharpen` | Niveau d'intensité de la netteté (par défaut : 0). | INT | Non | 0 à 100 |
| `smart_grain` | Niveau d'intensité du grain intelligent (par défaut : 2). | INT | Non | 0 à 100 |
| `mode` | Le mode de traitement à utiliser. `"creative"` est destiné à l'amélioration artistique, `"faithful"` à la préservation de l'aspect original, et `"flexible"` à l'optimisation ciblée. | COMBO | Oui | `"creative"`<br>`"faithful"`<br>`"flexible"` |
| `skin_detail` | Niveau d'amélioration des détails de la peau. Cette entrée n'est disponible et requise que lorsque le `mode` est défini sur `"faithful"` (par défaut : 80). | INT | Non | 0 à 100 |
| `optimized_for` | Cible d'optimisation de l'amélioration. Cette entrée n'est disponible et requise que lorsque le `mode` est défini sur `"flexible"`. | COMBO | Non | `"enhance_skin"`<br>`"improve_lighting"`<br>`"enhance_everything"`<br>`"transform_to_real"`<br>`"no_make_up"` |

**Contraintes :**

* Le nœud accepte exactement une image en entrée.
* L'image d'entrée doit avoir une hauteur et une largeur minimales de 160 pixels.
* Le rapport hauteur/largeur de l'image d'entrée doit être compris entre 1:3 et 3:1 (validation non stricte).
* Le paramètre `skin_detail` n'est actif que lorsque le `mode` est défini sur `"faithful"`.
* Le paramètre `optimized_for` n'est actif que lorsque le `mode` est défini sur `"flexible"`.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `image` | Le portrait amélioré. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageSkinEnhancerNode/fr.md)

---
**Source fingerprint (SHA-256):** `e02cae2e119ddab931b790865889adf53f47a2ebb03d488477c289dfda7204f5`
