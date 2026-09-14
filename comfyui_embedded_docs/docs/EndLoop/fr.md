# EndLoop

End Loop marque la fin d'un bloc de boucle. Il collecte la valeur produite par le dernier nœud du corps de la boucle et renvoie soit uniquement l'itération finale, soit toutes les itérations, selon le réglage `accumulate`, tout en renvoyant également une valeur à Start Loop afin que l'itération suivante puisse commencer.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `output_value` | Valeur renvoyée par End Loop. Elle renvoie l'itération finale ou toutes les itérations selon `accumulate`. | ANY | Non | Tout type de valeur |
| `next_iteration_value` | Valeur envoyée par End Loop à Start Loop pour l'itération suivante. | ANY | Non | Tout type de valeur |
| `accumulate` | Renvoie `output_value` à chaque itération lorsqu'activé ; sinon, renvoie uniquement l'itération finale. | BOOLEAN | Non | `true`<br>`false` (par défaut : `false`) |
| `terminations` | Connectez les sorties qui doivent s'exécuter à chaque itération. Leurs valeurs ne sont pas renvoyées. Emplacements extensibles nommés `termination_1`, `termination_2`, etc. | ANY | Non | 0 à 50 emplacements |

Remarque : `terminations` est une liste extensible d'emplacements avec un minimum de 0 et un maximum de 50 connexions. Les valeurs connectées ici forcent l'exécution à chaque itération mais ne font pas partie du résultat renvoyé.

Remarque : Ce nœud est un nœud de liste d'entrées, ses entrées reçoivent donc les valeurs collectées à chaque itération de la boucle.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `outputs` | La valeur `output_value` de l'itération finale, ou les valeurs accumulées sur plusieurs itérations lorsque `accumulate` est activé. | ANY (list) |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EndLoop/fr.md)

---
**Source fingerprint (SHA-256):** `473ba61d8e6fecdd1205297e2c602e3fd821044aff87d15a3f4b7646748d9999`
