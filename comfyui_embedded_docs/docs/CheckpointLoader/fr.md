# Charger Point de Contrôle Avec Config (OBSOLÈTE)

Le nœud CheckpointLoader charge un checkpoint de modèle pré-entraîné ainsi que son fichier de configuration. Il prend un fichier de configuration et un fichier de checkpoint en entrées et renvoie les composants du modèle chargé, notamment le modèle principal, le modèle CLIP et le modèle VAE, pour une utilisation dans le workflow.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `config_name` | Le fichier de configuration qui définit l'architecture et les paramètres du modèle | STRING | Oui | Fichiers de configuration disponibles |
| `ckpt_name` | Le fichier de checkpoint contenant les poids et paramètres du modèle entraîné | STRING | Oui | Fichiers de checkpoint disponibles |

**Remarque :** Ce nœud nécessite la sélection d'un fichier de configuration et d'un fichier de checkpoint. Le fichier de configuration doit correspondre à l'architecture du fichier de checkpoint chargé.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le composant modèle principal chargé, prêt pour l'inférence | MODEL |
| `CLIP` | Le composant modèle CLIP chargé pour l'encodage de texte | CLIP |
| `VAE` | Le composant modèle VAE chargé pour l'encodage et le décodage d'images | VAE |

**Remarque importante :** Ce nœud a été marqué comme obsolète et pourrait être supprimé dans les versions futures. Envisagez d'utiliser des nœuds de chargement alternatifs pour les nouveaux workflows.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/fr.md)

---
**Source fingerprint (SHA-256):** `820cd9f7a5ccd5a70d2b29906c8deca3632d2ccba84ca51022717e061afb72b3`
