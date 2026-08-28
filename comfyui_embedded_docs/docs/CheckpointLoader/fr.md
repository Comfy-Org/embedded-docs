# Charger Point de Contrôle Avec Config (OBSOLÈTE)

Le nœud CheckpointLoader charge un checkpoint de modèle pré-entraîné avec son fichier de configuration. Il prend un fichier de configuration et un fichier de checkpoint en entrées et retourne les composants du modèle chargé — le modèle principal, le modèle CLIP et le modèle VAE — pour les utiliser dans le workflow. Ce nœud est obsolète.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `nom_config` | Le fichier de configuration qui définit l'architecture et les paramètres du modèle | COMBO | Oui | Fichiers de configuration disponibles |
| `nom_ckpt` | Le fichier de checkpoint contenant les poids et paramètres du modèle entraîné | COMBO | Oui | Fichiers de checkpoint disponibles |

**Remarque :** Ce nœud nécessite la sélection d'un fichier de configuration et d'un fichier de checkpoint. Le fichier de configuration doit correspondre à l'architecture du fichier de checkpoint chargé.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le composant de modèle principal chargé, prêt pour l'inférence | MODEL |
| `CLIP` | Le composant de modèle CLIP chargé pour l'encodage de texte | CLIP |
| `VAE` | Le composant de modèle VAE chargé pour l'encodage et le décodage d'images | VAE |

**Remarque importante :** Ce nœud a été marqué comme obsolète et pourrait être supprimé dans les versions futures. Envisagez d'utiliser des nœuds de chargement alternatifs pour les nouveaux workflows.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/fr.md)

---
**Source fingerprint (SHA-256):** `820cd9f7a5ccd5a70d2b29906c8deca3632d2ccba84ca51022717e061afb72b3`
