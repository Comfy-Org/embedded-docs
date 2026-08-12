# Latent AV MiniMax H3 Vidéo+Audio Vide

Ce nœud crée un latent vide qui combine à la fois les informations vidéo et audio pour le modèle MiniMax H3. Vous définissez la largeur, la hauteur et la longueur du contenu, et le nœud produit un latent vide que le modèle peut utiliser comme point de départ pour la génération. La durée (longueur) est automatiquement ajustée pour correspondre à la grille de trames requise par le modèle de 17k+5 trames à 24 fps.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `largeur` | La largeur du latent en pixels. Les valeurs doivent être des multiples de 32. Défaut : 1344. | INT | Oui | 32 - MAX_RESOLUTION (pas 32) |
| `hauteur` | La hauteur du latent en pixels. Les valeurs doivent être des multiples de 32. Défaut : 768. | INT | Oui | 32 - MAX_RESOLUTION (pas 32) |
| `longueur` | Nombre de trames à 24 fps, arrondi à la grille 17k+5 du modèle (124 = ~5 s ; la plage entraînée est d'environ 124 à 362, les valeurs plus longues ne sont pas testées). Défaut : 124. | INT | Oui | 5 - 3600 (pas 17) |

Remarque : la valeur `length` est arrondie au nombre de trames supérieur qui correspond à la grille 17k+5 du modèle (17 x k + 5 trames, par exemple 5, 22, 39, 56, 73, 90, 107, 124, etc.). Les valeurs `width` et `height` doivent être des multiples de 32. La résolution maximale est la valeur définie par le système dans ComfyUI.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `latent` | Le latent vidéo+audio conjoint vide généré pour MiniMax H3, dimensionné selon la largeur, la hauteur et la longueur d'entrée. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxH3LatentAV/fr.md)

---
**Source fingerprint (SHA-256):** `ee24f4ac630858d87b9b98bb402689a5790e0ed882ec47dffe7b497216e37a5c`
