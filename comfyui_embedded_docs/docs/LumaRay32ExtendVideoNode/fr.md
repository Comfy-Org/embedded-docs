# Luma Ray 3.2 Extension Vidéo

Luma Ray 3.2 Extend Video poursuit une génération vidéo Luma Ray 3.2 précédente en créant un nouveau segment de 5 secondes soit après le clip d’origine (forward), soit avant celui-ci (backward). Connectez la sortie `generation_id` d’un nœud Luma Ray 3.2 antérieur pour utiliser ce clip comme image de départ (forward) ou image de fin (backward) de l’extension.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `direction` | Forward continue après le clip précédent ; backward est ajouté avant celui-ci. Forward utilise le clip source comme image de départ ; backward l’utilise comme image de fin. La sélection de « Forward (continue after) » ajoute l’option `loop`. | DYNAMIC_COMBO | Oui | « Forward (continue after) »<br>« Backward (lead-in before) » |
| `source_generation_id` | ID de génération de la vidéo Ray 3.2 précédente à étendre. Connectez la sortie `generation_id` d’un autre nœud Luma Ray 3.2. Cette valeur est requise et ne doit pas être vide. | STRING | Oui | – |
| `prompt` | Invite textuelle (prompt) pour le nouveau contenu. Doit contenir entre 1 et 6000 caractères. | STRING | Oui | 1 à 6000 caractères |
| `resolution` | Résolution de sortie pour le segment vidéo étendu. Défaut : « 720p ». | COMBO | Oui | « 540p »<br>« 720p »<br>« 1080p » |
| `seed` | Graine (seed) pour déterminer si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. Défaut : 0. | INT | Oui | 0 à 0xFFFFFFFFFFFFFFFF |

### Entrées Forward (continue after)

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `loop` | Boucler la vidéo étendue de manière transparente (extension forward uniquement). Défaut : False. | BOOLEAN | Non | True<br>False |

### Entrées Backward (lead-in before)

Cette direction n’ajoute aucun paramètre supplémentaire.

**Remarque :** Les extensions durent toujours 5 secondes. Le paramètre `loop` n’est disponible que lorsque `direction` est « Forward (continue after) » ; lors de l’utilisation de « Backward (lead-in before) », l’option `loop` n’est pas disponible. Le `prompt` doit contenir entre 1 et 6000 caractères. Le `source_generation_id` est requis et doit être connecté à partir de la sortie `generation_id` d’un nœud Luma Ray 3.2 antérieur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | Le segment vidéo étendu généré de 5 secondes. | VIDEO |
| `generation_id` | Identifiant unique pour cette génération, qui peut être connecté à un autre nœud Luma Ray 3.2 Extend Video pour d’autres extensions. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`
