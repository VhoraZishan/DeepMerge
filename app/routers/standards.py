from fastapi import APIRouter, Body
from typing import List, Dict, Any
from app.services.standards import export_dwc_occurrences, cf_metadata_stub


router = APIRouter(prefix="/standards", tags=["standards"])


@router.post("/dwc/export")
async def export_dwc(records: List[Dict[str, Any]] = Body(...)):
	"""Map input records to Darwin Core occurrence fields (CSV-ready rows as JSON)."""
	mapped = export_dwc_occurrences(records)
	return {"rows": mapped, "count": len(mapped)}


@router.get("/cf/metadata")
async def get_cf_metadata(dataset: str, variable: str, units: str, standard_name: str):
	"""Return CF/ERDDAP-style metadata stub for variable."""
	return cf_metadata_stub(dataset, variable, units, standard_name)


