Voici la traduction en français de la documentation du nœud ComfyUI `WanTrackToVideo` :

Le nœud WanTrackToVideo convertit les données de suivi de mouvement en séquences vidéo en traitant les points de suivi et en générant les trames vidéo correspondantes. Il prend des coordonnées de suivi en entrée et produit un conditionnement vidéo ainsi que des représentations latentes utilisables pour la génération vidéo. Lorsqu'aucune piste n'est fournie, il revient à une conversion standard image-vers-vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Conditionnement positif pour la génération vidéo | CONDITIONING | Oui | - |
| `negative` | Conditionnement négatif pour la génération vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE pour l'encodage et le décodage | VAE | Oui | - |
| `tracks` | Données de suivi au format JSON sous forme de chaîne multiligne (par défaut : "[]") | STRING | Oui | - |
| `largeur` | Largeur de la vidéo de sortie en pixels (par défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre de trames dans la vidéo de sortie (par défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `batch_size` | Nombre de vidéos à générer simultanément (par défaut : 1) | INT | Oui | 1 à 4096 |
| `température` | Paramètre de température pour le patch de mouvement (par défaut : 220.0, pas : 0.1) | FLOAT | Oui | 1.0 à 1000.0 |
| `topk` | Valeur top-k pour le patch de mouvement (par défaut : 2) | INT | Oui | 1 à 10 |
| `start_image` | Image de départ pour la génération vidéo | IMAGE | Non | - |
| `clip_vision_output` | Sortie de vision CLIP pour un conditionnement supplémentaire | CLIPVISIONOUTPUT | Non | - |

**Remarque :** Lorsque `tracks` contient des données de suivi valides, le nœud traite les pistes de mouvement pour générer une vidéo. Lorsque `tracks` est vide, il bascule en mode standard image-vers-vidéo. Si `start_image` est fourni, il initialise la première trame de la séquence vidéo.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `negative` | Conditionnement positif avec les informations de piste de mouvement appliquées | CONDITIONING |
| `latent` | Conditionnement négatif avec les informations de piste de mouvement appliquées | CONDITIONING |
| `latent` | Représentation latente de la vidéo générée | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `b3e12492d3dafa100266f6be8fe05e4d62b827f1a2bdb4029f804b107dc691ed`
