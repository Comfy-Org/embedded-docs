# ImageCropToMask

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `images` | L’image ou le lot d’images à recadrer. | IMAGE | Oui | — |
| `masks` | Le masque ou le lot de masques qui définit la zone du sujet. Un masque unique est appliqué à toutes les images ; sinon, la taille du lot de masques doit correspondre à celle du lot d’images. Si la résolution du masque diffère de celle de l’image, le masque est automatiquement redimensionné pour correspondre. | MASK | Oui | — |
| `width` | Largeur de sortie en pixels. (défaut : 1024) | INT | Oui | 64 à 4096 (pas 8) |
| `height` | Hauteur de sortie en pixels. (défaut : 1024) | INT | Oui | 64 à 4096 (pas 8) |
| `pad_factor` | Marge supplémentaire autour de la boîte englobante du masque, sous forme de multiplicateur. (défaut : 1.0) | FLOAT | Oui | 1.0 à 2.0 (pas 0.01) |
| `grow_mask` | Agrandit ou réduit le masque de ce nombre de pixels avant le recadrage. Les valeurs positives agrandissent le masque, les valeurs négatives le réduisent. (défaut : 0) | INT | Oui | -32 à 32 (pas 1) |
| `background` | Couleur d’arrière-plan derrière le sujet masqué. (défaut : #000000) | COLOR | Oui | — |

Remarque : La région de recadrage est centrée sur la boîte englobante du masque et son rapport largeur/hauteur correspond à `width` / `height`. Le nœud détecte et corrige automatiquement un masque inversé (pixels de premier plan le long du bord, arrière-plan au centre). Si le masque ne contient aucun pixel de premier plan, le nœud essaie le masque inversé ; si celui-ci est également vide, il émet un avertissement et recadre l’image entière. Une erreur est déclenchée lorsque la taille du lot de masques ne correspond pas à celle du lot d’images et qu’il ne s’agit pas d’un masque unique.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `images` | Les images composites recadrées (sujet masqué sur la couleur d’arrière-plan choisie), redimensionnées à `width` x `height`. La taille du lot correspond au lot d’images d’entrée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropToMask/fr.md)

---
**Source fingerprint (SHA-256):** `fcc14b5db7318699526dd544d404f78f9d1ab362b73769276f113f2b1062b214`
