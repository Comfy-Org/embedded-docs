# LTXV Figer le latent

Le nœud LTXV Freeze Latent définit le masque de bruit d'un latent à zéro, ce qui garde ce latent propre et inchangé pendant l'exécution de l'échantillonnage. Il fonctionne à la fois sur les latents vidéo et audio, de sorte qu'un latent peut être figé avant d'être concaténé avec d'autres ou lorsqu'il ne doit pas du tout être débruité.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `latent` | Latent vidéo ou audio à figer. L'audio est en 4D ; la vidéo est en 5D. | LATENT | Oui | N/A |

### Contraintes

- Le latent doit contenir un tenseur simple. Un latent audio-vidéo concaténé n'est pas accepté ; il doit d'abord être séparé avec le nœud Separate AV Latent.
- Seuls les latents 4D (audio) et 5D (vidéo) sont pris en charge. Toute autre forme provoque une erreur.
- Le masque de bruit généré est créé avec des zéros en utilisant le même dispositif que le tenseur d'entrée. Pour les latents vidéo, le masque a la forme (batch, 1, frames, 1, 1) ; pour les latents audio, il a la forme (batch, 1, frames, 1).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `latent` | Le latent d'entrée avec un masque de bruit de zéros ajouté, afin qu'il reste propre pendant l'échantillonnage. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVFreezeLatent/fr.md)

---
**Source fingerprint (SHA-256):** `d5d228687f0a124644323c0448dcce53ed6eb2224d3f44d1756079b2a71539ca`
