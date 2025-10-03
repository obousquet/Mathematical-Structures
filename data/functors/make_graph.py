from typing import Dict, Any, List
import copy

def generate(cache) -> Dict[str, List[Dict[str, Any]]]:
    """
    Generate nodes and edges for the graph.
    """
    nodes = []
    edges = []
    # Add mathematician nodes
    for m in cache.get_table_entries("classes"):
        # Color based on on-objects, on-morphisms, and on-limits fields
        on_objects = m.get("on-objects", False)
        on_morphisms = m.get("on-morphisms", False)
        on_limits = m.get("on-limits", False)
        
        if on_limits:
            # Limits/colimits: orange
            color = {"color": "#FF8C00", "fillcolor": "#FFE5CC"}
        elif on_objects and on_morphisms:
            # Both objects and morphisms: purple
            color = {"color": "#8B4789", "fillcolor": "#E6D5F5"}
        elif on_objects:
            # Objects only: blue
            color = {"color": "#4169E1", "fillcolor": "#D5E5F5"}
        elif on_morphisms:
            # Morphisms only: green
            color = {"color": "#2E8B57", "fillcolor": "#D5F5E5"}
        else:
            # Neither or unspecified: gray
            color = {"color": "#AAAAAA", "fillcolor": "#F5F5F5"}
        
        shape = "box"
        nodes.append({
            "id": f'#classes/{m["id"]}',
            "label": m.get("name", m.get("short_name", str(m["id"]))),
            "ref": f'#classes/{m["id"]}',
            "shape": shape,
            **color,
            "style": "filled",
        })
    for r in cache.get_table_entries("relationships"):
        _, p1 = cache.lookup(r["containee"])
        _, p2 = cache.lookup(r["container"])
        label = ''
        arrow = copy.copy({
                "arrowhead": "normal",
                "style": "dashed",
                "color": "#000000",
            })
        ref = ''
        if r.get("witness"):
            _, w = cache.lookup(r["witness"])
            if w:
                label = w.get("short_name", w.get("name", str(w["id"])))
                ref = f'#witnesses/{w["id"]}'
                arrow = copy.copy(arrow)
                arrow["style"] = "solid"
        edges.append({
            "source": f'#classes/{p1["id"]}',
            "target": f'#classes/{p2["id"]}',
            "ref": f'#relationships/{r["id"]}',
            "label": label,
            "label_ref": ref,
            **arrow
        })

    # Remove transitive edges for Hasse diagram
    # Build adjacency list
    adj = {}
    for e in edges:
        adj.setdefault(e["source"], set()).add(e["target"])

    def reachable(src, dst, exclude=None):
        # DFS to check if dst is reachable from src, excluding direct edge src->dst
        stack = [src]
        visited = set()
        while stack:
            node = stack.pop()
            if node == dst:
                return True
            visited.add(node)
            for neighbor in adj.get(node, []):
                if exclude and node == src and neighbor == dst:
                    continue
                if neighbor not in visited:
                    stack.append(neighbor)
        return False

    hasse_edges = []
    for e in edges:
        # If there is an alternate path from source to target, exclude this edge
        if not reachable(e["source"], e["target"], exclude=True):
            hasse_edges.append(e)

    return {"nodes": nodes, "edges": hasse_edges}
