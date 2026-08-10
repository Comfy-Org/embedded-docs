# LumaRay32ExtendVideoNode

Luma Ray 3.2 Extend Video poursuit une génération vidéo précédente de Luma Ray 3.2 en créant un nouveau segment de 5 secondes, soit après le clip d'origine (vers l'avant), soit avant (vers l'arrière). Connectez la sortie `generation_id` d'un nœud Luma Ray 3.2 antérieur pour utiliser ce clip comme image de départ (vers l'avant) ou de fin (vers l'arrière) de l'extension.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `source_generation_id` | ID de génération de la vidéo Ray 3.2 précédente à étendre. Connectez la sortie `generation_id` d'un autre nœud Luma Ray 3.2. Cette valeur est obligatoire et ne doit pas être vide. | STRING | Oui | - |
| `direction` | Vers l'avant continue après le clip précédent ; vers l'arrière est préfixé avant lui. La sélection de « Forward (continue after) » ajoute également l'option `loop`. | COMBO | Oui | "Forward (continue after)"<br>"Backward (lead-in before)" |
| `loop` | Boucle la vidéo étendue de manière transparente (extension vers l'avant uniquement). Disponible uniquement lorsque `direction` est « Forward (continue after) ». Par défaut : False. | BOOLEAN | Non | True<br>False |
| `prompt` | Invite textuelle pour le nouveau contenu. Doit contenir entre 1 et 6000 caractères. | STRING | Oui | - |
| `resolution` | Résolution de sortie pour le segment vidéo étendu. Par défaut : "720p". | COMBO | Oui | "540p"<br>"720p"<br>"1080p" |
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
