# Magnific Image Upscale (Creative)

Ce nœud utilise le service Magnific AI pour améliorer et augmenter la résolution d'une image de manière créative. Il permet de guider l'amélioration avec une invite textuelle, de choisir un style spécifique pour optimiser le traitement et de contrôler divers aspects du processus créatif comme le détail, la ressemblance avec l'original et la force de stylisation. Le nœud produit en sortie une image à résolution augmentée selon le facteur choisi (2x, 4x, 8x ou 16x), avec une taille de sortie maximale de 25,3 mégapixels.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à mettre à l'échelle supérieure et à améliorer. | IMAGE | Oui | - |
| `prompt` | Une description textuelle pour guider l'amélioration créative de l'image. La valeur par défaut est une chaîne vide (aucune invite n'est envoyée dans ce cas). | STRING | Oui | - |
| `scale_factor` | Le facteur par lequel augmenter les dimensions de l'image. | COMBO | Oui | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `optimized_for` | Le style ou type de contenu pour lequel optimiser le processus d'amélioration. | COMBO | Oui | `"standard"`<br>`"soft_portraits"`<br>`"hard_portraits"`<br>`"art_n_illustration"`<br>`"videogame_assets"`<br>`"nature_n_landscapes"`<br>`"films_n_photography"`<br>`"3d_renders"`<br>`"science_fiction_n_horror"` |
| `creativity` | Contrôle le niveau d'interprétation créative appliqué à l'image (par défaut : 0). | INT | Oui | -10 à 10 |
| `hdr` | Le niveau de définition et de détail (par défaut : 0). | INT | Oui | -10 à 10 |
| `resemblance` | Le niveau de ressemblance avec l'image d'origine (par défaut : 0). | INT | Oui | -10 à 10 |
| `fractality` | La force de l'invite et la complexité par pixel carré (par défaut : 0). | INT | Oui | -10 à 10 |
| `engine` | Le moteur d'IA spécifique à utiliser pour le traitement. Il s'agit d'un paramètre avancé. | COMBO | Oui | `"automatic"`<br>`"magnific_illusio"`<br>`"magnific_sharpy"`<br>`"magnific_sparkle"` |
| `auto_downscale` | Réduit automatiquement la taille de l'image d'entrée si la sortie dépasserait la limite maximale de pixels (par défaut : False). Il s'agit d'un paramètre avancé. | BOOLEAN | Oui | - |

**Contraintes :**

* L'entrée `image` doit être exactement une image.
* L'image d'entrée doit avoir une hauteur et une largeur minimales de 160 pixels.
* Le rapport d'aspect de l'image d'entrée doit être compris entre 1:3 et 3:1.
* La taille finale de sortie (dimensions d'entrée multipliées par `scale_factor`) ne peut pas dépasser 25 300 000 pixels. Si cette limite venait à être dépassée :
  - Lorsque `auto_downscale` est activé, le nœud réduit automatiquement la taille de l'image d'entrée (la réduction supplémentaire est limitée à 2x au maximum) ou utilise un `scale_factor` inférieur afin que la sortie reste dans la limite.
  - Lorsque `auto_downscale` est désactivé, le nœud lève une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image de sortie améliorée de manière créative et dont la résolution a été augmentée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerCreativeNode/fr.md)

---
**Source fingerprint (SHA-256):** `36c38e87f9f1e568c78cf794aeb0a268c6d25d639006eb2cf18ee040d3071ad4`
