# WanInfiniteTalkToVideo

## WanInfiniteTalkToVideo génère des séquences vidéo à partir d'une entrée audio. Il utilise un modèle de diffusion vidéo, conditionné sur des caractéristiques audio extraites d'un ou deux locuteurs, pour produire une représentation latente d'une vidéo de tête parlante. Le nœud peut générer une nouvelle séquence ou prolonger une séquence existante en utilisant les images précédentes comme contexte de mouvement.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `mode` | Le mode d'entrée audio. `single_speaker` utilise une seule entrée audio. `two_speakers` active l'entrée audio supplémentaire et les masques répertoriés dans la section Entrées pour deux locuteurs. | DYNAMIC_COMBO | Oui | `"single_speaker"`<br>`"two_speakers"` |
| `modèle` | Le modèle de diffusion vidéo de base. | MODEL | Oui | - |
| `correctif du modèle` | Le patch de modèle contenant les couches de projection audio. | MODEL_PATCH | Oui | - |
| `positif` | Le conditionnement positif pour guider la génération. | CONDITIONING | Oui | - |
| `négatif` | Le conditionnement négatif pour guider la génération. | CONDITIONING | Oui | - |
| `vae` | Le VAE utilisé pour encoder les images vers et depuis l'espace latent. | VAE | Oui | - |
| `largeur` | La largeur de la vidéo de sortie en pixels. Doit être divisible par 16. (par défaut : 832) | INT | Oui | 16 - MAX_RESOLUTION (step 16) |
| `hauteur` | La hauteur de la vidéo de sortie en pixels. Doit être divisible par 16. (par défaut : 480) | INT | Oui | 16 - MAX_RESOLUTION (step 16) |
| `longueur` | Le nombre d'images à générer. (par défaut : 81) | INT | Oui | 1 - MAX_RESOLUTION (step 4) |
| `sortie vision clip` | Sortie de vision CLIP optionnelle pour un conditionnement supplémentaire. | CLIP_VISION_OUTPUT | Non | - |
| `image de départ` | Image de départ optionnelle pour initialiser la séquence vidéo. | IMAGE | Non | - |
| `sortie encodeur audio 1` | La sortie principale de l'encodeur audio contenant les caractéristiques du premier locuteur. | AUDIO_ENCODER_OUTPUT | Oui | - |
| `nombre d’images de mouvement` | Nombre d'images précédentes à utiliser comme contexte de mouvement. (par défaut : 9) | INT | Oui | 1 - 33 |
| `échelle audio` | Un facteur d'échelle appliqué au conditionnement audio. (par défaut : 1.0) | FLOAT | Oui | -10.0 - 10.0 |
| `images précédentes` | Images vidéo précédentes optionnelles pour prolonger la séquence. Les dernières `motion_frame_count` images sont utilisées comme contexte de mouvement. | IMAGE | Non | - |

### Entrées pour deux locuteurs

Les entrées de cette section sont affichées lorsque `mode` est défini sur `"two_speakers"`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio_encoder_output_2` | La deuxième sortie de l'encodeur audio contenant les caractéristiques du deuxième locuteur. | AUDIO_ENCODER_OUTPUT | Non | - |
| `mask_1` | Masque pour le premier locuteur, requis si deux entrées audio sont utilisées. | MASK | Non | - |
| `mask_2` | Masque pour le deuxième locuteur, requis si deux entrées audio sont utilisées. | MASK | Non | - |

**Contraintes des paramètres :**

- Lorsque `mode` est défini sur `"two_speakers"`, `audio_encoder_output_2`, `mask_1` et `mask_2` sont requis pour la configuration du deuxième locuteur.
- Si `audio_encoder_output_2` est fourni, `mask_1` et `mask_2` doivent également être fournis.
- Si `mask_1` et `mask_2` sont tous deux fournis, `audio_encoder_output_2` doit également être fourni.
- Si `previous_frames` est fourni, il doit contenir au moins autant d'images que spécifié par `motion_frame_count`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle patché avec le conditionnement audio appliqué. | MODEL |
| `positif` | Le conditionnement positif, potentiellement modifié avec un contexte supplémentaire tel qu'une image de départ ou une sortie de vision CLIP. | CONDITIONING |
| `négatif` | Le conditionnement négatif, potentiellement modifié avec un contexte supplémentaire. | CONDITIONING |
| `latent` | La séquence vidéo générée dans l'espace latent. | LATENT |
| `image rognée` | Le nombre d'images du début du contexte de mouvement qui doivent être supprimées lors de l'extension d'une séquence. Équivaut à `motion_frame_count` lorsque `previous_frames` est fourni, sinon 0. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `b7359490c1de86d9c82122bc227295b3b7f8a3493f629365ae0f22f9f34d9a66`
