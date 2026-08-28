# Et

Le nœud And effectue une opération ET logique sur un ensemble de valeurs d’entrée. Il renvoie `true` uniquement si toutes les valeurs fournies sont considérées comme vraies (truthy) selon les règles de vérité de Python. Ce nœud est utile pour vérifier que plusieurs conditions sont toutes remplies avant de continuer.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `valeurs` | Une valeur à évaluer. Le nœud accepte au moins une valeur, et vous pouvez en ajouter d’autres en cliquant sur le bouton « + » du nœud. Accepte tout type de données. | ANY | Oui | 1 ou plus (aucun maximum) |

**Remarque :** Le nœud utilise les règles de vérité de Python pour déterminer si une valeur est `true` ou `false`. Par exemple, une chaîne vide, le nombre 0, une liste vide et `None` sont tous considérés comme `false`. Toutes les autres valeurs sont considérées comme `true`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `BOOLEAN` | Renvoie `true` si toutes les valeurs d’entrée sont vraies (truthy), sinon renvoie `false`. | BOOLEAN |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/fr.md)

---
**Source fingerprint (SHA-256):** `e7359c46da62f9859ea4f4a239cf20c565b5f7de22d280afc00c7ca321f1c89d`
