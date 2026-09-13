# SD_4XUpscale_Conditioning

Le nœud SD_4XUpscale_Conditioning prépare les données de conditionnement pour l'agrandissement d'images avec des modèles de diffusion. Il met à l'échelle les images d'entrée selon un ratio choisi, ajoute une augmentation de bruit optionnelle et renvoie les conditionnements positif et négatif modifiés, ainsi qu'un latent vide pour la taille agrandie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Images d'entrée à agrandir. | IMAGE | Oui | - |
| `positive` | Données de conditionnement positives qui guident la génération vers le contenu souhaité. | CONDITIONING | Oui | - |
| `negative` | Données de conditionnement négatives qui éloignent la génération du contenu indésirable. | CONDITIONING | Oui | - |
| `scale_ratio` | Multiplicateur appliqué aux dimensions de l'image d'entrée lors de la préparation du conditionnement et du latent agrandis (par défaut : 4.0). | FLOAT | Oui | 0.0 - 10.0 (pas 0.01) |
| `noise_augmentation` | Quantité de bruit à ajouter pendant le processus d'agrandissement (par défaut : 0.0). | FLOAT | Oui | 0.0 - 1.0 (pas 0.001) |

Remarque : `noise_augmentation` est un paramètre avancé, affiché dans l'interface du nœud sous l'option « Advanced ».

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif modifié avec les données d'image mises à l'échelle et les paramètres d'augmentation de bruit appliqués. | CONDITIONING |
| `negative` | Conditionnement négatif modifié avec les données d'image mises à l'échelle et les paramètres d'augmentation de bruit appliqués. | CONDITIONING |
| `latent` | Représentation latente vide correspondant aux dimensions agrandies. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/fr.md)

---
**Source fingerprint (SHA-256):** `f215e890bd86f42d4da9c6f575fc92e65844e2e2056c5610310d8089e5d61902`
