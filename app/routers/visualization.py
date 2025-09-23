from fastapi import APIRouter, Query


router = APIRouter(prefix="/viz", tags=["visualization"])


@router.get("/layers")
async def list_layers():
	"""List available geospatial/data layers (stub)."""
	return {
		"layers": [
			{"id": "sst_recent", "type": "raster", "title": "SST (recent)"},
			{"id": "landings_points", "type": "points", "title": "Fisheries Landings"},
		],
	}


@router.get("/dashboard")
async def get_dashboard_config(name: str = Query("default")):
	"""Return dashboard layout/config (for Grafana/Plotly clients)."""
	return {
		"name": name,
		"widgets": [
			{"type": "timeseries", "title": "SST vs Landings", "query": "correlate(sst, sardine)"},
		]
	}


