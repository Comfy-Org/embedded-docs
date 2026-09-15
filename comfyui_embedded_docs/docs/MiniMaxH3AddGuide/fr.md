# Ajouter un guide pour MiniMax H3

Ce nœud ancre une image, un court clip, un audio ou un clip avec sa bande sonore à n'importe quelle image d'une vidéo MiniMax H3. Il ajoute une image clé de guidage au conditionnement à l'index d'image choisi, et vous pouvez chaîner plusieurs de ces nœuds pour ancrer plusieurs images dans la même vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positive` | Le conditionnement auquel l'image clé de guidage est attachée. | CONDITIONING | Oui | - |
| `vae` | VAE vidéo, nécessaire lorsqu'une image est connectée. | VAE | Non | - |
| `audio_vae` | VAE audio, nécessaire lorsqu'un audio est connecté. | VAE | Non | - |
| `latent` | Le latent audio-vidéo MiniMax H3 qui définit la vidéo cible. Doit être un latent AV MiniMax H3 (imbriqué, avec deux tenseurs 5D, le tenseur vidéo ayant 24 canaux). | LATENT | Oui | - |
| `image` | Image ou images vidéo à ancrer. Les lots multi-images sont ancrés comme un clip et recadrés à la longueur de clip valide du modèle : 5, 22, 39... (17k + 5) images. Les lots de moins de 5 images n'utilisent que la première image. | IMAGE | Non | - |
| `audio` | Bande sonore à ancrer en démarrant au même index d'image, recadrée à la durée restante de la vidéo. | AUDIO | Non | - |
| `frame_idx` | Index d'image auquel ancrer l'image ou la première image du clip. Les valeurs négatives sont comptées depuis la fin de la vidéo. (valeur par défaut : 0) | INT | Oui | -9999 à 9999 |

**Contraintes :**
- Au moins un des paramètres `image` ou `audio` doit être fourni ; sinon le nœud génère une erreur.
- `vae` est requis lorsque `image` est connecté.
- `audio_vae` est requis lorsque `audio` est connecté.
- Les lots `image` de moins de 5 images n'utilisent que la première image ; les lots de 5 images ou plus sont recadrés à une longueur de clip valide (5, 22, 39, etc.).
- `frame_idx` doit placer le guide dans la plage d'images de la vidéo, et un clip de plusieurs images doit tenir entièrement dans la vidéo ; sinon le nœud génère une erreur.
- Lorsqu'un audio est connecté, l'index d'image ne doit pas dépasser la fin de la piste audio de la vidéo.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Le conditionnement avec l'image clé de guidage ajoutée, contenant l'index d'image résolu et, lorsqu'ils sont fournis, les latents d'image ou d'audio encodés. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3AddGuide/fr.md)

---
**Source fingerprint (SHA-256):** `7a2f742421cc2655bd9c914258801e4538f1554a7c5e2b0836b2df1577f5a104`
