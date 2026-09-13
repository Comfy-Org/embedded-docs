# Charger le conditionnement

Ce nœud charge un conditionnement précédemment enregistré avec le nœud Save Conditioning, ou tout fichier safetensors contenant un tenseur `conditioning`, depuis le dossier embeddings. Il restaure également toutes les options supplémentaires et les valeurs de listes numérotées stockées avec le conditionnement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `conditioning_name` | Le fichier à charger depuis le dossier embeddings. La liste des choix est construite à partir des fichiers actuellement disponibles dans ce dossier. | COMBO | Oui | Tous les fichiers du dossier embeddings |

**Remarque :** Le fichier sélectionné doit contenir un tenseur `conditioning`. Toutes les clés supplémentaires stockées dans le fichier sont restaurées : les clés numérotées (par exemple `key.0`, `key.1`) sont regroupées en listes ordonnées, et les autres clés sont restaurées comme options simples. Les options supplémentaires sont lues à partir des métadonnées `conditioning_options` du fichier lorsqu'elles sont présentes.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `CONDITIONING` | Le conditionnement chargé depuis le fichier, avec les options restaurées. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningLoader/fr.md)

---
**Source fingerprint (SHA-256):** `08fc58bcaa2309fcf03d4e4cc634b930aaf6ccf8097181fd3d45924abda144eb`
