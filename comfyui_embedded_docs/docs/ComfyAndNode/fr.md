> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI :

## Aperçu

Le nœud Et effectue une opération logique ET sur un ensemble de valeurs d'entrée. Il renvoie `true` uniquement si toutes les valeurs fournies sont considérées comme vraies selon les règles de vérité de Python. Ce nœud est utile pour vérifier que plusieurs conditions sont toutes remplies avant de poursuivre.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `valeurs` | ANY | Oui | 1 valeur ou plus | Une liste de valeurs à évaluer. Le nœud accepte au moins une valeur, et vous pouvez en ajouter d'autres en cliquant sur le bouton "+" du nœud. |

**Remarque :** Le nœud utilise les règles de vérité de Python pour déterminer si une valeur est `true` ou `false`. Par exemple, une chaîne vide, le nombre 0, une liste vide et `None` sont tous considérés comme `false`. Toutes les autres valeurs sont considérées comme `true`.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `BOOLEAN` | BOOLEAN | Renvoie `true` si toutes les valeurs d'entrée sont vraies, sinon renvoie `false`. |

---
**Source fingerprint (SHA-256):** `fd9d18ce698472a7e35ad3082f2ccff8ae264b11bd887a498f929cd877ff38c4`
