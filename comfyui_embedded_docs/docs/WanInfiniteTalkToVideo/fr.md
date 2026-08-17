# WanInfiniteTalkToVideo

Le nœud WanInfiniteTalkToVideo génère un clip vidéo de tête parlante à partir d'audio. Il conditionne un modèle de diffusion vidéo sur des caractéristiques audio d'un ou deux locuteurs, utilise éventuellement une image de départ ou des images précédentes comme contexte, et renvoie un modèle patché, un conditionnement et une vidéo latente pour l'échantillonnage.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `mode` | Le mode audio. La sélection de `"single_speaker"` utilise une entrée audio. La sélection de `"two_speakers"` ajoute les entrées du deuxième locuteur listées ci-dessous. | DYNAMIC_COMBO | Oui | `"single_speaker"`<br>`"two_speakers"` |
| `model` | Le modèle de diffusion vidéo de base à patcher. | MODEL | Oui | - |
| `model_patch` | Le patch de modèle contenant les couches de projection audio. | MODELPATCH | Oui | - |
| `positive` | Le conditionnement positif utilisé pour guider la génération vidéo. | CONDITIONING | Oui | - |
| `negative` | Le conditionnement négatif utilisé pour guider la génération vidéo. | CONDITIONING | Oui | - |
| `vae` | Le VAE utilisé pour encoder les images et les images précédentes dans l'espace latent. | VAE | Oui | - |
| `width` | La largeur de la vidéo générée en pixels, par pas de 16. (défaut : 832) | INT | Oui | 16 - MAX_RESOLUTION (step 16) |
| `height` | La hauteur de la vidéo générée en pixels, par pas de 16. (défaut : 480) | INT | Oui | 16 - MAX_RESOLUTION (step 16) |
| `length` | Le nombre d'images à générer. (défaut : 81) | INT | Oui | 1 - MAX_RESOLUTION (step 4) |
| `audio_encoder_output_1` | La sortie de l'encodeur audio pour le premier locuteur, contenant les caractéristiques audio utilisées pour le conditionnement. | AUDIOENCODEROUTPUT | Oui | - |
| `start_image` | Image de départ facultative utilisée pour initialiser le début de la vidéo. Elle est redimensionnée à `width` et `height`. | IMAGE | Non | - |
| `clip_vision_output` | Sortie CLIP vision facultative ajoutée aux conditionnements positif et négatif. | CLIPVISIONOUTPUT | Non | - |
| `motion_frame_count` | Nombre d'images précédentes à utiliser comme contexte de mouvement. (défaut : 9) | INT | Oui | 1 - 33 (step 1) |
| `audio_scale` | Facteur d'échelle appliqué au conditionnement audio. (défaut : 1.0) | FLOAT | Oui | -10.0 - 10.0 (step 0.01) |
| `previous_frames` | Images vidéo précédentes facultatives utilisées pour étendre une séquence existante. Le nœud utilise les `motion_frame_count` dernières images comme contexte de mouvement. | IMAGE | Non | - |

### Entrées pour un seul locuteur

La sélection de `single_speaker` n'ajoute aucune entrée supplémentaire.

### Entrées pour deux locuteurs

Ces entrées sont disponibles lorsque `mode` est `"two_speakers"`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio_encoder_output_2` | La sortie de l'encodeur audio pour le deuxième locuteur. Lorsqu'elle est fournie, `mask_1` et `mask_2` doivent également être fournis. | AUDIOENCODEROUTPUT | Non | - |
| `mask_1` | Masque pour le premier locuteur, requis si deux entrées audio sont utilisées. | MASK | Non | - |
| `mask_2` | Masque pour le deuxième locuteur, requis si deux entrées audio sont utilisées. | MASK | Non | - |

**Contraintes des paramètres :**

- Si `audio_encoder_output_2` est fourni, `mask_1` et `mask_2` doivent également être fournis.
- Si `mask_1` et `mask_2` sont fournis, `audio_encoder_output_2` doit également être fourni.
- Si `previous_frames` est fourni, il doit contenir au moins autant d'images que spécifié par `motion_frame_count`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle patché avec conditionnement audio et wrappers d'échantillonnage appliqués. | MODEL |
| `positive` | Le conditionnement positif, potentiellement modifié avec l'image de départ ou le contexte CLIP vision. | CONDITIONING |
| `negative` | Le conditionnement négatif, potentiellement modifié avec l'image de départ ou le contexte CLIP vision. | CONDITIONING |
| `latent` | Un tenseur latent initialisé à zéro représentant la vidéo à générer. | LATENT |
| `trim_image` | Le nombre d'images à retirer au début lors de l'extension à partir d'images précédentes ; 0 lors du démarrage d'une nouvelle séquence. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `b7359490c1de86d9c82122bc227295b3b7f8a3493f629365ae0f22f9f34d9a66`
