> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/fr.md)

# ComfyOrNode

Le nœud ComfyOrNode effectue une opération logique OU sur un ensemble de valeurs d'entrée. Il renvoie `true` si l'une des valeurs fournies est considérée comme vraie selon les règles standard de vérité de Python.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `value` | ANY | Oui | Valeurs multiples acceptées | Une valeur à évaluer pour sa vérité. Vous pouvez fournir plusieurs valeurs en ajoutant davantage d'entrées. Le nœud renvoie `true` si l'une de ces valeurs est vraie. |

**Remarque :** Le nœud accepte un minimum d'une valeur d'entrée. Vous pouvez ajouter autant d'entrées que nécessaire à l'aide de la fonction d'extension automatique.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `BOOLEAN` | BOOLEAN | Renvoie `true` si l'une des valeurs d'entrée est vraie ; renvoie `false` si toutes les valeurs d'entrée sont fausses. |

---
**Source fingerprint (SHA-256):** `00c60d5c80bbddc993af0bcd92e35dc77f153731329c23a6e4e9a980709111b1`
