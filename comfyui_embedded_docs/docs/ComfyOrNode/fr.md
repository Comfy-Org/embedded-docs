# Ou

Le nœud ComfyOrNode effectue une opération OU logique sur un ensemble de valeurs d'entrée. Il renvoie `true` si l'une des valeurs fournies est considérée comme vraie (truthy) selon les règles standard de vérité de Python.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `value` | Une valeur à évaluer pour déterminer si elle est vraie (truthy). Vous pouvez fournir plusieurs valeurs en ajoutant d'autres entrées. Le nœud renvoie `true` si l'une de ces valeurs est vraie. | ANY | Oui | Minimum 1 valeur ; plusieurs valeurs acceptées |

**Remarque :** Le nœud accepte un minimum de 1 valeur d'entrée. Vous pouvez ajouter d'autres entrées si nécessaire grâce à la fonctionnalité d'extension automatique.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `BOOLEAN` | Renvoie `true` si l'une des valeurs d'entrée est vraie (truthy) ; renvoie `false` si toutes les valeurs d'entrée sont fausses (falsy). | BOOLEAN |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/fr.md)

---
**Source fingerprint (SHA-256):** `f673aa2b0d754f55c51ba9c9ceea7d9de9a21d2e7308bd1281b4d4461243e4ad`
