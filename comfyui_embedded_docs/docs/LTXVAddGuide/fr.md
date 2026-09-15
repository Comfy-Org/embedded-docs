# LTXVAddGuide

Le nœud LTXVAddGuide encode les images ou vidéos d'entrée via un encodeur VAE et les ajoute comme images clés de guidage à une séquence vidéo latente. Il met à jour les conditionnements positif et négatif et renvoie le latent modifié, avec des options pour définir la trame de départ, la force de conditionnement, un masque d'attention facultatif et des paramètres IC-LoRA facultatifs.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positive` | Entrée de conditionnement positif à modifier avec le guidage par images clés. | CONDITIONING | Oui | - |
| `négatif` | Entrée de conditionnement négatif à modifier avec le guidage par images clés. | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les trames d'image/vidéo d'entrée. | VAE | Oui | - |
| `latent` | Séquence latente d'entrée qui recevra les trames de conditionnement. | LATENT | Oui | - |
| `image` | Image ou vidéo à utiliser pour conditionner la vidéo latente. Doit comporter 8*n + 1 trames. Si la vidéo ne comporte pas 8*n + 1 trames, elle sera recadrée au nombre de trames 8*n + 1 le plus proche. | IMAGE | Oui | - |
| `indice_de_l'image` | Indice de trame auquel commencer le conditionnement. Pour les images à trame unique ou les vidéos de 1 à 8 trames, toute valeur de `frame_idx` est acceptable. Pour les vidéos de 9 trames ou plus, `frame_idx` doit être divisible par 8, sinon il sera arrondi au multiple de 8 inférieur le plus proche. Les valeurs négatives sont comptées depuis la fin de la vidéo. Par défaut : 0. | INT | Oui | -9999 à 9999 |
| `force` | Force de l'influence du conditionnement : 1.0 applique un conditionnement complet et 0.0 n'applique aucun conditionnement. Par défaut : 1.0. | FLOAT | Oui | 0.0 à 10.0 |
| `attention_mask` | Masque spatial facultatif dans l'espace pixel. Contrôle l'influence du conditionnement par région via l'auto-attention, multipliée par la force. | MASK | Non | - |
| `iclora_parameters` | Paramètres IC-LoRA facultatifs provenant d'un nœud Get IC-LoRA Parameters. Utilisés pour ajuster le traitement des guides comme requis par certains IC-LoRA (par ex., ceux avec un reference_downscale_factor > 1). Lorsqu'ils sont chaînés, chaque LTXVAddGuide utilise uniquement les paramètres qui lui sont connectés. | IC_LORA_PARAMETERS | Non | - |

**Remarque :** L'image/la vidéo d'entrée doit avoir un nombre de trames suivant le motif 8*n + 1 (par ex., 1, 9, 17, 25 trames). Si l'entrée ne correspond pas à ce motif, elle sera automatiquement recadrée au nombre de trames valide le plus proche.

**Remarque sur `iclora_parameters` :** Lors de l'utilisation de paramètres IC-LoRA avec un `reference_downscale_factor` supérieur à 1, les dimensions spatiales du latent (largeur et hauteur) doivent être divisibles par ce facteur. Le nœud générera une erreur si cette condition n'est pas remplie.

**Remarque :** Les trames guides encodées doivent tenir dans la séquence latente à la position de trame sélectionnée. Si les trames conditionnées dépassent la longueur de la séquence latente, le nœud lève une erreur.

**Remarque :** L'ajout d'un guide à un latent qui combine des canaux audio et vidéo n'est pas pris en charge et lèvera une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Conditionnement positif mis à jour avec les informations de guidage par images clés. | CONDITIONING |
| `negative` | Conditionnement négatif mis à jour avec les informations de guidage par images clés. | CONDITIONING |
| `latent` | Séquence latente avec les trames de conditionnement intégrées et le masque de bruit mis à jour. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/fr.md)

---
**Source fingerprint (SHA-256):** `031bc9030dafed85b5ff1cbceae36234e9d5f77f7f4b040267067ecd16a27929`
