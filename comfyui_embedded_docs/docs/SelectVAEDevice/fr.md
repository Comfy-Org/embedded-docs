> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectVAEDevice/fr.md)

## Présentation

Ce nœud vous permet de sélectionner manuellement sur quel périphérique GPU le modèle VAE doit être placé. Par défaut, le VAE est placé sur le périphérique attribué par le chargeur de modèle, mais vous pouvez le fixer sur un GPU spécifique (par exemple, `gpu:0`, `gpu:1`). Si le périphérique sélectionné n'est pas disponible sur votre machine, le nœud transmettra le VAE sans modification et enregistrera un message au lieu d'échouer.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `vae` | VAE | Oui | | Le modèle VAE à attribuer à un périphérique spécifique. |
| `périphérique` | COMBO | Oui | `"default"`<br>`"gpu:0"`<br>`"gpu:1"`<br>`"gpu:2"`<br>`"gpu:3"`<br>`"gpu:4"`<br>`"gpu:5"`<br>`"gpu:6"`<br>`"gpu:7"` | Le périphérique cible pour le VAE. `"default"` restaure le périphérique attribué par le chargeur. `"gpu:N"` fixe le VAE sur le Nième GPU disponible. Le CPU n'est pas un choix pris en charge et sera ignoré s'il est fourni. (par défaut : `"default"`) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `vae` | VAE | Le modèle VAE, désormais attribué au périphérique sélectionné. Si le périphérique demandé est indisponible ou invalide, le VAE est transmis sans modification. |

---
**Source fingerprint (SHA-256):** `011154043fc02f930b0074de656bb24baf4dfe74bcfd2e89ea76284f0a5b7d8e`
