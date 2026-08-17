# SAM3 Suivi Vidéo

```markdown
Suivez des objets à travers les frames vidéo à l'aide du tracker mémoire de SAM3. Ce nœud traite une séquence de frames vidéo et maintient les identités des objets d'un frame à l'autre, en utilisant soit des masques initiaux, soit des invites textuelles pour définir quoi suivre.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Frames vidéo sous forme d'images en lot | IMAGE | Oui | Frames vidéo en lot |
| `model` | Le modèle SAM3 à utiliser pour le suivi | MODEL | Oui | Modèle SAM3 |
| `initial_mask` | Masque(s) pour le premier frame à suivre (un par objet). Requis si `conditioning` n'est pas fourni. | MASK | Non | Un masque par objet |
| `conditioning` | Conditionnement textuel pour détecter de nouveaux objets pendant le suivi. Requis si `initial_mask` n'est pas fourni. | CONDITIONING | Non | Conditionnement textuel |
| `detection_threshold` | Seuil de score pour la détection basée sur une invite textuelle (par défaut : 0.5). | FLOAT | Oui | 0.0 to 1.0 |
| `max_objects` | Nombre maximal d'objets suivis. Les masques initiaux comptent dans cette limite. 0 utilise la limite interne de 64 (par défaut : 4). | INT | Oui | 0 to 64 |
| `detect_interval` | Exécuter la détection toutes les N frames (1=à chaque frame). Des valeurs plus élevées économisent du calcul (par défaut : 1). | INT | Oui | 1 ou plus |

**Remarque :** Soit `initial_mask`, soit `conditioning` doit être fourni. Si les deux sont omis, le nœud générera une erreur. Lorsque les deux sont fournis, les masques initiaux définissent les objets à suivre à partir du premier frame et les invites textuelles détectent des objets supplémentaires pendant le suivi.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `track_data` | Données de suivi contenant les masques d'objets et les métadonnées sur toutes les frames vidéo, y compris les dimensions d'origine des frames. | SAM3_TRACK_DATA |
```

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/fr.md)

---
**Source fingerprint (SHA-256):** `ef584628b334997a001a857a7deffb7eda34db8fa50e3d734a07b5e92566d48d`
