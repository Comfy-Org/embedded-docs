# WanAnimate2ToVideo

WanAnimate2ToVideo anime un personnage à partir d'une image de référence en transférant les expressions faciales, les mouvements du corps et les gestes des mains d'une vidéo de pose distincte. Il construit les données de conditionnement et un latent de départ que le sampler de génération vidéo utilise pour créer l'animation.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positive` | Le conditionnement positif pour la génération vidéo. | CONDITIONING | Oui | N/A |
| `negative` | Le conditionnement négatif pour la génération vidéo. | CONDITIONING | Oui | N/A |
| `vae` | Le VAE utilisé pour encoder l'image de référence et les images vidéo dans l'espace latent. | VAE | Oui | N/A |
| `width` | Largeur de la vidéo de sortie en pixels. (par défaut : 832) | INT | Oui | 16 à MAX_RESOLUTION (pas 16) |
| `height` | Hauteur de la vidéo de sortie en pixels. (par défaut : 480) | INT | Oui | 16 à MAX_RESOLUTION (pas 16) |
| `length` | Nombre d'images à générer. (par défaut : 81) | INT | Oui | 1 à MAX_RESOLUTION (pas 4) |
| `batch_size` | Nombre de vidéos à générer simultanément. (par défaut : 1) | INT | Oui | 1 à 4096 |
| `reference_image` | Le personnage à animer. Si ce paramètre est omis, une image noire est utilisée. | IMAGE | Non | N/A |
| `pose_video` | La vidéo dont le mouvement est transféré au personnage de référence. Si elle contient moins d'images que `length`, la dernière image est répétée pour combler les images manquantes. | IMAGE | Non | N/A |
| `clip_vision_output` | Vision CLIP de l'image de référence. | CLIP_VISION_OUTPUT | Non | N/A |
| `positive_pose` | Invite pour la branche de la vidéo de pose, décrivant le mouvement plutôt que le personnage. Par défaut, utilise `positive`. Utilisée pour les passes cond et uncond. | CONDITIONING | Non | N/A |
| `clip_vision_output_pose` | Vision CLIP de la première image de la vidéo de pose. Par défaut, utilise `clip_vision_output`. | CLIP_VISION_OUTPUT | Non | N/A |
| `continue_motion` | Séquence de mouvement précédente à partir de laquelle continuer pour la cohérence temporelle. Seule la dernière image de cette séquence est utilisée comme image de mouvement initiale. | IMAGE | Non | N/A |
| `video_frame_offset` | Décalage en images dans la vidéo de pose. Connectez-le à la sortie `video_frame_offset` du nœud précédent lors d'une extension. (par défaut : 0) | INT | Oui | 0 à MAX_RESOLUTION |
| `pose_strength` | Module l'influence de la vidéo de pose sur le mouvement. 1.0 correspond au comportement entraîné ; une valeur inférieure affaiblit l'adhérence, une valeur supérieure l'amplifie. 0.0 l'atténue mais ne le supprime pas complètement. (par défaut : 1.0) | FLOAT | Oui | 0.00 à 10.00 (pas 0.01) |
| `pose_start_percent` | Pourcentage d'échantillonnage auquel l'influence de la pose commence. En dehors de cette fenêtre, la branche de pose est entièrement ignorée, ce qui accélère également ces étapes. (par défaut : 0.0) | FLOAT | Oui | 0.00 à 1.00 (pas 0.01) |
| `pose_end_percent` | Pourcentage d'échantillonnage auquel l'influence de la pose se termine. Le mouvement est en grande partie établi tôt, donc, par exemple, 0.7 peut assouplir les détails fins tout en conservant la chorégraphie. (par défaut : 1.0) | FLOAT | Oui | 0.00 à 1.00 (pas 0.01) |
| `reference_image_strength` | Module la force avec laquelle les images générées prêtent attention à l'image latente de l'image de référence. En dessous de 1.0, l'adhérence à l'identité et à l'apparence est relâchée (par exemple, pour laisser l'invite restyler) ; au-dessus, elle est renforcée contre la dérive. (par défaut : 1.0) | FLOAT | Oui | 0.00 à 10.00 (pas 0.01) |

**Notes de validation :**

- `pose_start_percent` ne doit pas être supérieur à `pose_end_percent` ; sinon le nœud lève une ValueError.
- Si `pose_video` est fourni, son nombre d'images doit être supérieur à `video_frame_offset` ; sinon le nœud lève une ValueError.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Conditionnement positif pour l'échantillonnage, avec l'image de référence, le masque et, le cas échéant, les données de pose. | CONDITIONING |
| `negative` | Conditionnement négatif pour l'échantillonnage, avec la même image de référence, le masque et, le cas échéant, les données de pose. | CONDITIONING |
| `latent` | Latent de départ rempli de zéros pour le sampler vidéo ; les premières `trim_latent` images latentes doivent être supprimées avant le décodage. | LATENT |
| `trim_latent` | Nombre d'images latentes à supprimer avant le décodage. | INT |
| `trim_image` | Nombre d'images se chevauchant lors de l'extension d'une vidéo. | INT |
| `video_frame_offset` | Décalage en images dans la vidéo de pose ; égal au décalage d'entrée ajusté plus le nombre d'images générées. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimate2ToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `7e1f497983ab63a68e5ef5439b3ef4e9295f79f78530c9dc5de16a8238475f05`
