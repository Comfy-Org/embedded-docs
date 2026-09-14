# LoopResult

LoopResult est un nœud de sortie réservé aux développeurs qui marque le point de fermeture d’un bloc de boucle. Il collecte les valeurs qui lui sont transmises dans l’ordre (nommées `output0`, `output1`, etc.) et libère le bloc d’exécution externe identifié par un ID de fermeture. Comme l’empreinte des entrées renvoie toujours NaN, le nœud est considéré comme toujours modifié et est réexécuté à chaque exécution.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `close_id` | Identifiant du bloc de boucle à fermer ; seule la première valeur de la liste est utilisée | STRING | Oui | - |
| `output0`, `output1`, ... | Valeurs collectées depuis le bloc de boucle. Le nœud accepte toutes les entrées supplémentaires et les rassemble dans l’ordre séquentiel en commençant à `output0`, en s’arrêtant au premier index manquant | Tout type | Non | - |

Remarque : Ce nœud accepte toutes les entrées (`accept_all_inputs`). Toute entrée au-delà de `close_id` est traitée comme une valeur de boucle collectée et doit être nommée `output0`, `output1`, `output2`, etc., sans interruption, pour être incluse dans le résultat.

## Sorties

Ce nœud ne renvoie aucune sortie. Il libère uniquement le bloc d’exécution externe associé à `close_id`.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopResult/fr.md)

---
**Source fingerprint (SHA-256):** `637f8a39b0e99e8d4453cfc482463bd14d909b710264021ac2c27fdcd68b6063`
