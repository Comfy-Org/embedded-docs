> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerPreciseV2Node/fr.md)

Voici la traduction en français de la documentation du nœud Magnific Image Upscale (Precise V2) :

Le nœud Magnific Image Upscale (Precise V2) effectue un agrandissement d'image haute fidélité avec un contrôle précis de la netteté, du grain et de l'amélioration des détails. Il traite les images via une API externe, prenant en charge une résolution de sortie maximale de 10060×10060 pixels. Le nœud propose différents styles de traitement et peut automatiquement réduire l'échelle de l'entrée si la sortie demandée dépasse la taille maximale autorisée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à agrandir. Une seule image est requise. Les dimensions minimales sont de 160x160 pixels. Le rapport hauteur/largeur doit être compris entre 1:3 et 3:1. |
| `facteur d’agrandissement` | STRING | Oui | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` | Le multiplicateur d'agrandissement souhaité. |
| `style` | STRING | Oui | `"sublime"`<br>`"photo"`<br>`"photo_denoiser"` | Le style de traitement. "sublime" est destiné à un usage général, "photo" est optimisé pour les photographies, et "photo_denoiser" est destiné aux photos bruitées. |
| `netteté` | INT | Non | 0 à 100 | Contrôle l'intensité de l'accentuation de l'image pour améliorer la définition des contours et la clarté. Des valeurs plus élevées produisent un résultat plus net. Par défaut : 7. |
| `grain intelligent` | INT | Non | 0 à 100 | Ajoute un grain intelligent ou une amélioration de texture pour éviter que l'image agrandie ne paraisse trop lisse ou artificielle. Par défaut : 7. |
| `ultra-détail` | INT | Non | 0 à 100 | Contrôle la quantité de détails fins, de textures et de micro-détails ajoutés lors du processus d'agrandissement. Par défaut : 30. |
| `réduction automatique` | BOOLEAN | Non | - | Lorsqu'il est activé, le nœud réduit automatiquement l'échelle de l'image d'entrée si les dimensions de sortie calculées dépassent la résolution maximale autorisée de 10060x10060 pixels. Cela permet d'éviter les erreurs mais peut affecter la qualité. Par défaut : Faux. |

**Remarque :** Si `auto_downscale` est désactivé et que la taille de sortie demandée (dimensions d'entrée × `scale_factor`) dépasse 10060x10060 pixels, le nœud générera une erreur.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `image` | IMAGE | L'image agrandie résultante. |

---
**Source fingerprint (SHA-256):** `cceff30e9702c6a24ab8102698c59f1afb20ec50e7f279b3c0d50befc9673b24`
