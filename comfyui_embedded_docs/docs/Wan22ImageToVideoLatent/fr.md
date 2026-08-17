# Wan22ImageToVideoLatent

Le nœud Wan22ImageToVideoLatent prépare l’entrée latente utilisée pour la génération vidéo Wan 2.2. Il crée un latent vidéo vide avec la largeur, la hauteur et le nombre d’images spécifiés, et, lorsqu’une image de départ est fournie, encode cette image dans les premières images du latent. Il produit également un masque de bruit qui indique quelles images sont déjà remplies par l’image et lesquelles doivent encore être générées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vae` | Le modèle VAE utilisé pour encoder l’image de départ dans l’espace latent. | VAE | Oui | - |
| `width` | La largeur de la vidéo de sortie en pixels (défaut : 1280, pas : 32). | INT | Oui | 32 to MAX_RESOLUTION |
| `height` | La hauteur de la vidéo de sortie en pixels (défaut : 704, pas : 32). | INT | Oui | 32 to MAX_RESOLUTION |
| `length` | Le nombre d’images de la vidéo (défaut : 49, pas : 4). | INT | Oui | 1 to MAX_RESOLUTION |
| `batch_size` | Le nombre de latents vidéo à générer en parallèle (défaut : 1). | INT | Oui | 1 to 4096 |
| `start_image` | Image ou séquence d’images facultative placée dans les premières images du latent vidéo. Seules les `length` premières images sont utilisées. L’image est redimensionnée à `width` x `height` avec un rééchantillonnage bilinéaire et un recadrage centré avant d’être encodée par le VAE. | IMAGE | Non | - |

**Remarque :** Les dimensions spatiales du latent sont `width / 16` et `height / 16`, donc `width` et `height` doivent être divisibles par 16. La dimension temporelle du latent est calculée comme `((length - 1) // 4) + 1` et il possède 48 canaux. Lorsqu’un `start_image` est fourni, l’image encodée remplit les premières images du latent et le `noise_mask` est défini à 0 pour ces images et à 1 pour les images restantes, ce qui indique à l’échantillonneur de conserver les images de départ inchangées et de générer le reste. Lorsqu’aucun `start_image` n’est fourni, le latent est rempli de zéros et aucun masque de bruit n’est inclus.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Le latent vidéo généré, répété `batch_size` fois. Lorsqu’un `start_image` est fourni, il contient également un `noise_mask` marquant les images encodées par l’image (0) et les images à générer (1). | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/fr.md)

---
**Source fingerprint (SHA-256):** `3d05980641eeef2e86df7a845aa8b2bd703882db98fe71adef2746ab34a9d717`
