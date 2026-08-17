# LTXVAddGuide

LTXVAddGuide ajoute un guidage de conditionnement vidéo aux séquences latentes en encodant les images ou vidéos d'entrée et en les incorporant comme images clés dans les données de conditionnement. Il traite l'entrée via un encodeur VAE et place stratégiquement les latents résultants à des positions de frames spécifiées tout en mettant à jour les conditionnements positif et négatif avec les informations des images clés. Le nœud gère les contraintes d'alignement des frames et permet de contrôler la force de l'influence du conditionnement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Conditionnement positif d'entrée à modifier avec le guidage par images clés | CONDITIONING | Oui | - |
| `negative` | Conditionnement négatif d'entrée à modifier avec le guidage par images clés | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les frames de l'image/vidéo d'entrée | VAE | Oui | - |
| `latent` | Séquence latente d'entrée qui recevra les frames de conditionnement | LATENT | Oui | - |
| `image` | Image ou vidéo sur laquelle conditionner la vidéo latente. Doit contenir 8*n + 1 frames. Si la vidéo ne contient pas 8*n + 1 frames, elle sera recadrée aux 8*n + 1 frames les plus proches. | IMAGE | Oui | - |
| `frame_idx` | Indice de frame auquel commencer le conditionnement. Pour les images à frame unique ou les vidéos de 1 à 8 frames, toute valeur de `frame_idx` est acceptable. Pour les vidéos de 9 frames et plus, `frame_idx` doit être divisible par 8, sinon il sera arrondi à l'inférieur au multiple de 8 le plus proche. Les valeurs négatives sont comptées à partir de la fin de la vidéo. (défaut : 0) | INT | Non | -9999 to 9999 |
| `strength` | Force de l'influence du conditionnement, où 1.0 applique un conditionnement complet et 0.0 n'applique aucun conditionnement (défaut : 1.0) | FLOAT | Non | 0.0 to 10.0 |
| `attention_mask` | Masque spatial optionnel dans l'espace des pixels. Contrôle l'influence du conditionnement par région via l'auto-attention, multiplié par la force. | MASK | Non | - |
| `iclora_parameters` | Paramètres IC-LoRA optionnels provenant d'un nœud Get IC-LoRA Parameters. Utilisés pour ajuster le traitement du guidage selon les exigences de certains IC-LoRA (par exemple, ceux avec un `reference_downscale_factor` > 1). En chaîne, chaque LTXVAddGuide utilise uniquement les paramètres qui lui sont connectés. | IC_LORA_PARAMETERS | Non | - |

**Remarques :**

- L'image/vidéo d'entrée doit avoir un nombre de frames suivant le motif 8*n + 1 (par exemple, 1, 9, 17, 25 frames). Si l'entrée dépasse ce motif, elle sera automatiquement recadrée au nombre de frames valide le plus proche.
- Lors de l'utilisation de paramètres IC-LoRA avec un `reference_downscale_factor` supérieur à 1, les dimensions spatiales latentes (largeur et hauteur) doivent être divisibles par ce facteur. Le nœud génère une erreur si cette condition n'est pas remplie.
- Le guidage doit tenir dans la séquence latente : l'indice de frame de départ plus le nombre de frames de guidage ne peut pas dépasser la longueur latente, sinon le nœud génère une erreur.
- Le nœud ne prend pas en charge les latents combinés audio-vidéo. Tant le `latent` d'entrée que le guidage encodé doivent utiliser le format latent vidéo standard à 128 canaux, sinon le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif mis à jour avec les informations de guidage par images clés | CONDITIONING |
| `negative` | Conditionnement négatif mis à jour avec les informations de guidage par images clés | CONDITIONING |
| `latent` | Séquence latente avec frames de conditionnement incorporées et masque de bruit mis à jour | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/fr.md)

---
**Source fingerprint (SHA-256):** `3e0d1422fbd1b5b3e4c69e641af2ecdb5ae8de3f4368b336917a0dce4286771e`
