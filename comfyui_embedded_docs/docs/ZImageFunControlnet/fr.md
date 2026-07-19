# ZImageFunControlnet

Voici la traduction en français de la documentation du nœud ZImageFunControlnet :

Le nœud ZImageFunControlnet applique un réseau de contrôle spécialisé pour influencer le processus de génération ou d'édition d'images. Il utilise un modèle de base, un correctif de modèle et un VAE, vous permettant d'ajuster la force de l'effet de contrôle. Ce nœud peut fonctionner avec une image de base, une image d'incrustation et un masque pour des modifications plus ciblées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de base utilisé pour le processus de génération. | MODEL | Oui | - |
| `modèle_patch` | Un modèle de correctif spécialisé qui applique les directives du réseau de contrôle. | MODEL_PATCH | Oui | - |
| `vae` | L'autoencodeur variationnel utilisé pour encoder et décoder les images. | VAE | Oui | - |
| `force` | La force de l'influence du réseau de contrôle. Les valeurs positives appliquent l'effet, tandis que les valeurs négatives peuvent l'inverser (par défaut : 1.0). | FLOAT | Oui | -10.0 à 10.0 |
| `image` | Une image de base facultative pour guider le processus de génération. | IMAGE | Non | - |
| `image_de_repeinture` | Une image facultative utilisée spécifiquement pour l'incrustation dans les zones définies par un masque. | IMAGE | Non | - |
| `mask` | Un masque facultatif qui définit les zones d'une image à éditer ou à incruster. | MASK | Non | - |

**Remarque :** Le paramètre `inpaint_image` est généralement utilisé conjointement avec un `mask` pour spécifier le contenu de l'incrustation. Le comportement du nœud peut changer en fonction des entrées facultatives fournies (par exemple, utiliser `image` pour le guidage ou utiliser `image`, `mask` et `inpaint_image` pour l'incrustation).

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle avec le correctif du réseau de contrôle appliqué, prêt à être utilisé dans un pipeline d'échantillonnage. | MODEL |
| `positive` | Le conditionnement positif, potentiellement modifié par les entrées du réseau de contrôle. | CONDITIONING |
| `negative` | Le conditionnement négatif, potentiellement modifié par les entrées du réseau de contrôle. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/fr.md)

---
**Source fingerprint (SHA-256):** `465f9eb0dd60af23e6cdc2031579e404b4fed021738e592ee6acbb6ee57e83a0`
