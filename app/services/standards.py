from __future__ import annotations

from typing import Iterable, Dict, Any, List


def export_dwc_occurrences(records: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
	"""Map internal biodiversity records to Darwin Core occurrence fields.

	Returns a list of dicts ready for CSV export (DwC Occurrence core subset).
	"""
	mapped: List[Dict[str, Any]] = []
	for r in records:
		mapped.append({
			"scientificName": r.get("species") or r.get("scientificName"),
			"eventDate": r.get("timestamp") or r.get("eventDate"),
			"decimalLatitude": r.get("latitude") or r.get("lat"),
			"decimalLongitude": r.get("longitude") or r.get("lon"),
			"basisOfRecord": r.get("basisOfRecord") or "HumanObservation",
			"recordedBy": r.get("recordedBy") or r.get("source") or "Unknown",
			"occurrenceID": r.get("id") or r.get("occurrenceID"),
			"country": r.get("country") or "India",
			"stateProvince": r.get("state") or r.get("region"),
			"license": r.get("license") or "CC-BY-4.0",
		})
	return mapped


def cf_metadata_stub(dataset_name: str, variable: str, units: str, standard_name: str) -> Dict[str, Any]:
	"""Return a CF/ERDDAP-style metadata dict for a variable (stub, not NetCDF)."""
	return {
		"title": dataset_name,
		"Conventions": "CF-1.10, ACDD-1.3",
		"variable": {
			"name": variable,
			"units": units,
			"standard_name": standard_name,
			"long_name": variable.replace("_", " ").title(),
		},
	}


