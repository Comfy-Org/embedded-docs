# Charger le modèle MoGe

Charge un modèle MoGe (géométrie monoculaire) depuis un fichier et le prépare pour une utilisation dans les tâches d'estimation de géométrie. Le nœud lit le fichier de modèle sélectionné dans le dossier `geometry_estimation` et initialise le modèle MoGe avec ses poids enregistrés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model_name` | Le nom du fichier de modèle MoGe à charger. Sélectionnez parmi les fichiers de modèle disponibles dans le dossier `geometry_estimation` de votre installation ComfyUI. | COMBO | Oui | Liste des fichiers de modèle disponibles dans le dossier `geometry_estimation` |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MOGE_MODEL` | L'instance du modèle MoGe chargé, prête à être utilisée dans les flux de travail d'estimation de géométrie. | MOGE_MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMoGeModel/fr.md)

---
**Source fingerprint (SHA-256):** `b5b55f94d3762852d5a1480c0b00d15da4e534adbeb544bf7c47da012e5a6353`
