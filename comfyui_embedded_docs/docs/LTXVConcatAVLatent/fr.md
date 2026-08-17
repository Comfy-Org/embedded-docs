# Concaténer le latent AV

Le nœud LTXVConcatAVLatent fusionne un latent vidéo et un latent audio en un seul latent conjoint pour une utilisation avec des modèles audio-visuels tels que LTXV ou MiniMax H3. Il regroupe les `samples` des deux entrées, et si l'une des entrées contient un `noise_mask`, ces masques sont également regroupés. Si le latent vidéo est déjà un latent AV, le nœud conserve son flux vidéo et remplace son flux audio par le latent audio fourni.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `video_latent` | Représentation latente des données vidéo. | LATENT | Oui |  |
| `audio_latent` | Représentation latente des données audio à combiner avec le latent vidéo. | LATENT | Oui |  |

**Remarque sur la longueur audio :** Lorsque `video_latent` est déjà un latent AV, `audio_latent` doit correspondre au flux audio intégré dans toutes les dimensions sauf une. Le nœud tronque ou complète par des zéros l'audio le long de cette dimension pour correspondre à la longueur du flux existant. La partie complétée reste non masquée afin que le modèle puisse la générer.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `latent` | Un latent contenant les `samples` vidéo et audio appariés. Si l'une des entrées fournit un `noise_mask`, la sortie contient également un `noise_mask` apparié ; un masque manquant est remplacé par des uns. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/fr.md)

---
**Source fingerprint (SHA-256):** `0231f9db2ce73132d8555fbb33f295b68aa68a0c1c54e4a0c5d2e1f67b5611cb`
