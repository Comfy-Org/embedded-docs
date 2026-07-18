Le nœud WanPhantomSubjectToVideo génère du contenu vidéo en traitant des entrées de conditionnement et des images de référence optionnelles. Il crée des représentations latentes pour la génération vidéo et peut intégrer un guidage visuel à partir des images d’entrée lorsqu’elles sont fournies. Le nœud prépare les données de conditionnement avec une concaténation temporelle pour les modèles vidéo et produit un conditionnement modifié ainsi que des données vidéo latentes générées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Entrée de conditionnement positive pour guider la génération vidéo | CONDITIONING | Oui | - |
| `négatif` | Entrée de conditionnement négative pour éviter certaines caractéristiques | CONDITIONING | Oui | - |
| `vae` | Modèle VAE pour encoder les images lorsqu’elles sont fournies | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie en pixels (par défaut : 832, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre d’images dans la vidéo générée (par défaut : 81, doit être divisible par 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_lot` | Nombre de vidéos à générer simultanément (par défaut : 1) | INT | Oui | 1 à 4096 |
| `images` | Images de référence optionnelles pour le conditionnement temporel | IMAGE | Non | - |

**Remarque :** Lorsque des `images` sont fournies, elles sont automatiquement mises à l’échelle pour correspondre à la `width` et à la `height` spécifiées, et seules les premières images correspondant à `length` sont utilisées pour le traitement.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Conditionnement positif modifié avec concaténation temporelle lorsque des images sont fournies | CONDITIONING |
| `texte_négatif` | Conditionnement négatif modifié avec concaténation temporelle lorsque des images sont fournies | CONDITIONING |
| `texte_img_négative` | Conditionnement négatif avec concaténation temporelle mise à zéro lorsque des images sont fournies | CONDITIONING |
| `latent` | Représentation vidéo latente générée avec les dimensions et la longueur spécifiées | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `2e3e8277dca9e998220fc5939c2cc72fdc15e80cc4b95daa33f5b92e2270dd73`
