# Transfert de style d'image Magnific

Ce nœud applique le style visuel d'une image de référence à votre image d'entrée. Il utilise un service d'IA externe pour traiter les images, vous permettant de contrôler la force du transfert de style et la préservation de la structure de l'image d'origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image à laquelle appliquer le transfert de style. | IMAGE | Oui | - |
| `reference_image` | L'image de référence dont extraire le style. | IMAGE | Oui | - |
| `prompt` | Une invite textuelle facultative pour guider le transfert de style. | STRING | Non | - |
| `style_strength` | Pourcentage de force du style (par défaut : 100). | INT | Non | 0 à 100 |
| `structure_strength` | Maintient la structure de l'image d'origine (par défaut : 50). | INT | Non | 0 à 100 |
| `flavor` | Variante du transfert de style. | COMBO | Non | "faithful"<br>"gen_z"<br>"psychedelia"<br>"detaily"<br>"clear"<br>"donotstyle"<br>"donotstyle_sharp" |
| `engine` | Sélection du moteur de traitement. | COMBO | Non | "balanced"<br>"definio"<br>"illusio"<br>"3d_cartoon"<br>"colorful_anime"<br>"caricature"<br>"real"<br>"super_real"<br>"softy" |
| `portrait_mode` | Active le mode portrait pour les améliorations faciales. | COMBO | Non | "disabled"<br>"enabled" |
| `portrait_style` | Style visuel appliqué aux images de portrait. Cette entrée n'est disponible que lorsque `portrait_mode` est réglé sur "enabled". | COMBO | Non | "standard"<br>"pop"<br>"super_pop" |
| `portrait_beautifier` | Intensité de l'embellissement facial sur les portraits. Cette entrée n'est disponible que lorsque `portrait_mode` est réglé sur "enabled". | COMBO | Non | "none"<br>"beautify_face"<br>"beautify_face_max" |
| `fixed_generation` | Lorsqu'il est désactivé, chaque génération introduit un certain degré d'aléatoire, conduisant à des résultats plus diversifiés (par défaut : True). | BOOLEAN | Non | - |

**Contraintes :**

* Exactement une `image` et une `reference_image` sont requises.
* Les deux images doivent avoir un rapport hauteur/largeur compris entre 1:3 et 3:1.
* Les deux images doivent avoir une hauteur et une largeur minimales de 160 pixels.
* Les paramètres `portrait_style` et `portrait_beautifier` ne sont actifs et requis que lorsque `portrait_mode` est réglé sur "enabled".

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image résultante après application du transfert de style. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageStyleTransferNode/fr.md)

---
**Source fingerprint (SHA-256):** `4ae400183618953c369d089d39b878f0a24592967c29d779c577fb8b7339dea8`
