from fastapi import APIRouter, Depends, HTTPException, status
from typing import Literal


router = APIRouter(prefix="/auth", tags=["auth"])


def get_current_user_role() -> Literal["scientist", "admin", "policymaker"]:
	"""Stub role provider. Replace with JWT validation later."""
	return "scientist"


def require_role(*allowed: str):
	def _dep(role: str = Depends(get_current_user_role)):
		if role not in allowed:
			raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
		return role
	return _dep


@router.get("/whoami")
async def whoami(role: str = Depends(get_current_user_role)):
	return {"role": role}

@router.get("/admin/ping")
async def admin_ping(_: str = Depends(require_role("admin"))):
	return {"ok": True}


