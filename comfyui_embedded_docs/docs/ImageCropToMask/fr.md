# Recadrer l’image selon le masque

Recadre une image sur la boîte englobante de son masque, produisant un sujet centré sur une couleur d’arrière-plan unie. Le nœud compose l’image masquée sur l’arrière-plan choisi et redimensionne le résultat aux dimensions de sortie spécifiées, ce qui le rend adapté aux pipelines 3D qui attendent un sujet centré, sans arrière-plan, à une résolution fixe.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | L’image d’entrée ou le lot d’images à recadrer. | IMAGE | Oui | — |
| `masques` | Le masque ou le lot de masques qui définit la zone du sujet. Un seul masque est appliqué à toutes les images ; sinon, la taille du lot de masques doit correspondre à celle du lot d’images. Si la résolution du masque diffère de celle de l’image, le masque est automatiquement redimensionné pour correspondre. | MASK | Oui | — |
| `largeur` | Largeur de sortie en pixels. (par défaut : 1024) | INT | Oui | 64 à 4096 (pas de 8) |
| `hauteur` | Hauteur de sortie en pixels. (par défaut : 1024) | INT | Oui | 64 à 4096 (pas de 8) |
| `pad_factor` | Marge supplémentaire autour de la boîte englobante du masque, sous forme de multiplicateur. (par défaut : 1.0) | FLOAT | Oui | 1.0 à 2.0 (pas de 0.01) |
| `grow_mask` | Agrandit ou réduit le masque de ce nombre de pixels avant le recadrage. Les valeurs positives agrandissent le masque, les valeurs négatives le réduisent. (par défaut : 0) | INT | Oui | -32 à 32 (pas de 1) |
| `arrière-plan` | Couleur d’arrière-plan derrière le sujet masqué. (par défaut : #000000) | COLOR | Oui | — |

Remarque : La région de recadrage est centrée sur la boîte englobante du masque et son rapport d’aspect correspond à `width` / `height`. Le nœud détecte et corrige automatiquement un masque inversé (pixels de premier plan sur le bord, arrière-plan au centre). Si le masque ne contient aucun pixel de premier plan, le nœud essaie le masque inversé ; si celui-ci est également vide, il journalise un avertissement et recadre l’image entière. Une erreur est levée lorsque la taille du lot de masques ne correspond pas à celle du lot d’images et qu’il ne s’agit pas d’un masque unique.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `images` | Les images composites recadrées (sujet masqué sur la couleur d’arrière-plan choisie), redimensionnées à `width` x `height`. La taille du lot correspond à celle du lot d’images d’entrée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropToMask/fr.md)

---
**Source fingerprint (SHA-256):** `fcc14b5db7318699526dd544d404f78f9d1ab362b73769276f113f2b1062b214`
