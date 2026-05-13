> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/fr.md)

Le nœud WanInfiniteTalkToVideo génère des séquences vidéo à partir d’une entrée audio. Il utilise un modèle de diffusion vidéo, conditionné par des caractéristiques audio extraites d’un ou deux locuteurs, pour produire une représentation latente d’une vidéo de tête parlante. Le nœud peut générer une nouvelle séquence ou en étendre une existante en utilisant les images précédentes pour le contexte de mouvement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `mode` | COMBO | Oui | `"single_speaker"`<br>`"two_speakers"` | Le mode d’entrée audio. `"single_speaker"` utilise une seule entrée audio. `"two_speakers"` active les entrées pour un second locuteur et les masques correspondants. |
| `modèle` | MODEL | Oui | - | Le modèle de diffusion vidéo de base. |
| `correctif du modèle` | MODELPATCH | Oui | - | Le patch de modèle contenant les couches de projection audio. |
| `positif` | CONDITIONING | Oui | - | Le conditionnement positif pour guider la génération. |
| `négatif` | CONDITIONING | Oui | - | Le conditionnement négatif pour guider la génération. |
| `vae` | VAE | Oui | - | Le VAE utilisé pour encoder les images vers et depuis l’espace latent. |
| `largeur` | INT | Non | 16 - MAX_RESOLUTION | La largeur de la vidéo de sortie en pixels. Doit être divisible par 16. (par défaut : 832) |
| `hauteur` | INT | Non | 16 - MAX_RESOLUTION | La hauteur de la vidéo de sortie en pixels. Doit être divisible par 16. (par défaut : 480) |
| `longueur` | INT | Non | 1 - MAX_RESOLUTION | Le nombre d’images à générer. (par défaut : 81) |
| `sortie vision clip` | CLIPVISIONOUTPUT | Non | - | Sortie CLIP vision optionnelle pour un conditionnement supplémentaire. |
| `image de départ` | IMAGE | Non | - | Une image de départ optionnelle pour initialiser la séquence vidéo. |
| `sortie encodeur audio 1` | AUDIOENCODEROUTPUT | Oui | - | La sortie principale de l’encodeur audio contenant les caractéristiques du premier locuteur. |
| `nombre d’images de mouvement` | INT | Non | 1 - 33 | Nombre d’images précédentes à utiliser comme contexte de mouvement lors de l’extension d’une séquence. (par défaut : 9) |
| `échelle audio` | FLOAT | Non | -10.0 - 10.0 | Facteur d’échelle appliqué au conditionnement audio. (par défaut : 1.0) |
| `images précédentes` | IMAGE | Non | - | Images vidéo précédentes optionnelles pour étendre la séquence. |
| `audio_encoder_output_2` | AUDIOENCODEROUTPUT | Non | - | La seconde sortie de l’encodeur audio. Requise lorsque `mode` est réglé sur `"two_speakers"`. |
| `mask_1` | MASK | Non | - | Masque pour le premier locuteur, requis si deux entrées audio sont utilisées. |
| `mask_2` | MASK | Non | - | Masque pour le second locuteur, requis si deux entrées audio sont utilisées. |

**Contraintes des paramètres :**

* Lorsque `mode` est réglé sur `"two_speakers"`, les paramètres `audio_encoder_output_2`, `mask_1` et `mask_2` deviennent obligatoires.
* Si `audio_encoder_output_2` est fourni, `mask_1` et `mask_2` doivent également être fournis.
* Si `mask_1` et `mask_2` sont fournis, `audio_encoder_output_2` doit également être fourni.
* Si `previous_frames` est fourni, il doit contenir au moins autant d’images que spécifié par `motion_frame_count`.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `positif` | MODEL | Le modèle patché avec le conditionnement audio appliqué. |
| `négatif` | CONDITIONING | Le conditionnement positif, potentiellement modifié avec un contexte supplémentaire (ex. : image de départ, CLIP vision). |
| `latent` | CONDITIONING | Le conditionnement négatif, potentiellement modifié avec un contexte supplémentaire. |
| `image rognée` | LATENT | La séquence vidéo générée dans l’espace latent. |
| `trim_image` | INT | Le nombre d’images depuis le début du contexte de mouvement qui doivent être supprimées lors de l’extension d’une séquence. |

---
**Source fingerprint (SHA-256):** `6bb976da5cac0b61edb7d4c9d206c7c7ea9ffc0e982034c23c7f2e891e972888`
