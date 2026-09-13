# Luma Ray 3.2 Extension Vidéo

Luma Ray 3.2 Extend Video prolonge une génération vidéo Luma Ray 3.2 précédente en créant un nouveau segment de 5 secondes soit après le clip original (forward), soit avant celui-ci (backward). Connectez la sortie `generation_id` d'un nœud Luma Ray 3.2 antérieur pour utiliser ce clip comme image de départ (forward) ou image de fin (backward) de l'extension. Les extensions durent toujours 5 secondes.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `source_generation_id` | ID de génération de la vidéo Ray 3.2 antérieure à prolonger. Connectez la sortie `generation_id` d'un autre nœud Luma Ray 3.2. Par défaut : "" (vide). Cette valeur est requise et ne doit pas être vide. | STRING | Oui | – |
| `direction` | L'option Forward (continue after) continue après le clip précédent ; l'option Backward (lead-in before) est ajoutée avant celui-ci. Forward utilise le clip source comme image de départ ; Backward l'utilise comme image de fin. Sélectionner « Forward (continue after) » ajoute l'option `loop`. | DYNAMIC_COMBO | Oui | "Forward (continue after)"<br>"Backward (lead-in before)" |
| `prompt` | Invite textuelle pour le nouveau contenu. Par défaut : "" (vide). Doit comporter entre 1 et 6000 caractères. | STRING | Oui | 1 à 6000 caractères |
| `resolution` | Résolution de sortie pour le segment vidéo prolongé. Par défaut : "720p". | COMBO | Oui | "540p"<br>"720p"<br>"1080p" |
| `seed` | Graine pour déterminer si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. Par défaut : 0. | INT | Oui | 0 à 0xFFFFFFFFFFFFFFFF (18446744073709551615) |

### Entrées Forward (continue after)

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `loop` | Lit la vidéo prolongée en boucle sans raccord (extension vers l'avant uniquement). Par défaut : False. | BOOLEAN | Non | True<br>False |

### Entrées Backward (lead-in before)

Cette direction n'ajoute aucun paramètre supplémentaire.

**Remarque :** Les extensions durent toujours 5 secondes. Le paramètre `loop` n'est disponible que lorsque `direction` vaut « Forward (continue after) » ; lorsque vous utilisez « Backward (lead-in before) », l'option `loop` n'est pas disponible. Le `prompt` doit comporter entre 1 et 6000 caractères. Le `source_generation_id` est requis et doit être connecté à la sortie `generation_id` d'un nœud Luma Ray 3.2 précédent.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | Le segment vidéo prolongé généré, d'une durée de 5 secondes. | VIDEO |
| `generation_id` | Identifiant unique pour cette génération, qui peut être connecté à un autre nœud Luma Ray 3.2 Extend Video pour d'autres extensions. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`
