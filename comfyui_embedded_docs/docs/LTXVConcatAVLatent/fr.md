Le nœud LTXVConcatAVLatent combine une représentation latente vidéo et une représentation latente audio en une seule sortie latente concaténée. Il fusionne les tenseurs `samples` des deux entrées et, s'ils sont présents, leurs tenseurs `noise_mask` également, les préparant ainsi pour un traitement ultérieur dans un pipeline de génération vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `video_latent` | La représentation latente des données vidéo. | LATENT | Oui |  |
| `audio_latent` | La représentation latente des données audio. | LATENT | Oui |  |

**Remarque :** Les tenseurs `samples` des entrées `video_latent` et `audio_latent` sont concaténés. Si l'une des entrées contient un `noise_mask`, celui-ci sera utilisé ; si l'un est manquant, un masque de uns (de même forme que les `samples` correspondants) est créé pour lui. Les masques résultants sont ensuite également concaténés.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `latent` | Un dictionnaire latent unique contenant les `samples` concaténés et, le cas échéant, le `noise_mask` concaténé provenant des entrées vidéo et audio. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/fr.md)

---
**Source fingerprint (SHA-256):** `322d6870f110fb1ef8b472cb49649cc9fff7865f4c7a83fbfd536f1fdfd694f8`
