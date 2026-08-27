# Magnific Image Upscale (Creative)

Ce nœud utilise le service Magnific AI pour agrandir et améliorer créativement une image. Il vous permet de guider l’amélioration avec une invite texte, de choisir un style spécifique à optimiser et de contrôler divers aspects du processus créatif comme le détail, la ressemblance avec l’original et l’intensité de stylisation. Le nœud produit une image agrandie selon le facteur choisi (2x, 4x, 8x ou 16x), avec une taille de sortie maximale de 25,3 mégapixels.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L’image d’entrée à agrandir et à améliorer. | IMAGE | Oui | - |
| `prompt` | Une description textuelle pour guider l’amélioration créative de l’image. Ce paramètre est facultatif (par défaut : vide). | STRING | Non | - |
| `facteur d’agrandissement` | Le facteur par lequel les dimensions de l’image sont agrandies. | COMBO | Oui | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `optimisé pour` | Le style ou le type de contenu pour lequel optimiser le processus d’amélioration. | COMBO | Oui | `"standard"`<br>`"soft_portraits"`<br>`"hard_portraits"`<br>`"art_n_illustration"`<br>`"videogame_assets"`<br>`"nature_n_landscapes"`<br>`"films_n_photography"`<br>`"3d_renders"`<br>`"science_fiction_n_horror"` |
| `créativité` | Contrôle le niveau d’interprétation créative appliquée à l’image (par défaut : 0). | INT | Non | -10 à 10 |
| `hdr` | Le niveau de définition et de détail (par défaut : 0). | INT | Non | -10 à 10 |
| `ressemblance` | Le niveau de ressemblance avec l’image d’origine (par défaut : 0). | INT | Non | -10 à 10 |
| `fractalité` | La force de l’invite et la complexité par pixel carré (par défaut : 0). | INT | Non | -10 à 10 |
| `moteur` | Le moteur IA spécifique à utiliser pour le traitement. Ce paramètre est avancé. | COMBO | Oui | `"automatic"`<br>`"magnific_illusio"`<br>`"magnific_sharpy"`<br>`"magnific_sparkle"` |
| `réduction automatique` | Réduire automatiquement la taille de l’image d’entrée si la sortie dépasse la limite maximale de pixels (par défaut : False). Ce paramètre est avancé. | BOOLEAN | Non | - |

**Contraintes :**

* L’image `image` d’entrée doit être exactement une seule image.
* L’image d’entrée doit avoir une hauteur et une largeur minimales de 160 pixels.
* Le rapport hauteur/largeur de l’image d’entrée doit être compris entre 1:3 et 3:1.
* La taille finale de sortie (dimensions d’entrée multipliées par le `scale_factor`) ne peut pas dépasser 25 300 000 pixels. Si cette limite est dépassée :
  - Lorsque `auto_downscale` est activé, le nœud réduit automatiquement la taille de l’image d’entrée (d’au plus 2x) ou utilise un `scale_factor` inférieur afin que la sortie reste dans la limite.
  - Lorsque `auto_downscale` est désactivé, le nœud lève une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L’image de sortie agrandie et améliorée de manière créative. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerCreativeNode/fr.md)

---
**Source fingerprint (SHA-256):** `36c38e87f9f1e568c78cf794aeb0a268c6d25d639006eb2cf18ee040d3071ad4`
