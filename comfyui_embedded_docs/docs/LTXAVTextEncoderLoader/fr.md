# Chargeur d'encodeur texte audio LTXV

Ce nœud charge un encodeur de texte spécialisé pour le modèle audio LTXV. Il combine un fichier d'encodeur de texte avec un fichier de checkpoint pour créer un modèle CLIP utilisé pour le conditionnement textuel dans la génération audio. Selon la description du nœud, l'encodeur de texte doit être un Gemma 3 12B ou un modèle Gemma 4 correspondant.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `text_encoder` | Le nom de fichier du modèle d'encodeur de texte LTXV à charger. Les options disponibles sont chargées à partir du dossier `text_encoders`. | COMBO | Oui | Plusieurs options disponibles |
| `ckpt_name` | Le nom de fichier du checkpoint à charger. Les options disponibles sont chargées à partir du dossier `checkpoints`. | COMBO | Oui | Plusieurs options disponibles |
| `device` | Spécifie le dispositif sur lequel charger le modèle. Utilisez `"cpu"` pour forcer le chargement sur le CPU. Le comportement par défaut (`"default"`) utilise le placement automatique du périphérique système (par défaut : `"default"`). Ceci est un paramètre avancé. | COMBO | Non | `"default"`<br>`"cpu"` |

**Remarque :** Les paramètres `text_encoder` et `ckpt_name` fonctionnent ensemble. Le nœud charge les deux fichiers spécifiés pour créer un modèle CLIP unique et fonctionnel. Les fichiers doivent être compatibles avec l'architecture LTXV, et l'encodeur de texte doit être un modèle Gemma 3 12B ou un modèle Gemma 4 équivalent.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `clip` | Le modèle CLIP LTXV chargé, prêt à être utilisé pour encoder les prompts textuels pour la génération audio. | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/fr.md)

---
**Source fingerprint (SHA-256):** `1f3df2c1791203ba849a87897de14052e0cb8370100dbca19df4cf30169a0a2a`
