# Bria Guided Remove Background

Ce nœud supprime l'arrière-plan d'une image avec Bria, en conservant ce que décrit le prompt. Les pixels d'origine sont renvoyés à pleine résolution avec un nouveau canal alpha au lieu d'être rendus à nouveau, de sorte que les détails fins et les contours sont préservés. Un prompt qui ne correspond à rien renvoie une image entièrement transparente. Pour un détourage simple sans indication, Bria Remove Image Background coûte moins cher.

## Entrées

Le sélecteur `moderation` révèle des options de modération supplémentaires lorsqu'il est défini sur `"true"`.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image à détourer. | IMAGE | Oui | - |
| `prompt` | Ce qu'il faut conserver et, éventuellement, ce qu'il faut supprimer ou restreindre, comme « la personne avec le tapis et la plante », « la femme à son bureau sans la lampe » ou « uniquement la chaise ». Ne doit pas être vide. Si rien ne correspond au prompt, le résultat est entièrement transparent. Valeur par défaut : `""` (chaîne vide). | STRING | Oui | 1 caractère ou plus |
| `moderation` | Paramètres de modération. Lorsqu'il est défini sur `"true"`, les indicateurs de modération visuelle ci-dessous deviennent disponibles. | DYNAMIC_COMBO | Oui | `"false"`<br>`"true"` |

### Entrées de modération « true »

Ces paramètres n'apparaissent que lorsque `moderation` est défini sur `"true"`. L'option `"false"` n'ajoute aucune entrée supplémentaire.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `visual_input_moderation` | Active la modération de contenu sur l'image d'entrée. Valeur par défaut : `False`. | BOOLEAN | Non | True / False |
| `visual_output_moderation` | Active la modération de contenu sur l'image générée. Valeur par défaut : `False`. | BOOLEAN | Non | True / False |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image détourée : les pixels d'origine avec un nouveau canal alpha. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGuidedRemoveBackground/fr.md)

---
**Source fingerprint (SHA-256):** `210fa214a0d0d8ad19a15ea4f6baa9f13499bc4c3767e270f19f2a08d67e25ac`
