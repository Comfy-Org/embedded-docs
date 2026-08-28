# LTXVImgToVideoInplace

LTXVImgToVideoInplace encode une image d'entrée dans l'espace latent et place ces trames encodées au début d'une vidéo latente existante. La valeur `strength` contrôle la force avec laquelle l'image encodée conditionne ces trames initiales, et lorsque `bypass` est activé, le latent d'entrée est retourné inchangé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vae` | Le modèle VAE utilisé pour encoder l'image d'entrée dans l'espace latent. | VAE | Oui | - |
| `image` | L'image d'entrée à encoder et utilisée pour conditionner le latent vidéo. | IMAGE | Oui | - |
| `latent` | La représentation vidéo latente cible à modifier. | LATENT | Oui | - |
| `force` | Contrôle la force avec laquelle l'image encodée conditionne les trames initiales du latent. Une valeur de 1,0 conditionne entièrement les trames initiales avec l'image encodée, tandis que des valeurs plus faibles les conditionnent moins fortement. Le masque de bruit pour les trames initiales est défini sur `1.0 - strength`. (défaut : 1,0) | FLOAT | Non | 0.0 - 1.0 |
| `contournement` | Contourne le conditionnement. Lorsqu'il est activé, le nœud retourne le latent d'entrée inchangé. (défaut : False) | BOOLEAN | Non | True or False |

**Remarque :** L'`image` sera automatiquement redimensionnée pour correspondre aux dimensions spatiales requises par le `vae` pour l'encodage, en fonction de la largeur et de la hauteur de l'entrée `latent`. Seuls les canaux RVB de l'`image` sont utilisés pour l'encodage.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `latent` | La représentation vidéo latente résultante. Lorsque `bypass` est désactivé, elle contient les `samples` mis à jour et un `noise_mask` qui applique la force de conditionnement aux trames initiales. Lorsque `bypass` est activé, il s'agit du latent d'entrée retourné inchangé. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/fr.md)

---
**Source fingerprint (SHA-256):** `69faa4b2e7b0fedeee531dc5a8809e23a79c9ce03e9760afb865160594fef30d`
