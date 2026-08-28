# Ou

Le nœud Or effectue une opération logique OU sur un ensemble de valeurs d’entrée. Il renvoie `true` si l’une des valeurs fournies est considérée comme vraie selon les règles standard de vérité de Python.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `valeurs` | Collection extensible de valeurs à évaluer pour déterminer leur véracité. Chaque emplacement d’entrée ajouté est nommé `value_1`, `value_2`, etc. Le nœud renvoie `true` si l’une de ces valeurs est vraie. | ANY | Oui | 1 valeur ou plus |

**Remarque :** Le nœud accepte au minimum 1 valeur d’entrée. Vous pouvez ajouter d’autres entrées selon vos besoins grâce à la fonction d’extension automatique.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `BOOLEAN` | Renvoie `true` si l’une des valeurs d’entrée est vraie ; renvoie `false` si toutes les valeurs d’entrée sont fausses. | BOOLEAN |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/fr.md)

---
**Source fingerprint (SHA-256):** `f673aa2b0d754f55c51ba9c9ceea7d9de9a21d2e7308bd1281b4d4461243e4ad`
