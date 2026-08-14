# MiniMaxH3AddGuide

Ce nœud ancre une image, un court clip, de l'audio ou un clip avec sa bande-son à n'importe quelle frame choisie d'une vidéo MiniMax H3. Il ajoute une image clé de guidage au conditionnement à l'index de frame spécifié, et vous pouvez chaîner plusieurs de ces nœuds pour ancrer plusieurs frames dans la même vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positive` | Le conditionnement auquel l'image clé de guidage est attachée. | CONDITIONING | Oui | - |
| `latent` | Le latent audio-vidéo MiniMax H3 qui définit la vidéo cible. Doit être un latent AV MiniMax H3 (imbriqué, avec deux tenseurs 5D de 24 canaux chacun). | LATENT | Oui | - |
| `frame_idx` | Index de frame pour ancrer l'image ou la première frame du clip. Les valeurs négatives sont comptées depuis la fin de la vidéo. (défaut : 0) | INT | Oui | -9999 à 9999 |
| `vae` | VAE vidéo, requis lorsqu'une image est connectée. | VAE | Non | - |
| `audio_vae` | VAE audio, requis lorsqu'un audio est connecté. | VAE | Non | - |
| `image` | Image ou frames vidéo à ancrer. Les lots multi-frames sont ancrés comme un clip et recadrés aux longueurs de clip valides du modèle : 5, 22, 39... (17k + 5) frames. Les lots de moins de 5 frames utilisent uniquement la première image. | IMAGE | Non | - |
| `audio` | Bande-son à ancrer à partir du même index de frame, recadrée à la durée restante de la vidéo. | AUDIO | Non | - |

**Contraintes :**
- Au moins l'un de `image` ou `audio` doit être fourni ; sinon le nœud génère une erreur.
- `vae` est requis lorsque `image` est connecté.
- `audio_vae` est requis lorsque `audio` est connecté.
- Les lots `image` de moins de 5 frames utilisent uniquement la première image ; les lots de 5 frames ou plus sont recadrés à une longueur de clip valide (5, 22, 39, etc.).
- `frame_idx` doit placer le guide dans la plage de frames de la vidéo, et un clip multi-frames doit tenir entièrement dans la vidéo ; sinon le nœud génère une erreur.
- Lorsque l'audio est connecté, l'index de frame ne doit pas dépasser la fin de la piste audio de la vidéo.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Le conditionnement avec l'image clé de guidage ajoutée, contenant l'index de frame résolu et, le cas échéant, les latents encodés d'image ou d'audio. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3AddGuide/fr.md)

---
**Source fingerprint (SHA-256):** `7a2f742421cc2655bd9c914258801e4538f1554a7c5e2b0836b2df1577f5a104`
