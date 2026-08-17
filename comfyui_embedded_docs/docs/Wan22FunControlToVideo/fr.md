# Wan22FunControlToVideo

Le nœud Wan22FunControlToVideo prépare les représentations de conditionnement et latentes pour la génération vidéo à l'aide de l'architecture du modèle vidéo Wan. Il traite les entrées de conditionnement positives et négatives ainsi que des images de référence et des vidéos de contrôle optionnelles pour créer les représentations nécessaires dans l'espace latent pour la synthèse vidéo. Le nœud gère la mise à l'échelle spatiale et les dimensions temporelles afin de générer des données de conditionnement appropriées pour les modèles vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Entrée de conditionnement positive pour guider la génération vidéo | CONDITIONING | Oui | - |
| `negative` | Entrée de conditionnement négative pour guider la génération vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images dans l'espace latent | VAE | Oui | - |
| `width` | Largeur de la vidéo de sortie en pixels (par défaut : 832, pas : 16) | INT | Oui | 16 to MAX_RESOLUTION |
| `height` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) | INT | Oui | 16 to MAX_RESOLUTION |
| `length` | Nombre d'images dans la séquence vidéo (par défaut : 81, pas : 4) | INT | Oui | 1 to MAX_RESOLUTION |
| `batch_size` | Nombre de séquences vidéo à générer (par défaut : 1) | INT | Oui | 1 to 4096 |
| `ref_image` | Image de référence optionnelle pour fournir un guidage visuel | IMAGE | Non | - |
| `control_video` | Vidéo de contrôle optionnelle pour guider le processus de génération | IMAGE | Non | - |

**Remarque :** Le paramètre `length` est traité par blocs de 4 images, et le nœud gère automatiquement la mise à l'échelle temporelle pour l'espace latent. Lorsque `ref_image` est fourni, il influence le conditionnement via les latents de référence. Lorsque `control_video` est fourni, il affecte directement la représentation latente concaténée utilisée dans le conditionnement. Le paramètre `start_image` n'est pas exposé comme entrée dans le schéma de ce nœud, mais il est référencé dans la logique d'exécution.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif modifié avec des données latentes spécifiques à la vidéo, y compris le latent concaténé, le masque et les latents de référence optionnels | CONDITIONING |
| `negative` | Conditionnement négatif modifié avec des données latentes spécifiques à la vidéo, y compris le latent concaténé, le masque et les latents de référence optionnels | CONDITIONING |
| `latent` | Tenseur latent vide avec des dimensions appropriées pour la génération vidéo, basées sur la taille du lot, les canaux latents et la mise à l'échelle spatiale/temporelle | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`
