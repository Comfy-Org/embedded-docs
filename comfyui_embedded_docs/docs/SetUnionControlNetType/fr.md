# Définir le Type de Réseau de Contrôle d'Union

Le nœud SetUnionControlNetType vous permet de choisir le type de contrôle utilisé par un réseau de contrôle. Il prend un réseau de contrôle existant et crée une copie modifiée avec le type de contrôle sélectionné, laissant le réseau de contrôle d'origine inchangé. Lorsque « auto » est sélectionné, le type de contrôle stocké est effacé afin que le type puisse être détecté automatiquement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `réseau_de_contrôle` | Le réseau de contrôle à modifier avec un nouveau réglage de type | CONTROL_NET | Oui | - |
| `type` | Le type de réseau de contrôle à appliquer. Utilisez « auto » pour la détection automatique du type ou sélectionnez un type de réseau de contrôle spécifique parmi les options disponibles (par défaut : « auto ») | COMBO | Oui | `"auto"`<br>`"openpose"`<br>`"depth"`<br>`"hed/pidi/softedge"`<br>`"canny"`<br>`"scribble"`<br>`"seg"`<br>`"tile"`<br>`"inpaint"`<br>`"lineart"`<br>`"blur"`<br>`"mlsd"`<br>`"normalbae"`<br>`"mask"` |

Lorsque `type` est défini sur `"auto"`, le nœud efface le type de contrôle stocké afin que le type puisse être détecté automatiquement. Lorsqu'un type spécifique est sélectionné, le nœud stocke le type de contrôle correspondant dans le réseau de contrôle copié.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `control_net` | Le réseau de contrôle modifié avec le type spécifié appliqué | CONTROL_NET |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/fr.md)

---
**Source fingerprint (SHA-256):** `db4b1a3cebafcff2be3172faa09cecbd5e19331376491c491cbe359013ed3da3`
