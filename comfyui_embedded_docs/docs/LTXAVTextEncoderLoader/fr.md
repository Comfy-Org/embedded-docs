Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/en.md)

Ce nœud charge un encodeur de texte spécialisé pour le modèle audio LTXV. Il combine un fichier d'encodeur de texte spécifique avec un fichier de point de contrôle pour créer un modèle CLIP pouvant être utilisé pour des tâches de conditionnement textuel liées à l'audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `text_encoder` | Le nom du fichier du modèle d'encodeur de texte LTXV à charger. Les options disponibles sont chargées depuis le dossier `text_encoders`. | STRING | Oui | Plusieurs options disponibles |
| `ckpt_name` | Le nom du fichier du point de contrôle à charger. Les options disponibles sont chargées depuis le dossier `checkpoints`. | STRING | Oui | Plusieurs options disponibles |
| `device` | Spécifie le périphérique sur lequel charger le modèle. Utilisez `"cpu"` pour forcer le chargement sur le CPU. Le comportement par défaut (`"default"`) utilise le placement automatique du périphérique du système. | STRING | Non | `"default"`<br>`"cpu"` |

**Remarque :** Les paramètres `text_encoder` et `ckpt_name` fonctionnent ensemble. Le nœud charge les deux fichiers spécifiés pour créer un modèle CLIP unique et fonctionnel. Les fichiers doivent être compatibles avec l'architecture LTXV.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `clip` | Le modèle CLIP LTXV chargé, prêt à être utilisé pour encoder des invites textuelles pour la génération audio. | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/fr.md)

---
**Source fingerprint (SHA-256):** `c072a0b3393aa44333bb15ae42179c50868a4e9d7ca706d6c7da5922625373e6`
