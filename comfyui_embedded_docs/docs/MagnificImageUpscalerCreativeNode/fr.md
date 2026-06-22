# Magnific Image Upscale (Creative)

Ce nœud utilise le service IA Magnific pour agrandir et améliorer de manière créative une image. Il vous permet de guider l'amélioration avec un texte descriptif, de choisir un style spécifique à optimiser, et de contrôler divers aspects du processus créatif comme le niveau de détail, la ressemblance avec l'original et la force de stylisation. Le nœud produit une image agrandie au facteur choisi (2x, 4x, 8x ou 16x), avec une taille de sortie maximale de 25,3 mégapixels.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à agrandir et améliorer. | IMAGE | Oui | - |
| `prompt` | Une description textuelle pour guider l'amélioration créative de l'image. Ce paramètre est facultatif (par défaut : vide). | STRING | Non | - |
| `facteur d’agrandissement` | Le facteur d'agrandissement des dimensions de l'image. | COMBO | Oui | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `optimisé pour` | Le style ou type de contenu pour lequel optimiser le processus d'amélioration. | COMBO | Oui | `"standard"`<br>`"soft_portraits"`<br>`"hard_portraits"`<br>`"art_n_illustration"`<br>`"videogame_assets"`<br>`"nature_n_landscapes"`<br>`"films_n_photography"`<br>`"3d_renders"`<br>`"science_fiction_n_horror"` |
| `créativité` | Contrôle le niveau d'interprétation créative appliqué à l'image (par défaut : 0). | INT | Non | -10 à 10 |
| `hdr` | Le niveau de définition et de détail (par défaut : 0). | INT | Non | -10 à 10 |
| `ressemblance` | Le niveau de ressemblance avec l'image originale (par défaut : 0). | INT | Non | -10 à 10 |
| `fractalité` | La force du texte descriptif et la complexité par pixel carré (par défaut : 0). | INT | Non | -10 à 10 |
| `moteur` | Le moteur IA spécifique à utiliser pour le traitement. Il s'agit d'un paramètre avancé. | COMBO | Oui | `"automatic"`<br>`"magnific_illusio"`<br>`"magnific_sharpy"`<br>`"magnific_sparkle"` |
| `réduction automatique` | Lorsqu'il est activé, le nœud réduit automatiquement l'image d'entrée si l'agrandissement demandé dépasse la taille de sortie maximale autorisée de 25,3 mégapixels. Il s'agit d'un paramètre avancé (par défaut : Faux). | BOOLEAN | Non | - |

**Contraintes :**

* L'`image` d'entrée doit être exactement une seule image.
* L'image d'entrée doit avoir une hauteur et une largeur minimales de 160 pixels.
* Le rapport hauteur/largeur de l'image d'entrée doit être compris entre 1:3 et 3:1.
* La taille de sortie finale (dimensions d'entrée multipliées par le `scale_factor`) ne peut pas dépasser 25 300 000 pixels. Si `auto_downscale` est désactivé et que cette limite serait dépassée, le nœud générera une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image de sortie agrandie et améliorée de manière créative. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerCreativeNode/fr.md)

---
**Source fingerprint (SHA-256):** `f5f046347c2992a2589153e803de14fc23b27187864b45eb566556418ebc161c`
