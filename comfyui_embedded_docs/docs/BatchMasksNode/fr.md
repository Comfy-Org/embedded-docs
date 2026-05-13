> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchMasksNode/fr.md)

Le nœud Batch Masks combine plusieurs entrées de masques individuelles en un seul lot. Il accepte un nombre variable d'entrées de masques et les produit sous forme d'un tenseur de masques regroupé, permettant le traitement par lots de masques dans les nœuds suivants.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `mask_0` | MASK | Oui | - | La première entrée de masque. |
| `mask_1` | MASK | Oui | - | La deuxième entrée de masque. |
| `mask_2` à `mask_49` | MASK | Non | - | Entrées de masques supplémentaires optionnelles. Le nœud peut accepter un minimum de 2 et un maximum de 50 masques au total. |

**Remarque :** Ce nœud utilise un modèle d'entrée à croissance automatique. Vous devez connecter au moins deux masques (`mask_0` et `mask_1`). Vous pouvez ajouter jusqu'à 48 entrées de masques optionnelles supplémentaires (`mask_2` à `mask_49`) pour un total de 50 masques. Tous les masques connectés seront combinés en un seul lot.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | MASK | Un seul lot de masques contenant tous les masques d'entrée empilés ensemble. |

---
**Source fingerprint (SHA-256):** `8eb7a2a2d8108b619387b049d92348b8e9fc6d5e94e78c856c8520b88cdf77f2`
