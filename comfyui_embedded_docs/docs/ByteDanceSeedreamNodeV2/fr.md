> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/fr.md)

Voici la traduction de la documentation technique du nœud ComfyUI **ByteDanceSeedreamNodeV2** :

## Aperçu

Ce nœud génère ou édite des images à l'aide des modèles Seedream de ByteDance (versions 4.0, 4.5 et 5.0). Il peut créer de nouvelles images à partir d'une invite textuelle ou éditer des images existantes en fournissant des images de référence, avec une prise en charge des résolutions allant jusqu'à 4K.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Invite textuelle pour créer ou éditer une image. |
| `model` | COMBO | Oui | `"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` | Version du modèle Seedream à utiliser pour la génération. Chaque modèle possède des capacités et une tarification différentes. |
| `seed` | INT | Non | 0 à 2147483647 | Graine à utiliser pour la génération (par défaut : 0). |
| `watermark` | BOOLEAN | Non | Vrai / Faux | Indique s'il faut ajouter un filigrane "Généré par IA" à l'image (par défaut : Faux). |

### Paramètres spécifiques au modèle

Lorsque vous sélectionnez un modèle, des paramètres supplémentaires deviennent disponibles :

- **Préréglage de taille** : Un menu déroulant pour sélectionner une résolution d'image prédéfinie (par exemple, "2048x2048", "1024x1024"). Les préréglages disponibles dépendent du modèle sélectionné.
- **Largeur** : La largeur de l'image générée en pixels (par défaut : 2048).
- **Hauteur** : La hauteur de l'image générée en pixels (par défaut : 2048).
- **Nombre max. d'images** : Le nombre maximum d'images à générer (par défaut : 1). Lorsqu'il est défini sur 1, la génération séquentielle d'images est désactivée.
- **Images de référence** : Jusqu'à 10 (pour Seedream 4.0 et 4.5) ou 14 (pour Seedream 5.0 Lite) images de référence pour l'édition. Les images doivent avoir un rapport hauteur/largeur compris entre 1:3 et 3:1.
- **Échec en cas de génération partielle** : Si activé, le nœud générera une erreur si toutes les images demandées ne sont pas générées avec succès (par défaut : Faux).

### Contraintes de résolution

- **Seedream 5.0 Lite et 4.5** : La résolution minimale est de 3,68 mégapixels (par exemple, 1920x1920).
- **Seedream 4.0** : La résolution minimale est de 0,92 mégapixel (par exemple, 960x960).
- **Tous les modèles** : La résolution maximale est de 16,78 mégapixels (par exemple, 4096x4096).

### Contraintes du nombre d'images

- Le nombre total d'images de référence plus les images générées ne peut pas dépasser 15.
- Pour Seedream 5.0 Lite, un maximum de 14 images de référence sont prises en charge.
- Pour Seedream 4.0 et 4.5, un maximum de 10 images de référence sont prises en charge.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `image` | IMAGE | L'image générée ou éditée sous forme de tenseur. Si plusieurs images ont été demandées, elles sont concaténées en un seul lot. |