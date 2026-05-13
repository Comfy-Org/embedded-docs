> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProDepthNode/fr.md)

Ce nœud génère des images en utilisant une image de contrôle de profondeur comme guide. Il prend une image de contrôle et un texte d’invite, puis crée une nouvelle image qui respecte à la fois les informations de profondeur de l’image de contrôle et la description de l’invite. Le nœud se connecte à une API externe pour effectuer le processus de génération d’images.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `control_image` | IMAGE | Oui | - | L’image de contrôle de profondeur utilisée pour guider la génération de l’image |
| `prompt` | STRING | Non | - | Invite pour la génération de l’image (par défaut : chaîne vide) |
| `prompt_upsampling` | BOOLEAN | Non | - | Indique s’il faut effectuer un suréchantillonnage de l’invite. Si activé, modifie automatiquement l’invite pour une génération plus créative, mais les résultats sont non déterministes (la même graine ne produira pas exactement le même résultat). (par défaut : False) |
| `skip_preprocessing` | BOOLEAN | Non | - | Indique s’il faut ignorer le prétraitement ; définir sur True si `control_image` est déjà convertie en profondeur, sur False s’il s’agit d’une image brute. (par défaut : False) |
| `guidance` | FLOAT | Non | 1-100 | Force de guidage pour le processus de génération de l’image (par défaut : 15) |
| `steps` | INT | Non | 15-50 | Nombre d’étapes pour le processus de génération de l’image (par défaut : 50) |
| `seed` | INT | Non | 0-18446744073709551615 | La graine aléatoire utilisée pour créer le bruit. (par défaut : 0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output_image` | IMAGE | L’image générée en fonction de l’image de contrôle de profondeur et de l’invite |

---
**Source fingerprint (SHA-256):** `34b80d7d63158b7dc4ad02da6b3a573b713d77efd0955d3477409f776f964462`
