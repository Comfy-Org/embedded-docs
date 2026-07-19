# LumaRay32ExtendVideoNode

Ce nœud étend une génération vidéo Luma Ray 3.2 précédente en ajoutant un nouveau contenu soit après celle-ci (extension vers l'avant), soit avant celle-ci (extension vers l'arrière). Connectez la sortie d'ID de génération d'un nœud Luma Ray 3.2 antérieur pour créer une extension transparente de 5 secondes de votre vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `source_generation_id` | ID de génération de la vidéo Ray 3.2 antérieure à étendre. Connectez la sortie `generation_id` d'un autre nœud Luma Ray 3.2. | STRING | Oui | - |
| `direction` | "Forward" continue après le clip antérieur ; "backward" est ajouté avant celui-ci. Lorsque "Forward (continue after)" est sélectionné, vous pouvez éventuellement activer le mode boucle. | COMBO | Oui | "Forward (continue after)"<br>"Backward (lead-in before)" |
| `loop` | Boucle la vidéo étendue de manière transparente (extension vers l'avant uniquement). | BOOLEAN | Non | True<br>False |
| `prompt` | Invite textuelle décrivant le nouveau contenu à générer. | STRING | Oui | - |
| `resolution` | Résolution de sortie pour le segment vidéo étendu. | COMBO | Oui | "540p"<br>"720p"<br>"1080p" |
| `seed` | Graine aléatoire pour des résultats de génération reproductibles. | INT | Oui | - |

**Remarque :** Le paramètre `loop` est disponible uniquement lorsque `direction` est défini sur "Forward (continue after)". Lors de l'utilisation de "Backward (lead-in before)", l'option de boucle n'est pas disponible. L'`prompt` doit contenir entre 1 et 6000 caractères.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `generation_id` | Le segment vidéo étendu généré de 5 secondes. | VIDEO |
| `generation_id` | Identifiant unique pour cette génération, qui peut être connecté à un autre nœud Luma Ray 3.2 Extend Video pour des extensions supplémentaires. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`
