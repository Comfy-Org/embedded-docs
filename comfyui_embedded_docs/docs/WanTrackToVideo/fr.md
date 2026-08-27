# WanTrackToVideo

Le nœud WanTrackToVideo convertit des données de suivi de mouvement en séquences vidéo en traitant les points de suivi et en générant les trames vidéo correspondantes. Il prend des coordonnées de suivi en entrée et produit des conditionnements vidéo ainsi que des représentations latentes utilisables pour la génération vidéo. Lorsqu'aucune piste n'est fournie, il revient à la conversion standard image-vers-vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Conditionnement positif pour la génération vidéo | CONDITIONING | Oui | - |
| `negative` | Conditionnement négatif pour la génération vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE pour l'encodage et le décodage | VAE | Oui | - |
| `tracks` | Données de suivi au format JSON sous forme de chaîne multiligne (par défaut : « [] »). Chaque piste est complétée ou tronquée à une longueur fixe de 121 points. | STRING | Oui | - |
| `largeur` | Largeur de la vidéo de sortie en pixels (par défaut : 832, pas : 16) | INT | Oui | 16 to MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) | INT | Oui | 16 to MAX_RESOLUTION |
| `longueur` | Nombre de trames dans la vidéo de sortie (par défaut : 81, pas : 4) | INT | Oui | 1 to MAX_RESOLUTION |
| `batch_size` | Nombre de vidéos à générer simultanément (par défaut : 1) | INT | Oui | 1 à 4096 |
| `température` | Paramètre de température pour le motion patching (par défaut : 220.0, pas : 0.1) | FLOAT | Oui | 1.0 à 1000.0 |
| `topk` | Valeur top-k pour le motion patching (par défaut : 2) | INT | Oui | 1 à 10 |
| `start_image` | Image de départ pour la génération vidéo | IMAGE | Non | - |
| `clip_vision_output` | Sortie CLIP vision pour un conditionnement supplémentaire | CLIP_VISION_OUTPUT | Non | - |

**Remarque :** Lorsque `tracks` contient des données de suivi valides, le nœud traite les pistes de mouvement pour générer la vidéo. Lorsque `tracks` est vide, il passe en mode standard image-vers-vidéo. Si `start_image` est fourni, il initialise la première trame de la séquence vidéo, et le résultat du motion patching est ajouté aux conditionnements positif et négatif. Si `clip_vision_output` est fourni, il est également ajouté aux conditionnements positif et négatif.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif avec informations de suivi de mouvement appliquées | CONDITIONING |
| `negative` | Conditionnement négatif avec informations de suivi de mouvement appliquées | CONDITIONING |
| `latent` | Représentation latente de la vidéo générée | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `e67fe326dd7e5ae63ddc35946d8144138d04d9523ec1ad2e08ea6bc1dc9325da`
