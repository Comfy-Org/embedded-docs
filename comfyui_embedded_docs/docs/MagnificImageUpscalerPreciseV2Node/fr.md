# Magnific Image Upscale (Precise V2)

Le nœud Magnific Image Upscale (Precise V2) effectue une mise à l'échelle d'image haute fidélité avec un contrôle fin de la netteté, du grain et de l'amélioration des détails. Il traite les images via une API externe, prenant en charge une résolution de sortie maximale de 10060×10060 pixels. Le nœud propose différents styles de traitement et peut automatiquement réduire la taille de l'image d'entrée si la sortie demandée dépasse la taille maximale autorisée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à mettre à l'échelle. Une seule image est requise. Les dimensions minimales sont de 160x160 pixels. Le rapport hauteur/largeur doit être compris entre 1:3 et 3:1. | IMAGE | Oui | - |
| `facteur d’agrandissement` | Le facteur de mise à l'échelle souhaité. | COMBO | Oui | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `style` | Style de traitement : sublime pour un usage général, photo pour les photographies, photo_denoiser pour les photos bruitées. | COMBO | Oui | `"sublime"`<br>`"photo"`<br>`"photo_denoiser"` |
| `netteté` | Intensité de la netteté de l'image. Des valeurs plus élevées augmentent la définition des contours et la clarté. Défaut : 7. | INT | Non | 0 à 100 |
| `grain intelligent` | Amélioration intelligente du grain/des textures pour éviter que l'image ne paraisse trop lisse ou artificielle. Défaut : 7. | INT | Non | 0 à 100 |
| `ultra-détail` | Contrôle les détails fins, les textures et les micro-détails ajoutés lors de la mise à l'échelle. Défaut : 30. | INT | Non | 0 à 100 |
| `réduction automatique` | Réduit automatiquement l'image d'entrée si la sortie dépasse la résolution maximale. Défaut : False. | BOOLEAN | Non | - |

**Remarque :** Si `auto_downscale` est désactivé et que la taille de sortie demandée (dimensions d'entrée × `scale_factor`) dépasse 10060x10060 pixels, le nœud générera une erreur. Lorsque `auto_downscale` est activé, le nœud tentera de trouver un facteur d'échelle optimal qui minimise la perte de qualité.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image mise à l'échelle résultante. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerPreciseV2Node/fr.md)

---
**Source fingerprint (SHA-256):** `aeb2b3569fd7b1d2417890586b8ac84ff921c4405f63f190188af93044ccfd28`
