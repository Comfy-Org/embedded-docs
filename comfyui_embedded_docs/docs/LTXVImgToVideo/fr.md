# LTXVImgToVideo

Le nœud **LTXVImgToVideo** prépare une représentation latente pour générer une vidéo à partir d'une image d'entrée. L'image est redimensionnée à la largeur et à la hauteur demandées, encodée avec le VAE, puis placée dans les premières images latentes. Un masque de bruit est créé à l'aide de `strength` pour contrôler la quantité de contenu de l'image d'origine conservée ou modifiée. Les conditionnements positif et négatif sont transmis sans modification.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Données de conditionnement positives fournies en entrée et renvoyées inchangées. | CONDITIONING | Oui | - |
| `negative` | Données de conditionnement négatives fournies en entrée et renvoyées inchangées. | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder l'image d'entrée dans l'espace latent. | VAE | Oui | - |
| `image` | Image d'entrée qui est redimensionnée et encodée pour former le début du latent vidéo. | IMAGE | Oui | - |
| `width` | Largeur de la vidéo de sortie en pixels (défaut : 768, pas : 32). | INT | Oui | 64 à MAX_RESOLUTION |
| `height` | Hauteur de la vidéo de sortie en pixels (défaut : 512, pas : 32). | INT | Oui | 64 à MAX_RESOLUTION |
| `length` | Nombre d'images (frames) dans la vidéo générée (défaut : 97, pas : 8). | INT | Oui | 9 à MAX_RESOLUTION |
| `batch_size` | Nombre de vidéos à générer dans un même lot latent (défaut : 1). | INT | Oui | 1 à 4096 |
| `strength` | Contrôle la quantité de contenu de l'image encodée conservée dans les premières images latentes. Une valeur de 1.0 préserve entièrement l'image d'origine, tandis que 0.0 permet une modification maximale (défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 |

Remarque : `MAX_RESOLUTION` est la résolution maximale autorisée par l'installation de ComfyUI.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif transmis sans modification. | CONDITIONING |
| `negative` | Conditionnement négatif transmis sans modification. | CONDITIONING |
| `latent` | Latent vidéo contenant l'image d'entrée encodée au début de la séquence, ainsi qu'un masque de bruit basé sur `strength`. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `4ebc7f80b4d9ac3329e3349c7048885de22b827b5bdd102976687afd7e07a16b`
