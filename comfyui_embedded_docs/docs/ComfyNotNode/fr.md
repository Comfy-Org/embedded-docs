> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNotNode/fr.md)

## Aperçu

Le nœud Not effectue une opération logique NON sur n'importe quelle valeur d'entrée. Il renvoie Vrai si la valeur d'entrée est considérée comme fausse (comme 0, chaîne vide, None, Faux), et renvoie Faux si la valeur d'entrée est vraie. Il utilise les règles standard de Python pour déterminer la véracité.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `valeur` | ANY | Oui | Toute valeur | La valeur d'entrée à inverser. Tout type de données est accepté et évalué selon les règles de véracité de Python. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | BOOLEAN | L'inverse logique de la valeur d'entrée. Renvoie Vrai si l'entrée est fausse, Faux si l'entrée est vraie. |

---
**Source fingerprint (SHA-256):** `fd8f940218538fce28079bc836379703c0e3c04f80351520497855c464176877`
