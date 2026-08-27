# WanPhantomSubjectToVideo

Le nœud WanPhantomSubjectToVideo prépare les données de conditionnement et un latent pour la génération vidéo Wan. Il crée une vidéo latente vide à partir de la largeur, de la hauteur, de la longueur et de la taille de lot demandées et, lorsque des images de référence sont fournies, les encode avec le VAE et les ajoute aux conditionnements sous forme de guidage visuel de dimension temporelle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Entrée de conditionnement positive pour guider la génération vidéo | CONDITIONING | Oui | - |
| `négatif` | Entrée de conditionnement négative pour éviter certaines caractéristiques | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images de référence lorsqu'elles sont fournies | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie en pixels (par défaut : 832, doit être un multiple de 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, doit être un multiple de 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre de frames dans la vidéo générée (par défaut : 81, doit être un multiple de 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_lot` | Nombre de vidéos à générer simultanément (par défaut : 1) | INT | Oui | 1 à 4096 |
| `images` | Images de référence facultatives utilisées comme guidage visuel de dimension temporelle | IMAGE | Non | - |

**Remarque :** Lorsque des `images` sont fournies, elles sont automatiquement redimensionnées pour correspondre à la `width` et à la `height` spécifiées, et seules les premières `length` images sont utilisées pour le traitement. Chaque image est encodée avec le `vae` et concaténée le long de la dimension temporelle, et seuls les canaux RVB de chaque image sont utilisés.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Conditionnement positif avec concaténation dimensionnelle temporelle des images de référence encodées lorsque des images sont fournies ; sinon, le `positive` d'entrée est renvoyé inchangé | CONDITIONING |
| `texte_négatif` | Conditionnement négatif avec concaténation dimensionnelle temporelle des images de référence encodées lorsque des images sont fournies ; sinon, le `negative` d'entrée est renvoyé inchangé | CONDITIONING |
| `texte_img_négative` | Conditionnement négatif avec concaténation dimensionnelle temporelle remplie de zéros lorsque des images sont fournies ; sinon, le `negative` d'entrée est renvoyé inchangé | CONDITIONING |
| `latent` | Tenseur vidéo latent rempli de zéros avec 16 canaux ; son nombre de frames est dérivé de `length` et ses dimensions spatiales de `height` et `width` | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
