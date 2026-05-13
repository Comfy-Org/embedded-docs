> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddTextPrefix/fr.md)

Le nœud Ajouter un Préfixe de Texte modifie un texte en ajoutant une chaîne spécifiée au début de chaque texte d'entrée. Il prend le texte et un préfixe en entrée, puis renvoie le résultat combiné.

## Entrées

| Paramètre | Type de Données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `text` | STRING | Oui | | Le texte auquel le préfixe sera ajouté. |
| `prefix` | STRING | Non | | La chaîne à ajouter au début du texte (par défaut : ""). |

## Sorties

| Nom de Sortie | Type de Données | Description |
|---------------|-----------------|-------------|
| `text` | STRING | Le texte résultant avec le préfixe ajouté au début. |

---
**Source fingerprint (SHA-256):** `7f1282b1b84ea06a96ecefdec8e9e684cb6e7d3e618250dfb6e54d01f9e9ba87`
