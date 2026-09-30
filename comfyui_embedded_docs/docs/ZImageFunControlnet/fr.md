# ZImageFunControlnet

ZImageFunControlnet applique un patch de réseau de contrôle à un modèle de base afin qu’il puisse guider le processus de génération ou d’édition d’image. Il combine un modèle, un patch de modèle et un VAE, et vous permet de contrôler l’intensité avec laquelle l’effet de contrôle influence le résultat. Les entrées facultatives image, image d’inpainting et masque permettent des modifications plus ciblées. Le nœud fonctionne avec les patches Z-Image ControlNet et avec les patches Qwen Image 2.1 Fun ControlNet chargés via le nœud Load Model Patch.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de base utilisé pour le processus de génération. | MODEL | Oui | - |
| `modèle_patch` | Un patch de modèle spécialisé qui applique le guidage du réseau de contrôle. | MODEL_PATCH | Oui | - |
| `vae` | L’autoencodeur variationnel utilisé pour l’encodage et le décodage des images. | VAE | Oui | - |
| `force` | L’intensité de l’influence du réseau de contrôle. Les valeurs positives appliquent l’effet, tandis que les valeurs négatives peuvent l’inverser (par défaut : 1.0). | FLOAT | Oui | -10.0 à 10.0 (pas 0.01) |
| `image` | Une image de base facultative pour guider le processus de génération. | IMAGE | Non | - |
| `image_de_repeinture` | Une image facultative utilisée spécifiquement pour l’inpainting des zones définies par un masque. | IMAGE | Non | - |
| `mask` | Un masque facultatif qui définit les zones d’une image à éditer ou à traiter par inpainting. | MASK | Non | - |
| `start_percent` | Le point dans le processus de débruitage, exprimé comme une fraction du nombre total d’étapes d’échantillonnage, où le réseau de contrôle commence à prendre effet (par défaut : 0.0). | FLOAT | Non | 0.0 à 1.0 (pas 0.001) |
| `end_percent` | Le point dans le processus de débruitage où le réseau de contrôle cesse de prendre effet (par défaut : 1.0). | FLOAT | Non | 0.0 à 1.0 (pas 0.001) |

**Remarque :** Le paramètre `inpaint_image` est généralement utilisé conjointement avec un `mask` pour spécifier le contenu à inpaint. Le comportement du nœud peut changer selon les entrées facultatives fournies (par exemple, utiliser `image` pour le guidage ou utiliser `image`, `mask` et `inpaint_image` pour l’inpainting). Les valeurs `start_percent` et `end_percent` limitent le réseau de contrôle à une fenêtre du processus de débruitage, et en dehors de cette fenêtre le modèle est échantillonné sans le patch. Si `strength` vaut 0, ou si aucun de `image`, `inpaint_image` et `mask` n’est connecté, le nœud renvoie le modèle de base inchangé. Pour les patches Z-Image Control, un masque fourni est inversé (1.0 - mask) avant utilisation, tandis qu’un patch Qwen Image 2.1 Fun ControlNet utilise le masque tel quel. Ce nœud est marqué comme expérimental.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle avec le patch de réseau de contrôle appliqué, prêt à être utilisé dans un pipeline d’échantillonnage. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/fr.md)

---
**Source fingerprint (SHA-256):** `9673b8b6e091713bcc93fe5fd1cfed12e6941571d1017e10ac94c19e1afd4ca1`
