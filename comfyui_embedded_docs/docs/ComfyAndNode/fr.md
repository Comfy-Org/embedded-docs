# Et

Le nœud And effectue une opération logique AND sur un groupe de valeurs d'entrée. Il renvoie `true` uniquement lorsque chaque valeur connectée est considérée comme vraie selon les règles de véracité de Python, ce qui le rend utile pour vérifier que plusieurs conditions sont toutes remplies en même temps.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `valeurs` | Un groupe extensible de valeurs à évaluer. Le nœud commence avec un emplacement et vous pouvez en ajouter d'autres en cliquant sur le bouton « + » du nœud. Accepte tout type de données. | ANY | Oui | Minimum 1 (pas de maximum) |

**Remarque :** Cette entrée est un groupe d'emplacements extensible. Les emplacements sont ajoutés individuellement (par exemple `value_1`, `value_2`, etc.), et au moins un emplacement doit être présent.

**Remarque :** Le nœud utilise les règles de véracité de Python pour déterminer si une valeur est `true` ou `false`. Par exemple, une chaîne vide, le nombre 0, une liste vide et `None` sont tous traités comme `false`. Toutes les autres valeurs sont traitées comme `true`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `BOOLEAN` | Renvoie `true` si toutes les valeurs d'entrée sont évaluées comme vraies, sinon renvoie `false`. | BOOLEAN |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/fr.md)

---
**Source fingerprint (SHA-256):** `e7359c46da62f9859ea4f4a239cf20c565b5f7de22d280afc00c7ca321f1c89d`
