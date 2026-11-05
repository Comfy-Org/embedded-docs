# Tencent HY

Ce nœud génère des réponses textuelles avec le modèle Hy4 de Tencent. Il envoie une invite textuelle, ainsi qu'éventuellement une ou plusieurs images comme contexte, et renvoie la réponse du modèle sous forme de texte.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle utilisé pour générer la réponse. Sa sélection révèle ses entrées ci-dessous. Par défaut : `"Hy4"`. | DYNAMIC_COMBO | Oui | `"Hy4"` |

### Entrées Hy4

Ces entrées apparaissent lorsque `model` est défini sur `"Hy4"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Le message à envoyer au modèle. Ne doit pas être vide. Par défaut : "" (chaîne vide). | STRING | Oui | Au moins 1 caractère |
| `images` | Jusqu'à 20 images. Chaque image d'un lot compte. Par défaut : aucune image. | AUTOGROW | Non | 0 à 20 images |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |
| `system_prompt` | Instructions fondamentales qui dictent le comportement du modèle. Par défaut : "" (chaîne vide). | STRING | Non | - |
| `reasoning` | Le modèle réfléchit avant de répondre. Les réponses prennent plus de temps et consomment plus de tokens, et les tâches très difficiles peuvent expirer. Par défaut : False. | BOOLEAN | Oui | true<br>false |
| `temperature` | Contrôle le caractère aléatoire. Les résultats varient encore à 0. Par défaut : 1.0. | FLOAT | Oui | 0.0 à 1.4 (pas : 0.01) |
| `max_tokens` | Nombre maximum de tokens à générer, y compris les tokens de raisonnement lorsque `reasoning` est activé. Les réponses très longues peuvent expirer. Par défaut : 32000. | INT | Oui | 1 à 64000 |

**Contraintes :**

* Au plus 20 images sont acceptées par requête, en comptant chaque image d'un lot.
* Le filtre de contenu de Tencent peut bloquer une requête, ce qui déclenche une erreur.
* Si `max_tokens` est épuisé avant la fin de la réponse, le nœud déclenche une erreur : augmentez `max_tokens` ou désactivez `reasoning`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `STRING` | La réponse textuelle du modèle Hy4. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentHyNode/fr.md)

---
**Source fingerprint (SHA-256):** `c7c1d2908d2fba8172fa279b7d273f5f3f96cf10b531f81650824fc8e0176f21`
