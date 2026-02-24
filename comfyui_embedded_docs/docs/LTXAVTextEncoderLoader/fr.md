> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/fr.md)

Ce nœud charge un encodeur de texte spécialisé pour le modèle audio LTXV. Il combine un fichier d'encodeur de texte spécifique avec un fichier de point de contrôle pour créer un modèle CLIP pouvant être utilisé pour des tâches de conditionnement de texte liées à l'audio.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `text_encoder` | STRING | Oui | Plusieurs options disponibles | Le nom de fichier du modèle d'encodeur de texte LTXV à charger. Les options disponibles sont chargées depuis le dossier `text_encoders`. |
| `ckpt_name` | STRING | Oui | Plusieurs options disponibles | Le nom de fichier du point de contrôle à charger. Les options disponibles sont chargées depuis le dossier `checkpoints`. |
| `device` | STRING | Non | `"default"`<br>`"cpu"` | Spécifie le périphérique sur lequel charger le modèle. Utilisez `"cpu"` pour forcer le chargement sur le CPU. Le comportement par défaut (`"default"`) utilise le placement automatique du périphérique par le système. |

**Note :** Les paramètres `text_encoder` et `ckpt_name` fonctionnent ensemble. Le nœud charge les deux fichiers spécifiés pour créer un seul modèle CLIP fonctionnel. Les fichiers doivent être compatibles avec l'architecture LTXV.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `clip` | CLIP | Le modèle CLIP LTXV chargé, prêt à être utilisé pour encoder des invites textuelles pour la génération audio. |
