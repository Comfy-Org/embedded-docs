# LTXVAddGuide

Le nœud LTXVAddGuide ajoute un guidage de conditionnement vidéo aux séquences latentes en encodant des images ou vidéos d'entrée et en les incorporant comme images clés dans les données de conditionnement. Il traite l'entrée via un encodeur VAE et place stratégiquement les latents résultants à des positions de frames spécifiées, tout en mettant à jour le conditionnement positif et négatif avec les informations des images clés. Le nœud gère les contraintes d'alignement des frames et permet de contrôler la force de l'influence du conditionnement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Conditionnement positif d'entrée à modifier avec le guidage par images clés | CONDITIONING | Oui | - |
| `négatif` | Conditionnement négatif d'entrée à modifier avec le guidage par images clés | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les frames de l'image/vidéo d'entrée | VAE | Oui | - |
| `latent` | Séquence latente d'entrée qui recevra les frames de conditionnement | LATENT | Oui | - |
| `image` | Image ou vidéo pour conditionner la vidéo latente. Doit contenir 8*n + 1 frames. Si la vidéo n'a pas 8*n + 1 frames, elle sera recadrée à la valeur la plus proche de 8*n + 1 frames. | IMAGE | Oui | - |
| `indice_de_l'image` | Index de frame où commencer le conditionnement. Pour les images à frame unique ou les vidéos de 1 à 8 frames, toute valeur de `frame_idx` est acceptable. Pour les vidéos de 9 frames ou plus, `frame_idx` doit être divisible par 8, sinon il sera arrondi à l'inférieur au multiple de 8 le plus proche. Les valeurs négatives sont comptées à partir de la fin de la vidéo. (défaut : 0) | INT | Oui | -9999 à 9999 |
| `force` | Force de l'influence du conditionnement, où 1,0 applique un conditionnement complet et 0,0 aucun conditionnement (défaut : 1,0) | FLOAT | Oui | 0,0 à 10,0 |
| `attention_mask` | Masque spatial optionnel en espace pixel. Contrôle l'influence du conditionnement par région via l'auto-attention, multiplié par `strength`. | MASK | Non | - |
| `iclora_parameters` | Paramètres IC-LoRA facultatifs provenant d'un nœud Get IC-LoRA Parameters. Utilisés pour ajuster le traitement du guidage selon les exigences de certains IC-LoRA (par exemple, ceux avec un `reference_downscale_factor` > 1). En chaînage, chaque LTXVAddGuide n'utilise que les paramètres qui lui sont connectés. | IC_LORA_PARAMETERS | Non | - |

**Remarque :** L'image/vidéo d'entrée doit avoir un nombre de frames suivant le motif 8*n + 1 (par exemple, 1, 9, 17, 25 frames). Si l'entrée dépasse ce motif, elle sera automatiquement recadrée au nombre de frames valide le plus proche.

**Remarque sur `iclora_parameters` :** Lors de l'utilisation de paramètres IC-LoRA avec un `reference_downscale_factor` supérieur à 1, les dimensions spatiales latentes (largeur et hauteur) doivent être divisibles par ce facteur. Le nœud lèvera une erreur si cette condition n'est pas respectée.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif mis à jour avec les informations de guidage par images clés | CONDITIONING |
| `négatif` | Conditionnement négatif mis à jour avec les informations de guidage par images clés | CONDITIONING |
| `latent` | Séquence latente avec les frames de conditionnement incorporées et le masque de bruit mis à jour | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/fr.md)

---
**Source fingerprint (SHA-256):** `3e0d1422fbd1b5b3e4c69e641af2ecdb5ae8de3f4368b336917a0dce4286771e`
