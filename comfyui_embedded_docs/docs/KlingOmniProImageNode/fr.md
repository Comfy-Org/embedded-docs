> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageNode/fr.md)

Le nœud Kling Omni Image (Pro) crée ou modifie des images à l'aide du dernier modèle d'IA Kling. Il génère des images à partir d'une description textuelle et peut éventuellement utiliser des images de référence pour guider le style ou le contenu. Le nœud envoie une requête à une API externe, qui traite la tâche et renvoie la ou les images finales.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
| :--- | :--- | :--- | :--- | :--- |
| `model_name` | COMBO | Oui | `"kling-v3-omni"`<br>`"kling-image-o1"` | Le modèle d'IA Kling spécifique à utiliser pour la génération d'images. |
| `prompt` | STRING | Oui | - | Une description textuelle du contenu de l'image. Cela peut inclure des descriptions à la fois positives et négatives. Le texte doit contenir entre 1 et 2500 caractères. |
| `resolution` | COMBO | Oui | `"1K"`<br>`"2K"`<br>`"4K"` | La résolution cible de l'image générée. Remarque : la résolution 4K n'est pas prise en charge pour le modèle `kling-image-o1`. |
| `aspect_ratio` | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"21:9"` | Le rapport hauteur/largeur souhaité (largeur par rapport à la hauteur) pour l'image générée. |
| `series_amount` | COMBO | Oui | `"disabled"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"` | Générer une série d'images. Cette fonctionnalité n'est pas prise en charge pour le modèle `kling-image-o1`. (par défaut : "disabled") |
| `reference_images` | IMAGE | Non | - | Jusqu'à 10 images de référence supplémentaires. Chaque image doit avoir une largeur et une hauteur d'au moins 300 pixels, et son rapport hauteur/largeur doit être compris entre 1:2,5 et 2,5:1. |
| `seed` | INT | Non | 0 à 2147483647 | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. (par défaut : 0) |

## Sorties

| Nom de la sortie | Type de données | Description |
| :--- | :--- | :--- |
| `image` | IMAGE | La ou les images finales générées ou modifiées par le modèle d'IA Kling. Si une série a été demandée, plusieurs images sont renvoyées sous forme de lot. |

---
**Source fingerprint (SHA-256):** `7bbed260436bc60e284c99e091cd28b2b0cf50e98e876f94278f1ac2834e61f8`
