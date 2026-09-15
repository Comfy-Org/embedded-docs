# HunyuanImageToVideo

Le nœud HunyuanImageToVideo convertit les images en représentations latentes vidéo à l'aide du modèle vidéo Hunyuan. Il prend des entrées de conditionnement et des images de départ facultatives pour générer des latents vidéo pouvant être traités ultérieurement par des modèles de génération vidéo. Le nœud prend en charge différents types de guidage pour contrôler la manière dont l'image de départ influence le processus de génération vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Entrée de conditionnement positive pour guider la génération vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images dans l'espace latent | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie en pixels (par défaut : 848, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre de trames dans la vidéo de sortie (par défaut : 53, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Nombre de vidéos à générer simultanément (par défaut : 1) | INT | Oui | 1 à 4096 |
| `type_de_guidage` | Méthode d'incorporation de l'image de départ dans la génération vidéo (par défaut : "v1 (concat)"). Option avancée | COMBO | Oui | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `image_de_départ` | Image de départ facultative (ou séquence d'images) pour initialiser la génération vidéo. Seules les `length` premières trames et les 3 premiers canaux de couleur sont utilisés | IMAGE | Non | - |

**Remarque :** Lorsque `start_image` est fourni, le nœud utilise différentes méthodes de guidage selon le `guidance_type` sélectionné :

- "v1 (concat)" : Concatène le latent de l'image avec le latent vidéo et applique un masque pour mélanger l'image dans la vidéo
- "v2 (replace)" : Remplace les trames vidéo initiales par le latent de l'image et applique un masque de bruit
- "custom" : Utilise l'image comme latent de référence pour le guidage

Si `start_image` n'est pas fourni, aucun conditionnement de guidage n'est ajouté et le latent est renvoyé sous forme de bloc de zéros simple.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif modifié avec le guidage par image appliqué lorsque start_image est fourni | CONDITIONING |
| `latent` | Représentation latente vidéo prête pour un traitement ultérieur par des modèles de génération vidéo | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `0ed00d59513492f31760a18ce3b0edf10b64cad848ba52c4e47d5f61fae9accc`
